import requests
import threading
import time
import os

# ========== Banner function with yellow CDF line ==========
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    print(r"""
   ██████╗
  ██╔════╝
  ██║
  ██║
  ╚██████╗
   ╚═════╝
                +_______________________________+
  ██████╗       |                               |
  ██╔══██╗      |    This tool is Developed     |
  ██║  ██║      |             By                |
  ██║  ██║      |                               |
  ██████╔╝      |       </ x!t eXploiteR>       |
  ╚═════╝       |                               |
                |                               |
  ███████╗      |                               |
  ██╔════╝      +_______________________________+
  █████╗
  ██╔══╝
  ██║
  ╚═╝
""")
    print(YELLOW + "        [ Admin Panel Finder | By Team CDF ]" + RESET)


# ========== SETTINGS ==========
THREADS = 10
WORDLIST_FILE = "admins.txt"  # Wordlist filename
HEADERS = {
    "User-Agent": "Mozilla/5.0 (CDF Scanner)"
}
TIMEOUT = 10  # seconds timeout for requests

found_panels = []  # Store found admin panels


# ========== Function to scan each path ==========
def scan_path(target, path):
    url = target.rstrip("/") + "/" + path.strip()
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        text_lower = r.text.lower()
        if r.status_code == 200 and "login" in text_lower:
            print(f"[+] Possible Admin Panel Found: {url}")
            found_panels.append(url)
        elif any(error in text_lower for error in ["sql syntax", "mysql", "error in your sql"]):
            print(f"[!] SQLi Warning: {url}")
    except requests.RequestException:
        # Could log errors here if needed
        pass


# ========== Function to start scanning with threads ==========
def start_scan(target, wordlist):
    threads = []
    for path in wordlist:
        while threading.active_count() > THREADS:
            time.sleep(0.1)
        t = threading.Thread(target=scan_path, args=(target, path))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


# ========== MAIN ==========
if __name__ == "__main__":
    banner()

    target = input("Enter Target Website URL (with http/https): ").strip()
    if not target.startswith("http"):
        print("[-] ERROR: Please include http:// or https:// in the URL")
        exit()

    try:
        with open(WORDLIST_FILE, "r") as f:
            wordlist = f.readlines()
    except FileNotFoundError:
        print(f"[-] ERROR: Wordlist '{WORDLIST_FILE}' not found!")
        exit()

    print(f"\n[+] Starting scan on {target} with {len(wordlist)} paths...\n")
    start_scan(target, wordlist)

    print("\n[✔] Scan Complete!")
    if found_panels:
        print("[+] Found Admin Panels:")
        for url in found_panels:
            print("   -->", url)
    else:
        print("[-] No admin panels found.")