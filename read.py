#%% #讀取檔案
from numpy import append


data  = []
with open('d.txt','r') as f: # r的意思是讀取模式  as f是當作file的意思 -->把這個檔案當作file
    for line in f:  # 檔案一行一行的讀，每一行這邊取成line'
        data.append(line.strip()) #因為print本身就會有換行，我們檔案裏面也有一個換行，所以印出來會有兩次換行，才要用strip來去掉
                                  # strip的功能是把多餘的空格跟換行去掉 這個功能只能對字串用
print(data)
# %%
data = []
count = 0
with open('reviews.txt','r') as f:
     for line in f:
         data.append(line)
         count += 1
         if count % 100000 == 0:
            print(len(data)) #看現在讀到第幾筆
print(data[0]) 
print('--------------------')
print(data[1])




# %% # 算留言平均長度
data = []
with open('reviews.txt','r') as f:
     for line in f:
         data.append(line)
sum_len = 0
for d in data:
    sum_len += len(d)
print(sum_len)
print('平均留言程度=',sum_len/len(data))

#%% #篩選資料長度小於100的資料
data = []
with open('reviews.txt','r') as f:
     for line in f:
         data.append(line)
new = []
for r in data:
    if(len(r)) <= 100:
        new.append(r)
print('一共有',len(new),'筆資料長度小於100')
print(new[0])
# %% #篩選資料裡面有出現good的資料
data = []
with open('reviews.txt','r') as f:
     for line in f:
         data.append(line)
good = []
for r in data:
    if 'good' in r:
        good.append(r)
# good = [r for r in data if 'good' in d] #後面兩句話等於上面兩個篩選的條件，最前面的r是如果有符合篩選的條件就把那個東西加到清單內
print('一共有',len(good),'筆資料出現good')
print(good[0])


# %%
