#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Auteur: Ivan Wandja


import unittest
import sys

import CorrCode as correct
import StudentCode as student


class TestReplace(unittest.TestCase):
    def setUp(self):
        self.rep = """
Vous avez retourne :
{}
-----
A la place de :
{}

Lorsque :
text = {}
char_1 = {}
char_2 = {}
                """
#chaque test teste différents types de phrases avec des nombres inclus et un paragraphe(test_4)

    def test_1(self):
        text = """My name is Ivan, Ivan means amma get rich"""
        char_1 = "an"
        char_2 = "ana"
        try:
            student_ans = student.replace(text, char_1, char_2)
        except Exception as e:
            self.fail("""
            Votre fonction a provoqué l'exception {} avec comme argument :
            text = {}
            char_1 = {}
            char_2 = {}
                """.format(e, text, char_1, char_2))
        correct_ans = correct.replace(text, char_1, char_2)
        self.assertEqual(student_ans, correct_ans, self.rep.format(student_ans, correct_ans, text, char_1, char_2))

    def test_2(self):
        text = """Seven"""
        char_1 = "n"
        char_2 = "re"
        try:
            student_ans = student.replace(text, char_1, char_2)
        except Exception as e:
            self.fail("""
            Votre fonction a provoqué l'exception {} avec comme argument :
            text = {}
            char_1 = {}
            char_2 = {}
                """.format(e, text, char_1, char_2))
        correct_ans = correct.replace(text, char_1, char_2)
        self.assertEqual(student_ans, correct_ans, self.rep.format(student_ans, correct_ans, text, char_1, char_2))

    def test_3(self):
        text = "welcome to my bedroom"
        char_1 = "bed"
        char_2 = "bath"
        try:
            student_ans = student.replace(text, char_1, char_2)
        except Exception as e:
            self.fail("""
            Votre fonction a provoqué l'exception {} avec comme argument :
            text = {}
            char_1 = {}
            char_2 = {}
                """.format(e, text, char_1, char_2))
        correct_ans = correct.replace(text, char_1, char_2)
        self.assertEqual(student_ans, correct_ans, self.rep.format(student_ans, correct_ans, text, char_1, char_2))

    def test_4(self):
        text = """
        Staying at home and calling a doctor as soon as the first symptoms appear is an effective reflex.
        It is at this stage the best response that can be given. 
        It is at the time of the onset of symptoms that the person is most contagious."""
        char_1 = "effective"
        char_2 = "exceptional"

        try:
            student_ans = student.replace(text, char_1, char_2)
        except Exception as e:
            self.fail("""
            Votre fonction a provoqué l'exception {} avec comme argument :
            text = {}
            char_1 = {}
            char_2 = {}
                """.format(e, text, char_1, char_2))
        correct_ans = correct.replace(text, char_1, char_2)
        self.assertEqual(student_ans, correct_ans, self.rep.format(student_ans, correct_ans, text, char_1, char_2))

    def test_5(self):
        text = " I made 999,999,980 Euros last year"
        char_1 = "9"
        char_2 = "0"

        try:
            student_ans = student.replace(text, char_1, char_2)

        except Exception as e:
            self.fail("""
            Votre fonction a provoqué l'exception {} avec comme argument :
            text = {}
            char_1 = {}
            char_2 = {}
                """.format(e, text, char_1, char_2))

        correct_ans = correct.replace(text, char_1, char_2)
        self.assertEqual(student_ans, correct_ans, self.rep.format(student_ans, correct_ans, text, char_1, char_2))


if __name__ == '__main__':
    unittest.main()