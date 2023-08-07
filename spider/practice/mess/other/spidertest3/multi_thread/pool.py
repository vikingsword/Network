import concurrent.futures
import requests


def download_file(url, filename):
    """下载文件的函数"""
    print("Downloading file from: {}".format(url))
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)
    print("Download completed for file: {}".format(filename))


def main():
    urls = [
        "http://example.com/file1.txt",
        "http://example.com/file2.txt",
        "http://example.com/file3.txt",
        # 添加更多的文件URL
    ]

    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # 提交下载任务给线程池
        download_tasks = {
            executor.submit(download_file, url, i + 1): url
            for i, url in enumerate(urls)
        }

        # 等待所有下载任务完成
        for future in concurrent.futures.as_completed(download_tasks):
            url = download_tasks[future]
            try:
                future.result()
            except Exception as e:
                print("Error occurred while downloading file from {}: {}".format(url, e))

    print("All downloads completed.")


if __name__ == '__main__':
    main()
