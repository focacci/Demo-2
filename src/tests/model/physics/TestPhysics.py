from unittest import TestCase

from model.Physics import Physics
from model.Player import Player
from model.PhysicsVector import PhysicsVector
from model.PhysicalObject import PhysicalObject
from model.World import World


class TestPhysics(TestCase):

    def test_computePotentialLocation(self):
        physics = Physics()

        location = PhysicsVector(0, 0, 0)
        velocity = PhysicsVector(1, 0, 3)
        obj = PhysicalObject(location, velocity)

        dt = 5

        actual_location = physics.computePotentialLocation(obj, dt)
        expected_location = PhysicsVector(5, 0, 15)

        self.assertEqual(expected_location.x, actual_location.x)
        self.assertEqual(expected_location.y, actual_location.y)
        self.assertEqual(expected_location.z, actual_location.z)

    def test_updateVelocity(self):
        physics = Physics()

        location = PhysicsVector(0, 0, 0)
        velocity = PhysicsVector(0, 0, 20)
        obj = PhysicalObject(location, velocity)
        world = World(5)
        dt = 3

        physics.updateVelocity(obj, world, dt)

        expected = PhysicsVector(0, 0, 5)

        self.assertEqual(obj.velocity.x, expected.x)
        self.assertEqual(obj.velocity.y, expected.y)
        self.assertEqual(obj.velocity.z, expected.z)

    def test_detectPlatformCollision(self):



    def test_updateWorld(self):
        physics = Physics()
        location = PhysicsVector(5, 0, 5)
        velocity = PhysicsVector(0, 0, 0)
        player = Player(location, velocity)
        world = World(5)
        dt = 3
