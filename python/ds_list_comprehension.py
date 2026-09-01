# transformation + filtering

domains = ['www.google.com', 'openai.com', 'localhost','WWW.DATA.COM']

cleaned = [
    d.lower().replace('www.','')
    for d in domains
    if '.' in d
]
print(cleaned)

cleaned = [d for d in domains if '.' in d
]
print(cleaned)