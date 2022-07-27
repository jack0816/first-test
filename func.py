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

# %% #return用法

def add(x, y):
    return x + y

result = add(3,4)
print(result)

#算清單平均
def avg(numbers):
    sum(numbers)    #sum可以對清單用，就能算出清單總數
    a =  sum(numbers) / len(numbers)
    return a

r = avg([2,3,4])
print(r)

# %%
x = input('請輸入年分')
x = int(x)

def is_leep(x):
    if x % 4 != 0:
        return False
    elif x % 4 == 0 and x % 100 != 0 :
        return True
    elif x % 100 == 0 and x % 400 != 0 :
        return False
    elif x % 400 == 0 and x % 3200 != 0:
        return True
print(is_leep(x))
# %%
def sum_of_list(x):
    return sum(x)
print(sum_of_list([1,2,3]))

# %%
