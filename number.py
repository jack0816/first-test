#%%
import random
# start = input('請輸入開始值')
# end = input('請輸入結束值')
# start = int(start)
#　end = int(end)
# r = random.randint(start ,end)
r = random.randint(1 ,100)
count = 0
while True:
    num = input('請輸入字串:')
    count = count + 1
    num = int(num)
    if num == r:
        print('猜到了，密碼是：' , num)
        print('這是你猜的第',count,'次')
        break
    elif num < r:
        print('猜錯了，再猜大一點')
    else:
        print('猜錯了，再猜小一點')
    print('這是你猜的第',count,'次')

# %%
