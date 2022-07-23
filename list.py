#%% # list清單
a = ['toyato' , ' honda']
a.append('ggg')   #新增東西進清單
print(len(a)) #印出清單長度
print(a)
print(a[0])
print('ggg' in a) #是非題，看這個物件是否再清單裡面
# %%  #for迴圈
car = ['toyato' , ' honda']
for x in car:
    print(x) 

# %% #字串當清單
a = 'dfgh' #它會自動看成 a = ['d' ,'f' , 'g' , 'h']
for c in a:
    print(c)
print(len(a))
# %%
