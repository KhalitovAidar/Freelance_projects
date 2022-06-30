import time

from binance.client import Client

k = 0
API_KEY = 'xsULbhyqbxX6v8lB2FmZzLNg3HauLh3iJt2glYeSNR39yFcyPTeIICmqKPoKfuvL'
API_SECRET = '6f68Gmv2nvVTxWgj7XeEyhoRUE41fVmBdmB85ialSThAu8g0Tv0ChNViDjshmIVW'
client = Client(API_KEY, API_SECRET)


def create_order(*args, symbol, quantity, price, side, stopPricestop, stopPricetake_profit, k=0):
    client.futures_create_order(
            symbol=symbol,
            recvWindow=20000,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=price
        )

    time.sleep(10)
    r = client.futures_get_all_orders()
    orderId = r[-1]['orderId']

    while k < 1:
        r = client.futures_get_all_orders()
        for i in r:
            if i['orderId'] == orderId and (i['status'] == 'EXPIRED' or i['status'] == 'FILLED'):
                if side == 'BUY':
                    profit = client.futures_create_order(
                        symbol=symbol,
                        recvWindow=20000,
                        side='SELL',
                        type='LIMIT',
                        timeInForce='GTC',
                        quantity=quantity,
                        price=stopPricetake_profit
                    )
                    orderIdprofit = client.futures_get_open_orders()[-1]['orderId']

                    stop = client.futures_create_order(
                        symbol=symbol,
                        recvWindow=20000,
                        side='SELL',
                        type='STOP',
                        quantity=quantity,
                        price=price,
                        stopPrice=stopPricestop
                    )

                    orderIdstop = client.futures_get_open_orders()[-1]['orderId']
                    k+=1

                if side == 'SELL':
                    profit = client.futures_create_order(
                        symbol=symbol,
                        recvWindow=20000,
                        side='BUY',
                        type='LIMIT',
                        timeInForce='GTC',
                        quantity=quantity,
                        price=stopPricetake_profit
                    )
                    orderIdprofit = client.futures_get_open_orders()[-1]['orderId']

                    stop = client.futures_create_order(
                        symbol=symbol,
                        recvWindow=20000,
                        side='BUY',
                        type='STOP',
                        quantity=quantity,
                        price=price,
                        stopPrice=stopPricestop
                    )

                    orderIdstop = client.futures_get_open_orders()[-1]['orderId']
                    k += 1

    if k >= 1:
        function(*args)

    statusProfit = 'NEW'
    statusStop = 'NEW'

    while (statusProfit == 'NEW') and (statusStop == 'NEW'):
        r = client.futures_get_all_orders()
        for i in r:
            if i['orderId'] == orderIdprofit:
                statusProfit = i['status']
                print('statusProfit:' + statusProfit)
            if i['orderId'] == orderIdstop:
                statusStop = i['status']
                print('statusStop:' + statusStop)

    if statusProfit != 'NEW':
        client.futures_cancel_order(
            symbol=symbol,
            orderId=orderIdstop
        )
        return 'PROFIT_USED'

    if statusStop != 'NEW':
        client.futures_cancel_order(
            symbol=symbol,
            orderId=orderIdprofit
        )
        return 'STOP_USED'

def function(*args):
    create_order(
    symbol=args[0],
    quantity=args[1],
    side=args[2],
    price=args[3],
    stopPricestop=args[4],
    stopPricetake_profit=args[5]
    )

args1 = ('XRPUSDT', 9, "BUY", 0.7050, 0.7030, 0.7070)
order1 = create_order(*args1, symbol='XRPUSDT', quantity=8, side="BUY", price=0.7060, stopPricestop=0.7040, stopPricetake_profit=0.7080)#вписать параметры

args2 = ['XRPUSDT', 8, "BUY", 0.7030, 0.7010, 0.7090]
order2 = create_order(*args2, symbol=, quantity=, side=, price=, stopPricestop=, stopPricetake_profit=)#вписать параметры