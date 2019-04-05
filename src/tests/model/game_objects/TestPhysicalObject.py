from unittest import TestCase

from model.PhysicalObject import PhysicalObject
from model.PhysicsVector import PhysicsVector


class TestPhysicalObject(TestCase):

    def test_object_location(self):
        location = PhysicsVector(1, 2, 3)
        velocity = PhysicsVector(4, 5, 6)
        obj = PhysicalObject(location, velocity)

        x = obj.location.x
        y = obj.location.y
        z = obj.location.z

        self.assertEqual(x, 1, "location x")
        self.assertEqual(y, 2, "location y")
        self.assertEqual(z, 3, "location z")

    def test_object_velocity(self):
        location = PhysicsVector(1, 2, 3)
        velocity = PhysicsVector(4, 5, 6)
        obj = PhysicalObject(location, velocity)

        x = obj.velocity.x
        y = obj.velocity.y
        z = obj.velocity.z

        self.assertEqual(x, 4, "velocity x")
        self.assertEqual(y, 5, "velocity y")
        self.assertEqual(z, 6, "velocity z")
