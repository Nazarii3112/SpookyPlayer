# translations.py
from PyQt5.QtWidgets import QAction, QMenu

class Translator:
    def __init__(self):
        self.translations = self.create_translations()
        self.current_language = 'Русский'

    def create_translations(self):
        translations = {
            'Русский': {
                'playlistlabel': '• Плей листы',
                'searchlabel': '• Поиск',
                'addPlaylistButton': 'Создать',
                'addTrackPlaylistButton': 'Добавить в плейлист',
                'addTrackPlaylistButton_2': 'Добавить в избранное (SOON)',
                'file': 'Файл',
                'view': 'Вид',
                'changelanguage': 'Сменить язык',
                'help': 'Помощь',
                'delete_from_playlist': 'Удалить с плейлиста',
                'create_playlist_prompt': 'Введите название плейлиста:',
                'create_playlist_title': 'Создать плейлист',
                'playlist_load_error': 'Не удалось загрузить плейлисты',
                'track_load_error': 'Не удалось загрузить треки',
            },
            'Українська': {
                'playlistlabel': '• Плейлисти',
                'searchlabel': '• Пошук',
                'addPlaylistButton': 'Створити',
                'addTrackPlaylistButton': 'Додати в плейлист',
                'addTrackPlaylistButton_2': 'Додати в обране (SOON)',
                'file': 'Файл',
                'view': 'Вид',
                'changelanguage': 'Змінити мову',
                'help': 'Допомога',
                'delete_from_playlist': 'Видалити з плейлиста',
                'create_playlist_prompt': 'Введіть назву плейлиста:',
                'create_playlist_title': 'Створити плейлист',
                'playlist_load_error': 'Не вдалося завантажити плейлисти',
                'track_load_error': 'Не вдалося завантажити треки',
            },
            'English': {
                'playlistlabel': '• Playlists',
                'searchlabel': '• Search',
                'addPlaylistButton': 'Create',
                'addTrackPlaylistButton': 'Add to playlist',
                'addTrackPlaylistButton_2': 'Add to favorites (SOON)',
                'file': 'File',
                'view': 'View',
                'changelanguage': 'Change language',
                'help': 'Help',
                'delete_from_playlist': 'Remove from playlist',
                'create_playlist_prompt': 'Enter playlist name:',
                'create_playlist_title': 'Create Playlist',
                'playlist_load_error': 'Failed to load playlists',
                'track_load_error': 'Failed to load tracks',
            }
        }
        return translations

    def update_language(self, language, ui):
        self.current_language = language
        t = self.translations[language]

        ui.playlistlabel.setText(t['playlistlabel'])
        ui.searchlabel.setText(t['searchlabel'])
        ui.addPlaylistButton.setText(t['addPlaylistButton'])
        ui.addTrackPlaylistButton.setText(t['addTrackPlaylistButton'])
        ui.addTrackPlaylistButton_2.setText(t['addTrackPlaylistButton_2'])

        menubar = ui.menubar
        menubar.clear()

        file_menu = menubar.addMenu(t['file'])
        view_menu = menubar.addMenu(t['view'])
        help_menu = menubar.addMenu(t['help'])

        changelanguage_menu = QMenu(t['changelanguage'], ui)
        view_menu.addMenu(changelanguage_menu)

        self.add_language_action(changelanguage_menu, 'Русский', ui)
        self.add_language_action(changelanguage_menu, 'Українська', ui)
        self.add_language_action(changelanguage_menu, 'English', ui)

    def add_language_action(self, menu, language, ui):
        action = QAction(language, ui)
        action.triggered.connect(lambda: self.update_language(language, ui))
        menu.addAction(action)
