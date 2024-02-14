from Scanner_util import Scanner
import menu_functions
from colors import *

def main():
    subs_found = list()
    dirs_found = list()
    ports_found = list()

    type_scan = menu_functions.menu_selection()
    if((type_scan >= '1') and (type_scan <= '4')):
        scanner = Scanner(str(input(f'{YELLOW}{chr(0x0a)}Enter the target domain and domain extension (example.com): {BLUE}')))

    match type_scan:
        
        case '1': #sub directories
            scanner.get_wordlist()
            subs_found = scanner.scan_type.subscan()
            print(f'{chr(0x0a)}{YELLOW}SCAN COMPLETE :: {BLUE}{scanner.domain}{YELLOW} :: PRINTING FOUND SUBDOMAINS{RESET}')
            scanner.print_results(subs_found)

        case '2': #directories
            scanner.get_wordlist()
            dirs_found=scanner.scan_type.dirscan()
            print(f'{chr(0x0a)}{YELLOW}SCAN COMPLETE :: {BLUE}{scanner.domain}{YELLOW} :: PRINTING FOUND DIRECTORIES{RESET}')
            scanner.print_results(dirs_found)

        case '3': #ports
            scanner.get_port_range()
            ports_found = scanner.scan_type.portscan()
            print(f'{chr(0x0a)}{YELLOW}SCAN COMPLETE :: {BLUE}{scanner.domain}{YELLOW} :: PRINTING FOUND PORTS{RESET}')
            scanner.print_results(ports_found)

        case '4': #full
            scanner.get_wordlist()
            scanner.get_port_range()
            ports_found = scanner.scan_type.portscan()
            subs_found = scanner.scan_type.subscan()
            dirs_found = scanner.scan_type.dirscan()
            print(f'{chr(0x0a)*2}{YELLOW}SCAN COMPLETE :: {BLUE}{scanner.domain}{YELLOW} :: PRINTING RESULTS{RESET}')
            print(f'{chr(0x0a)}{YELLOW}FOUND SUBDOMAINS')
            scanner.print_results(subs_found)
            print(f'{chr(0x0a)}{YELLOW}FOUND DIRECTORIES{RESET}')
            scanner.print_results(dirs_found)
            print(f'{chr(0x0a)}{YELLOW}PRINTING FOUND PORTS{RESET}')
            scanner.print_results(ports_found)

        case '5': #exit
            print(f'{GREEN}Exiting...{RESET}')

        case _: #default
            print(f'{RED}Error: One or more invalid selections.{chr(0x0a)}Please check if your selection is available or refer to the manual.{chr(0x0a)}Exiting Scanner...{RESET}')
    
    input(f'{YELLOW}Press [ENTER] to EXIT{RESET}')

if (__name__ == "__main__"):
    menu_functions.title_disclaimer()
    main()
