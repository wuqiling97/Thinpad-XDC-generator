constrains = [
'''#Clock
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D18} [get_ports clk_in] ;#50MHz main clock in
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C18} [get_ports clk_uart_in] ;#11.0592MHz clock for UART
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets clk_uart_in_IBUF]

create_clock -period 20.000 -name clk_in -waveform {0.000 10.000} [get_ports clk_in]
create_clock -period 90.422 -name clk_uart_in -waveform {0.000 45.211} [get_ports clk_uart_in]
''',

'''#Touch Button red+click
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J19} [get_ports touch_btn[0]] ;#BTN1
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E25} [get_ports touch_btn[1]] ;#BTN2
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F23} [get_ports touch_btn[2]] ;#BTN3
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E23} [get_ports touch_btn[3]] ;#BTN4
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H19} [get_ports touch_btn[4]] ;#BTN5
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F22} [get_ports touch_btn[5]] ;#BTN6

#required if touch_btn[4] used as manual clock source
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets touch_btn_IBUF[4]]
''',

'''#CPLD
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P20} [get_ports uart_wrn]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K22} [get_ports uart_rdn]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M20} [get_ports uart_tbre]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M16} [get_ports uart_tsre]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J24} [get_ports uart_dataready]
''',

'''#Ext serial
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L19} [get_ports txd] ;#GPIO5
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K21} [get_ports rxd] ;#GPIO6
''',

'''#USB
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K3} [get_ports sl811_a0]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M1} [get_ports sl811_we_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J3} [get_ports sl811_rd_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K1} [get_ports sl811_cs_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M2} [get_ports sl811_rst_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J4} [get_ports sl811_drq]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H3} [get_ports sl811_dack]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M4} [get_ports sl811_int]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L8} [get_ports sl811_data[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M6} [get_ports sl811_data[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L5} [get_ports sl811_data[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L7} [get_ports sl811_data[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L4} [get_ports sl811_data[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L3} [get_ports sl811_data[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L2} [get_ports sl811_data[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R7} [get_ports sl811_data[7]]
''',

'''#Ethernet
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D4} [get_ports dm9k_we_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D3} [get_ports dm9k_rd_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C3} [get_ports dm9k_cs_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C4} [get_ports dm9k_rst_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H8} [get_ports dm9k_int]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E3} [get_ports dm9k_cmd]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G1} [get_ports dm9k_data[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H2} [get_ports dm9k_data[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J1} [get_ports dm9k_data[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H7} [get_ports dm9k_data[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G4} [get_ports dm9k_data[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K2} [get_ports dm9k_data[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K7} [get_ports dm9k_data[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K6} [get_ports dm9k_data[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F3} [get_ports dm9k_data[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H6} [get_ports dm9k_data[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H4} [get_ports dm9k_data[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H1} [get_ports dm9k_data[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J5} [get_ports dm9k_data[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J6} [get_ports dm9k_data[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K5} [get_ports dm9k_data[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F5} [get_ports dm9k_data[15]]
''',

'''#Digital Video
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J21} [get_ports video_clk]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N18} [get_ports video_pixel[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N21} [get_ports video_pixel[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T19} [get_ports video_pixel[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U17} [get_ports video_pixel[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G20} [get_ports video_pixel[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M15} [get_ports video_pixel[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L18} [get_ports video_pixel[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M14} [get_ports video_pixel[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P16} [get_ports video_hsync]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R16} [get_ports video_vsync]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J20} [get_ports video_de]
''',

'''#LEDS
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A17} [get_ports leds[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G16} [get_ports leds[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E16} [get_ports leds[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H17} [get_ports leds[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G17} [get_ports leds[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F18} [get_ports leds[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F19} [get_ports leds[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F20} [get_ports leds[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C17} [get_ports leds[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F17} [get_ports leds[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B17} [get_ports leds[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D19} [get_ports leds[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A18} [get_ports leds[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A19} [get_ports leds[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E17} [get_ports leds[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E18} [get_ports leds[15]]

#number display 0
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D16} [get_ports leds[16]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F15} [get_ports leds[17]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H15} [get_ports leds[18]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G15} [get_ports leds[19]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H16} [get_ports leds[20]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H14} [get_ports leds[21]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G19} [get_ports leds[22]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J8} [get_ports leds[23]]

#DPY2
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H9} [get_ports leds[24]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G8} [get_ports leds[25]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G7} [get_ports leds[26]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G6} [get_ports leds[27]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D6} [get_ports leds[28]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E5} [get_ports leds[29]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F4} [get_ports leds[30]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G5} [get_ports leds[31]]
''',

'''#DIP_SW switches
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N3} [get_ports dip_sw[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N4} [get_ports dip_sw[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P3} [get_ports dip_sw[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P4} [get_ports dip_sw[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R5} [get_ports dip_sw[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T7} [get_ports dip_sw[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R8} [get_ports dip_sw[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T8} [get_ports dip_sw[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N2} [get_ports dip_sw[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N1} [get_ports dip_sw[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P1} [get_ports dip_sw[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R2} [get_ports dip_sw[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R1} [get_ports dip_sw[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T2} [get_ports dip_sw[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U1} [get_ports dip_sw[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U2} [get_ports dip_sw[15]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U6} [get_ports dip_sw[16]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R6} [get_ports dip_sw[17]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U5} [get_ports dip_sw[18]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T5} [get_ports dip_sw[19]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U4} [get_ports dip_sw[20]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T4} [get_ports dip_sw[21]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T3} [get_ports dip_sw[22]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R3} [get_ports dip_sw[23]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P5} [get_ports dip_sw[24]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P6} [get_ports dip_sw[25]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P8} [get_ports dip_sw[26]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N8} [get_ports dip_sw[27]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N6} [get_ports dip_sw[28]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N7} [get_ports dip_sw[29]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M7} [get_ports dip_sw[30]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M5} [get_ports dip_sw[31]]
''',

'''# flash
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K8}  [get_ports flash_a[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C26} [get_ports flash_a[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B26} [get_ports flash_a[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B25} [get_ports flash_a[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A25} [get_ports flash_a[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D24} [get_ports flash_a[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C24} [get_ports flash_a[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B24} [get_ports flash_a[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A24} [get_ports flash_a[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C23} [get_ports flash_a[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D23} [get_ports flash_a[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A23} [get_ports flash_a[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C21} [get_ports flash_a[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B21} [get_ports flash_a[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E22} [get_ports flash_a[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E21} [get_ports flash_a[15]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E20} [get_ports flash_a[16]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D21} [get_ports flash_a[17]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B20} [get_ports flash_a[18]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D20} [get_ports flash_a[19]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B19} [get_ports flash_a[20]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C19} [get_ports flash_a[21]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A20} [get_ports flash_a[22]]

set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F8} [get_ports flash_data[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E6} [get_ports flash_data[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B5} [get_ports flash_data[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A4} [get_ports flash_data[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A3} [get_ports flash_data[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B2} [get_ports flash_data[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C2} [get_ports flash_data[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F2} [get_ports flash_data[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F7} [get_ports flash_data[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A5} [get_ports flash_data[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D5} [get_ports flash_data[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B4} [get_ports flash_data[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A2} [get_ports flash_data[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B1} [get_ports flash_data[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G2} [get_ports flash_data[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E1} [get_ports flash_data[15]]

set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G9} [get_ports flash_byte_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN A22} [get_ports flash_ce_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D1} [get_ports flash_oe_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C22} [get_ports flash_rp_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN B22} [get_ports flash_vpen]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN C1} [get_ports flash_we_n]
''',

'''# base ram
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F24} [get_ports base_ram_addr[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G24} [get_ports base_ram_addr[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L24} [get_ports base_ram_addr[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L23} [get_ports base_ram_addr[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N16} [get_ports base_ram_addr[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G21} [get_ports base_ram_addr[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K17} [get_ports base_ram_addr[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L17} [get_ports base_ram_addr[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J15} [get_ports base_ram_addr[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H23} [get_ports base_ram_addr[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P14} [get_ports base_ram_addr[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L14} [get_ports base_ram_addr[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L15} [get_ports base_ram_addr[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K15} [get_ports base_ram_addr[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J14} [get_ports base_ram_addr[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M24} [get_ports base_ram_addr[15]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N17} [get_ports base_ram_addr[16]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N23} [get_ports base_ram_addr[17]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N24} [get_ports base_ram_addr[18]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P23} [get_ports base_ram_addr[19]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M26} [get_ports base_ram_be_n[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L25} [get_ports base_ram_be_n[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D26} [get_ports base_ram_be_n[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN D25} [get_ports base_ram_be_n[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M22} [get_ports base_ram_data[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N14} [get_ports base_ram_data[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N22} [get_ports base_ram_data[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R20} [get_ports base_ram_data[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M25} [get_ports base_ram_data[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N26} [get_ports base_ram_data[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P26} [get_ports base_ram_data[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P25} [get_ports base_ram_data[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J23} [get_ports base_ram_data[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J18} [get_ports base_ram_data[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN E26} [get_ports base_ram_data[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H21} [get_ports base_ram_data[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H22} [get_ports base_ram_data[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H18} [get_ports base_ram_data[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G22} [get_ports base_ram_data[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J16} [get_ports base_ram_data[15]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN N19} [get_ports base_ram_data[16]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P18} [get_ports base_ram_data[17]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P19} [get_ports base_ram_data[18]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R18} [get_ports base_ram_data[19]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K20} [get_ports base_ram_data[20]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M19} [get_ports base_ram_data[21]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN L22} [get_ports base_ram_data[22]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN M21} [get_ports base_ram_data[23]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K26} [get_ports base_ram_data[24]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K25} [get_ports base_ram_data[25]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J26} [get_ports base_ram_data[26]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN J25} [get_ports base_ram_data[27]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN H26} [get_ports base_ram_data[28]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G26} [get_ports base_ram_data[29]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN G25} [get_ports base_ram_data[30]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN F25} [get_ports base_ram_data[31]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K18} [get_ports base_ram_ce_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN K16} [get_ports base_ram_oe_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN P24} [get_ports base_ram_we_n]
''',

'''# extend ram
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN Y21} [get_ports ext_ram_addr[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN Y26} [get_ports ext_ram_addr[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AA25} [get_ports ext_ram_addr[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN Y22} [get_ports ext_ram_addr[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN Y23} [get_ports ext_ram_addr[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T18} [get_ports ext_ram_addr[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T23} [get_ports ext_ram_addr[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T24} [get_ports ext_ram_addr[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U19} [get_ports ext_ram_addr[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V24} [get_ports ext_ram_addr[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN W26} [get_ports ext_ram_addr[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN W24} [get_ports ext_ram_addr[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN Y25} [get_ports ext_ram_addr[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN W23} [get_ports ext_ram_addr[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN W21} [get_ports ext_ram_addr[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V14} [get_ports ext_ram_addr[15]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U14} [get_ports ext_ram_addr[16]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T14} [get_ports ext_ram_addr[17]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U15} [get_ports ext_ram_addr[18]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T15} [get_ports ext_ram_addr[19]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U26} [get_ports ext_ram_be_n[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T25} [get_ports ext_ram_be_n[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R17} [get_ports ext_ram_be_n[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R21} [get_ports ext_ram_be_n[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN W20} [get_ports ext_ram_data[0]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN W19} [get_ports ext_ram_data[1]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V19} [get_ports ext_ram_data[2]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN W18} [get_ports ext_ram_data[3]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V18} [get_ports ext_ram_data[4]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T17} [get_ports ext_ram_data[5]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V16} [get_ports ext_ram_data[6]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V17} [get_ports ext_ram_data[7]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V22} [get_ports ext_ram_data[8]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN W25} [get_ports ext_ram_data[9]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V23} [get_ports ext_ram_data[10]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V21} [get_ports ext_ram_data[11]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U22} [get_ports ext_ram_data[12]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN V26} [get_ports ext_ram_data[13]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U21} [get_ports ext_ram_data[14]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U25} [get_ports ext_ram_data[15]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AC24} [get_ports ext_ram_data[16]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AC26} [get_ports ext_ram_data[17]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AB25} [get_ports ext_ram_data[18]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AB24} [get_ports ext_ram_data[19]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AA22} [get_ports ext_ram_data[20]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AA24} [get_ports ext_ram_data[21]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AB26} [get_ports ext_ram_data[22]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN AA23} [get_ports ext_ram_data[23]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R25} [get_ports ext_ram_data[24]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R23} [get_ports ext_ram_data[25]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R26} [get_ports ext_ram_data[26]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U20} [get_ports ext_ram_data[27]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T22} [get_ports ext_ram_data[28]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R22} [get_ports ext_ram_data[29]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN T20} [get_ports ext_ram_data[30]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN R14} [get_ports ext_ram_data[31]]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN Y20} [get_ports ext_ram_ce_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U24} [get_ports ext_ram_oe_n]
set_property -dict {IOSTANDARD LVCMOS33 PACKAGE_PIN U16} [get_ports ext_ram_we_n]
''',

'''
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]
'''
]
pin_dict = {
	'clk_in': 'D18',
	'clk_uart_in': 'C18',
	'touch_btn[0]': 'J19',
	'touch_btn[1]': 'E25',
	'touch_btn[2]': 'F23',
	'touch_btn[3]': 'E23',
	'touch_btn[4]': 'H19',
	'touch_btn[5]': 'F22',
	'uart_wrn': 'P20',
	'uart_rdn': 'K22',
	'uart_tbre': 'M20',
	'uart_tsre': 'M16',
	'uart_dataready': 'J24',
	'txd': 'L19',
	'rxd': 'K21',
	'sl811_a0': 'K3',
	'sl811_we_n': 'M1',
	'sl811_rd_n': 'J3',
	'sl811_cs_n': 'K1',
	'sl811_rst_n': 'M2',
	'sl811_drq': 'J4',
	'sl811_dack': 'H3',
	'sl811_int': 'M4',
	'sl811_data[0]': 'L8',
	'sl811_data[1]': 'M6',
	'sl811_data[2]': 'L5',
	'sl811_data[3]': 'L7',
	'sl811_data[4]': 'L4',
	'sl811_data[5]': 'L3',
	'sl811_data[6]': 'L2',
	'sl811_data[7]': 'R7',
	'dm9k_we_n': 'D4',
	'dm9k_rd_n': 'D3',
	'dm9k_cs_n': 'C3',
	'dm9k_rst_n': 'C4',
	'dm9k_int': 'H8',
	'dm9k_cmd': 'E3',
	'dm9k_data[0]': 'G1',
	'dm9k_data[1]': 'H2',
	'dm9k_data[2]': 'J1',
	'dm9k_data[3]': 'H7',
	'dm9k_data[4]': 'G4',
	'dm9k_data[5]': 'K2',
	'dm9k_data[6]': 'K7',
	'dm9k_data[7]': 'K6',
	'dm9k_data[8]': 'F3',
	'dm9k_data[9]': 'H6',
	'dm9k_data[10]': 'H4',
	'dm9k_data[11]': 'H1',
	'dm9k_data[12]': 'J5',
	'dm9k_data[13]': 'J6',
	'dm9k_data[14]': 'K5',
	'dm9k_data[15]': 'F5',
	'video_clk': 'J21',
	'video_pixel[7]': 'N18',
	'video_pixel[6]': 'N21',
	'video_pixel[5]': 'T19',
	'video_pixel[4]': 'U17',
	'video_pixel[3]': 'G20',
	'video_pixel[2]': 'M15',
	'video_pixel[1]': 'L18',
	'video_pixel[0]': 'M14',
	'video_hsync': 'P16',
	'video_vsync': 'R16',
	'video_de': 'J20',
	'leds[0]': 'A17',
	'leds[1]': 'G16',
	'leds[2]': 'E16',
	'leds[3]': 'H17',
	'leds[4]': 'G17',
	'leds[5]': 'F18',
	'leds[6]': 'F19',
	'leds[7]': 'F20',
	'leds[8]': 'C17',
	'leds[9]': 'F17',
	'leds[10]': 'B17',
	'leds[11]': 'D19',
	'leds[12]': 'A18',
	'leds[13]': 'A19',
	'leds[14]': 'E17',
	'leds[15]': 'E18',
	'leds[16]': 'D16',
	'leds[17]': 'H14',
	'leds[18]': 'H16',
	'leds[19]': 'F15',
	'leds[20]': 'H15',
	'leds[21]': 'G15',
	'leds[22]': 'G19',
	'leds[23]': 'J8',
	'leds[24]': 'H9',
	'leds[25]': 'E5',
	'leds[26]': 'D6',
	'leds[27]': 'G8',
	'leds[28]': 'G7',
	'leds[29]': 'G6',
	'leds[30]': 'F4',
	'leds[31]': 'G5',
	'dip_sw[0]': 'N3',
	'dip_sw[1]': 'N4',
	'dip_sw[2]': 'P3',
	'dip_sw[3]': 'P4',
	'dip_sw[4]': 'R5',
	'dip_sw[5]': 'T7',
	'dip_sw[6]': 'R8',
	'dip_sw[7]': 'T8',
	'dip_sw[8]': 'N2',
	'dip_sw[9]': 'N1',
	'dip_sw[10]': 'P1',
	'dip_sw[11]': 'R2',
	'dip_sw[12]': 'R1',
	'dip_sw[13]': 'T2',
	'dip_sw[14]': 'U1',
	'dip_sw[15]': 'U2',
	'dip_sw[16]': 'U6',
	'dip_sw[17]': 'R6',
	'dip_sw[18]': 'U5',
	'dip_sw[19]': 'T5',
	'dip_sw[20]': 'U4',
	'dip_sw[21]': 'T4',
	'dip_sw[22]': 'T3',
	'dip_sw[23]': 'R3',
	'dip_sw[24]': 'P5',
	'dip_sw[25]': 'P6',
	'dip_sw[26]': 'P8',
	'dip_sw[27]': 'N8',
	'dip_sw[28]': 'N6',
	'dip_sw[29]': 'N7',
	'dip_sw[30]': 'M7',
	'dip_sw[31]': 'M5',
	'flash_a[0]': 'K8',
	'flash_a[1]': 'C26',
	'flash_a[2]': 'B26',
	'flash_a[3]': 'B25',
	'flash_a[4]': 'A25',
	'flash_a[5]': 'D24',
	'flash_a[6]': 'C24',
	'flash_a[7]': 'B24',
	'flash_a[8]': 'A24',
	'flash_a[9]': 'C23',
	'flash_a[10]': 'D23',
	'flash_a[11]': 'A23',
	'flash_a[12]': 'C21',
	'flash_a[13]': 'B21',
	'flash_a[14]': 'E22',
	'flash_a[15]': 'E21',
	'flash_a[16]': 'E20',
	'flash_a[17]': 'D21',
	'flash_a[18]': 'B20',
	'flash_a[19]': 'D20',
	'flash_a[20]': 'B19',
	'flash_a[21]': 'C19',
	'flash_a[22]': 'A20',
	'flash_data[0]': 'F8',
	'flash_data[1]': 'E6',
	'flash_data[2]': 'B5',
	'flash_data[3]': 'A4',
	'flash_data[4]': 'A3',
	'flash_data[5]': 'B2',
	'flash_data[6]': 'C2',
	'flash_data[7]': 'F2',
	'flash_data[8]': 'F7',
	'flash_data[9]': 'A5',
	'flash_data[10]': 'D5',
	'flash_data[11]': 'B4',
	'flash_data[12]': 'A2',
	'flash_data[13]': 'B1',
	'flash_data[14]': 'G2',
	'flash_data[15]': 'E1',
	'flash_byte_n': 'G9',
	'flash_ce_n': 'A22',
	'flash_oe_n': 'D1',
	'flash_rp_n': 'C22',
	'flash_vpen': 'B22',
	'flash_we_n': 'C1',
	'base_ram_addr[0]': 'F24',
	'base_ram_addr[1]': 'G24',
	'base_ram_addr[2]': 'L24',
	'base_ram_addr[3]': 'L23',
	'base_ram_addr[4]': 'N16',
	'base_ram_addr[5]': 'G21',
	'base_ram_addr[6]': 'K17',
	'base_ram_addr[7]': 'L17',
	'base_ram_addr[8]': 'J15',
	'base_ram_addr[9]': 'H23',
	'base_ram_addr[10]': 'P14',
	'base_ram_addr[11]': 'L14',
	'base_ram_addr[12]': 'L15',
	'base_ram_addr[13]': 'K15',
	'base_ram_addr[14]': 'J14',
	'base_ram_addr[15]': 'M24',
	'base_ram_addr[16]': 'N17',
	'base_ram_addr[17]': 'N23',
	'base_ram_addr[18]': 'N24',
	'base_ram_addr[19]': 'P23',
	'base_ram_be_n[0]': 'M26',
	'base_ram_be_n[1]': 'L25',
	'base_ram_be_n[2]': 'D26',
	'base_ram_be_n[3]': 'D25',
	'base_ram_data[0]': 'M22',
	'base_ram_data[1]': 'N14',
	'base_ram_data[2]': 'N22',
	'base_ram_data[3]': 'R20',
	'base_ram_data[4]': 'M25',
	'base_ram_data[5]': 'N26',
	'base_ram_data[6]': 'P26',
	'base_ram_data[7]': 'P25',
	'base_ram_data[8]': 'J23',
	'base_ram_data[9]': 'J18',
	'base_ram_data[10]': 'E26',
	'base_ram_data[11]': 'H21',
	'base_ram_data[12]': 'H22',
	'base_ram_data[13]': 'H18',
	'base_ram_data[14]': 'G22',
	'base_ram_data[15]': 'J16',
	'base_ram_data[16]': 'N19',
	'base_ram_data[17]': 'P18',
	'base_ram_data[18]': 'P19',
	'base_ram_data[19]': 'R18',
	'base_ram_data[20]': 'K20',
	'base_ram_data[21]': 'M19',
	'base_ram_data[22]': 'L22',
	'base_ram_data[23]': 'M21',
	'base_ram_data[24]': 'K26',
	'base_ram_data[25]': 'K25',
	'base_ram_data[26]': 'J26',
	'base_ram_data[27]': 'J25',
	'base_ram_data[28]': 'H26',
	'base_ram_data[29]': 'G26',
	'base_ram_data[30]': 'G25',
	'base_ram_data[31]': 'F25',
	'base_ram_ce_n': 'K18',
	'base_ram_oe_n': 'K16',
	'base_ram_we_n': 'P24',
	'ext_ram_addr[0]': 'Y21',
	'ext_ram_addr[1]': 'Y26',
	'ext_ram_addr[2]': 'AA25',
	'ext_ram_addr[3]': 'Y22',
	'ext_ram_addr[4]': 'Y23',
	'ext_ram_addr[5]': 'T18',
	'ext_ram_addr[6]': 'T23',
	'ext_ram_addr[7]': 'T24',
	'ext_ram_addr[8]': 'U19',
	'ext_ram_addr[9]': 'V24',
	'ext_ram_addr[10]': 'W26',
	'ext_ram_addr[11]': 'W24',
	'ext_ram_addr[12]': 'Y25',
	'ext_ram_addr[13]': 'W23',
	'ext_ram_addr[14]': 'W21',
	'ext_ram_addr[15]': 'V14',
	'ext_ram_addr[16]': 'U14',
	'ext_ram_addr[17]': 'T14',
	'ext_ram_addr[18]': 'U15',
	'ext_ram_addr[19]': 'T15',
	'ext_ram_be_n[0]': 'U26',
	'ext_ram_be_n[1]': 'T25',
	'ext_ram_be_n[2]': 'R17',
	'ext_ram_be_n[3]': 'R21',
	'ext_ram_data[0]': 'W20',
	'ext_ram_data[1]': 'W19',
	'ext_ram_data[2]': 'V19',
	'ext_ram_data[3]': 'W18',
	'ext_ram_data[4]': 'V18',
	'ext_ram_data[5]': 'T17',
	'ext_ram_data[6]': 'V16',
	'ext_ram_data[7]': 'V17',
	'ext_ram_data[8]': 'V22',
	'ext_ram_data[9]': 'W25',
	'ext_ram_data[10]': 'V23',
	'ext_ram_data[11]': 'V21',
	'ext_ram_data[12]': 'U22',
	'ext_ram_data[13]': 'V26',
	'ext_ram_data[14]': 'U21',
	'ext_ram_data[15]': 'U25',
	'ext_ram_data[16]': 'AC24',
	'ext_ram_data[17]': 'AC26',
	'ext_ram_data[18]': 'AB25',
	'ext_ram_data[19]': 'AB24',
	'ext_ram_data[20]': 'AA22',
	'ext_ram_data[21]': 'AA24',
	'ext_ram_data[22]': 'AB26',
	'ext_ram_data[23]': 'AA23',
	'ext_ram_data[24]': 'R25',
	'ext_ram_data[25]': 'R23',
	'ext_ram_data[26]': 'R26',
	'ext_ram_data[27]': 'U20',
	'ext_ram_data[28]': 'T22',
	'ext_ram_data[29]': 'R22',
	'ext_ram_data[30]': 'T20',
	'ext_ram_data[31]': 'R14',
	'ext_ram_ce_n': 'Y20',
	'ext_ram_oe_n': 'U24',
	'ext_ram_we_n': 'U16'
}
set_pin_str = \
    'set_property -dict {{IOSTANDARD LVCMOS33 PACKAGE_PIN {pin}}} [get_ports {port}]'
set_dedicate_str = 'set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets {port}_IBUF]'
clk_in = 'create_clock -period 20.000 -name {port} -waveform {{0.000 10.000}} [get_ports {port}]'
clk_uart_in = 'create_clock -period 90.422 -name {port} -waveform {{0.000 45.211}} [get_ports {port}]'
default_str = '''set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]'''

friendly_names = {
    'clk_in': '主时钟 50 MHz', 'clk_uart_in': 'uart时钟 11.0592 MHz',
    'touch_btn': 'touch_btn',
    'uart_wrn': 'uart_wrn', 'uart_rdn': 'uart_rdn', 'uart_tbre': 'uart_tbre', 'uart_tsre': 'uart_tsre', 'uart_dataready': 'uart_dataready',
    'txd': 'txd', 'rxd': 'rxd',
    'sl811_a0': 'sl811_a0', 'sl811_we_n': 'sl811_we_n', 'sl811_rd_n': 'sl811_rd_n', 'sl811_cs_n': 'sl811_cs_n', 'sl811_rst_n': 'sl811_rst_n', 'sl811_drq': 'sl811_drq', 'sl811_dack': 'sl811_dack', 'sl811_int': 'sl811_int', 'sl811_data': 'sl811_data',
    'dm9k_we_n': 'dm9k_we_n', 'dm9k_rd_n': 'dm9k_rd_n', 'dm9k_cs_n': 'dm9k_cs_n', 'dm9k_rst_n': 'dm9k_rst_n', 'dm9k_int': 'dm9k_int', 'dm9k_cmd': 'dm9k_cmd', 'dm9k_data': 'dm9k_data',
    'video_clk': 'video_clk', 'video_pixel': 'video_pixel', 'video_hsync': 'video_hsync', 'video_vsync': 'video_vsync', 'video_de': 'video_de',
    'leds': 'leds',
    'dip_sw': 'dip_sw',
    'flash_a': 'flash_a', 'flash_data': 'flash_data', 'flash_byte_n': 'flash_byte_n', 'flash_ce_n': 'flash_ce_n', 'flash_oe_n': 'flash_oe_n', 'flash_rp_n': 'flash_rp_n', 'flash_vpen': 'flash_vpen', 'flash_we_n': 'flash_we_n',
    'base_ram_addr': 'base_ram_addr', 'base_ram_be_n': 'base_ram_be_n', 'base_ram_data': 'base_ram_data', 'base_ram_ce_n': 'base_ram_ce_n', 'base_ram_oe_n': 'base_ram_oe_n', 'base_ram_we_n': 'base_ram_we_n',
    'ext_ram_addr': 'ext_ram_addr', 'ext_ram_be_n': 'ext_ram_be_n', 'ext_ram_data': 'ext_ram_data', 'ext_ram_ce_n': 'ext_ram_ce_n', 'ext_ram_oe_n': 'ext_ram_oe_n', 'ext_ram_we_n': 'ext_ram_we_n'
}
varnames = [
    ['clk_in', 'clk_uart_in'],
    ['touch_btn'],
    ['uart_wrn', 'uart_rdn', 'uart_tbre', 'uart_tsre', 'uart_dataready'],
    ['txd', 'rxd'],
    ['sl811_a0', 'sl811_we_n', 'sl811_rd_n', 'sl811_cs_n', 'sl811_rst_n', 'sl811_drq', 'sl811_dack', 'sl811_int', 'sl811_data'],
    ['dm9k_we_n', 'dm9k_rd_n', 'dm9k_cs_n', 'dm9k_rst_n', 'dm9k_int', 'dm9k_cmd', 'dm9k_data'],
    ['video_clk', 'video_pixel', 'video_hsync', 'video_vsync', 'video_de'],
    ['leds'],
    ['dip_sw'],
    ['flash_a', 'flash_data', 'flash_byte_n', 'flash_ce_n', 'flash_oe_n', 'flash_rp_n', 'flash_vpen', 'flash_we_n'],
    ['base_ram_addr', 'base_ram_be_n', 'base_ram_data', 'base_ram_ce_n', 'base_ram_oe_n', 'base_ram_we_n'],
    ['ext_ram_addr', 'ext_ram_be_n', 'ext_ram_data', 'ext_ram_ce_n', 'ext_ram_oe_n', 'ext_ram_we_n'],
    []
]
varname_ranges = [
    {'clk_in': range(0, 1), 'clk_uart_in': range(0, 1)},
    {'touch_btn': range(0, 6)},
    {'uart_wrn': range(0, 1), 'uart_rdn': range(0, 1), 'uart_tbre': range(0, 1), 'uart_tsre': range(0, 1),
     'uart_dataready': range(0, 1)},
    {'txd': range(0, 1), 'rxd': range(0, 1)},
    {'sl811_a0': range(0, 1), 'sl811_we_n': range(0, 1), 'sl811_rd_n': range(0, 1), 'sl811_cs_n': range(0, 1),
     'sl811_rst_n': range(0, 1), 'sl811_drq': range(0, 1), 'sl811_dack': range(0, 1), 'sl811_int': range(0, 1),
     'sl811_data': range(0, 8)},
    {'dm9k_we_n': range(0, 1), 'dm9k_rd_n': range(0, 1), 'dm9k_cs_n': range(0, 1), 'dm9k_rst_n': range(0, 1),
     'dm9k_int': range(0, 1), 'dm9k_cmd': range(0, 1), 'dm9k_data': range(0, 16)},
    {'video_clk': range(0, 1), 'video_pixel': range(0, 8), 'video_hsync': range(0, 1), 'video_vsync': range(0, 1),
     'video_de': range(0, 1)},
    {'leds': range(0, 32)},
    {'dip_sw': range(0, 32)},
    {'flash_a': range(0, 23), 'flash_data': range(0, 16), 'flash_byte_n': range(0, 1), 'flash_ce_n': range(0, 1),
     'flash_oe_n': range(0, 1), 'flash_rp_n': range(0, 1), 'flash_vpen': range(0, 1), 'flash_we_n': range(0, 1)},
    {'base_ram_addr': range(0, 20), 'base_ram_be_n': range(0, 4), 'base_ram_data': range(0, 32),
     'base_ram_ce_n': range(0, 1), 'base_ram_oe_n': range(0, 1), 'base_ram_we_n': range(0, 1)},
    {'ext_ram_addr': range(0, 20), 'ext_ram_be_n': range(0, 4), 'ext_ram_data': range(0, 32),
     'ext_ram_ce_n': range(0, 1), 'ext_ram_oe_n': range(0, 1), 'ext_ram_we_n': range(0, 1)},
    {}
]
docs = [
    '高频时钟',
    '按钮，0-3为普通按钮，4-5为微动',
    'cpld',
    'ext serial',
    'usb',  # 5
    'ethernet',
    'video',
    'leds, 0-15为二极管, 16-31为数码管',
    '拨码开关',  # 10
    'flash',
    'base ram',
    'extend ram',
    'default',
]
docs_infile = [
    'clocks',
    'button, 0-3 red, 4-5 click',
    'cpld',
    'ext serial',
    'usb',  # 5
    'ethernet',
    'video',
    'leds',
    'switches',
    'flash',
    'base ram',
    'extend ram',
    'default',
]
for i, s in enumerate(docs_infile):
    docs_infile[i] = '# ' + s
