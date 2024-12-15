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
        print(f'Общий список лидеров')
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    def test_run1(self):
        tour1 = r.Tournament(90, self.runner1, self.runner3)
        res = tour1.start()
        self.all_results.update(res)
        print(f'результаты tour1')
        for key, value in res.items():
            print(f'{key}: {value}')
        self.assertTrue(self.all_results[2], self.runner3.name)

    def test_run2(self):
        tour2 = r.Tournament(90, self.runner2, self.runner3)
        res = tour2.start()
        self.all_results.update(res)
        print(f'результаты tour2')
        for key, value in res.items():
            print(f'{key}: {value}')
        self.assertTrue(self.all_results[2], self.runner3.name)

    def test_run3(self):
        tour3 = r.Tournament(90, self.runner1, self.runner2, self.runner3)
        res = tour3.start()
        self.all_results.update(res)
        print(f'результаты tour3')
        for key, value in res.items():
            print(f'{key}: {value}')
        self.assertTrue(self.all_results[3] == self.runner3.name)

if __name__ == "__main__":
    unittest.main()