from abc import ABC, abstractmethod
from ray import Ray
from hittable import HitRecord
import vec3
import math
import rtweekend
import material
import random

class Material(ABC):
    @abstractmethod
    def scatter(self, r_in, rec, attenuation, scattered):
        pass


class Lambertian(Material):
    def __init__(self, albedo):
        self.albedo = albedo

    def scatter(self, r_in, rec, attenuation, scattered):
        scatter_direction = rec.normal + vec3.random_unit_vector()
        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        scattered = Ray(rec.point.val, scatter_direction.val)
        attenuation = self.albedo
        return True, scattered, attenuation

class Metal(Material):
    def __init__(self, albedo, fuzz):
        self.albedo = albedo
        self.fuzz = min(fuzz, 1.0)

    def scatter(self, r_in, rec, attenuation, scattered):
        reflected = vec3.reflect(r_in.directions().unitVec(), rec.normal)
        d=vec3.random_in_unit_sphere()*self.fuzz
        scattered = Ray(rec.point.val, (reflected+d).val)
        attenuation = self.albedo
        return (rec.normal.dot(scattered.directions()) > 0), scattered, attenuation
    
class Dielectric(Material):
    def __init__(self, index_of_refraction=0.0):
        self.ir = index_of_refraction

    def scatter(self, r_in, rec, attenuation, scattered):
        attenuation=vec3.Vec3(1.0, 1.0, 1.0)
        if rec.front_face:
            refraction_ratio = 1.0 / self.ir
        else:
            self.ir

        unit_direction = r_in.directions().unitVec()
        cos_theta = min(rec.normal.dot(-unit_direction), 1.0)
        sin_theta = math.sqrt(1.0 - cos_theta*cos_theta)

        cannot_refract = (refraction_ratio * sin_theta > 1.0)

        if cannot_refract or (material.reflectance(cos_theta, refraction_ratio) > random.random()):
            direction = vec3.reflect(unit_direction, rec.normal)
        else:
            direction = vec3.refract(unit_direction, rec.normal, refraction_ratio)

        scattered=Ray(rec.point.val,direction.val)
        return True, scattered, attenuation
    
def reflectance(cosine, ref_idx):
    r0 = (1 - ref_idx) / (1 + ref_idx)
    r0 = r0 * r0
    return r0 + (1 - r0) * math.pow((1 - cosine), 5)



