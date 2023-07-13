import asyncio
import time
import aiohttp

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


async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            file_name = url.replace('https://', 'async_').replace('/', '').replace('.', '') + '.html'
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(text)
                print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


start_time = time.time()


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())



