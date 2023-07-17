
url = 'https://wallhaven.cc/search?categories=100&purity=001&sorting=views&order=desc&ai_art_filter=1&page='
def getUrls(url):
    urls = []
    pages = []
    for page in range(1, 100):
        pages.append(page)
        urls.append(url + str(page))
    return urls, pages


urls, pages = getUrls(url)
print(urls)
print(pages)