#%% #建立清單

#讀取檔案
products = []
with open('product.csv','r',encoding= 'UTF-8') as f:
    for line in f:
        name , price = line.strip().split(',')  #先用split把多餘的空格去掉，再用split切割(因為切割完變成兩塊，所以用兩個變數去存)
        products.append([name,price])
print(products)



while True:
    name = input('請輸入商品名稱:')
    if name == 'q': #quit
       break
    #建立二維度清單
    price = input('請輸入價格:')
    price = int(price)
    p = [name,price] #p是小清單
    products.append(p) #把小清單裝到大清單裡面
print(products[0][0])  #取大清單的第一項的第一小項

for p in products:
    print(p[0],'的價格是',p[1]) # 取小清單的第一項跟第二項
#寫到電腦檔案
with open('product.csv','w',encoding = 'UTF-8') as f:  #open:打開檔案的意思 csv可以存成excel檔  因為一個檔案有開就一定要關掉，所以with的功能是幫檔案自動close，跳出with的範圍就不能再寫入了
                                                      # 要先去說明要用甚麼編碼寫入，之後excel也要調編碼(要用甚麼編碼讀取)
    f.write('商品,價格\n')                             #在excel檔最上方新增標題欄
    for p in products:
        f.write(p[0] + ',' +  str(p[1]) + '\n')  #寫入
        


# %%
