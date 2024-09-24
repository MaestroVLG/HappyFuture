import logging
from test_code import Runner

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

class RunnerTest:

    def test_walk(self):
        try:
            runner = Runner('Kirill', -10)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(10, 5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
