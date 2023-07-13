import argparse
import asyncio
import time
from pathlib import Path
from queue import Queue

import aiofiles

from multipimage import download_multiproc


async def read_urls_from_file(file_path, chunk_size=100):
    async with aiofiles.open(file_path, 'r') as file:
        while True:
            chunk = [line.strip() for line in await file.readlines(chunk_size)]
            if not chunk:
                break
            yield chunk


async def main():
    parser = argparse.ArgumentParser(description='Скачивание файлов с заданных URL-адресов')
    parser.add_argument('-f', '--file', default='urls.txt', type=str, help='Путь к файлу с URL-адресами')
    parser.add_argument('-m', '--mode', choices=['a', 't', 'm'], default='m',
                        help='Режим выполнения (async, threading, multiprocessing')
    parser.add_argument('-p', '--processes', type=int, default=4,
                        help='Режим выполнения (Количество процессов/потоков для использования'
                        '(только для threading и multiprocessing)')

    args = parser.parse_args()

    if not args.file:
        print('Не указан файл с URL-адресами')
        return
    file_path = Path(args.file)
    if not file_path.exists():
        print(f'Файл не найден {file_path}')
        return

    url_queue = Queue()
    async for chunk in read_urls_from_file(file_path, chunk_size=100):
        for url in chunk:
            url_queue.put(url)
            if args.mode == 'm':
                download_multiproc(url_queue, args.processes)
            elif args.mode == 'a':
                pass
            elif args.mode == 't':
                ...
            else:
                print('Некорректный режим выполнения. Допустимые значения: async, threading и multiprocessing')


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Время загрузки всех файлов {total_time:.2f} сек.')
