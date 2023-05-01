from vec3 import Vec3

class Ray:
    def __init__(self, origin=[0,0,0], direction=[0,0,0]):
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




# new=Ray([1,2,3],[1,1,1])
# print(new)
# new.writeFile('testray.ppm')