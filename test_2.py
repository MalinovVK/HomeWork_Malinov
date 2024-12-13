from HumanMoveTest import runner_and_tournament as r
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('словарь создан')
        cls.all_results = {}

    def setUp(self):
        self.runner1 = r.Runner('Усэйн', 10)
        self.runner2 = r.Runner('Андрей', 9)
        self.runner3 = r.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    def test_run1(self):
        tour1 = r.Tournament(90, self.runner1, self.runner3)
        results1 = tour1.start()
        self.all_results.update(results1)
        self.assertTrue(self.runner1.name, self.runner3.name)

    def test_run2(self):
        tour2 = r.Tournament(90, self.runner2, self.runner3)
        results2 = tour2.start()
        self.all_results.update(results2)
        self.assertTrue(self.runner2.name, self.runner3.name)

    def test_run3(self):
        tour3 = r.Tournament(90, self.runner1, self.runner2, self.runner3)
        results3 = tour3.start()
        self.all_results.update(results3)
        self.assertTrue(self.runner2.name, self.runner3.name)
# max(self.all_results, key=lambda k: self.all_results[k])