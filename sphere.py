from hittable import Hittable
from Vec3 import Vec3
import math
from ray import Ray

class Sphere(Hittable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def hit(self, r, t_min, t_max):
        oc = r.origin() - self.center
        print(oc.val)
        a = r.direction().length_squared()
        half_b = oc.dot(r.direction())
        c = oc.length_squared() - self.radius * self.radius
        discriminant = half_b * half_b - a * c
        print('discriminant', discriminant)
        if discriminant < 0:
            return False
        sqrtd = math.sqrt(discriminant)

        root = (-half_b - sqrtd) / a
        print('root',root)
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False
        hit_point = r.at(root)
        outward_normal = (hit_point - self.center) / self.radius
        return True

news=Sphere(Vec3(1,6,5), 5)
newr=Ray([2,10,9], [40,40,40])
print(news.hit(newr,5,6))
print(news.hit(newr,-1,50))