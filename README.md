# Snake
Snake game

## General info
This project is a simple Snake game using Tkinter library 

## Technologies
* Python 3.10
* PyCharm 2022.1
* Tkinter library

## Startup
To run this project, run Snake.py

## Info
W tym kodzie nie jest łatwo dostrzec naruszeń zasad SOLID, ponieważ jest to dość prosta implementacja gry. Jednakże, można by argumentować, że zasada pojedynczej odpowiedzialności nie jest całkowicie przestrzegana, ponieważ klasa Game ma zarówno metody do obsługi zdarzeń (handle_events()), jak i metody do aktualizacji i rysowania ekranu (update() i draw()).

Można by rozważyć wydzielenie odpowiedzialności dla tych różnych funkcjonalności do osobnych klas, takich jak InputHandler, ScreenUpdater i GameLogic. To zwiększyłoby separację kodu i ułatwiło testowanie poszczególnych komponentów.

Jednakże, w przypadku tak prostego programu jak ten, taka modyfikacja może być uważana za over-engineering. W każdym razie, SOLID jest zestawem wytycznych, a nie sztywnych zasad, więc w niektórych przypadkach można mieć na uwadze ich zasady, ale i tak zastosować własne osądy w kwestii implementacji.
