import requests

class MusicSearch:
    def __init__(self):
        self.genius_api_token = "lwlriXAaqs2fFr67n5bPSrxkfAnPkDtfGWEdGSCHJBjUaTETmI_-Cb_FSsJdl4Gk"

    def search_music_by_lyrics(self, lyrics):
        headers = {
            "Authorization": f"Bearer {self.genius_api_token}"
        }
        search_url = "https://api.genius.com/search"
        params = {"q": lyrics}
        
        response = requests.get(search_url, headers=headers, params=params)
        if response.status_code == 200:
            json_data = response.json()
            hits = json_data['response']['hits']
            results = []
            for hit in hits:
                title = hit['result']['title']
                artist = hit['result']['primary_artist']['name']
                results.append(f"{title} - {artist}")
            return results
        else:
            print("Ошибка при поиске:", response.status_code)
            return []

    def search_in_database(self, words, cursor):
        results = []
        # Проверяем все слова одно за другим, пока не найдем совпадение
        for word in words:
            cursor.execute('SELECT title, artist, online_url FROM tracks WHERE title LIKE ?', (f'%{word}%',))
            db_results = cursor.fetchall()
            if db_results:  # Если есть результаты, добавляем их
                results.extend(db_results)
        return results  # Возвращаем все найденные результаты
