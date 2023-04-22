import unittest
import Vec3

class vec3test(unittest.TestCase):
    def test_add__with_pos_vec(self):
        new1=Vec3.Vec3(1,0,10)
        new2=Vec3.Vec3(99,0,4)
        self.assertEqual((new1+new2).val, [100,0,14])

    def test_add_with_neg_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        new2=Vec3.Vec3(-99,0,-4)
        self.assertEqual((new1+new2).val, [-100,0,-14])

    def test_sub_with_pos_vec(self):
        new1=Vec3.Vec3(1,0,10)
        new2=Vec3.Vec3(99,0,4)
        self.assertEqual((new1-new2).val, [-98,0,6])

    def test_sub_with_neg_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        new2=Vec3.Vec3(-99,0,-4)
        self.assertEqual((new1-new2).val, [98,0,-6])

    def test_neg_with_pos_vec(self):
        new1=Vec3.Vec3(1,0,10)
        self.assertEqual((-new1).val, [-1,0,-10])

    def test_neg_with_neg_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        self.assertEqual((-new1).val, [1,0,10])

    def test_mul_with_pos_vec(self):
        new1=Vec3.Vec3(1,0,10)
        self.assertEqual((new1*4).val, [4,0,40])

    def test_mul_with_neg_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        self.assertEqual((new1*(-4)).val, [4,0,40])

    def test_truediv_with_pos_vec(self):
        new1=Vec3.Vec3(1,0,10)
        self.assertEqual((new1/4).val, [0.25,0,2.5])

    def test_truediv_with_neg_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        self.assertEqual((new1/(-4)).val, [0.25,0,2.5])

    def test_truediv_vec_with_zero(self):
        new1=Vec3.Vec3(-1,0,-10)
        self.assertEqual((new1/0).val, [0,0,0])#'Please input another number!')

    def test_len_with_pos_vec(self):
        new1=Vec3.Vec3(1,0,10)
        self.assertEqual(len(new1), 10)

    def test_lensq_with_pos_vec(self):
        new1=Vec3.Vec3(1,0,10)
        self.assertEqual(new1.length_squared(), 101.0)

    def test_len_with_neg_vec(self):
        new1=Vec3.Vec3(-6,0,6)
        self.assertEqual(len(new1), 8)

    def test_lensq_with_neg_vec(self):
        new1=Vec3.Vec3(-6,0,6)
        self.assertEqual(new1.length_squared(), 72.0)

    def test_multiply_with_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        new2=Vec3.Vec3(1,5,6)
        self.assertEqual((new1.multiply(new2)).val,[-1,0,-60])

    def test_multiply_with_zero_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        new2=Vec3.Vec3(0,0,0)
        self.assertEqual((new1.multiply(new2)).val, [0,0,0])

    def test_dot_with_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        new2=Vec3.Vec3(1,5,6)
        self.assertEqual((new1.dot(new2)),-61)

    def test_dot_with_zero_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        new2=Vec3.Vec3(0,0,0)
        self.assertEqual((new1.dot(new2)), 0)

    def test_cross_with_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        new2=Vec3.Vec3(1,5,6)
        self.assertEqual((new1.cross(new2)),59)

    def test_cross_with_zero_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        new2=Vec3.Vec3(0,0,0)
        self.assertEqual((new1.cross(new2)), 0)

    def test_unitVec_with_zero_vec(self):
        new1=Vec3.Vec3(-1,0,-10)
        self.assertEqual((new1.unitVec()).val,[-0.1,0,-1])

    def test_unitVec_with_vec(self):
        new1=Vec3.Vec3(5,-1,7)
        self.assertEqual((new1.unitVec()).val, [0.625, -0.125, 0.875])

    def test_writeColor_with_pos_vec(self):
        new1=Vec3.Vec3(1,0,10)
        self.assertEqual(new1.writeColor([.1,.2,.3]), [25,51,76])

    def test_writeColor_with_neg_vec(self):
        new1=Vec3.Vec3(-6,0,6)
        self.assertEqual(new1.writeColor([.5,.4,.7]), [127,102,179])

    def test_writeColor_with_neg_pixel_color(self):
        new1=Vec3.Vec3(-6,0,6)
        self.assertEqual(new1.writeColor([-.5,0,.7]), 'Please enter positive pixcel color!')

    def test_writeFile_without_existed_file_with_pos_vec(self):
        new1=Vec3.Vec3(1,2,3)
        new1.writeFile('testvec3',3,4)
        vec3_actual = open('testvec3','r')
        expected='P3 \n3 4\n255 \n0 0 63 0 63 63 0 127 63 \n85 0 63 85 63 63 85 127 63 \n170 0 63 170 63 63 170 127 63 \n255 0 63 255 63 63 255 127 63 \n'
        assert expected==vec3_actual.read()

    def test_ppm_writeFile_no_existed_file_with_neg_vec(self):
        new1=Vec3.Vec3(-5,7,9)
        new1.writeFile('testvec3',5,2)
        vec3_actual = open('testvec3','r')
        expected='P3 \n5 2\n255 \n0 0 63 0 127 63 0 255 63 0 383 63 0 511 63 \n51 0 63 51 127 63 51 255 63 51 383 63 51 511 63 \n'
        assert expected==vec3_actual.read()

    def test_ppm_writeFile_with_existed_file(self):
        with open('testvec3', 'w') as file:
            file.write('Testing!')
        new1=Vec3.Vec3(5,7,-9)
        new1.writeFile('testvec3',5,2)
        vec3_actual = open('testvec3','r')
        expected='P3 \n5 2\n255 \n0 0 63 0 127 63 0 255 63 0 383 63 0 511 63 \n51 0 63 51 127 63 51 255 63 51 383 63 51 511 63 \n'
        assert expected==vec3_actual.read()


if __name__ == '__main__':
    unittest.main()