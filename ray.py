from vec3 import Vec3

class Ray:
    def __init__(self, origin, direction):
        self.orig = Vec3(origin[0],origin[1],origin[2])
        self.dir = Vec3(direction[0],direction[1],direction[2])

    def origin(self):
        return self.orig

    def direction(self):
        return self.dir

    def at(self, t):
        return self.orig + self.dir*t


    # def writeColor(self, pixel_color):
    #     for c in pixel_color:
    #         if c<0:
    #             return 'Please enter positive pixel color!'
    #     r = int(255.999 * pixel_color[0])
    #     g = int(255.999 * pixel_color[1])
    #     b = int(255.999 * pixel_color[2])
    #     return Vec3(r,g,b)


    def ray_color(self,r):
        direction = r.direction()
        unitdir=direction.unitVec()
        t = (unitdir.val[1] + 1.0)*0.5
        res=Vec3(1.0, 1.0, 1.0)*(1.0-t) + Vec3(0.5, 0.7, 1.0)*t
        return res.val

    # def writeFile(self, filename):
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

    #     with open(filename, 'w') as file:
    #         file.write('P3 \n'+str(image_width)+' '+str(image_height)+'\n255 \n')
    #         for j in range(image_height-1, -1, -1):
    #             for i in range(image_width):
    #                 u = i / (image_width-1)
    #                 v = j / (image_height-1)
    #                 dst = (lower_left_corner + horizontal*u + vertical*v - ori)
    #                 r = Ray(ori.val, dst.val)
    #                 pixel_color = self.ray_color(r)
    #                 curr=self.writeColor(pixel_color).val
    #                 for c in curr:
    #                     file.write(str(c)+' ')
    #                 file.write('\n')


# new=Ray([1,2,3],[1,1,1])
# print(new)
# new.writeFile('testray.ppm')