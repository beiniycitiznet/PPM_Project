from hittable import Hittable
from vec3 import Vec3
import math
from ray import Ray


class Sphere(Hittable):
    def __init__(self, center, radius, mat_ptr):
        self.center = center
        self.radius = radius
        self.mat_ptr = mat_ptr

    def hit(self, center, radius, r):
        oc = r.origin() - center
        a = r.direction().length_squared()
        b = 2 * oc.dot(r.direction())
        c = oc.length_squared() - radius ** 2
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return -1
        else:
            return (-b - math.sqrt(discriminant)) / (2 * a)

    def hitted(self, r, t_min, t_max, rec):
        offset = r.origins() - self.center
        
        a = r.directions().length_squared()
        b = 2 * Vec3.dot(offset, r.directions())
        c = offset.length_squared() - self.radius ** 2

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return False, rec

        sqrtd = math.sqrt(discriminant)

        root = (-b - sqrtd) / (2 * a)
        if t_min <= root and root <= t_max:
            rec.t = root
            rec.point = r.at(rec.t)
            outward_normal = (rec.point - self.center) / self.radius
            rec.set_face_normal(r, outward_normal)
            rec.mat_ptr=self.mat_ptr
            return True, rec

        root = (-b + sqrtd) / (2 * a)
        if t_min <= root and root<= t_max:
            rec.t = root
            rec.point = r.at(rec.t)
            outward_normal = (rec.point - self.center) / self.radius
            rec.set_face_normal(r, outward_normal)
            rec.mat_ptr=self.mat_ptr
            return True, rec

        return False, rec

    def ray_color(self, r):
        t = self.hit(Vec3(0, 0, -1), 0.5, r)
        if t > 0:
            face_nromal = (r.at(t) - Vec3(0, 0, -1)).unitVec()
            return (Vec3(face_nromal.x + 1, face_nromal.y + 1, face_nromal.z + 1)*0.5).val
        unit_direction = r.directions().unitVec()
        t = 0.5 * (unit_direction.y + 1)
        return  (Vec3(1, 1, 1)*(1 - t) + Vec3(0.5, 0.7, 1)*t).val


# news=Sphere(Vec3(1,6,5), 5)
# newr=Ray([2,10,9], [40,40,40])
# print(news.hit(newr,5,6))
# print(news.hit(newr,-1,50))
# print(news.ray_color(newr))
# news.writeFile('sphere.ppm')