# **Игра "Инопланетное вторжение"**
**This game for my sons Ilya and David**

**created by** [©eazakiev](https://github.com/eazakiev)
***
![image](images/alien_ships.png)
## Описание
Каждый игрок управляет кораблем, который находится в середине нижнего края экрана. 
Игрок перемещает корабль вправо и влево клавишами управления курсором. Клавиша "пробел" 
используется для стрельбы. В начале игры флот пришельцев находится в верхней части
экрана и постепенно опускается вниз, также смещаясь в сторону. Игрок выстрелами уничтожает пришельцев. 
Если ему удается сбить всех пришельцев, появляется новый флот, который движется быстрее предыдущего.
Если пришелец сталкивается с кораблем игрока или доходит до нижнего края экрана,
игрок теряет корабль. Если игрок теряет все три корабля, игра заканчивается.
***

## Установка
Создайте и активируйте виртуальное окружение.
Установите зависимости в виртуальном окружении env/ :
```
pip install -r requirements.txt
```
***

## Запуск
Находясь в папке проекта, запустите файл alien_invasion.py

```commandline
python alien_invasion.py
```