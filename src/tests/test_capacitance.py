import unittest
from emsim.core.parallel_plates import capacitance_parallel_plates
from emsim.core.sphere import capacitance_sphere
from emsim.core.cylinder import capacitance_coaxial_cylinder

class TestCapacitance(unittest.TestCase):
    def test_parallel_plates(self):
        area = 0.01       # m²
        distance = 0.01   # m
        epsilon_r = 1.0
        C = capacitance_parallel_plates(area, distance, epsilon_r)
        self.assertAlmostEqual(C, 8.854e-12, places=14)

    def test_sphere(self):
        radius = 0.01     # m
        C = capacitance_sphere(radius)
        expected = 4 * 3.1415926535 * 8.854e-12 * 0.01
        self.assertAlmostEqual(C, expected, places=14)

    def test_cylinder(self):
        length = 1.0
        r_in = 0.01
        r_out = 0.02
        epsilon_r = 1.0
        C = capacitance_coaxial_cylinder(length, r_in, r_out, epsilon_r)
        expected = (2 * 3.1415926535 * 8.854e-12 * 1.0) / np.log(0.02/0.01)
        self.assertAlmostEqual(C, expected, places=14)

if __name__ == '__main__':
    unittest.main()
