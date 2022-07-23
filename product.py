#%% #建立清單
products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q': #quit
       break
    #建立二維度清單
    price = input('請輸入價格:')
    p = [name,price] #p是小清單
    products.append(p) #把小清單裝到大清單裡面
print(products)


# %%
