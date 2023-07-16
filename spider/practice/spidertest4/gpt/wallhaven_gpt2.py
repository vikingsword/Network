import requests
from bs4 import BeautifulSoup
import concurrent.futures
import os


# 发送HTTP请求并获取网页内容
def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content


# 解析HTML页面，提取图片链接
def extract_image_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    image_links = []
    for figure in soup.find_all('figure', class_='thumb'):
        img = figure.find('img')
        if img and 'data-src' in img.attrs:
            image_links.append(img.attrs['data-src'])
    return image_links


# 下载图片
def download_image(url, save_folder):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = url.split("/")[-1]  # 从URL中提取文件名
        save_path = os.path.join(save_folder, file_name)
        with open(save_path, 'wb') as f:
            total_length = response.headers.get('content-length')
            if total_length is None:  # 如果无法获取总大小，则直接写入文件
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                done = int(50 * dl / total_length)
                print(f"\rDownloading: [{'=' * done}>{' ' * (50 - done)}] {file_count}/{total_files}", end='')


# 爬取单个页面的任务
def crawl_page(page):
    url = f"https://wallhaven.cc/search?categories=001&purity=010&topRange=1y&sorting=favorites&order=desc&ai_art_filter=0&page={page}"
    html = get_page(url)
    image_links = extract_image_links(html)

    # 创建保存图片的文件夹
    folder_path = r"J:\WallPaper\Sketchy\temp"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 下载图片并保存到文件夹中
    for image_link in image_links:
        # 提取图片ID
        image_id = image_link.split("/")[-1].split(".")[0]
        full_image_link = f"https://w.wallhaven.cc/full/{image_id[0:2]}/wallhaven-{image_id}.jpg"
        download_image(full_image_link, folder_path)


# 主函数
def main():
    num_pages = 20
    global file_count
    global total_files
    file_count = 0
    total_files = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # 提交任务给线程池
        futures = [executor.submit(crawl_page, page) for page in range(1, num_pages + 1)]

        # 等待任务完成
        concurrent.futures.wait(futures)


def download_image_with_progress(url, save_folder):
    global file_count
    global total_files
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = url.split("/")[-1]  # 从URL中提取文件名
        save_path = os.path.join(save_folder, file_name)
        with open(save_path, 'wb') as f:
            total_length = response.headers.get('content-length')
            if total_length is None:  # 如果无法获取总大小，则直接写入文件
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                done = int(50 * dl / total_length)
                file_count += 1
                print(f"\rDownloading: [{'=' * done}>{' ' * (50 - done)}] {file_count}/{total_files}", end='')


# 爬取单个页面的任务
def crawl_page(page):
    url = f"https://wallhaven.cc/search?categories=001&purity=010&topRange=1y&sorting=favorites&order=desc&ai_art_filter=0&page={page}"
    html = get_page(url)
    image_links = extract_image_links(html)

    # 创建保存图片的文件夹
    folder_path = r"J:\WallPaper\Sketchy\temp"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    global total_files
    total_files += len(image_links)

    # 下载图片并保存到文件夹中
    for image_link in image_links:
        # 提取图片ID
        image_id = image_link.split("/")[-1].split(".")[0]
        full_image_link = f"https://w.wallhaven.cc/full/{image_id[0:2]}/wallhaven-{image_id}.jpg"
        download_image_with_progress(full_image_link, folder_path)


# 主函数
def main():
    num_pages = 20
    global file_count
    global total_files
    file_count = 0
    total_files = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # 提交任务给线程池
        futures = [executor.submit(crawl_page, page) for page in range(1, num_pages + 1)]

        # 等待任务完成
        concurrent.futures.wait(futures)


if __name__ == '__main__':
    main()
