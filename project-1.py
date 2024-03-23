class car:
    def company(self,name):
        i=['Toyata','Mercedes','Suzuki']
        self.n=input("enter the car company")
        if self.n=="toyota":
            print(" Heartly Welcome to toyoto")
            self.model()
        elif self.n=="Mercedes":
            print("heartly welcome to mercedes")
            self.modul()
        elif self.n=="Suzuki":
            print("heartly welcome to suzki")
            self.modul()
        else:
            print("please enter the vaild company")
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
