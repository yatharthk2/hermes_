from colorama import Fore
from chalicelib.mongo_code.data.mongo_setup import global_init
from chalicelib.mongo_code import program_hosts


def main():
    global_init()

    print_header()


    program_hosts.run()



def print_header():
    

    print(Fore.RED + '**************** Hermes.ai  ****************')
    print(Fore.GREEN )
    print("Welcome to Hermes.ai")
    print()

if __name__ == '__main__':
    main()
