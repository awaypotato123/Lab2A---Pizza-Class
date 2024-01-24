#Riyadh Ahmed - 301068729
#Jan 24 2024


class Pizza:
    valid_sizes = ["small","medium","large"]
    prices = {
        "small" : "$6.49",
        "medium": "$8.49",
        "large": "$10.49",
        "x-large": "$13.49"
    }
    
def __init__(self,size="medium",topping=None):
    self.size = size

    if topping is None:
        self.list_of_toppings = ["cheese"]
    else:
        self.list_of_toppings = list(topping)


#instance methods
def addToppings(self,newTopping):
    
    list.extend(newTopping)

def __str__(self):
    print(f'{size} pizza with {topping} for {price}')

#instance properties
    
    @property
    def priceofPizza(price):

        return price
    
    @property 
    def sizeofPizza(size):
        return size
      
        
    @property
    def size_setter(self,valid_sizes):
        try:
            if valid_sizes == 'gigantic':
                raise Exception('invalid size')
        except Exception as e:
            print(e)
