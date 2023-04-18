import ray
import Vec3
from hittable import Hittable, HitRecord


class HittableList(Hittable):
    def __init__(self):
        self.objects = []

    def add(self, new):
        self.objects.append(new)
        return self.objects

    def pop(self):
        self.objects.pop()
        return self.objects

    def reset(self):
        self.objects=[]
        return self.objects

    # def hit(self, r, t_min, t_max, rec, point, normal, t, front_face):
    #     temp_rec = HitRecord(point, normal, t, front_face)
    #     hit_anything = False
    #     closest_so_far = t_max

    #     for obj in self.objects:
    #         if obj.hit(r, t_min, closest_so_far, temp_rec):
    #             hit_anything = True
    #             closest_so_far = temp_rec.t
    #             rec.t = temp_rec.t
    #             rec.p = temp_rec.p
    #             rec.normal = temp_rec.normal
    #             rec.material = temp_rec.material

    #     return hit_anything