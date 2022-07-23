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
# %%
