import multiprocessing
import time
import requests
import os


def download(url):
    start_time = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        file_name = url.rsplit('/', 1)[-1]
        file_name = os.path.join('images', file_name)
        with open(file_name, 'wb') as f:
            f.write(content)
        end_time = time.time()
        print(f'Загружен файл {file_name} ({end_time - start_time:.2f}) сек.')
    else:
        print(f'Ошибка при загрузке файла {url}')


def download_multiproc(url_queue, num_processes ):
    processes = []
    for i in range(num_processes):
        if not url_queue.empty:
            url = url_queue.get()
            process = multiprocessing.Process(target=download, args=(url,))
            process.start()
            processes.append(process)

    for process in processes:
        process.join()


def main(urls):
    for url in urls:
        processes = []
        process = multiprocessing.Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    urls = ['https://wmpics.space/di-M1L5.jpg',
            'https://wmpics.space/di-43IW.png',
            'https://wmpics.space/di-8XGD.png',
            'https://wmpics.space/di-8OSV.png',
            'https://wmpics.space/di-2ZP2.png'
            ]
    start_time = time.time()
    main(urls)
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Время загрузки всех файлов {total_time:.2f} сек.')


