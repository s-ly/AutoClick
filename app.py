""" Программа для автоматического простотра Ютуб. Главный модуль."""

import pyautogui # основной модуль
import time

# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# print(screenWidth, screenHeight)
# currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
# print(currentMouseX, currentMouseY)
# pyautogui.moveTo(1000, 150) # Move the mouse to XY coordinates.
# pyautogui.click('images/img_02.png')







def searchDrag(img):
    """ Ищет изображение и подводитк нему курсор. """
    speedMove = 0.5

    img_location = pyautogui.locateOnScreen(img, confidence=0.9) # confidence=0.9 - погрешность поиска
    if img_location != None:
        # print(img_location)
        img_center = pyautogui.center(img_location)
        # print(img_center)
        pyautogui.moveTo(img_center.x, img_center.y, speedMove)
        return True
    else:        
        print('No found: ' + img)
        # pyautogui.move(10, 10, 1)
        # searchDrag(img)
        return False



    # try:
    #     x, y = pyautogui.locateCenterOnScreen(img, confidence=0.9) # confidence=0.9 - погрешность поиска
    #     print(x ,y)
    # except pyautogui.ImageNotFoundException:
    #     print('no')
    # pyautogui.moveTo(x, y, speedMove) # Перемещает курсор, 3й параметр скорость (меньше быстрее)
    # pyautogui.click()


def pause():
    print('спим 0.75 сек')
    time.sleep(0.75)


def step_01():
    print('\nШаг 1: старт')
    print('Едем на шапку и прыгаем вниз')
    if searchDrag('images/img_05.png'):
        print('Шаг 1: логотип найден')
    else:
        print('Шаг 1: не найден логотип')
        pyautogui.move(10, 10, 1)
        step_01() # повторный вызав 1-г шага
        return
    pyautogui.move(10, 300, 1) # смешаем курсор вниз
    print('Шаг 1: ок')
    step_02()


def step_02():
    print('\nШаг 2: старт')
    print('Ищем шестерёнку и жмём')
    if searchDrag('images/img_04.png'):
        print('Шаг 2: шестерёнка найден')
    else:
        print('Шаг 2: не найдена шестерёнка')
        pyautogui.move(10, 10, 1)
        step_02() # повторный вызао 2-г шага
        return
    pyautogui.click()
    print('Шаг 2: ок')
    pause()
    step_03()


def step_03():
    print('\nШаг 3: старт')
    print('Ищем скорость и жмём')
    if searchDrag('images/img_08.png'):
        print('Шаг 3: скорость найден')
    else:
        print('Шаг 3: не найдена скорость')
        pyautogui.move(10, 10, 1)
        print('Шаг 3: повторный вызов шага 2')
        step_02() # повторный вызао 2-г шага
        return
    pyautogui.click()
    print('Шаг 3: ок')
    pause()
    step_04()


def step_04():
    print('\nШаг 4: старт')
    print('Ищем 0.25x потом скролим')
    if searchDrag('images/img_12.png'):
        print('Шаг 4: 0.25x найден')
    else:
        print('Шаг 4: не найдена 0.25x')
        pyautogui.move(10, 10, 1)
        print('Шаг 4: повторный вызов шага 2')
        step_02() # повторный вызао 2-г шага
        return
    pyautogui.scroll(-200)
    print('Шаг 4: ок')
    pause()
    step_05()


def step_05():
    print('\nШаг 5: старт')
    print('Ищем 2x потом нажимаем')
    if searchDrag('images/img_09.png'):
        print('Шаг 5: 2x найден')
    else:
        print('Шаг 5: не найдена 2x')
        pyautogui.move(10, 10, 1)
        print('Шаг 5: повторный вызов шага 2')
        step_02() # повторный вызао 2-г шага
        return
    pyautogui.click()
    print('Шаг 5: ок')
    pause()
    step_06()


def step_06():
    print('\nШаг 6: старт')
    print('Ищем шестерёнку и отводим к ней')
    if searchDrag('images/img_04.png'):
        print('Шаг 2: шестерёнка найден')
    else:
        print('Шаг 2: не найдена шестерёнка')
        pyautogui.move(10, 10, 1)
        step_06() # повторный вызао 6-г шага
        return
    print('Шаг 6: ок')
    pause()
    step_07()


def step_07():
    print('\nШаг 7: старт')
    print('Ищем качество и жмём')
    if searchDrag('images/img_10.png'):
        print('Шаг 7: качество найден')
    else:
        print('Шаг 7: не найдена качество')
        pyautogui.move(10, 10, 1)
        step_06() # повторный вызао 6-г шага
        return
    pyautogui.click()
    print('Шаг 7: ок')
    pause()
    step_08()


def step_08():
    print('\nШаг 8: старт')
    print('Ищем 1080 и скрол')
    if searchDrag('images/img_13.png'):
        print('Шаг 8: 1080 найден')
    else:
        print('Шаг 8: не найдена 1080')
        pyautogui.move(10, 10, 1)
        step_06() # повторный вызао 6-г шага
        return
    pyautogui.scroll(-200)
    pause()
    print('Шаг 8: ок')
    step_09()


def step_09():
    print('\nШаг 9: старт')
    print('Ищем 144 и жмём')
    if searchDrag('images/img_11.png'):
        print('Шаг 9: 144 найден')
    else:
        print('Шаг 9: не найдена 144')
        pyautogui.move(10, 10, 1)
        step_06() # повторный вызао 6-г шага
        return
    pyautogui.click()
    pause()
    print('Шаг 9: ок')

# print('ищем скорость')
# searchDrag('images/img_08.png')
# print('после скорость 1 sleep 1')
# time.sleep(1)
# pyautogui.click()
# # pyautogui.click()

# searchDrag('images/img_08.png')
# print('sleep 2')
# time.sleep(1)

# pyautogui.scroll(-200)

# print('sleep 3')
# time.sleep(1)
# # searchDrag('images/img_04.png')

# searchDrag('images/img_09.png')
# pyautogui.click()

def start():
    print('\nПрограмма автоматического простотра РуТуб v0.1')
    step_01()
    print('\nЗавершение работы программы')


start()







# img_location = pyautogui.locateOnScreen('images/img_01.png', confidence=0.9) # confidence=0.9 - погрешность поиска
# if img_location != None:
#     print(img_location)
#     img_center = pyautogui.center(img_location)
#     print(img_center)
#     pyautogui.moveTo(img_center.x, img_center.y, 1)
# else:
#     print('No found img')