import unittest
import ray

class raytest(unittest.TestCase):
    def test_ray_init_orig(self):
        new=ray.Ray((1,0,10),(2,2,2))
        self.assertEqual(new.origin().val, [1,0,10])

    def test_ray_init_dir(self):
        new=ray.Ray((1,0,10),(-2,2,2))
        self.assertEqual(new.direction().val, [-2,2,2])

    def test_ray_pos_at(self):
        new=ray.Ray((1,0,10),(1,1,3))
        self.assertEqual(new.at(2).val, [3,2,16])

    def test_ray_neg_at(self):
        new=ray.Ray((1,0,10),(1,-1,3))
        self.assertEqual(new.at(-2).val, [-1,2,4])

    # def test_writeColor_with_no_error(self):
    #     new=ray.Ray((1,0,10),(1,1,3))
    #     self.assertEqual(new.writeColor([.5,.4,.7]).val, [127,102,179])

    # def test_writeColor_with_neg_pixel_color(self):
    #     new=ray.Ray((1,0,10),(1,1,3))
    #     self.assertEqual(new.writeColor([-.5,0,.7]), 'Please enter positive pixcel color!')

    # def test_writeFile(self):
    #     new=ray.Ray([1,2,3],[1,1,1])
    #     self.assertEqual(new.writeFile('testray'), None)

if __name__ == '__main__':
    unittest.main()