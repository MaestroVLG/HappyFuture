import unittest
from runner import Runner
from tournament import Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        runner = Runner("Kirill")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        runner = Runner("Kirill")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        runner1 = Runner("Kirill")
        runner2 = Runner("Anton")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            print(value)

    def test_run_1(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        tournament = Tournament(90, [self.runner1, self.runner3])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(list(self.all_results.values())[-1][-1] == "Ник")

    def test_run_2(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        tournament = Tournament(90, [self.runner2, self.runner3])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(list(self.all_results.values())[-1][-1] == "Ник")

    def test_run_3(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(list(self.all_results.values())[-1][-1] == "Ник")

    # Дополнительный тест
    def test_correct_order(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        finishers = tournament.start()
        for i in range(1, len(finishers)):
            self.assertTrue(finishers[i].speed >= finishers[i - 1].speed)

if __name__ == "__main__":
    unittest.main()

