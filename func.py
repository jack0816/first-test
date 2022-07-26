#%%  #function  函式/功能
#Function是用來收納程式碼的
#它是個功能，不會自動執行


def wash():  #def的意思是define 定義
    print('加水')
    print('加洗衣精')
    print('旋轉')

wash()  #使用function

#%%  #Function帶參數
def wash(dry=False,water=8):  #def的意思是define 定義
    print('加水',water,'分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

wash()
wash(water=10)
wash(False)

#%%
def add(x, y):
    print(x + y)

add(10,20)


def add(x=0, y=0):  #function的參數帶預設值，呼叫參數就不一定要給參數值(如果沒給就自動用預設值)
                    # (寫預設值的等號不用空格)
    print(x + y)

add()

# %%
