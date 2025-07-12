import requests
import threading
import time
import os
from datetime import datetime

# ========== CONFIG ==========
THREADS = 50
WORDLIST_FILE = "admins.txt"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Team CDF Admin Finder)"
}
TIMEOUT = 8
found_panels = []
error_logs = []

# ========== BANNER ==========
def banner():
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    os.system('cls' if os.name == 'nt' else 'clear')
    print(CYAN + r"""
====================================================×

 ██████╗
██╔════╝
██║
██║
╚██████╗
 ╚═════╝
              ×-------------------------------×
██████╗       |                               |
██╔══██╗      |    This tool is Developed     |
██║  ██║      |             By                |
██║  ██║      |                               |
██████╔╝      |       </ x!t eXploiteR>       |
╚═════╝       |                               |
              |                               |
███████╗      |                               |
██╔════╝      ×-------------------------------×
█████╗
██╔══╝
██║
╚═╝
=====================================================×


      🔎 Real-Time Admin Panel Finder | 🛡 Team CDF
""" + RESET)

# ========== SCAN FUNCTION ==========
def scan_path(target, path):
    url = target.rstrip("/") + "/" + path.strip()
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        status = r.status_code
        if status == 200:
            print(f"\033[92m[✅ FOUND]\033[0m {url}")
            found_panels.append(url)
        elif status in [301, 302]:
            print(f"\033[94m[↪ REDIRECT]\033[0m {url} ➜ {r.headers.get('Location', '')}")
        elif status == 403:
            print(f"\033[91m[⛔ FORBIDDEN]\033[0m {url}")
        else:
            print(f"[{status}] {url}")
    except Exception as e:
        error_logs.append((url, str(e)))

# ========== THREAD START ==========
def start_scan(target, paths):
    threads = []
    for path in paths:
        while threading.active_count() > THREADS:
            time.sleep(0.05)
        t = threading.Thread(target=scan_path, args=(target, path))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

# ========== MAIN ==========
if _name_ == "_main_":
    banner()
    target = input("🌐 Enter full website URL (with http/https): ").strip()

    if not target.startswith("http"):
        print("❌ Please include http:// or https:// in the URL")
        exit()

    try:
        with open(WORDLIST_FILE, "r", encoding='utf-8', errors='ignore') as f:
            paths = f.readlines()
    except:
        print(f"❌ Wordlist file '{WORDLIST_FILE}' not found.")
        exit()

    print(f"\n🚀 Starting Scan at {datetime.now().strftime('%H:%M:%S')} | Total paths: {len(paths)}\n")
    start_scan(target, paths)

    print("\n✅ Scan complete.\n")
    if found_panels:
        print("🎯 Found Admin Panels:")
        for url in found_panels:
            print("   🔗", url)
    else:
        print("❌ No admin panels found.")

    if error_logs:
        print(f"\n⚠ {len(error_logs)} errors occurred during scan.")
