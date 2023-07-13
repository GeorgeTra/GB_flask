import threading
import time
import requests
import os

urls = [

]


def download(url):
    response = requests.get(url)
    file_name = url.replace('https://', 'thread_').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
        print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


threads = []
start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
