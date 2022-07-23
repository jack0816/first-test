#%%
import random
r = random.randint(1 ,100)
count = 0
while True:
    num = input('請輸入字串:')
    count = count + 1
    num = int(num)
    if num == r:
        print('猜到了')
        break
    elif num < r:
        print('猜錯了，再猜大一點')
    else:
        print('猜錯了，再猜小一點')
    print('這是你猜的第',count,'次')

# %%
