#!/usr/bin/python3
# -*- coding: utf-8 -*-
import unittest
import sys

import CorrCode as correct
import StudentCode as student


class test_question(unittest.TestCase):

    def test_siblings_1(self):
        rep = """
        Vôtre fonction a retourné {} lorsqu'on ouvre le fichier contenant :
        "Tunga!Olive-Mihigo!3\n"
        alors que la réponse attendue est {}.
              """
        filename = "test_1.txt"
        with open(filename, "w") as file:
            file.write("Tunga!Olive-Mihigo!3\n")
        corr = correct.siblings(filename)
        try:
            stu = student.siblings(filename)
        except Exception as e:
            self.fail("""
        Vôtre fonction a provoqué l'exception {}: {} lorsqu'il ouvre un fichier avec le contenu dans le format correcte""".format(
                type(e), e))
        self.assertEqual(corr, stu, rep.format(stu, corr))

    def test_siblings_2(self):
        rep = """
        Vôtre fonction a retourné {} lorsqu'on ouvre le fichier contenant :
        "Hirwa!Abby-Mihigo!18\n"
        "Manzi!Jonathan-Mihigo!19\n"
        "Ingenzi!Vany!18\n"
        "DeSiena!Palmina!19\n"
        "Kwuete!Samuel!21\n"
        alors que la réponse attendue est {}.
              """
        filename = "test_2.txt"
        with open(filename, "w") as file:
            file.write("Hirwa!Abby-Mihigo!18\n")
            file.write("Manzi!Jonathan-Mihigo!19\n")
            file.write("Ingenzi!Vany!18\n")
            file.write("DeSiena!Palmina!19\n")
            file.write("Kwuete!Samuel!21\n")
        corr = correct.siblings(filename)
        try:
            stu = student.siblings(filename)
        except Exception as e:
            self.fail("""
        Vôtre fonction a provoqué l'exception {}: {} lorsqu'il ouvre un fichier avec le contenu dans le format correcte""".format(
                type(e), e))
        self.assertEqual(corr, stu, rep.format(stu, corr))

    def test_siblings_3(self):  # Quand il n y a rien dans le fichier
        rep = """
        Vôtre fonction ne léver pas l'erreur ValueError quand le fichier est vide.
              """
        filename = "test_3.txt"
        with open(filename, "w") as file:
            pass
        try:
            with self.assertRaises(ValueError):
                student.siblings(filename)
        except Exception as e:
            self.fail("Vôtre fonction a provoque l'exception {} lorsqu'on il reçoit comme argument un fichier non vide au lieu de ValueError".format(type(e)))

    def test_siblings_4(self):  # Quand le fichier contient des erreurs
        rep = """
        Vôtre fonction a retourné {} lorsqu'on ouvre le fichier contenant :
        "HirwaAbby-Mihigo!18\n"
        "Manzi!Jonathan-Mihigo!19\n"
        "Ingenzi!Vany!18\n"
        "DeSienaPalmina!19\n"
        "Kwuete!Samuel!21\n"
        alors que la réponse attendue est {}.
               """
        filename = "test_4.txt"
        with open(filename, "w") as file:
            file.write("HirwaAbby-Mihigo18\n")
            file.write("Manzi!Jonathan-Mihigo!19\n")
            file.write("Ingenzi!Vany!18\n")
            file.write("DeSienaPalmina!19\n")
            file.write("Kwuete!Samuel!21\n")
        corr = correct.siblings(filename)
        try:
            stu = student.siblings(filename)

        except Exception as e:
            self.fail("""
        Vôtre fonction a provoqué l'exception {}: {} avec comme argument un fichier dont le format,
        n'est pas comme celui dans la norme.
                      """.format(type(e), e, n))
        self.assertEqual(corr, stu, rep.format(stu, corr))

    def test_siblings_5(self):
        filename = "non_existant.txt"
        try:
            with self.assertRaises(FileNotFoundError):
                student.siblings(filename)
        except Exception as e:
            self.fail("Vôtre fonction a provoqué l'exception {} lorsqu' il reçoit comme argument un fichier non existant au lieu de FileNotFoundError".format(type(e)))

if __name__ == '__main__':
    unittest.main()