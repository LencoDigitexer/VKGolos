import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import GUI # Это наш конвертированный файл дизайна
import os
import requests
import json
class ExampleApp(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.Join.clicked.connect(self.Vhod)
        self.request_2.clicked.connect(self.Send_GL)
        lst = os.listdir(path=".")
        for i in range(len(lst)):
            self.list.addItem(lst[i])

    def Vhod(self):
        global login, password, token
        login = self.login.text()
        password = self.password.text()  
        self.login.clear()
        self.password.clear()
        token = requests.get("https://api.vk.com/oauth/token?grant_type=password&client_id=2274003&scope=messages&client_secret=hHbZxrka2uZ6jB1inYsH&username={0}&password={1}".format(login, password))
        token = token.text
        token = json.loads(token)
        token = token["access_token"]
        self.console.addItem("Token: " + token)
    def Send_test(self):
        chat = self.peer_id.text()
        text = "Я это сообщение оправил через свое приложение"
        send = requests.get("https://api.vk.com/method/messages.send?access_token={0}&chat_id={2}&message={1}".format(token, text, chat))
        send = send.text
        send = json.loads(send)
        print(send)
    def Send_GL(self):
        chat = self.peer_id.text()
        s = self.list.currentText()
        url = requests.get("https://api.vk.com/method/docs.getUploadServer?access_token={}&type=audio_message&v=5.63".format(token))
        url = url.text
        url = json.loads(url)
        url = url["response"]["upload_url"]
        symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")
        tr = {ord(a):ord(b) for a, b in zip(*symbols)}
        print (s.translate(tr))
        s_new = s.translate(tr)
        self.console.addItem(s_new)
        file_ = {'file': (s_new, open(s, 'rb'))}
        r = requests.post(url, files=file_)
        a = r.text
        b = json.loads(a)
        print(b)
        c = b["file"]
        r = requests.get('https://api.vk.com/method/docs.save?access_token={0}&file={1}&title=test&tags=test_tags&v=5.92'.format(token, c))
        b = r.text
        datates = json.loads(b)
        print(datates)
        ids = datates["response"]["audio_message"]["id"]
        owner_ids = datates["response"]["audio_message"]["owner_id"]
        print(ids)
        print(owner_ids)
        audio = 'doc{0}_{1}'.format(owner_ids, ids)
        print(audio)
        send = requests.get("https://api.vk.com/method/messages.send?access_token={0}&chat_id={1}&attachment={2}".format(token, chat, audio))
        send = send.text
        send = json.loads(send)
        print(send)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()