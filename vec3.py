import math
from random import random, uniform


class Vec3:
    def __init__ (self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
        if self==None:
            self.val=[0,0,0]
        else:
            self.val=[float(x),float(y),float(z)]

    def __repr__(self) -> str:
        return f'{self.val}'
        
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
    
    def near_zero(self):
        s = 1e-8
        return (abs(self.x) < s) and (abs(self.y) < s) and (abs(self.z) < s)
    
def random_unit_vector():
    return random_in_unit_sphere().unitVec()
    
def random_range(min, max):
    return Vec3(uniform(min, max), uniform(min, max), uniform(min, max))

def refract(uv, n, etai_over_etat):
    cos_theta = min(n.dot(-uv), 1.0)
    r_out_perp = (uv + n*cos_theta)*etai_over_etat 
    r_out_parallel = n*(-math.sqrt(abs(1.0 - r_out_perp.length_squared())))
    return r_out_perp + r_out_parallel


def random_in_unit_sphere():
    while True:
        p = random_range(-1,1)
        if p.length_squared() >= 1:
            continue
        return p

    
def random_in_hemisphere(normal):
    in_unit_sphere = random_in_unit_sphere()
    if normal.dot(in_unit_sphere) > 0.0:
        return in_unit_sphere
    else:
        return -in_unit_sphere
    


def reflect(v, n):
    return v - n * 2 * v.dot(n) 

    
# new1=Vec3(-5,7,9)
# new2=Vec3(-1,-1,-1)
# print(type(new1.dot(new2)))
# print(new1.writeColor([.1,.2,.3]))
# print(new1.writeFile('testvec3',5,2))

    
    
