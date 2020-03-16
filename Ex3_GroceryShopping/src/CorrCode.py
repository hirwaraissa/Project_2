class Shop:

    def __init__(self,lst_shelves=[]):
        self.lst_shelves= self.sorting_shelves(lst_shelves)

    def grocery_shopping(self,lst):
        l = []
        for ray in self.lst_shelves:
            for item in lst:
                if ray.buy_item(item):
                    l.append(item)
        return l

    def add_shelf(self,new_shelf):
        if isinstance(new_shelf,Shelf) and new_shelf not in self.lst_shelves:
            for shelf in self.lst_shelves:
                if shelf.cordinate == new_shelf.cordinate:
                    return True
            self.lst_shelves.append(new_shelf)
            self.lst_shelves = self.sorting_shelves(self.lst_shelves)
        else:
            return False

    def sorting_shelves(self,lst):
        liste = []
        index = 0
        while len(lst) != 0:
            count = 0
            for product in lst:
                if lst[index].cordinate<=product.cordinate:
                    count+=1
            if count == len(lst):
                liste.append(lst.pop(index))
                index = 0
            else:
                index+=1
        return liste

class Shelf:

    def __init__(self,lst_products=[],cordinate=0):
        self.lst_products = self.sorting_products(lst_products)
        self.cordinate = cordinate

    def sorting_products(self,lst):
        liste = []
        index = 0
        while len(lst) != 0:
            count = 0
            for product in lst:
                if lst[index].name<=product.name:
                    count+=1
            if count == len(lst):
                liste.append(lst.pop(index))
                index = 0
            else:
                index+=1
        return liste

    def add_item(self, new_item):
        if new_item not in self.lst_products:
            for product in self.lst_products:
                if product.name == new_item.name:
                    return 
            self.lst_products.append(new_item)
            self.lst_products = self.sorting_products(self.lst_products)

    def buy_item(self,product):
        for item in self.lst_products:
            if item.name == product.lower():
                item.buy()
                return True
        return False

class Product:

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def buy(self):
        if self.quantity > 0:
            self.quantity -= 1
            
    def restock(self,qt):
        self.quantity = max(self.quantity,qt)