# VKGolos - отправка голосовых из mp3
    $ git clone https://github.com/LencoDigitexer/VKGolos.git
    $ cd VKGolos
    
В эту папку закидываем mp3 файлы (например, пак голосовых ).
> Запускаем:

    $ python3 VKGOLOS.py
    
<p align="center">
  <img src="src/screen.png" alt="Sublime's custom image"/>
</p>

Вводим логин и пароль - получаем токен

<p align="center">
  <img src="src/logpass.png" alt="Sublime's custom image"/>
</p>

Выбираем музыку из списка (он генерируется перед запуском скрипта)

<p align="center">
  <img src="src/choose_music.png" alt="Sublime's custom image"/>
</p>

> Profit!

<p align="center">
  <img src="src/profit.png" alt="Sublime's custom image"/>
</p>

# Как узнать id беседы

Заходим в беседу

<p align="center">
  <img src="src/Screenshot_1.png" alt="Sublime's custom image"/>
</p>

Смотрим на строку адреса в браузере (в Яндекс Браузере на нее нужно нажать, чтобы увидеть полный адрес)

<p align="center">
  <img src="src/Screenshot_2.png" alt="Sublime's custom image"/>
</p>

Видим адрес 
>    vk.com/im?sel=c8
    
После <b>sel=c</b> идет число - это число является id беседы.
Вставляем в соответствующее поле программы


# Как узнать id пользователя
Инструкция точно такая же, как и для беседы.
Но адрес уже другой
>   vk.com/im?sel=510166866

<p align="center">
  <img src="src/Screenshot_3.png" alt="Sublime's custom image"/>
</p>

После <b>sel=</b> идет число - это число является id человека вконтакте.
Вставляем в соответствующее поле программы
