from hittable import Hittable
from vec3 import Vec3
import math
from ray import Ray


class Sphere(Hittable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

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
        offset = r.origin() - self.center
        a = r.direction().length_squared()
        b = 2 * Vec3.dot(offset, r.direction())
        c = offset.length_squared() - self.radius ** 2

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            return False, rec

        sqrtd = math.sqrt(discriminant)

        root = (-b - sqrtd) / (2 * a)
        if t_min <= root and root <= t_max:
            rec.t = root
            rec.p = r.at(rec.t)
            outward_normal = (rec.p - self.center) / self.radius
            rec.set_face_normal(r, outward_normal)
            return True, rec

        root = (-b + sqrtd) / (2 * a)
        if t_min <= root and root<= t_max:
            rec.t = root
            rec.point = r.at(rec.t)
            outward_normal = (rec.point - self.center) / self.radius
            rec.set_face_normal(r, outward_normal)
            return True, rec

        return False, rec


    # def writeColor(self, pixel_color):
    #     for c in pixel_color:
    #         if c<0:
    #             return 'Please enter positive pixcel color!'
    #     r = int(255.999 * pixel_color[0])
    #     g = int(255.999 * pixel_color[1])
    #     b = int(255.999 * pixel_color[2])
    #     return Vec3(r,g,b)

    def ray_color(self, r):
        t = self.hit(Vec3(0, 0, -1), 0.5, r)
        if t > 0:
            face_nromal = (r.at(t) - Vec3(0, 0, -1)).unitVec()
            return (Vec3(face_nromal.x + 1, face_nromal.y + 1, face_nromal.z + 1)*0.5).val
        unit_direction = r.direction().unitVec()
        t = 0.5 * (unit_direction.y + 1)
        return  (Vec3(1, 1, 1)*(1 - t) + Vec3(0.5, 0.7, 1)*t).val

    # def writeFile(self, filename):
    #     aspect_ratio = 16 / 9
    #     image_width = 400
    #     image_height = int(image_width / aspect_ratio)

    #     viewport_height = 2
    #     viewport_width = aspect_ratio * viewport_height
    #     focal_length = 1

    #     ori = Vec3(0, 0, 0)
    #     horizontal = Vec3(viewport_width, 0, 0)
    #     vertical = Vec3(0, viewport_height, 0)
    #     lower_left_corner = ori - horizontal/2 - vertical/2 - Vec3(0, 0, focal_length)

    #     board=[[[0,0,0] for w in range(image_width)] for h in range(image_height)]
    #     res='P3 \n'+str(image_width)+' '+str(image_height)+'\n255 \n'

    #     for j in range(image_height-1, -1, -1):
    #         for i in range(image_width):
    #             u = i / (image_width-1)
    #             v = j / (image_height-1)
    #             r = Ray(ori.val, (lower_left_corner + horizontal*u + vertical*v - ori).val)
    #             pixel_color = self.ray_color(r)
    #             board[j][i]=self.writeColor(pixel_color).val
                
    #     for h in board:
    #         for w in h:
    #             for c in w:
    #                 res=res+str(c)+' '
    #         res+='\n'

    #     with open(filename, 'w') as file:
    #         file.write(res)

# news=Sphere(Vec3(1,6,5), 5)
# newr=Ray([2,10,9], [40,40,40])
# print(news.hit(newr,5,6))
# print(news.hit(newr,-1,50))
# print(news.ray_color(newr))
# news.writeFile('sphere.ppm')