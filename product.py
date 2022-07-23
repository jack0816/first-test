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
print(products[0][0])  #取大清單的第一項的第一小項

for p in products:
    print(p[0],'的價格是',p[1]) # 取小清單的第一項跟第二項
    

# %%
