import whois

domain = whois.whois('www.baidu.com')
print(domain.__dict__)
