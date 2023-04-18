import unittest
from sphere import Sphere
from Vec3 import Vec3
from ray import Ray

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
        self.assertEqual(news.hit(newr,5,6), False)

    def test_sphere_hit_success(self):
        news=Sphere(Vec3(1,6,5), 5)
        newr=Ray([2,10,9], [40,40,40])
        self.assertEqual(news.hit(newr,-1,50), True)



if __name__ == '__main__':
    unittest.main()