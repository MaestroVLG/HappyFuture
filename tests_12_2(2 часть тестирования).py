class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            max_distance = 0
            fastest_runner = None
            for participant in self.participants:
                participant.run()
                if participant.distance > max_distance:
                    max_distance = participant.distance
                    fastest_runner = participant

            if fastest_runner:
                finishers[place] = fastest_runner
                place += 1
                self.participants.remove(fastest_runner)

        return finishers


import unittest
from runner import Runner
from tournament import Tournament


class TournamentTest(unittest.TestCase):
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
        tournament = Tournament(90, [self.runner1, self.runner3])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(list(self.all_results.values())[-1][-1] == "Ник")

    def test_run_2(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(list(self.all_results.values())[-1][-1] == "Ник")

    def test_run_3(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        self.all_results[len(self.all_results) + 1] = tournament.start()
        self.assertTrue(list(self.all_results.values())[-1][-1] == "Ник")

    # Дополнительный тест
    def test_correct_order(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        finishers = tournament.start()
        for i in range(1, len(finishers)):
            self.assertTrue(finishers[i].speed >= finishers[i - 1].speed)

if __name__ == "__main__":
    unittest.main()
