class father:
   def bike(self):
    print("GT")
   def laptop(self):
    print("2Gb")
class bunny(father):
    def laptop(self):
      print("8Gb")
obj=bunny()
obj.bike()
obj.laptop()

#create a class car showroom which has function as follows
#1, function is company it takes one arguement which is the car company name and prints welcome to the mercedez family.
#2, according to the car company model selected, the models of the company will be listed. The user has to select a model from the list.
#3. Based on the car company and model calculate the on road price which is equals to ex showroom price+CGST+SGST+insurance and diplay the final price.
#note: The ex showroom price changes from model to model but the cgst, sgst musst remain default for all the cars.