from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'Имя текущего пользователя -  {self.nickname}'

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Фильм: {self.title}'

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return
        print('Неправильный логин или пароль')

    def register(self,  nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже зарегистрирован')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Пользователь {self.current_user.nickname} успешно зарегистрирован')
        # print(f'Возраст пользователя {self.current_user.age} лет')

    def log_out(self):
        self.current_user = None
        return self.current_user

    def add(self, *args):
        global video
        for video in args:
            if any(vid.title == video.title for vid in self.videos):
                print(f'Фильм "{video.title}" уже есть в базе')
                continue
            else:
                self.videos.append(video)
                print(f'Фильм "{video.title}" добавлен в фильмотеку')

    def get_videos(self, word_search):
        word_search_lower = word_search.lower()
        get_video = list(video.title for video in self.videos if word_search_lower in video.title.lower())
        return f'По запросу "{word_search}" найдены фильмы - {get_video}'

    def watch_video(self, title):
        if not any(vid.title == title for vid in self.videos):
                print(f'Фильма "{title}" нет в фильмотеке')

        elif self.current_user == None:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18:
            print(f'{self.current_user.nickname}. Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for i in range (1, video.duration + 1):
                print(i, end=' ')
                sleep(1)
            print('Конец видео')

# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)
v4 = Video('Для чего девушкам парень программист?', 10)
# Добавление видео
ur.add(v1, v2, v3, v4)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

