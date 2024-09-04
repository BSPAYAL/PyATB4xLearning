#LIST

my_shopping_list = ["milk","bread","buuter"]
print(my_shopping_list[0])
print(len(my_shopping_list))


def bring_food(my_list):
    my_list.append("cheese")
    my_list.remove("bread")
    return my_list
l = bring_food(my_shopping_list)
print(l)


