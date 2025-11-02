#!/usr/bin/env python3
import os
import sys
import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class AlfaRootUserAgentGenerator:
    def __init__(self):
        self.browsers = [
            "Chrome", "Firefox", "Safari", "Edge", "Opera"
        ]
        self.os_list = [
            "Windows", "Macintosh", "Linux", "Android", "iOS"
        ]

    def generate_banner(self):
        os.system('clear')
        print(f"""
{Fore.YELLOW}
 █████╗ ██╗     ███████╗ █████╗     ██████╗  ██████╗  ██████╗ ████████╗
██╔══██╗██║     ██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝
███████║██║     █████╗  ███████║    ██████╔╝██║   ██║██║   ██║   ██║   
██╔══██║██║     ██╔══╝  ██╔══██║    ██╔══██╗██║   ██║██║   ██║   ██║   
██║  ██║███████╗██║     ██║  ██║    ██║  ██║╚██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   
{Fore.GREEN}
[+] Team: ACS
[+] Tool: Alfa Root User Agent Generator
[+] Version: 1.0
{Style.RESET_ALL}
""")

    def generate_user_agent(self):
        browser = random.choice(self.browsers)
        os_name = random.choice(self.os_list)
        version_major = random.randint(80, 110)
        version_minor = random.randint(0, 9)
        
        templates = [
            f"Mozilla/5.0 ({os_name}; {browser}/{version_major}.{version_minor})",
            f"Mozilla/5.0 (X11; {os_name} x86_64) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version_major}.{version_minor}",
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{version_major}.{version_minor}"
        ]
        
        return random.choice(templates)

    def generate_multiple_user_agents(self, count):
        print(f"\n{Fore.CYAN}[*] Generating User Agents...{Style.RESET_ALL}")
        user_agents = set()
        
        progress_chars = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        
        for i in range(count):
            while len(user_agents) < count:
                ua = self.generate_user_agent()
                user_agents.add(ua)
                
                # Animated progress
                sys.stdout.write(f"\r{Fore.GREEN}[{progress_chars[i % len(progress_chars)]}] Generated: {len(user_agents)}/{count}{Style.RESET_ALL}")
                sys.stdout.flush()
                time.sleep(0.1)
        
        return list(user_agents)

    def save_user_agents(self, user_agents):
        os.makedirs('output', exist_ok=True)
        filename = f'output/user_agents_{int(time.time())}.txt'
        
        with open(filename, 'w') as f:
            for ua in user_agents:
                f.write(f"{ua}\n")
        
        print(f"\n{Fore.GREEN}[✓] User Agents saved to {filename}{Style.RESET_ALL}")

    def run(self):
        self.generate_banner()
        
        while True:
            try:
                count = int(input(f"{Fore.YELLOW}[?] Enter number of User Agents to generate (max 1000): {Style.RESET_ALL}"))
                
                if 1 <= count <= 1000:
                    user_agents = self.generate_multiple_user_agents(count)
                    
                    # Preview first 10 UAs
                    print(f"\n{Fore.MAGENTA}[Preview] First 10 User Agents:{Style.RESET_ALL}")
                    for ua in user_agents[:10]:
                        print(f"{Fore.CYAN}• {ua}{Style.RESET_ALL}")
                    
                    save_choice = input(f"{Fore.GREEN}[?] Save User Agents to file? (y/n): {Style.RESET_ALL}").lower()
                    
                    if save_choice == 'y':
                        self.save_user_agents(user_agents)
                    
                    continue_choice = input(f"{Fore.YELLOW}[?] Generate more User Agents? (y/n): {Style.RESET_ALL}").lower()
                    
                    if continue_choice != 'y':
                        break
                else:
                    print(f"{Fore.RED}[!] Please enter a number between 1 and 1000.{Style.RESET_ALL}")
            
            except ValueError:
                print(f"{Fore.RED}[!] Invalid input. Please enter a number.{Style.RESET_ALL}")

def main():
    try:
        generator = AlfaRootUserAgentGenerator()
        generator.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Exiting...{Style.RESET_ALL}")
        sys.exit(0)

if __name__ == "__main__":
    main()
