from selenium import webdriver
from lxml import etree


def init_driver():
    edge_option = webdriver.EdgeOptions()
    edge_option.add_argument('--headless')
    edge_option.add_argument('--gpu-disable')
    edge_option.add_argument('--mute-audio')
    driver = webdriver.Edge(options=edge_option)
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver




def get_page_urls(driver):
    base_url = 'https://www.ntdm9.com'
    with open('anime_homepage.txt', 'r', encoding='utf-8') as f:
        for url in f:
            url = url.strip()
            print("home_url = ", url)
            driver.get(url)
            page_source = driver.page_source
            # get anime title
            tree1 = etree.HTML(page_source)
            anime_title = tree1.xpath('//div[@class="blockcontent"]//h4[@class="detail_imform_name"]/text()')[0]
            print("anime_title = ", anime_title)
            # get every episode url
            tree2 = etree.HTML(page_source)
            li_list = tree2.xpath('//div[@id="main0"]//ul/li')
            for li in li_list:
                href = li.xpath('./a/@href')[0]
                episode_url = base_url + href
                print("episode_url = ", episode_url)
                # episode_download(episode_url)


def episode_download(url):
    driver = init_driver()
    driver.get(url)



if __name__ == '__main__':
    driver = init_driver()
    get_page_urls(driver)