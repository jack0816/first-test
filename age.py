#%%   #else if:  #另外如果 python 打elif
age = input('請輸入年齡:')
age = int(age) #型別轉換:把str轉換成int
if age < 13 :
    print('國小')
elif age >= 13 and age <18: #另外如果
    print('國高中')
elif age >= 18 and age <22: #另外如果
    print('大學')
else:
    print('出社會')

# %%
#計算bmi
w = input('請輸入體重:')
h = input('請輸入身高')
w = float(w)
h = float(h)
height = h / 100
bmi = w / (height * height)
if bmi < 18.5:
    print('你的bmi值為', bmi ,'屬於體重過輕')
elif bmi >= 18.5 and bmi < 24: 
    print('你的bmi值為', bmi ,'屬於正常範圍')
elif bmi >= 24 and bmi < 27: 
    print('你的bmi值為', bmi ,'稍重')
elif bmi >= 27 and bmi < 30: 
    print('你的bmi值為', bmi ,'輕度肥胖')
elif bmi >= 30 and bmi < 35: 
    print('你的bmi值為', bmi ,'中度肥胖')
elif bmi >= 35 and bmi < 40: 
    print('你的bmi值為', bmi ,'重度肥胖')

# %%
driving =input('你有沒有開過車')
age = input('年齡')
age = int(age)
if driving == '有':
    if age >= 18:
        print('恭喜妳通過測驗')
    else:
        print('你為什麼開過車')
elif driving == '沒有':
    if age >= 18:
        print('你可以去考駕照了')
    else:
        print('加油再等幾年')
     #   raise SystemExit #讓程式在這邊中止
else:
    print('錯誤')
    
# %%
