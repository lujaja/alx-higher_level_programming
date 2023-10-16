#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
"""Define unittest for base.py
    TestBase_instantiation
    TestBase_to_json_string
    TestBsae_save_to_file
    TestBase_from_json_string
    Test_base_create
    TestBase_load_from_file
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_base(unittest.TestCase):
    
    def test_no_arg(self):
        o1 = Base()
        o2 = Base()
        self.assertNotEqual(1, o1.id)
        self.assertNotEqual(2, o2.id)

    def test_id(self):
        obj = Base(12)
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(12, obj.id)
        self.assertEqual(2, obj2.id)

    def test_id_public(self):
        obj = Base(10)
        self.assertEqual(10, obj.id)

    def test_no_insatnces_private(self):
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_objects)
        

    def test_set_id(self):
        b1= Base({1, 3})
        self.assertEqual({1, 3}, b1.id)
        
    def test_tuple_id(self):
        b1 = Base((1, 2))
        self.assertEqual((1, 2), b1.id)
        
    def test_list_id(self):
        b1 = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b1.id)
    
    def test_dict_id(self):
        b1 = Base({'ninja': [1, 2]})
        self.assertEqual({'ninja': [1, 2]}, b1.id)

    def test_comple_id(self):
        b1 = Base(complex(5))
        self.assertEqual(complex(5), b1.id)
        with self.assertRaises(NameError):
            self.assertEqual(complex(n5), b2.id)
        
    def test_float_id(self):
        b1 = Base(5.5)
        self.assertEqual(5.5, b1.id)

    def test_None_id(self):
        b1 = Base(None)
        self.assertEqual(1, b1.id)

    def test_unique_id(self):
        b1 = Base(10)
        self.assertEqual(10, b1.id)

    def test_float_inf(self):
        b1 = Base(float('inf'))
        self.assertEqual(float('inf'), b1.id)

    def test_float_NaN(self):
        b1 = Base(float('nan'))
        self.assertNotEqual(float('nan'), b1.id)

    def test_byte_id(self):
        b1 = Base(b'ninja')
        self.assertEqual(b'ninja', b1.id)

    def test_memview_id(self):
        b1 = Base(b'abcdefg')
        self.assertEqual(b'abcdefg', b1.id)

    def test_frozenset_id(self):
        b1 = Base(frozenset({1, 2}))
        self.assertEqual(frozenset({1, 2}), b1.id)


if __name__ == '__main__':
    unittest.main()
