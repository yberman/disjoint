import unittest

import disjoint


class TestDisjoint(unittest.TestCase):
    def setUp(self):
        self.ds = disjoint.Disjoint([1,2,3])

    def tearDown(self):
        self.ds = None

    def test_join_root1(self):
        self.ds.join(1, 2)
        self.assertEqual(self.ds.root(1), self.ds.root(2))
        self.ds.join(2, 3)
        self.assertEqual(self.ds.root(1), self.ds.root(3))

    def test_join_root2(self):
        self.ds.join(1, 2)
        self.assertEqual(self.ds.root(1), self.ds.root(1))
        self.assertEqual(self.ds.root(1), self.ds.root(2))
        self.assertNotEqual(self.ds.root(1), self.ds.root(3))

