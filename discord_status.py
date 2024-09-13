from pypresence import Presence
import time

class DiscordPresence:
    def __init__(self, client_id):
        self.client_id = client_id
        self.rpc = Presence(client_id)
        self.rpc.connect()

    def update_status(self, song_title, artist_name, duration, current_time):
        self.rpc.update(
            state=f"Играет: {song_title}",
            details=f"Исполнитель: {artist_name}",
            start=int(time.time()) - current_time,  # Время начала песни
            end=int(time.time()) - current_time + duration,  # Время окончания песни
            large_image='cur',  # Ключ большого изображения (настройте в Discord Developer Portal)
            small_image='tg',  # Ключ маленького изображения (настройте в Discord Developer Portal)
            buttons=[{"label": "Слушать", "url": "https://your_link_here"}]  # Опциональная кнопка
        )

# Пример использования
discord_presence = DiscordPresence(client_id='1248615215738650724')

# Обновляем статус в цикле
while True:
    # Например, получаем текущую песню, ее исполнителя и длительность
    song_title = "Название песни"
    artist_name = "Имя исполнителя"
    duration = 300  # Длительность в секундах
    current_time = 120  # Текущее время воспроизведения в секундах

    discord_presence.update_status(song_title, artist_name, duration, current_time)
    
    time.sleep(15)  # Обновляем статус каждые 15 секунд
