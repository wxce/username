import os, requests, threading, random, string;from itertools import cycle
try: os.remove('usernames.txt')
except: pass
for _ in range(50): file = open('usernames.txt', 'a+');username = ''.join(random.choices(string.ascii_letters + string.digits, k=3));file.write(username+'\n')
usernames = open('usernames.txt').read().splitlines()
proxies = open('proxies.txt').read().splitlines()
def check(username):
  proxy = random.choice(proxies)
  request = requests.get('https://github.com/%s' % username, proxies={'http': 'http://' + proxy})
  if not request.status_code in (200, 201, 204):
    print('[~] Available: %s' % username)
    file = open('available.txt', 'a+')
    file.write(username+'\n') 
  else:
    print('[~] Unavailable: %s' % username)
for username in usernames:
  #check(username)
  threading.Thread(target=check, args=(username,)).start()
