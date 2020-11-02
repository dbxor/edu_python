
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

#%%
# 엑셀파일을 읽기 위해서는 pip3 install xlrd
rs3 = pd.read_excel("gdp_per_capita_y2k.xlsx",
                        sheet_name = 'gdp_per_capita', 
                        header = 0, 
                        #names = ['region', 'sales_representative', 'sales_amount'], 
                        #dtype = {'region': str, 'sales_representative': np.int64,'sales_amount': float}, # dictionary type
                        #index_col = 'Country Name', 
                        usecols= "A,B,C,D,E", 
                        na_values = 'NaN', 
                        thousands = ',', 
                        #nrows = 10, 
                        comment = '#')
#filter_kor = rs3["Country Code"] == "KOR"

#rs_kor = rs3[filter_kor]

#rs_kor = rs3[rs3["Country Code"].eq("KOR")]
rs_kor = rs3[rs3["Country Name"].str.contains("Kor")]
print(rs_kor.shape)

print(rs_kor.head())

#%%
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

x = range(0, 100)
y = [v*v for v in x]

ax1.plot(x, y)
ax2.bar(x, y)
ax3.barh(x, y)
ax4.scatter(x,y)


plt.show()
#%%
#plt.figure(1)
fig, ax_list = plt.subplots(2,2)
print(type(fig))
ax_list[0,0].plot([2,3])
ax_list[0][1].bar(3,5, width = 0.2)
plt.show()
#%%
def cal_upper_lower(price):
        offset = price * 0.3
        upper = price + offset
        lower = price - offset
        return (upper, lower, price)
(upper, lower, price) = cal_upper_lower(10000)
print(lower, upper, price)
# %%
