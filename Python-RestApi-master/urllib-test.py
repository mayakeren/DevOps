import urllib.request
val = urllib.request.urlopen("http://www.google.com").read()
print(val)
