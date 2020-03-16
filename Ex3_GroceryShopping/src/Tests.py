#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Ingenzi Vany Valentin

import unittest
import sys

import Studentcode as student

class Test_GroceryShopping(unittest.TestCase):

    def test1_all_classes(self):
        """
        Ce test permet de voir si les élèves ont implimenté trois classes sont implimenté.
        Ce que je fait ce que j'appele les trois classes simplement.
        """
        try:
            trial = student.Product('test', 0)
            testing = student.Shelf([trial], 1)
            shop = student.Shop([testing])
        except Exception as e:
            self.fail("Vous n'avez pas implimenté les 3 classes de la maniére indiqué.")

    def test2_product_buy(self):
        """
        Ce test permet de test la méthode buy sur la classe Product.
        """
        rep = """
        Après un appel de vôtre méthode 'buy' sur un Product initialisé avec {} comme quantité.
        La quantité du produit devient {} au lieu de {}."""
        try:
            arg = 0 # Ici j'utulise une variable pour avoir un feedback plus claire au cas ou il y à un erreur
            product1 = student.Product('test1', arg) # Le constructeur de l'eleve
            product1.buy()
            test1 = product1.quantity # Je regarde la quantite apres être achetée

            arg = 3
            product2 = student.Product('test2', arg) # Le constructeur de l'eleve
            product2.buy()
            test2 = product2.quantity # Je regarde la quantite apres être achetée

        except Exception as e:
            self.fail("""
        Vôtre fonction 'buy' a provoqué l'exception {} aprés un appel sur un Product initialisé comme quantité {} """.format(
                e, 0, arg))

        self.assertEqual(test1, 0, rep.format(0, test1, 0))
        self.assertEqual(test2, 2, rep.format(3, test2, 2))

    def test3_product_restock(self):
        """
        Ce test permet d'evaluer la méthode restock de la classe Product
        """
        rep = """
        Après un appel de vôtre méthode 'restock' avec comme argument {} sur un Product avec {} comme quantité.
        La quantité du produit dévient {} au lieu de {}."""
        try:
            arg_init, arg_restock = (3, 2) #Le principe des ces variables ce de pouvoir les utuliser en cas d'erreur comme l'élève peut voir son erreur.
            produit1 = student.Product('test1', arg_init)
            produit1.restock(arg_restock)
            test1 = produit1.quantity #Ici la quantité ne doit pas changer car arg_restock est plus pétit que la quantité actuelle.

            arg_init, arg_restock = (0, 5)
            produit2 = student.Product('test2', arg_init)
            produit2.restock(arg_restock)
            test2 = produit2.quantity

        except Exception as e:
            self.fail("""
        Vôtre fonction 'restock' a provoqué l'exception {} aprés un appel avec comme argument {}.
        Sur un Product qui a comme quantité {}. """.format(e, arg_restock, arg_init))

        self.assertEqual(test1, 3, rep.format(2, 3, test1, 3))
        self.assertEqual(test2, 5, rep.format(5, 0, test2, 5))

    def test3_shelf_add_item(self):
        """
        Ce test permet de test la méthode 'add_item' et la méthode 'sorting_products' de la classe Shelf
        """
        rep = """
        Après un appel de vôtre méthode 'add_item' avec comme argument un Product {}.
        La longeur de lst_products est {} au lieu de {}"""

        rep2 = """
        Aprés un ajout de vôtre méthode 'add_item' ne trie pas la lst_products, de l'ordre alphabétique.

        Aprés l'ajout des ces trois éléments.
        Product('mango',1)
        Product('donut',3)
        Product('eau',0)

        l'élément à l'indice {} dans lst_products devrait être {} au lieu de {}.
        """
        try:
            test1_msg = "non existant dans self.lst_products"
            shelf = student.Shelf([student.Product("mango", 1)], 1)
            donut = student.Product('donut', 3)
            shelf.add_item(donut)
            test1 = len(shelf.lst_products)

            test2_msg = "déjà dans self.lst_products"
            shelf.add_item(donut)
            test2 = len(shelf.lst_products)

            test3_msg = "avec le même nom que l'un des produits dans self.lst_products"
            shelf.add_item(student.Product("donut", 1))
            test3 = len(shelf.lst_products)

            shelf.add_item(student.Product("eau", 0)) #j'ajoute ceci pour que l'élève ne mentient pas une longeur de la liste constante pour passe les tests.

            test4_msg = "avec le même nom que l'un des produits dans self.lst_products"
            shelf.add_item(student.Product("mango", 5))
            test4 = len(shelf.lst_products)

        except Exception as e:
            self.fail("""
            Vôtre fonction 'add_item' a provoqué l'exception {} aprés un appel 
            avec une instance de la classe Product """.format(e, arg_restock, arg_init))

        # Test les ajouts
        self.assertEqual(test1, 2, rep.format(test1_msg, test1, 2))
        self.assertEqual(test2, 2, rep.format(test2_msg, test2, 2))
        self.assertEqual(test3, 2, rep.format(test3_msg, test3, 2))
        self.assertEqual(test4, 3, rep.format(test4_msg, test4, 3))

        # Test si la liste est trie
        self.assertEqual(shelf.lst_products[0].name, "donut", rep2.format(0, "donut", shelf.lst_products[0].name))
        self.assertEqual(shelf.lst_products[1].name, "eau", rep2.format(1, "eau", shelf.lst_products[1].name))
        self.assertEqual(shelf.lst_products[2].name, "mango", rep2.format(2, "mango", shelf.lst_products[2].name))

    def test4_shelf_init(self):
        """
        Ce test permet d'évaluer l'initialisateur de la classe shelf et sorting_shelf.
        """
        rep = """

        Vôtre initialisateur de la classe Shelf ne tri pas directement la liste donnée à l'initialisateur,
        regardez si vous avez implimenté la methode sorting_products que vous pouvez appeler dans __init__."""
        try:
            pain = student.Product('pain', 2)
            donut = student.Product('donut', 4)
            shelf = student.Shelf([pain, donut], 1)
        except Exception as e:
            self.fail("""
        Vôtre fonction __init__ de la classe Shelf a provoqué l'exception {} lorsque nous initialisons un rayon avec
        une liste de deux produits de la classe Product.""".format(e))
        self.assertEqual(shelf.lst_products[0].name, donut.name, rep)
        self.assertEqual(shelf.lst_products[1].name, pain.name, rep)

    def test5_shop_add_shelf(self):
        """
        Ce test permet d'évaluer la méthode 'add_shelf' et 'sorting_shelf' de la classe Shop.
        """
        rep =  """ 
        Après un appel de vôtre méthode 'add_shelf' avec comme argument un Shelf {}.
        La longeur de lst_products est {} au lieu de {}"""

        rep2 = """
        Aprés un ajout d'un Shelf avec vôtre méthode'add_shelf' de la classe Shop. 
        La méthode ne tri pas les shelfs en fonction de leur cordonne dans l'ordre croissant.
        Regardez si vous avez bien implimenté la méthode 'sorting_shelf' que vous pouvez utuliser.
        
        Aprés l'ajout de ces trois éléments.
        
        rayon_pâtisserie= Shelf([...],1)
        rayon_frigo = Shelf([],4)
        rayon_alcool = Shelf([],3)
        
        l'élément à l'indice {} dans lst_shelves devrait être {} au lieu de {}.
        """
        try:
            pain = student.Product('pain', 2)
            donut = student.Product('yaourt', 4)

            shelf_1 = student.Shelf([], 1)
            shelf_2 = student.Shelf([], 4)
            shelf_3 = student.Shelf([], 3)

            shop = student.Shop()

            test1_msg = " non existant dans lst_shelves"
            shop.add_shelf(shelf_1)
            test1 = len(shop.lst_shelves)

            test2_msg = " déjà existante dans lst_shelves"
            shop.add_shelf(shelf_1)
            test2 = len(shop.lst_shelves)

            shop.add_shelf(shelf_2) #j'ajoute ceci pour que l'élève ne mentient pas une longeur de la liste constante pour passe les tests.

            test3_msg = " portant le même cordonée qu'un autre shelf"
            shop.add_shelf(student.Shelf([],4))
            test3 = len(shop.lst_shelves)

            shop.add_shelf(shelf_3)
        except Exception as e:
            self.fail("""
        Vôtre méthode 'add_shelf' a provoqué l'exception {} lorsqu'elle a comme argument
        un objet de la classe Shelf """.format(e))

        # Test l'ajout des instances Shelf.
        self.assertEqual(test1,1,rep.format(test1_msg,1,test1))
        self.assertEqual(test2,1,rep.format(test2_msg,1,test2))
        self.assertEqual(test3,2,rep.format(test3_msg,2,test3))

        # Test le tri aprés l'ajout
        self.assertEqual(shop.lst_shelves[0],shelf_1,rep2.format(0,"rayon_pâtisserie","rayon_frigo" if shop.lst_shelves[0].cordinate == 4 else "rayon_alcool"))
        self.assertEqual(shop.lst_shelves[1],shelf_3,rep2.format(1,"rayon_alcool","rayon_pâtessirie" if shop.lst_shelves[1].cordinate == 1 else "rayon frigo" ))
        self.assertEqual(shop.lst_shelves[2],shelf_2,rep2.format(2,"rayon_frigo", "rayon_alcool" if shop.lst_shelves[2].cordinate == 3 else "rayon_pâtessirie"))

    def test6_shop_grocerry_shopping(self):
        """
        Ceci permet de la méthode 'grocerry_shopping' de la classe Shop.
        Ce test ne passerai pas si les classes n'est pas implimentés de la maniére indiqué.
        """
        rep = """ 
        Vôtre méthode 'grocerry_shopping' n'est pas implimenté de la façon demandé, n'oubliez pas de trier
        les rayons selon leur cordonnes.
        Voir si vôtre code retourne la même chose que l'exemple donne dans l'énoncé.
        """
        try:
            # Creates products
            pain_chocolat = student.Product('pain chocolat', 2)
            parfum = student.Product('parfum', 1)
            telephone = student.Product('gsm', 8)
            yoghurt = student.Product('yoghurt', 4)
            fromages = student.Product('fromages', 99)
            salami = student.Product('salami', 23)

            # Create rays
            shelf_sanitaires = student.Shelf([parfum],3)
            shelf_bread = student.Shelf([pain_chocolat], 5)
            shelf_frigo = student.Shelf([yoghurt, fromages], 1)
            shelf_frigo.add_item(salami)
            shelf_electronique = student.Shelf([telephone], 2)

            # Creates a shop
            carrefour = student.Shop([shelf_bread, shelf_electronique])
            carrefour.add_shelf(shelf_frigo)
            carrefour.add_shelf(shelf_sanitaires)

            # Runs grocery shopping
            first_test = carrefour.grocery_shopping(['parfum', 'gsm', 'wallet', 'ecouteurs'])  # ['gsm','parfum']
            second_test = carrefour.grocery_shopping(['pain chocolat','parfum'])  # ['pain chocolat']
            parfum.restock(2) #Je restock le parfum
            third_test = carrefour.grocery_shopping(['bic', 'gsm', 'salami', 'ecouteurs','parfum'])  # ['salami','parfum','gsm']

        except Exception as e:
            self.fail(
        "Vôtre méthode 'grocerry_shopping' a provoqué l'exception {}: {} ".format(type(e), e))

        self.assertEqual(first_test, ['gsm','parfum'], rep)
        self.assertEqual(second_test, ['pain chocolat'], rep)
        self.assertEqual(third_test, ['salami','gsm','parfum'], rep)

if __name__ == '__main__':
    unittest.main(2)