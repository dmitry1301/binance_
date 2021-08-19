import time
from config import ASSET, TIME, GROW_PERCENT, CURRENCY, CRYPTOCURRENCY, FALL_PERCENT
from api import price, balance, order_market_buy, order_market_sell
from logging import buy_message_success, sell_message_success


def main(FIRST_PRICE):
    # Функция обрезает число до n кол-во символов(Нужна чтобы при покупки и продажи не возникло ошибки)
    def toFixed(f: float, n=0):
        a, b = str(f).split('.')
        return '{}.{}{}'.format(a, b[:n], '0' * (n - len(b)))

    # Засыпаем
    time.sleep(TIME)
    # Получаем новую цену
    PRICE = price(ASSET)
    # Процентное изменение
    PROCENT = ((PRICE - FIRST_PRICE) / FIRST_PRICE) * 100

    print('Цена отсчета:', str(FIRST_PRICE), '| Процент:', str(PROCENT))

    # Покупка
    if PROCENT >= GROW_PERCENT:
        try:
            print('BUY')
            # Покупаем
            order_market_buy(toFixed(float(balance(CURRENCY)['free']) / price(ASSET), 5))
            # Отправляем сообщение
            buy_message_success()
            # Перезапускаем функцию
            main(PRICE)
        except:
            print('Ошибка при покупке!')
            # Перезапускаем функцию
            main(PRICE)

    # Продажа
    elif PROCENT <= FALL_PERCENT:
        try:
            print('SELL')
            # Покупаем
            order_market_sell(toFixed(float(balance(CRYPTOCURRENCY)['free']), 5))
            # Отправляем сообщение
            sell_message_success()
            # Перезапускаем функцию
            main(PRICE)
        except:
            print('Ошибка при продаже!')
            # Перезапускаем функцию
            main(PRICE)

    else:
        # Перезапускаем функцию
        main(FIRST_PRICE)

# Запуск алгоритма из консоли
# START_PRICE = price(ASSET)
# main(START_PRICE)
