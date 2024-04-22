try:
    from googlesearch import search
    import time
    import argparse
    from colorama import Fore, Style
except ImportError: 
    print("No module found")
    
def banner():
    txt = ("""
 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ 
 
                                                                            v1.0 """)
    
    author = ("""
 Author:  Alfian Nurrizky
 Github:  https://github.com/alfiannurrizky
 Linkedin: https://www.linkedin.com/in/alfian-nurrizky/ \n\n""")
    print(txt)
    print(author)
  
def query(domain, payload, take):
    counter = 0
    results_found = False
    
    for result in search("site:" + domain +" "+  payload, num=int(take), stop=int(take), pause=5):
        counter += 1
        results_found = True
        
        print(f"[+]{Fore.GREEN} {counter}. Payload {payload} -> {result}")
        
        time.sleep(0.1)
                
        if counter == int(take):
            print("\n")
            break
                
        time.sleep(0.1)
        
    if not results_found:
        print("\033[1;91m[!] No Results Found! \033[0m\n")

 
def dorking():
    banner()

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--domain", help="Input domain e.g google.com")
        parser.add_argument("-t", "--take", help="Number of result you want")
        parser.add_argument("-w", "--wordlist", help="Path to the wordlist file (OPTIONAL)")
        args = parser.parse_args()
        parser.parse_args()
        
        if not args.domain and not args.take:
            parser.error("Please provide either the -d option and the -t option.")
        elif not args.domain:
            parser.error("Please provide either the -d option")
        elif not args.take:
            parser.error("Please provide either the -t option")
        
        count = 0
        if args.wordlist:
            payload_file = open(args.wordlist, "r")
        else:
            payload_file = open('payload.txt', "r")
            
        lines = payload_file.readlines()
        
        for line in lines:
            count += 1
            payload = line.strip()
        
            termwidth = 100
            print(f"╭{'─' * (termwidth - 2)}╮\n{Fore.YELLOW} ╰─> SEARCHING FOR PAYLOAD{Style.RESET_ALL} : {Fore.WHITE}{payload}\n{Style.RESET_ALL}╰{'─' * (termwidth - 2)}╯\n")
        
            query(args.domain, payload, args.take)
            
    except KeyboardInterrupt:
        print("\n")
        print(f"{Fore.RED}[!] Byee See You Again..!\033[0m\n")
        time.sleep(1)
        
    print ("[!] DORKING DONE...")
    print ("\n\033[34mGDORKS\033[0m\n")
    print ("\033[1;91m[!] SEE YOU! \033[0m\n\n")


if __name__ == "__main__":
    dorking()
        