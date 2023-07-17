import threading
import urllib.request

def download_file(url, filename):
    """下载文件的函数"""
    print("Downloading file from: {}".format(url))
    urllib.request.urlretrieve(url, filename)
    print("Download completed for file: {}".format(filename))

def main():
    urls = [
        "http://example.com/file1.txt",
        "http://example.com/file2.txt",
        "http://example.com/file3.txt",
        # 添加更多的文件URL
    ]

    # 创建并启动线程下载文件
    threads = []
    for i, url in enumerate(urls):
        filename = "file{}.txt".format(i+1)
        thread = threading.Thread(target=download_file, args=(url, filename))
        thread.start()
        threads.append(thread)

    # 等待所有线程完成下载
    for thread in threads:
        thread.join()

    print("All downloads completed.")

if __name__ == '__main__':
    main()
