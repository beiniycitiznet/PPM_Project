# Ray Tracing in Python

This repository contains Python code for basic ray tracing.

### vec3.py
This file contains the implementation of the Vec3 class, which represents a 3D vector. This class initialized with three float values that represent the x, y, and z coordinates of the vector. The class overloads several operators such as addition, subtraction, multiplication, division, and negation to enable vector arithmetic. The class also includes methods to compute the length, squared length, unit vector, dot product, cross product, and to generate a random vector. Additionally, the module includes utility functions to compute a random unit vector, a random vector within a given range, and to perform reflection and refraction calculations on vectors.

### ray.py
This file contains the implementation of the Ray class, which represents a ray in 3D space. This class includes a method for calculating the position of the ray at a given time.

### hittable.py
This file contains the implementation of the Hittable class, which represents an object that can be hit by a ray. This class includes a method for checking whether a given ray intersects with the object.

### sphere.py
This file contains the implementation of the Sphere class, which represents a sphere object. This class includes a method for checking whether a given ray intersects with the sphere.

### camera.py
This file contains the implementation of the Camera class, which represents a virtual camera that can be used to render a scene. This class includes a method for generating a ray that starts at the camera's position and passes through a given pixel on the screen.

### main.py
This file contains the implementation of the main program, which uses the other classes to render a simple PPM file.

### material.py
This file contains the implementations of three material types used in ray tracing simulations: Lambertian, Metal, and Dielectric. Each material type is defined as a class that inherits from an abstract Material class and implements a scatter method. 

## How to run the program

To run the program, simply run the main.py file in a Python environment. The program will generate a PPM file.
