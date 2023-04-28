import unittest
from sphere import Sphere
from vec3 import Vec3
from ray import Ray
from hittable import HitRecord

class spheretest(unittest.TestCase):
    def test_sphere_init_center(self):
        new=Sphere(Vec3(1,6,8), 5)
        self.assertEqual(new.center.val, [1,6,8])

    def test_sphere_init_radius(self):
        new=Sphere(Vec3(1,6,8), 5)
        self.assertEqual(new.radius, 5)

    def test_sphere_hit_fail(self):
        news=Sphere(Vec3(1,6,8), 5)
        newr=Ray([0,0,0], [40,40,40])
        self.assertEqual(news.hit(news.center, news.radius,newr), -1)

    def test_sphere_hit_success(self):
        news=Sphere(Vec3(1,6,5), 5)
        newr=Ray([2,10,9], [40,40,40])
        self.assertEqual(news.hit(news.center, news.radius,newr), -0.13791528696058955)
        
    def test_sphere_hitted_fail(self):
        news=Sphere(Vec3(1,6,8), 5)
        newr=Ray([0,0,0], [40,40,40])
        h=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(news.hitted(newr, 0,5,h), False)

    def test_sphere_hitted_success(self):
        news=Sphere(Vec3(1,6,5), 5)
        newr=Ray([2,10,9], [40,40,40])
        h=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
        self.assertEqual(news.hitted(newr, -1,5,h), True)



if __name__ == '__main__':
    unittest.main()