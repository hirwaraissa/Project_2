#Deux produits avec le meme nom, on fait quoi ?
#Deux rayon avec les memes cordonnnes, on fait quoi ?
class Shop:

    def __init__(self,lst_ray=[]):
        self.lst_ray = self.sorting_rays(lst_ray)

    def grocery_shopping(self,lst):
        l = []
        for ray in self.lst_ray:
            for item in lst:
                if ray.buy_item(item):
                    l.append(item)
        return l

    def add_ray(self,new_ray):
        if isinstance(new_ray,Ray) and new_ray not in self.lst_ray:
            for ray in self.lst_ray:
                if ray.cordinate == new_ray.cordinate:
                    return
            self.lst_ray.append(new_ray)
        self.lst_ray = self.sorting_rays(self.lst_ray)

    def sorting_rays(self,lst):
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

    def __str__(self):
        rays_cordinates = []
        for ray in self.lst_ray:
            rays_cordinates.append(ray.cordinate)
        return 'This shop is made up of these rays {0}'.format(rays_cordinates)

class Ray:

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

    def add_item(self,new_item):
        if isinstance(new_item,Product) and new_item not in self.lst_products:
            for product in self.lst_products:
                if product.name==new_item.name:
                    return
            self.lst_products.append(new_item)
        self.lst_products = self.sorting_products(self.sorting_products())

    def buy_item(self,product):
        for item in self.lst_products:
            if item.name == product.lower() and item.quantity>0:
                item.buy()
                return True
        return False

    def __str__(self):
        products = []
        for product in self.lst_products:
            products.append(product.name)
        return 'This ray is made up of these products {0}'.format(products)

class Product:

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def buy(self):
        self.quantity -= 1

    def __str__(self):
        return self.name

if __name__ == '__main__':
    #Create products
    pain_chocolat = Product('pain chocolat',2)
    pain_coupe = Product('pain au lait',2)
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
    faux_rayon = Ray([],5)

    #Creates a shop
    carrefour = Shop([ray_bread,ray_electronique])

    #Runs grocery shopping
    print(carrefour.grocery_shopping(['Parfum','Gsm','Wallet','ecouteurs'])) #['gsm']
    carrefour.add_ray(1)
    print(carrefour) #[2,5]
    carrefour.add_ray(ray_frigo)
    print(carrefour) #[1,2,5]
    carrefour.add_ray(ray_frigo)
    print(carrefour) #[1,2,5]
    carrefour.add_ray(faux_rayon)
    print(carrefour) #[1,2,5]
    print(carrefour.grocery_shopping(['pain au lait'])) #['pain au lait']
    print(ray_frigo) #This ray is made up of these products ['fromages', 'salami', 'yoghurt']
    print(carrefour.grocery_shopping(['bic', 'Gsm', 'salami', 'ecouteurs']))  # ['salami','Gsm']