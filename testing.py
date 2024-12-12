import runner as r
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        obj = r.Runner('Vlad')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)
    def test_run(self):
        obj = r.Runner('Vika')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)
    def test_challenge(self):
        obj1 = r.Runner('Ant')
        obj2 = r.Runner('Leonid')
        for i in range(10):
            obj1.run()
            obj2.walk()
        self.assertNotEqual(obj1.distance, obj2.distance)