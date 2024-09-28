# age = int(input("enter user age:"))

# if(age<13):
#     print("user is child")

# elif(age<20):
#     print("user is teen")

# elif(age<60):
#     print("user is adult")

# else:
#     print("user is old")


# day = str(input("enter day:"))
# age= int(input("enter your age"))

# if(day== "wednesday"):
#     if(age<18):
#         print("ticket cost $6 ")

#     else:
#         print("ticket cost $10")

# else:
#     if(age<18):
#         print("ticket cost $8 ")

#     else:
#         print("ticket cost $12t")


# marks = int(input("enter your marks"))

# if marks >=90:
#     grade="A"
# elif marks>=80:
#     grade="B" 
# elif marks>=70:
#     grade="C"
# else:
#     grade = "D"

# print(grade)

# numbers = [1 , -2 ,3 ,4 ,-1 ,5,-4 ,-2]
# pos_count=0
# for num in numbers:
#    if num>0:
#       pos_count += 1
# print(pos_count)

# n = int(input("enter number"))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum += i
# print(sum)

# n=int(input("enter number"))
# table=1

# for i in range(1 , 11):
#     if i!=5:
#         print(f"{n} * {i} = {n*i}")


# def sum(a , b):
#     return a+b

# res = sum(2,5)
# print(res) 


class car:
    count =0
    def __init__(self , brand , model):
        self.__brand = brand
        self.__model = model
        car.count+=1
    
    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    def fuelType(self):
        return "diesel or petrol"
    @staticmethod
    def description():
        return "this is the car"
    
    def setModel(self):
        return self.__model

class ElectricCar(car):
    def __init__(self , brand , model , battery):
        super().__init__(brand , model)
        self.battery = battery
    
    def fuelType(self):
        return "electric charge"


# myElectricCar =ElectricCar("mahindra" , "2053" , "1999mega") 
# print(myElectricV.fuelType())

myCar = car("tata","2024")
myCar.setModel = "city"
print(myCar.__model)


# print(mycar.fuelType())

# print(myElectricCar.count)

# print(car.description())

# myCar1 = car("tata" , "2020")
# print(myCar1.brand)
# print(myCar1.model)
# print(myCar1.full_name())

# mycar2 = car("safari" , "s24")
# print(mycar2.brand)
# print(mycar2.model)
