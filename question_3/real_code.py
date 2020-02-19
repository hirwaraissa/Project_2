#Deux produits avec le meme nom, on fait quoi ?
#Deux rayon avec les memes cordonnnes, on fait quoi ?
class Shop:

    def __init__(self,lst_ray=[]):
        self.lst_ray = lst_ray

    def grocery_shopping(self,lst):
        l =[]
        for item in lst:
            for ray in self.lst_ray:
                if ray.buy_item(item):
                    l.append(item)
        return l

class Ray:

    def __init__(self,lst_products=[],cordonates=1):
        self.lst_products = lst_products
        self.cordonates = cordonates

    def buy_item(self,product):
        for item in self.lst_products:
            if item.name == product and item.quantity>0:
                item.buy()
                return True
        return False

class Product:

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def buy(self):
        self.quantity -= 1

if __name__ == '__main__':
    #Create products
    pain_chocolat = Product('pain chocolat',2)
    pain_coupe = Product('pain coupé',2)
    parfum = Product('parfum',1)
    telephone = Product('gsm',8)
    bic = Product('bic',10)
    yoghurt = Product('yoghurt',4)
    fromages = Product('fromages',99)
    salami = Product('salami', 23)

    #Create rays
    ray_bread = Ray([pain_chocolat,pain_coupe],5)
    ray_frigo = Ray([yoghurt,fromages,salami],1)
    ray_electronique = Ray([telephone],2)

    #Creates a shop
    carrefour = Shop([ray_bread,ray_electronique,ray_frigo])

    #Runs grocery shopping
    print(carrefour.grocery_shopping(['parfum','gsm','wallet','ecouteurs']))
