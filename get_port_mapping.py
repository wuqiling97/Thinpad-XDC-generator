from data import *
import re
from functools import reduce


# get origin var name and pin name
slist = open('thinpad_top.xdc').read().split('\n')
getpin = re.compile('PACKAGE_PIN (?P<pin>\w+)')
getport = re.compile('get_ports {?(?P<port>\w+(\[\d+\])?)')
pin_dict = {}
for s in slist:
    try:
        pin = getpin.search(s).group('pin')
        port = getport.search(s).group('port')
        pin_dict[port] = pin
    except AttributeError:
        pass

set_pin_str = \
    'set_property -dict {{IOSTANDARD LVCMOS33 PACKAGE_PIN {pin}}} [get_ports {port}]'
set_dedicate_str = 'set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets {port}_IBUF]'
clk_in = 'create_clock -period 20.000 -name {port} -waveform {{0.000 10.000}} [get_ports {port}]'
clk_uart_in = 'create_clock -period 90.422 -name {port} -waveform {{0.000 45.211}} [get_ports {port}]'
default_str = '''set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]'''
for k, v in pin_dict.items():
    print(repr(k), ': ', repr(v), ',', sep='')
