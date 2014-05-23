bar = True
class Speakeasy(object):  
    def __init__(self, people, money, stock, price, bar):
        self.people = people
        self.money = money
        self.stock = stock
        self.price = price
        self.bar = bar

    

class Human(object):
        def __init__(self, name, money, thirst, desparation, employee, customer, interest, danger):
            self.name = name
            self.money = money
            self.thirst = thirst
            self.desparation = desparation
            self.employee = employee
            self.customer = customer
            self.interest = interest
            self.danger = danger
    
        
        # Action Methods    

        """ 
        def steal(self, money, stock, desparation, price, bar):
            self.stock = stock
            self.price = price
            self.bar = bar
            if bar == False and rand >= 10:
                for x in stock:
                    if desparation >= thirst and money <= price:
                        stock[x] -= 1
                        danger += price[x]
                        desparation -= price[x]
                        thirst -= price[x]
            else:
                desparation += 5

"""
        def buyDrink(self, money, stock, desparation, price, bar, thirst):
            self.stock = stock
            self.price = price
            self.bar = bar
            while bar == True:
                for x in stock:
                    """
                    print x
                    print "Drink price: " + str(price[x])
                    print "Customer's money: " + str(money)
                    print "Thirst: " + str(thirst)
                    """
                    if price[x] <= thirst and money >= price[x]:
                        self.money -= price[x]
                        stock[x] -= 1
                        print "The Customer bought a %s! They have %s dollars left to sate their thirst. Thirst: %s" % (x, str(self.money), self.thirst)
                        self.thirst -= price[x]
                        return
                        break
                    
                    else:
                        print "what have you done"
                        return
                        break
                break
            else:
                print "Customers want to buy, but there's no bartender. Hire one, or get him on the job." 
            
                

my_bar_prices = {
    "Hooch": 1,
    "Booze": 2,
    "Whiskey": 3,
    "Scotch": 5,
    "The Good Stuff": 10
    }

my_bar_stock = {
    "Hooch": 20,
    "Booze": 19,
    "Whiskey": 5,
    "Scotch": 3,
    "The Good Stuff": 1
    }
    
Jones = Human("Jones", 1000, 0, 0, True, False, 100, 0)
Charles = Human("Charles", 100, 10, 0, False, True, 5, 100)
EmployeeList = [Jones.name]
CustomerList = [Charles.name]
HumanList = [EmployeeList[::], CustomerList[::]]

mySpeakeasy = Speakeasy(HumanList, 10000, my_bar_stock, my_bar_prices, True)

print "People in the speakeasy: " + str(mySpeakeasy.people)

print Charles.buyDrink(Charles.money, my_bar_stock, Charles.desparation, my_bar_prices, True, Charles.thirst)

print "Binge time! Down that Whiskey!"

for x in range(3):
    print Charles.buyDrink(Charles.money, my_bar_stock, Charles.desparation, my_bar_prices, True, Charles.thirst)
    
print my_bar_stock
