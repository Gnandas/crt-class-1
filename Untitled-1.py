if name in i:
            print(" Heartly Welcome to",name)
    def model(self,name):
        a={'Toyata':['Fortuner','Innova'],'Mercedes':['BMW'],'Suzuki':['Swift','Alto']}
        if name in  a:
            print(a[name])
    def price(self,name,m):
        print("you selected",m)
        prices_list={'Fortuner':7500000,'Innova':5000000,'BMW':1000000,'Swift':2000000,'Alto':3000000}
        if m in prices_list:
            car_price=prices_list[m]
            GST=0.1*car_price
            insurance=10000
            final_price=car_price+GST+insurance
            print("final price",final_price)
n=input("Enter the car company:")
c=car()
c.company(n)
c.model(n)
m=input("Enter the car model:")
c.price(n,m)