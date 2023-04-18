import unittest
from sphere import Sphere
from Vec3 import Vec3
from ray import Ray
from hittable import Hittable
from hittablelist import HittableList

class hittablelist(unittest.TestCase):
    def test_hittablelist_add(self):
        newlist=HittableList()
        new=Sphere(Vec3(0,0,0),5)
        self.assertEqual(newlist.add(new), [new])

    def test_hittablelist_pop(self):
        newlist=HittableList()
        new=Sphere(Vec3(0,0,0),5)
        newlist.add(new)
        newlist.add(new)
        self.assertEqual(newlist.pop(), [new])

    def test_hittablelist_reset(self):
        newlist=HittableList()
        new=Sphere(Vec3(0,0,0),5)
        newlist.add(new)
        self.assertEqual(newlist.reset(), [])




if __name__ == '__main__':
    unittest.main()