from camera import Camera
from hittable import HitRecord, Hittable
from hittablelist import HittableList
from ppm import Ppmimage
from ray import Ray
from sphere import Sphere
from vec3 import Vec3
import vec3
import json
from random import random
import rtweekend


def load_json(filename):
    data = json.loads(filename.read())
    return data

def write_color(pixel_color, samples_per_pixel):
    # for c in pixel_color.val:
    #     if c<0:
    #         return 'Please enter positive pixcel color!'
    r, g, b = pixel_color.val
    scale = 1.0 / samples_per_pixel
    r *= scale*256
    g *= scale*256
    b *= scale*256
    return Vec3(r,g,b)

def ray_color(r, world, depth):
    rec = HitRecord()

    if depth <= 0:
        return Vec3(0, 0, 0)
    h, rec=world.hit(r, 0, float("inf"), rec)
    if h:
        target = vec3.random_in_unit_sphere()+rec.point + rec.normal 
        return ray_color(Ray(rec.point.val, (target - rec.point).val), world, depth-1)*0.5

    unit_direction = Vec3.unitVec(r.direction())
    t = (unit_direction.y + 1.0)*0.5
    return Vec3(1.0, 1.0, 1.0)*(1.0 - t) + Vec3(0.5, 0.7, 1.0)*t

def writeFile(filename):
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)
    samples_per_pixel = 100
    max_depth = 50
    
    world = HittableList([])
    world.add(Sphere(Vec3(0, 0, -1), 0.5))
    world.add(Sphere(Vec3(0, -100.5, -1), 100))

    cam = Camera()

    with open(filename, 'w') as file:
        file.write('P3 \n'+str(image_width)+' '+str(image_height)+'\n255 \n')
        for j in range(image_height-1, -1, -1):
            for i in range(image_width):
                pixel_color = Vec3(0, 0, 0)
                for s in range(samples_per_pixel):
                    u = (i + rtweekend.random_double(0,1)) / (image_width-1)
                    v = (j + rtweekend.random_double(0,1)) / (image_height-1)
                    r = cam.get_ray(u, v)
                    pixel_color += ray_color(r, world, max_depth)
                curr=write_color(pixel_color,samples_per_pixel).val
                for c in curr:
                    file.write(str(c)+' ')
                file.write('\n')
            print(j)

writeFile('test.ppm')



# def writeFile(filename):
#     aspect_ratio = 16.0 / 9.0
#     image_width = 400
#     image_height = int(image_width / aspect_ratio)
    

#     viewport_height = 2.0
#     viewport_width = aspect_ratio * viewport_height
#     focal_length = 1.0

#     ori = Vec3(0, 0, 0)
#     horizontal = Vec3(viewport_width, 0, 0)
#     vertical = Vec3(0, viewport_height, 0)
#     lower_left_corner = ori - horizontal/2 - vertical/2 - Vec3(0, 0, focal_length)

#     news=Sphere(Vec3(1,6,5), 5)
#     newt=Sphere(Vec3(2,9,4), 3)

#     with open(filename, 'w') as file:
#         file.write('P3 \n'+str(image_width)+' '+str(image_height)+'\n255 \n')
#         for j in range(image_height-1, -1, -1):
#             for i in range(image_width):
#                 u = i / (image_width-1)
#                 v = j / (image_height-1)
#                 dst = (lower_left_corner + horizontal*u + vertical*v - ori)
#                 r = Ray(ori.val, dst.val)
#                 pixel_color = news.ray_color(r)
#                 curr=writeColor(pixel_color).val
#                 for c in curr:
#                     file.write(str(c)+' ')
#                 file.write('\n')