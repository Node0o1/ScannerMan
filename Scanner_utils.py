from multiprocessing import Pool as Thread
import requests
import socket
from colors import *
from globals import *

class Scanner:
    domain = str()
    wordlist = list()
    port_start = int()
    port_end = int()

    @classmethod
    def __init__(self, domain):
        self.domain = domain
        self.scan_type = self.Scans(self)

    @staticmethod
    def spawn(func, scan_list) -> list:
        thread = Thread(processes = NUM_OF_THREADS, maxtasksperchild = MAX_TASK_PER_INSTANCE)  
        results = list(thread.map(func, scan_list ))
        thread.close()
        thread.join()
        return results
    
    @staticmethod
    def scan(sub_domain) -> str:
        try:
            response = requests.get(sub_domain, timeout = SCAN_TIMEOUT)
            status_code = response.status_code
            response.close()
        except:
            print(f'{RED}[-] {sub_domain}')
            return None
        else:
            if ((status_code >= 200) and (status_code <=299)):
                print(f'{GREEN}[+] {sub_domain}')
                return sub_domain
            else:
                print(f'{RED}[-] {sub_domain}')
                return None

    @staticmethod
    def probe(domain_port) -> int:
        (domain, port) = tuple(domain_port.split(':'))
        port = int(port)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(SOCK_TIMEOUT)
            host=socket.gethostbyname(domain)
            is_open_port = sock.connect_ex((host, port))
        sock.close()
        if(is_open_port == 0):
            print(f'{GREEN}[+] port #{port} connected')
            result = port
        else:
            print(f'{RED}[-]port #{port} failed')
            result = None
        return result
    
    @staticmethod
    def cleanup(found) -> list:
        results=list()
        for item in found:
            if((not item == None) and (not item in results)):
                results.append(item)
        return results
    
    @staticmethod
    def print_results(results):
        print(f'{YELLOW}RESULTS: {BLUE}{len(results)}{chr(0x0a)}')
        print([item for item in results])
        print(f'{RESET}')

    @classmethod
    def get_wordlist(self):
        try:
            infile=str(input(f'{YELLOW}Enter the path/to/wordlist.txt: {BLUE}'))
            with open(infile, mode = 'r') as fhandle:
                wordlist = fhandle.read()
                self.wordlist=wordlist.split('\n')
        except:
            print(f'{RED}ERROR: Wordlist {infile} does not exist.{chr(0x0a)}Exiting self...{RESET}')
            exit()

    @classmethod
    def get_port_range(self):
        try:
            self.port_start = int(input(f'{YELLOW}Enter the starting port #: {BLUE}'))
            self.port_end = int(input(f'{YELLOW}Enter the ending port #: {BLUE}'))
        except:
            print(f'{RED}Port numbers must be integer type.{chr(0x0a)}Exiting self...')
            exit()
    
    class Scans:
        @classmethod
        def __init__(self, Scanner):
            self.Scanner = Scanner

        @classmethod
        def subscan(self) -> list:
            print(f'{chr(0x0a)}{GREEN}Scanning {BLUE}{self.Scanner.domain}{GREEN} for sub domains.{chr(0x0a)}{YELLOW}Please wait...{chr(0x0a)}')
            scan_list=list([f'https://{word}.{self.Scanner.domain}' for word in self.Scanner.wordlist])
            func=self.Scanner.scan 
            found = self.Scanner.spawn(func, scan_list)
            return self.Scanner.cleanup(found)

        @classmethod
        def dirscan(self) -> list:
            print(f'{chr(0x0a)}{GREEN}Scanning {BLUE}{self.Scanner.domain}{GREEN} for directories.{chr(0x0a)}{YELLOW}Please wait...{chr(0x0a)}')
            scan_list=list([f'https://{self.Scanner.domain}/{word}' for word in self.Scanner.wordlist])
            func = self.Scanner.scan
            found = self.Scanner.spawn(func, scan_list)
            return self.Scanner.cleanup(found)

        @classmethod
        def portscan(self) -> list:
            print(f'{chr(0x0a)}{GREEN}Scanning {BLUE}{self.Scanner.domain}{GREEN} port #\'s {BLUE}{self.Scanner.port_start} - {self.Scanner.port_end}{chr(0x0a)}{YELLOW}Please wait...{chr(0x0a)}')
            scan_list=list([f'{self.Scanner.domain}:{port}' for port in range(self.Scanner.port_start, self.Scanner.port_end+1)])
            func = self.Scanner.probe
            found = self.Scanner.spawn(func, scan_list)
            return self.Scanner.cleanup(found)
        
