# book = {}

# book['tom'] = {
#     'name': 'tom',
#     'address' : 'mag pat na 5',
#     'phone ': 83938493
# }

# book['joe']  = {
#     'name': 'joe',
#     'address' : 'magistrate col pat na 5',
#     'phone ': 938895739
# }

# import json
# s = json.dumps(book)

# with open("C:\\Users\\rohit\\myProjects\\python_practice\\new.txt", 'w') as f:
#     f.write(s)

# with open("C:\\Users\\rohit\\myProjects\\python_practice\\new.txt", 'r') as f:
#     print(f.read())

# f = open('C:\\Users\\rohit\\myProjects\\python_practice\\new.txt', 'r')

# for line in f:
#   p= line.split(' ')
#   print(f"{line} word count {len(p)}")
# f.close()




class car:
    def __init__ (self , brand , modle):
        self.brand = brand
        self.model = modle
    
    def price(self , rs):
        print( self.brand,"and model", self.model " price of car is ", rs)
    
    def highBrand(self, rs):
        if rs < 500000:
            print(self.brand, "this is low brand car", rs)
        else:
            print(self.brand, "this is high brand car", rs)

honda = car