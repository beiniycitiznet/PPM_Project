import unittest
from sphere import Sphere
from Vec3 import Vec3
from ray import Ray
from hittable import Hittable, HitRecord
from hittablelist import HittableList

class hittablelist(unittest.TestCase):
    def test_hittablelist_init(self):
        newlist=HittableList([])
        new=Sphere(Vec3(0,0,0),5)
        self.assertEqual(newlist.add(new), [new])

    def test_hittablelist_add(self):
        newlist=HittableList([])
        new=Sphere(Vec3(0,0,0),5)
        self.assertEqual(newlist.add(new), [new])

    def test_hittablelist_pop(self):
        newlist=HittableList([])
        new=Sphere(Vec3(0,0,0),5)
        newlist.add(new)
        newlist.add(new)
        self.assertEqual(newlist.pop(), [new])

    def test_hittablelist_reset(self):
        newlist=HittableList([])
        new=Sphere(Vec3(0,0,0),5)
        newlist.add(new)
        self.assertEqual(newlist.reset(), [])

    def test_hittablelist_hit(self):
        new1=Sphere(Vec3(0,0,0), 1)
        new2=Sphere(Vec3(1,6,5), 5)
        l=HittableList([new1,new2])
        r=Ray([2,10,9], [40,40,40])
        h=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(l.hit(r,5,1,h), False)


if __name__ == '__main__':
    unittest.main()