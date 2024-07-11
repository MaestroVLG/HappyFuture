import datetime
import time
class Users:
    def __init__(self, nickname: str, password: int, age: str):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    def __init__(self, title:str, duration:int, adult_mode:bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def play(self):
        if self.adult_mode and self.time_now == 0:
            print('Это видео доступно только для взрослых. Подтвердите свой возраст.')
            return

        self.time_now += 1
        print(f'Текущее время воиспроизведения: {self.time_now} секунд')

    def stop(self):
        print(f'Воиспроизведение остановлено на {self.time_now} секунде')
        self.time_now = 0

    def rewind(self, seconds:int):
        if seconds > self.time_now:
            print(f'Нельзя перемотать назад чем текущая позиция воиспроизведения.')
            return

        self.time_now -= seconds
        print(f'Перемотка назад на {seconds} секунд. Текущее время воиспроизведения: {self.time_now} секунд')

    def forward(self, seconds:int):
        if seconds > self.duration - self.time_now:
            print('Нельзя перемотать дальше, чем продолжительность видео')
            return

        self.time_now += seconds
        print(f'Перемотка вперёд на {seconds} секунд. Текущее время воиспроизведения: {self.time_now} секунд')


class UrTube:
    def __init__(self):
      self.users = []
      self.videos = []
      self.current_users = None

    def log_in(self, login:str, password:str):
        hashed_password = int(password)
        for user in self.users:
            if user.nickname == login and user.password == hashed_password:
                self.current_user = user
                print("Вход выполенен успешно.")
                return

        print("Неверный логин или пароль.")

    def register(self, nickname:str, password:str, age:int):
        hashed_password = int(password)
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return

        new_user = User(nickname, hashed_password, age)
        self.users.append(nickname, password)

    def log_out(self):
        self.current_user = None
        print('Вы выщли из аккаунта.')

    def add(self, *videos: Video):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
        else:
            print(f'Видео {video.title} уже существует')

    def get_videos(self, poisk_zapros:str):
        poisk_zapros = poisk_zapros.lower()
        matching_videos = []
        for vido in self.videos:
            if poisk_zapros in video.title.lower():
                matching_videos.append(vido.title)


            return matching_videos


    def watch_video(self, video_title: str):
        if not self.current_user:
            print('Войдите в аккаунт чтобы посмотреть видео')
            return


        for video in self.videos:
            if video_title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, просмотр запрещён!')
                    return

                while video.time_now < video.duration:
                    video.play()
                    time.sleep(1)


                print('Конец видео')
                video.stop()
                return

        print('Видео не найдено')

    def create_user(self):
        nickname = input('Ввкдите никнейм: ')
        password = int(input('Введите пароль: '))
        age = int(input('ведите возраст: '))
        return User (nickname, password, age)

    def create_video(self):
        title = input('Введите назване видео: ')
        duration = int(input('Введите продолжительность видео (в секундах): '))
        adult_mode = bool(input('Видео содержит контент который предназначен для взрослых? (ДА/НЕТ): ').lower() == "да")
        return  Video(title, duration, adult_mode)













