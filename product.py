#%% #建立清單
products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q': #quit
       break
    #建立二維度清單
    price = input('請輸入價格:')
    p = []
    p.append(name)
    p.append(price)
    products.append(p)
print(products)
# %%
