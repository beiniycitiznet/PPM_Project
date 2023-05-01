from abc import ABC, abstractmethod
from ray import Ray
from hittable import HitRecord
import vec3


class Material(ABC):
    @abstractmethod
    def scatter(self, r_in, rec, attenuation, scattered):
        pass
        # raise NotImplementedError

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
        reflected = vec3.reflect(r_in.direction().unitVec(), rec.normal)
        d=vec3.random_in_unit_sphere()*self.fuzz
        scattered = Ray(rec.point.val, (reflected+d).val)
        attenuation = self.albedo
        return (rec.normal.dot(scattered.direction()) > 0), scattered, attenuation

