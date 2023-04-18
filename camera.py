import Vec3
import math


class Camera:
    def __init__(self):
        viewport_height = 2.0
        viewport_width = 16/9 * viewport_height
        focal_length = 1.0

        origin = Vec3(0, 0, 0)
        horizontal = Vec3(viewport_width, 0, 0)
        vertical = Vec3(0, viewport_height, 0)
        lower_left_corner = origin - horizontal/2 - vertical/2 - Vec3(0, 0, focal_length)
