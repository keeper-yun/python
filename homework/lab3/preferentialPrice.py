


price = eval(input(f'所购商品的价格:'))

def preferential(price):
    if(price<=0):
        return None
    elif(price<=500):
        price=price
    elif(price<=1000):
        price=price*0.95
    elif(price<=1500):
        price=price*0.9
    elif (price <= 2000):
        price = price * 0.85
    else:
        price = price * 0.8
    print(f'所购商品优惠后的价格为：{price}')

preferential(price)

