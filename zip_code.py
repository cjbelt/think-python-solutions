import urllib.request

conn = urllib.request.urlopen('https://greenteapress.com/wp/think-python/secret.html')

for line in conn:
    print(line.strip())
