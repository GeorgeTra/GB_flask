import multiprocessing
import time
import requests

urls = ['https://google.ru', 'https://gb.ru', 'https://vivazzi.pro/ru/',

        'https://vivazzi.pro/',

        'https://vivazzi.pro/ru/invest-vuspace/',

        'https://vivazzi.pro/ru/invest-vuspace/profit-ex/',

        'https://vivazzi.pro/ru/invest-vuspace/balance/',

        'https://vivazzi.pro/ru/invest-vuspace/faq/',

        'https://vivazzi.pro/ru/invest-vuspace/ap/',

        'https://vivazzi.pro/ru/invest/',

        'https://vivazzi.pro/ru/invest/chats/',

        'https://vivazzi.pro/ru/invest/foreword/',

        'https://vivazzi.pro/ru/invest/rules/',

        'https://vivazzi.pro/ru/invest/account-security/',

        'https://vivazzi.pro/ru/invest/scan/',

        'https://vivazzi.pro/ru/invest/cards/',

        'https://vivazzi.pro/ru/invest/cards/roketbank/',

        'https://vivazzi.pro/ru/invest/cards/tinkoff/',

        'https://vivazzi.pro/ru/invest/wallets/',

        'https://vivazzi.pro/ru/invest/wallets/blockchain/',

        'https://vivazzi.pro/ru/invest/wallets/advcash/',

        'https://vivazzi.pro/ru/invest/wallets/payeer/',

        'https://vivazzi.pro/ru/invest/wallets/yandex-money/',

        'https://vivazzi.pro/ru/invest/forex/',

        'https://vivazzi.pro/ru/invest/forex/about/',

        'https://vivazzi.pro/ru/invest/forex/schedule/',

        'https://vivazzi.pro/ru/invest/forex/swap/',

        'https://vivazzi.pro/ru/invest/brokers/',

        'https://vivazzi.pro/ru/invest/brokers/forex4you/',

        'https://vivazzi.pro/ru/invest/brokers/roboforex/',

        'https://vivazzi.pro/ru/viva-forex/',

        'https://vivazzi.pro/ru/viva-forex/multiplier/',

        'https://vivazzi.pro/ru/viva-tm/',

        'https://vivazzi.pro/ru/viva-tm/risk/',

        'https://vivazzi.pro/ru/viva-tm/advantages/']


def download(url):
    response = requests.get(url)
    file_name = url.replace('https://', 'multipr_').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
        print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = multiprocessing.Process(target=download, args=(url, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
