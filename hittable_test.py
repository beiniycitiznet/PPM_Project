import unittest
from hittable import HitRecord
from vec3 import Vec3
from ray import Ray

class hittabletest(unittest.TestCase):
    def test_HitRecord_init_point(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.point.val, [2,2,2])

    def test_HitRecord_init_normal(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.normal.val, [10,10,10])

    def test_HitRecord_init_t(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.t, 5)

    def test_HitRecord_init_frontface(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.front_face, True)

    def test_HitRecord_modt(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.modt(9), 9)

    def test_HitRecord_printt(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.printt(), 5)

    def test_HitRecord_printnormal(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.printnormal().val, [10,10,10])

    def test_HitRecord_modnormal(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.modnormal(Vec3(9,8,7)).val, [9,8,7])

    def test_HitRecord_printpoint(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.printpoint().val, [2,2,2])

    def test_HitRecord_modpoint(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.modpoint(Vec3(5,7,9)).val, [5,7,9])

    def test_HitRecord_printfrontface(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(new.printfront_face(), True)

    def test_set_face_normal(self):
        new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        newr=Ray((1,0,10),(1,1,3))
        self.assertEqual(new.set_face_normal(newr, Vec3(1,2,3)), [-1,-2,-3])

if __name__ == '__main__':
    unittest.main()