from platform import system
from os import system as cmd
from colors import *
import pyfiglet
import time

def get_cls_syscommand() -> str:
    return 'cls' if(system() == 'Windows') else 'clear' 
clearscreen = lambda: cmd(get_cls_syscommand())

def ascii_banner():
    bnr = pyfiglet.Figlet(font='cosmic', justify='right', width=100)
    bdr = pyfiglet.Figlet(justify='right', width=100)
    print(f'{YELLOW}{bdr.renderText("-"*16)}')
    print(f'{GREEN}{bnr.renderText("$_c_4_N_n_3_R")}')
    print(f'{GREEN}{bnr.renderText("M_4_N")}')
    print(f'{YELLOW}{bdr.renderText("-"*16)}')  

def disclaimer():
    print(f'''{MAGENTA}
                        Disclaimer: Use of this tool and others like it require
                          permission from the owner of the target domain/site.
                       Proceeding without proper authorization may be illegal and 
                        may result in lawful prosecution or lawsuits. It is your 
                       responsability to understand the law before using this tool. 
                                            Act responsibly.
          {RESET}''')
    time.sleep(2)
    continue_prompt = 'press [ENTER] to continue...'
    padding=int((100/2) + (len(continue_prompt) / 2))
    message=str.rjust(continue_prompt, padding)
    input(f'{YELLOW}{message}')

def menu_selection() -> str:
    print(f'\n{YELLOW}Please choose a scan option ({BLUE}1-6{YELLOW})')
    print(f'{GREEN}'+str.ljust('',65,'-'))
    print(f'\n{YELLOW}  '+str.ljust('Sub Domain Scan',55,'.'),f'{BLUE}1')
    print(f'\n{YELLOW}  '+str.ljust('Directory Scan',55,'.'),f'{BLUE}2')
    print(f'\n{YELLOW}  '+str.ljust('Port Scan',55,'.'),f'{BLUE}3')
    print(f'\n{YELLOW}  '+str.ljust('Full Scan',55,'.'),f'{BLUE}4')
    print(f'\n{YELLOW}  '+str.ljust('EXIT',55,'.'),f'{BLUE}5')
    print(f'\n{GREEN}'+str.ljust('',65,'-'))
    selection=str(input(f'{YELLOW}Selection: {BLUE}'))
    print(f'{RESET}')
    return selection

def title_disclaimer():
    clearscreen()
    ascii_banner()
    disclaimer()
