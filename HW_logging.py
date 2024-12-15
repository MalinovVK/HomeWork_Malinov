from HumanMoveTest import rt_with_exceptions as r
import unittest
import logging

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            logging.info('test_walk выполнен успешно')
            obj = r.Runner('Vlad', -10)
        except:
            obj.walk()
            self.assertEqual(obj.distance, 50)

    def test_run(self):
        try:
            logging.info('test_run выполнен успешно')
            obj = r.Runner(245)
        except:
            logging.warning('Неверный тип данных для объекта Runner')
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

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='UTF-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")
    logging.warning('Неверная скорость для Runner')