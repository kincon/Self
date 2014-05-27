bar = True
my_bar_prices = {
    "Hooch": 1,
    "Booze": 2,
    "Whiskey": 3,
    "Scotch": 5,
    "The Good Stuff": 10
    }

my_bar_stock = {
    "Hooch": 20,
    "Booze": 10,
    "Whiskey": 5,
    "Scotch": 3,
    "The Good Stuff": 1
    }
"""
def storeHuman(person):
    if person.customer == True:
        CustomerList.append(person.name)
        return CustomerList
    elif person.employee == True:
        EmployeeList.append(person.name)
        return EmployeeList
    else:
        print "This isn't a person."
        return
    return HumanList
    print HumanList
    print EmployeeList
    print CustomerList
storeHuman(James)
"""

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
                    if price[x] <= thirst and money >= price[x] and stock[x] > 0:
                        self.money -= price[x]
                        stock[x] -= 1
                        self.thirst -= price[x]
                        print "%s bought %s! They have %s dollars left to sate their thirst. Thirst: %s" % (self.name, x, str(self.money), self.thirst)
                        
                    
                    """
                    elif price[x] >= money and thirst >= price[x]:
                        desparation += price[x] / 2
                        return
                        """
                    
                    #Why does this else statement create an error if it's tabbed in one more time? Ask Paul.
                else:
                        print "what have you done"
                        break
                break
            else:
                print "Customers want to buy, but there's no bartender. Hire one, or get him on the job." 
        
        def untilDrunk(self, money, stock, desparation, price, bar, thirst):
            while thirst >= 1:
                self.buyDrink(money, stock, desparation, price, bar, thirst)
                return thirst
                

            """
                for x in stock:
                    if price[x] <= thirst and money >= price[x]:
                            self.money -= price[x]
                            stock[x] -= 1
                            self.thirst -= price[x]
                            print "The Customer bought a %s! They have %s dollars left to sate their thirst. Thirst: %s" % (x, str(self.money), self.thirst)
                            return
    
                        
                        #Why does this else statement create an error if it's tabbed in one more time? Ask Paul.
                    else:
                            print "what have you done"
                            return
                           """
                
            
                



"""
mySpeakeasy = Speakeasy(HumanList, 10000, my_bar_stock, my_bar_prices, True)

print "People in the speakeasy: " + str(mySpeakeasy.people)

print "Initial stock: " + str(my_bar_stock)

print Charles.buyDrink(Charles.money, my_bar_stock, Charles.desparation, my_bar_prices, True, Charles.thirst)

print "Binge time! Down that special drank!"
    
while Charles.thirst >= 1:
    print Charles.buyDrink(Charles.money, my_bar_stock, Charles.desparation, my_bar_prices, bar, Charles.thirst)
    
print "Final stock: " + str(my_bar_stock)
"""

Jones = Human("Jones", 1000, 0, 0, True, False, 100, 0)
Charles = Human("Charles", 100, 40, 0, False, True, 5, 100)
James = Human("James", 100, 10, 0, False, True, 5, 100)

EmployeeList = [Jones.name]
CustomerList = [Charles.name]
HumanList = [EmployeeList[::], CustomerList[::]]

Charles.untilDrunk(Charles.money, my_bar_stock, Charles.desparation, my_bar_prices, bar, Charles.thirst)

    
print str(my_bar_stock)
