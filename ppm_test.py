import unittest
import ppm

class ppmtest(unittest.TestCase):
    def test_ppm_when_image_created_without_pixel_passing(self):
        new=ppm.Ppmimage(10,2)
        self.assertEqual(new.writeString(), 'P3 \n10 2\n255 \n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 \n')
        new=ppm.Ppmimage(3,11)
        self.assertEqual(new.writeString(), 'P3 \n3 11\n255 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 \n')
        
    def test_ppm_when_image_created_without_pixel_not_passing(self):
        new=ppm.Ppmimage(-1,2)
        self.assertRaises(AttributeError, lambda:new.writeString())
        new=ppm.Ppmimage(-3,-2)
        self.assertRaises(AttributeError, lambda:new.writeString())
        new=ppm.Ppmimage(3,-2)
        self.assertRaises(AttributeError, lambda:new.writeString())

    def test_ppm_with_x_y_overage(self):
        new=ppm.Ppmimage(2,2)
        self.assertEqual(new.setPixel(3,2,[0,0,0]), None)
        self.assertEqual(new.setPixel(2,3,[0,0,0]), None)
        self.assertEqual(new.setPixel(2,2,[0,0,0]), None)

    def test_ppm_with_x_y_correctly_inputted(self):
        new=ppm.Ppmimage(2,2)
        self.assertEqual(new.setPixel(1,1,[0,0,0]), [[[0,0,0],[0,0,0]],[[0,0,0],[0,0,0]]])
        self.assertEqual(new.setPixel(1,0,[0,255,0]), [[[0,0,0],[0,255,0]],[[0,0,0],[0,0,0]]])
        self.assertEqual(new.setPixel(0,0,[0,0,255]), new.setPixel(1,0,[255,0,255]), [new.setPixel(0,1,[0,0,2]), new.setPixel(1,1,[1,1,1]), [[0,0,255],[255,0,255]],[[0,0,2],[1,1,1]]])

    def test_ppm_with_x_y_shortage(self):
        new=ppm.Ppmimage(5,5)
        self.assertEqual(new.setPixel(-1,2,[0,1,0]), None)
        self.assertEqual(new.setPixel(2,-3,[0,0,255]), None)
        self.assertEqual(new.setPixel(-2,-2,[1,0,0]), None)

    def test_setPixel_with_neg_color(self):
        new=ppm.Ppmimage(7,3)
        self.assertEqual(new.setPixel(1,2,[0,-1,0]), None)
        self.assertEqual(new.setPixel(2,1,[0,0,-255]), None)
        self.assertEqual(new.setPixel(0,0,[300,0,0]), None)

    # def test_ppm_when_image_created_with_pixel_and_error_setPixel(self):
    #     new=ppm.Ppmimage(4,9)
    #     self.assertEqual(new.setPixel(1,2,[0,-1,0]),None)
    #     self.assertEqual(new.writeString(), 'P3 \n4 9\n255 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n')
    
    # def test_ppm_when_image_created_with_pixel_and_error_init(self):
    #     new=ppm.Ppmimage(4,8)
    #     self.assertEqual(new.setPixel(-1,2,[0,1,0]),None)
    #     self.assertEqual(new.writeString(), 'P3 \n4 8\n255 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n')
 
    # def test_ppm_writeFile_no_existed_file(self):
    #     new=ppm.Ppmimage(4,3)
    #     new.setPixel(1,2,[0,255,0])
    #     new.writeFile('testppm')

    #     ppm_actual = open('testppm','r')
    #     expected='P3 \n4 3\n255 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 255 0 0 0 0 0 0 0 \n'
    #     assert expected==ppm_actual.read()

    # def test_ppm_writeFile_no_existed_file(self):
    #     new=ppm.Ppmimage(4,3)
    #     new.setPixel(1,2,[0,255,0])
    #     new.writeFile('testppm')

    #     ppm_actual = open('testppm','r')
    #     expected='P3 \n4 3\n255 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 255 0 0 0 0 0 0 0 \n'
    #     assert expected==ppm_actual.read()

    # def test_ppm_writeFile_with_existed_file(self):
    #     with open('testppm', 'w') as file:
    #         file.write('Testing!')
    #     new=ppm.Ppmimage(4,3)
    #     new.setPixel(1,2,[0,255,0])
    #     new.setPixel(2,2,[255,255,0])
    #     new.writeFile('testppm')

    #     ppm_actual = open('testppm','r')
    #     expected='P3 \n4 3\n255 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 0 0 0 0 0 \n0 0 0 0 255 0 255 255 0 0 0 0 \n'
    #     assert expected==ppm_actual.read()


if __name__ == '__main__':
    unittest.main()
    





