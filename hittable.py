from abc import ABC
from Vec3 import Vec3
from ray import Ray

class Hittable(ABC):
    def hit(self, r, t_min, t_max):
        pass

class HitRecord:
    def __init__(self, point, normal, t, front_face):
        self.point = point
        self.normal = normal
        self.t = t
        self.front_face = front_face
        
    def set_face_normal(self, ray, outward_normal):
        if ray.direction().dot(outward_normal) < 0:
            self.normal = outward_normal 
        else:
            self.normal=-outward_normal
        return self.normal.val

    def printt(self):
        return self.t

    def modt(self, t):
        self.t=t
        return self.t

    def printnormal(self):
        return self.normal

    def modnormal(self, normal):
        self.normal=normal
        return self.normal

    def printpoint(self):
        return self.point

    def modpoint(self, point):
        self.point=point
        return self.point

    def printfront_face(self):
        return self.front_face

    def modfront_face(self, front_face):
        self.front_face=front_face
        return self.front_face


# new=HitRecord(Vec3(2,2,2), Vec3(10,10,10), 5, True)
# newr=Ray((1,0,10),(1,1,3))
# print(new.set_face_normal(newr, Vec3(1,2,3)))