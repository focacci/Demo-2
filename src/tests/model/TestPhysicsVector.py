from unittest import TestCase
from model.PhysicsVector import PhysicsVector


class TestPhysicsVector(TestCase):

    def test_PhysicsVector(self):
        vector = PhysicsVector(1, 2, 3)

        x = 1
        y = 2
        z = 3

        self.assertEqual(vector.x, x)
        self.assertEqual(vector.y, y)
        self.assertEqual(vector.z, z)
