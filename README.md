# PPM Project (Ray Tracing)

This project contains several classes that can be used to implement 3D graphics and raytracing applications.

### Vec3 Class
The Vec3 class is a mathematical vector class that represents a 3D vector. It provides various functionalities that can be used to perform mathematical operations on vectors, such as addition, subtraction, multiplication, division, and dot product. It also includes functions to calculate the length of a vector, its squared length, and its unit vector. Additionally, this class includes functions to write the color values of pixels in an image file and to save the image file in PPM format.

### Ray Class
The Ray class represents a 3D ray that can be used to simulate the path of light in a scene. It includes a constructor that takes a point and a direction vector as input and generates a ray object. It also provides a function to get a point on the ray at a given distance from its origin.

### Hittable Class
The Hittable class is an abstract class that provides an interface for objects in a scene that can be hit by rays. It includes a function to check if a ray intersects with the object and another function to calculate the color of the object at the point of intersection.

### Sphere Class
The Sphere class is a concrete implementation of the Hittable class that represents a 3D sphere. It includes a constructor that takes a center point and a radius as input and generates a sphere object. It also provides an implementation of the hit function that checks if a ray intersects with the sphere and calculates the color of the sphere at the point of intersection.

### Camera Class
The Camera class represents a 3D camera that can be used to generate images of a scene. It includes a constructor that takes the position of the camera, the point it is looking at, the up direction, and the vertical field of view as input and generates a camera object. It also provides a function to generate a ray from the camera's position to a given pixel on the image plane.

### Ppmimage Class
To create a new Ppmimage object, you need to specify the width and height of the image. These values must be positive integers, otherwise an error message will be displayed. You can set the color of a pixel in the Ppmimage using the setPixel method. You can write the Ppmimage object to a file using the writeFile method. This method takes a filename as an argument and writes the image data to a file with the specified name. 

### HittableList Class
The HittableList class is a container for a list of objects that can be hit by a ray. It is commonly used in computer graphics applications to represent a scene or a set of objects that can be rendered.
