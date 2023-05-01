from hittable import Hittable


class HittableList(Hittable):
    def __init__(self, objects):
        self.objects = objects

    def add(self, new):
        self.objects.append(new)
        return self.objects

    def pop(self):
        self.objects.pop()
        return self.objects

    def reset(self):
        self.objects=[]
        return self.objects

    def hit(self, r, t_min, t_max, rec):
        hit_anything = False
        closest_so_far = t_max

        for obj in self.objects:
            h, rec=obj.hitted(r, t_min, closest_so_far, rec)
            if h:
                hit_anything = True
                closest_so_far = rec.t
        return hit_anything, rec


# new1=Sphere(Vec3(0,0,0), 1)
# new2=Sphere(Vec3(3,3,3),2)
# l=HittableList([new1,new2])
# r=Ray([0,0,0], [3,3,3])
# h=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
# print(l.hit(r,5,1,h))

    