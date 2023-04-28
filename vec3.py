import math
from random import random, uniform

class Vec3:
    def __init__ (self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        if self==None:
            self.val=[0,0,0]
        else:
            self.val=[float(x),float(y),float(z)]
        
    def __add__(self, v3):
        if v3==None:
            return self
        res=Vec3(self.val[0]+v3.val[0],self.val[1]+v3.val[1],self.val[2]+v3.val[2])
        return res

    def __sub__(self, v3):
        if v3==None:
            return self
        res=Vec3(self.val[0]-v3.val[0],self.val[1]-v3.val[1],self.val[2]-v3.val[2])
        return res

    def __neg__(self):
        res=Vec3(-self.val[0],-self.val[1],-self.val[2])
        return res
    
    def __mul__(self,c):
        if c==None:
            return Vec3(0,0,0)
        res=Vec3(self.val[0]*c,self.val[1]*c,self.val[2]*c)
        return res

    def __truediv__(self,c):
        if c==0 or c==None:
            return Vec3(0,0,0)
        res=self*(1/c)
        return res

    def __len__(self):
        return math.sqrt(self.val[0]*self.val[0]+self.val[1]*self.val[1]+self.val[2]*self.val[2])

    def length_squared(self):
            return self.val[0]*self.val[0]+self.val[1]*self.val[1]+self.val[2]*self.val[2]

    def val(self):
        return str(self.val[0])+', '+str(self.val[1])+', '+str(self.val[2])

    def multiply(self, vec):
        res=Vec3(self.val[0]*vec.val[0],self.val[1]*vec.val[1],self.val[2]*vec.val[2])
        return res

    def dot(self, vec):
        res=self.x*vec.x+self.y*vec.y+self.z*vec.z
        return res

    def cross(self,vec):
        res=self.x*vec.x-self.y*vec.y-self.z*vec.z
        return res
    
    def length(self):
        return math.sqrt(self.length_squared())

    def unitVec(self):
        return self/self.length()

    def random(self):
        return Vec3(random(), random(), random())
    
    def writeColor(self, pixel_color):
        for c in pixel_color:
            if c<0:
                return 'Please enter positive pixcel color!'
        r = int(255.999 * pixel_color[0])
        g = int(255.999 * pixel_color[1])
        b = int(255.999 * pixel_color[2])
        return Vec3(r,g,b)
    
def random_range(min, max):
    return Vec3(uniform(min, max), uniform(min, max), uniform(min, max))

def random_in_unit_sphere():
    while True:
        p = random_range(-1,1)
        if p.length_squared() >= 1: 
            continue
        return p
        
    # def ray_color(self, r, world):
    #     rec = HitRecord()
    #     if world.hit(r, 0, float("inf"), rec):
    #         target = rec.p + rec.normal + self.random_in_unit_sphere()
    #         return self.ray_color(Ray(rec.p, target - rec.p), world)*0.5
    #     else:
    #         unit_direction = self.unitVec(r.direction())
    #         t = (unit_direction.y() + 1.0)*0.5
    #         return main.writeColor(1.0, 1.0, 1.0)*(1.0 - t) + main.writeColor(0.5, 0.7, 1.0)*t


    

    # def ray_color(self, r, world, depth):
    #     if depth <= 0:
    #         return self.writeColor(0, 0, 0)

    #     rec = HitRecord()
    #     if world.hit(r, 0, float('inf'), rec):
    #         target = rec.p + rec.normal + self.random_in_unit_sphere()
    #         return self.ray_color(Ray(rec.p, target - rec.p), world, depth - 1)*0.5 

    #     unit_direction = self.unitVec(r.direction())
    #     t = (unit_direction.y() + 1.0)*0.5
    #     return self.writeColor(1.0, 1.0, 1.0)*(1.0 - t) + self.writeColor(0.5, 0.7, 1.0)*t

    # def writeFile(self, filename, width, height):
    #     if width<=0 or height<=0:
    #         return 'Please enter positive width and positive height'
    #     board=[[[0,0,0] for w in range(width)] for h in range(height)]
    #     res='P3 \n'+str(width)+' '+str(height)+'\n255 \n'
    #     for h in range(height-1,-1,-1):
    #         for w in range(width):
    #             scale=[h/(width), w/height,0.25]
    #             color=self.writeColor(scale)
    #             board[h][w]=color
    #     for h in board:
    #         for w in h:
    #             for c in w:
    #                 res=res+str(c)+' '
    #         res+='\n'
    #     with open(filename, 'w') as file:
    #         file.write(res)

    
# new1=Vec3(-5,7,9)
# new2=Vec3(-1,-1,-1)
# print(type(new1.dot(new2)))
# print(new1.writeColor([.1,.2,.3]))
# print(new1.writeFile('testvec3',5,2))

    
    
