#coding=utf-8

from __future__ import print_function
import re, sys
from functools import reduce
from data import *


def print_gen(file):
    def wrapper(*value, sep=' ', end='\n'):
        print(*value, sep=sep, end=end, file=file)
    return wrapper


keys = ['clocks', 'button', 'cpld', 'ext serial', 'usb',
        'ethernet', 'video', 'leds', 'num disp', 'switches',
        'flash', 'base ram', 'ext ram', 'default']
if len(sys.argv) == 2:
    fname = sys.argv[1]
    if not fname.endswith('.xdc'):
        fname += '.xdc'
else:
    fname = 'target.xdc'
fout = open(fname, 'w')

print("""对于某一个section，直接回车来跳过，输入任意字符来进入
对于section当中的变量，回车以跳过这个变量，输入则分为一下情况：
输入"y" or "yes"来使用原始名字
否则：
1. 变量为scalar: 输入自定义名字
2. 变量为vector: 
   1. 只输入变量名，把整个vector命名
   2. 输入"start-stop: varname" 来进行范围命名
   3. 输入"number: varname" 来对单个元素命名""")
for num, varname_range, doc in zip(range(0, len(docs)), varname_ranges, docs):
    custom_varname = []
    not_jump_sec = input('\nsection: ' + doc)
    if not_jump_sec:
        for k, v in varname_range.items():  # k: origin var name, v: range
            _ = friendly_names[k]
            _s = _ + ' ' + k if _ != k else k
            # 打印端口名
            print(_s, end='')
            if v.stop != 1:
                print('[{}:{}]'.format(v.start, v.stop-1), end='')

            string = input(': ').strip().replace(' ', '')
            if string in ['y', 'yes']:
                string = k
            elif not string:  # enter to accept current name
                continue
            if v.stop == 1:  # scalar port
                custom_varname.append((k, string))
            else:
                mappings = string.split(',')
                range_re = re.compile('(?P<start>\d+)(-(?P<stop>\d+))?:(?P<varname>\w+)')
                if len(mappings) == 1 and range_re.search(mappings[0]) == None:
                    for i in v:
                        custom_varname.append(('{}[{}]'.format(k, i), mappings[0] + '[{}]'.format(i)))
                else:
                    for mapping in mappings:
                        res = range_re.search(mapping)
                        start = int(res.group('start'))
                        stop = res.group('stop')
                        stop = int(stop) if stop is not None else None
                        varname = res.group('varname')
                        if stop:
                            for i in range(start, stop+1):
                                custom_varname.append(('{}[{}]'.format(k, i), varname+'[{}]'.format(i)))
                        else:
                            custom_varname.append(('{}[{}]'.format(k, start), varname))
    printf = print_gen(fout)
    if len(custom_varname) > 0:
        printf(docs_infile[num])
        for ori, new in custom_varname:
            printf(set_pin_str.format(pin=pin_dict[ori], port=new))
        custom_varname = list(zip(*custom_varname))
        origins = custom_varname[0]
        news = custom_varname[1]
        if num == 0:
            printf()
            if 'clk_in' in origins:
                printf(clk_in.format(port=news[origins.index('clk_in')]))
            if 'clk_uart_in' in origins:
                port = news[origins.index('clk_uart_in')]
                printf(clk_uart_in.format(port=port))
                printf(set_dedicate_str.format(port=port))
        elif num == 1:
            printf()
            clk_list = input('您要将哪些按钮作为时钟? 输入0-5的数字, 用逗号分隔; 回车以跳过\n')
            if clk_list:
                clk_list = clk_list.strip().replace(' ', '').split(',')
                clk_list = list(map(int, clk_list))
                for i, ori in enumerate(origins):
                    if int(ori[ori.find('[')+1:-1]) in clk_list:
                        printf(set_dedicate_str.format(port=custom_varname[1][i]))
        printf()
    if num == 12:
        printf(docs_infile[num])
        printf(default_str)
