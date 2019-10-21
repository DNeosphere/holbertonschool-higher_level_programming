#!/usr/bin/python3
"""
Unittest for Square class
"""

import unittest
import contextlib
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_classBase(self):
        s0 = Square(1)
        self.assertIsInstance(s0, Base)
        self.assertIsInstance(s0, Rectangle)
        self.assertIsInstance(s0, Square)

    def test_nb(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, '_Base__nb_objects'))
        Base._Base__nb_objects = 0

    def test_Square_arg(self):
        self.assertRaises(TypeError, Square)
        # self.assertRaisesRegex(TypeError,
        #                      "__init__() missing 2 required positional arguments: 'width' and 'height'",
        #                     Square)
        self.assertRaises(TypeError, Square, 1, 1, 1, 1, 1, 1)
        # self.assertRaisesRegex(TypeError,
        #                      "__init__() takes from 2 to 5 positional arguments but 7 were given",
        #                     Square, 1, 1, 1, 1, 1)
        Base._Base__nb_objects = 0

    def test_id(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'id'))
        Base._Base__nb_objects = 0

    def test_size(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'size'))
        Base._Base__nb_objects = 0

    def test_size_value(self):
        s0 = Square(1)
        self.assertEqual(s0.size, 1)
        Base._Base__nb_objects = 0

    def test_size_string(self):
        self.assertRaises(TypeError, Square, "string")
        self.assertRaisesRegex(TypeError, "width must be an integer", Square, "string")
        Base._Base__nb_objects = 0

    def test_size_neg(self):
        self.assertRaises(ValueError, Square, -1)
        self.assertRaisesRegex(ValueError, "width must be > 0", Square, -1)
        Base._Base__nb_objects = 0

    def test_height(self):
        s0 = Square(1, 1)
        self.assertTrue(hasattr(s0, 'height'))
        Base._Base__nb_objects = 0

    def test_height_value(self):
        s0 = Square(1)
        self.assertEqual(s0.height, 1)
        Base._Base__nb_objects = 0

    def test_width(self):
        s0 = Square(1, 1)
        self.assertTrue(hasattr(s0, 'width'))
        Base._Base__nb_objects = 0

    def test_width_value(self):
        s0 = Square(1)
        self.assertEqual(s0.width, 1)
        Base._Base__nb_objects = 0

    def test_x(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'x'))
        Base._Base__nb_objects = 0

    def test_x_value(self):
        s0 = Square(1, 1, 1)
        self.assertEqual(s0.x, 1)
        Base._Base__nb_objects = 0

    def test_x_string(self):
        self.assertRaises(TypeError, Square, 1, "string")
        self.assertRaisesRegex(TypeError, "x must be an integer", Square, 1, "string")
        Base._Base__nb_objects = 0

    def test_x_neg(self):
        self.assertRaises(ValueError, Square, 1, -1)
        self.assertRaisesRegex(ValueError, "x must be >= 0", Square, 1, -1)
        Base._Base__nb_objects = 0

    def test_y(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'y'))
        Base._Base__nb_objects = 0

    def test_y_value(self):
        s0 = Square(1, 1, 1)
        self.assertEqual(s0.y, 1)
        Base._Base__nb_objects = 0

    def test_y_string(self):
        self.assertRaises(TypeError, Square, 1, 1, "string")
        self.assertRaisesRegex(TypeError, "y must be an integer", Square, 1, 1, "string")
        Base._Base__nb_objects = 0

    def test_y_neg(self):
        self.assertRaises(ValueError, Square, 1, 1, -1)
        self.assertRaisesRegex(ValueError, "y must be >= 0", Square, 1, 1, -1)
        Base._Base__nb_objects = 0

    def test_automatic(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        s2 = Square(1)
        self.assertEqual(s2.id, 2)
        s3 = Square(1)
        self.assertEqual(s3.id, 3)
        s4 = Square(1)
        self.assertEqual(s4.id, 4)
        s5 = Square(1)
        self.assertEqual(s5.id, 5)
        Base._Base__nb_objects = 0

    def test_manual(self):
        s1 = Square(1, 0, 0, 45)
        self.assertEqual(s1.id, 45)
        s2 = Square(1, 0, 0, 56)
        self.assertEqual(s2.id, 56)
        s3 = Square(1, 0, 0, 67)
        self.assertEqual(s3.id, 67)
        s4 = Square(1, 0, 0, 78)
        self.assertEqual(s4.id, 78)
        s5 = Square(1, 0, 0, 89)
        self.assertEqual(s5.id, 89)
        Base._Base__nb_objects = 0

    def test_mixed(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        s2 = Square(1, 0, 0, 56)
        self.assertEqual(s2.id, 56)
        s3 = Square(1)
        self.assertEqual(s3.id, 2)
        s4 = Square(1, 0, 0, 78)
        self.assertEqual(s4.id, 78)
        s5 = Square(1)
        self.assertEqual(s5.id, 3)
        Base._Base__nb_objects = 0

    def test_area(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'area'))
        Base._Base__nb_objects = 0

    def test_area_value(self):
        s0 = Square(1)
        s1 = Square(3)
        s2 = Square(2)
        s3 = Square(8, 0, 0, 12)
        self.assertEqual(s0.area(), 1)
        self.assertEqual(s1.area(), 9)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 64)
        Base._Base__nb_objects = 0

    def test_display(self):
        s0 = Square(1)
        self.assertTrue(hasattr(s0, 'display'))
        Base._Base__nb_objects = 0

    def test_display(self):
        string = "##\n##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            Square(2).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        string = "####\n####\n####\n####"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            Square(4).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_display1(self):
        string = "+\n\n  ##\n  ##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("+", end="")
            Square(2, 2, 2).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_display2(self):
        string = "+ ##\n ##"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print("+", end="")
            Square(2, 1, 0).display()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_display_arg(self):
        s1 = Square(1, 1, 1)
        self.assertRaises(TypeError, s1.display, 1)
        # self.assertRaisesRegex(TypeError,
        #                      'display() takes 1 positional argument but 2 were given',
        #                     s1.display, 1)
        Base._Base__nb_objects = 0

    def test_str(self):
        string = "[Square] (1) 0/0 - 1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(1)
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
        string = "[Square] (12) 2/1 - 4"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s1 = Square(4, 2, 1, 12)
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
        string = "[Square] (1) 1/0 - 5"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            s2 = Square(5, 1)
            print(s2)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)

    def test_update_args(self):
        s1 = Square(10, 10, 10)
        s1.update(89)
        string = "[Square] (89) 10/10 - 10"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89)
        string = "[Square] (89) 10/10 - 10"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 2)
        string = "[Square] (89) 10/10 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 2, 4)
        string = "[Square] (89) 4/10 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 2, 4, 5)
        string = "[Square] (89) 4/5 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0

    def test_update_kwargs(self):
        s1 = Square(10, 10, 10)
        s1.update(size=1)
        string = "[Square] (1) 10/10 - 1"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(size=3, x=2)
        string = "[Square] (1) 2/10 - 3"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(y=1, size=2, x=3, id=89)
        string = "[Square] (89) 3/1 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(x=1, size=4, y=3)
        string = "[Square] (89) 1/3 - 4"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        s1.update(89, 2, 4, 5)
        string = "[Square] (89) 4/5 - 2"
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print(s1)
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, string)
        Base._Base__nb_objects = 0
