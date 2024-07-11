import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self._hash_password(password)
        self.age = age

    def _hash_password(self, password):
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = int(hashlib.sha256(password.encode()).hexdigest(), 16)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"User {nickname} logged in successfully.")
                return
        print("Invalid login or password.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"User {nickname} registered and logged in successfully.")

    def log_out(self):
        if self.current_user:
            print(f"User {self.current_user.nickname} logged out.")
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Video {video.title} added successfully.")
            else:
                print(f"Video {video.title} already exists.")

    def get_videos(self, search_word):
        search_word_lower = search_word.lower()
        found_videos = [video.title for video in self.videos if search_word_lower in video.title.lower()]
        return found_videos

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Watching video: {video.title}")
                for second in range(video.time_now, video.duration):
                    print(f"At second {second}")
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")
                return

        print("Video not found.")

# # Пример использования
# urtube = UrTube()
#
# # Регистрация и логин пользователя
# urtube.register("Alice", "password123", 25)
# urtube.log_in("Alice", "password123")
#
# # Добавление видео
# video1 = Video("Funny Cats", 10)
# video2 = Video("Scary Movie", 120, adult_mode=True)
# urtube.add(video1, video2)
#
# # Получение списка видео по ключевому слову
# print(urtube.get_videos("cats"))
#
# # Просмотр видео
# urtube.watch_video("Funny Cats")
# urtube.watch_video("Scary Movie")
#
# # Логаут пользователя
# urtube.log_out()