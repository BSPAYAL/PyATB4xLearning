def make_pizza(*toppings,base):
    print(toppings)

amit = make_pizza("mushroom","corn","cheese", base="thin crust")
#we can't pass multiple base only multiple topping is allowed when we have multiple parameter passed

#* toppings can be multiple.
#only one argument is allowed with *


def make_pizza(base, *toppings):#won't work
    print(toppings)

#"*" has to be the first argument , above won't work