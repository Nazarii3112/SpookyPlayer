import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from newdesign import Ui_MainWindow  # Импортируем дизайн из newdesign.py

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Назначаем действия кнопкам
        self.homebtn.clicked.connect(self.show_home)
        self.searchbtn.clicked.connect(self.show_search)
        self.playlistsbtn.clicked.connect(self.show_playlists)
        self.likes.clicked.connect(self.show_likes)
        self.playlists.clicked.connect(self.show_playlists2)
        
        # Инициализируем страницы stackedWidget
        self.stackedWidget.setCurrentIndex(1)  # stackedWidget - 1
        self.stackedWidget_2.setCurrentIndex(2)  # stackedWidget_2 - 2
    
    def show_home(self):
        self.stackedWidget.setCurrentIndex(2)  # homebtn - stackedWidget - 2
        if self.mimiplayer.isVisible():  # Проверяем, виден ли mimiplayer
            self.mimiplayer.setVisible(False)  # Скрываем mimiplayer
        else:
            print("все заебись")  # Выводим сообщение, если mimiplayer уже скрыт

    def show_search(self):
        self.stackedWidget.setCurrentIndex(0)  # searchbtn - stackedWidget - 1
        if not self.mimiplayer.isVisible():
            self.mimiplayer.setVisible(True)  # Показываем mimiplayer

    def show_playlists(self):
        self.stackedWidget.setCurrentIndex(3)
        if not self.mimiplayer.isVisible():
            self.mimiplayer.setVisible(True)  # Показываем mimiplayer

    def show_playlists2(self):
        self.stackedWidget_2.setCurrentIndex(1)  # playlistsbtn - stackedWidget - 4
        if not self.mimiplayer.isVisible():
            self.mimiplayer.setVisible(True)  # Показываем mimiplayer
    
    def show_likes(self):
        self.stackedWidget_2.setCurrentIndex(0)  # likes - stackedWidget_2 - 1
        if not self.mimiplayer.isVisible():
            self.mimiplayer.setVisible(True)  # Показываем mimiplayer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
