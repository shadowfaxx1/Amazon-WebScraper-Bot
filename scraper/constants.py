import pandas as pd 

url = "https://www.amazon.in/ref=nav_logo"
df=pd.read_excel(r"C:\Users\kaifk\lpth\selenium\project\amazon\scraper\Philps BB Tracker_12.07.xlsx")
link_list=[]
price_list=[]

for i in range(45,len(df)):
    link=(str)(df['ASIN'][i])
    price_match=(int)(df["BAU MOP"][i])
    link_list.append(link)
    price_list.append(price_match)
# print(price_list)

initializer=link_list[0]
print(len(link_list))

