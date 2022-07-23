#%% #讀取檔案
data  = []
with open('d.txt','r') as f: # r的意思是讀取模式  as f是當作file的意思 -->把這個檔案當作file
    for line in f:  # 檔案一行一行的讀，每一行這邊取成line'
        data.append(line.strip()) #因為print本身就會有換行，我們檔案裏面也有一個換行，所以印出來會有兩次換行，才要用strip來去掉
                                  # strip的功能是把多餘的空格跟換行去掉 這個功能只能對字串用
print(data)
# %%
data = []
with open('d.txt','r') as f:
     for line in f:
         data.append(line.strip())
print(data)
# %%
