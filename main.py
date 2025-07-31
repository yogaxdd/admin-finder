import requests
import threading
import time
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import sys
import os

class AdminFinder:
    def __init__(self, target_url, wordlist_file="wordlist.txt", threads=10, timeout=5):
        self.target_url = target_url.rstrip('/')
        self.wordlist_file = wordlist_file
        self.threads = threads
        self.timeout = timeout
        self.found_paths = []
        self.total_paths = 0
        self.checked_paths = 0
        
    def load_wordlist(self):
        """Load admin paths from wordlist file"""
        paths = []
        try:
            with open(self.wordlist_file, 'r', encoding='utf-8') as f:
                for line in f:
                    path = line.strip()
                    if path and not path.startswith('#'):
                        paths.append(path)
        except FileNotFoundError:
            print(f"❌ Wordlist file '{self.wordlist_file}' not found!")
            return []
        return paths
    
    def check_path(self, path):
        """Check if admin path exists"""
        try:
            full_url = urljoin(self.target_url, path)
            response = requests.get(full_url, timeout=self.timeout, allow_redirects=False)
            
            self.checked_paths += 1
            
            # Check for successful responses (200, 301, 302, 403, 401)
            if response.status_code in [200, 301, 302, 403, 401]:
                status_emoji = {
                    200: "✅",
                    301: "🔄", 
                    302: "🔄",
                    403: "🚫",
                    401: "🔐"
                }
                
                result = {
                    'path': path,
                    'url': full_url,
                    'status': response.status_code,
                    'emoji': status_emoji.get(response.status_code, "❓")
                }
                
                self.found_paths.append(result)
                print(f"{result['emoji']} Found: {path} - Status: {response.status_code}")
                return result
                
        except requests.exceptions.RequestException:
            self.checked_paths += 1
            pass
        except Exception as e:
            self.checked_paths += 1
            pass
    
    def scan(self):
        """Start the admin path scanning"""
        print(f"🎯 Target: {self.target_url}")
        print(f"📁 Wordlist: {self.wordlist_file}")
        print(f"🧵 Threads: {self.threads}")
        print("=" * 50)
        
        paths = self.load_wordlist()
        if not paths:
            return
        
        self.total_paths = len(paths)
        print(f"📋 Loaded {self.total_paths} paths to check")
        print("🔍 Starting scan...\n")
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.check_path, paths)
        
        end_time = time.time()
        duration = end_time - start_time
        
        self.print_results(duration)
    
    def print_results(self, duration):
        """Print scan results"""
        print("\n" + "=" * 50)
        print("📊 SCAN RESULTS")
        print("=" * 50)
        print(f"⏱️  Duration: {duration:.2f} seconds")
        print(f"📈 Checked: {self.checked_paths}/{self.total_paths} paths")
        print(f"🎯 Found: {len(self.found_paths)} potential admin panels")
        
        if self.found_paths:
            print("\n🔍 POTENTIAL ADMIN PANELS:")
            print("-" * 50)
            for result in self.found_paths:
                print(f"{result['emoji']} {result['path']}")
                print(f"   URL: {result['url']}")
                print(f"   Status: {result['status']}")
                print()
        else:
            print("\n❌ No admin panels found!")

def main():
    print("🔍 ADMIN PANEL FINDER")
    print("Script Made by @yogakokxd")
    print("=" * 30)
    
    # Get target URL
    target_url = input("Enter target URL (e.g., https://example.com): ").strip()
    
    if not target_url:
        print("❌ Please provide a target URL!")
        return
    
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
    
    # Get wordlist file
    wordlist_file = input("Enter wordlist file (default: wordlist.txt): ").strip()
    if not wordlist_file:
        wordlist_file = "wordlist.txt"
    
    # Get number of threads
    try:
        threads = int(input("Enter number of threads (default: 10): ").strip() or "10")
    except ValueError:
        threads = 10
    
    # Create and run scanner
    scanner = AdminFinder(target_url, wordlist_file, threads)
    scanner.scan()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Scan interrupted by user!")
    except Exception as e:
        print(f"\n❌ Error: {e}") 