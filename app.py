""" Программа для автоматического простотра Ютуб. Главный модуль."""

import pyautogui # основной модуль
import time

# screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# print(screenWidth, screenHeight)
# currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
# print(currentMouseX, currentMouseY)
# pyautogui.moveTo(1000, 150) # Move the mouse to XY coordinates.
# pyautogui.click('images/img_02.png')

sleep_time = 1
iterations = 1
step = 0





def searchDrag(img):
    """ Ищет изображение и подводитк нему курсор. """
    speedMove = 0.5

    # confidence=0.9 - погрешность поиска
    img_location = pyautogui.locateOnScreen(img, confidence=0.9) 
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



def pause():
    print('спим 0.75 сек')
    time.sleep(0.75)


def step_m100():
    global iterations    
    print('############################# Итерация: ' + str(iterations))

    print('\nШаг m100: старт')
    print('Поис адресной строки')
    if searchDrag('images/img_14.png'):
        print('Шаг m100: адресная строка найден')
    else:
        print('Шаг m100: не найден адресная строка')
        pyautogui.move(10, 10, 1)
        step_m100() # повторный вызав step_m100
        return
    pyautogui.move(300, 0, 1) # смешаем курсор вправо
    pyautogui.click(button='right')
    print('Шаг m100: ок')
    step_m101()


def step_m101():
    print('\nШаг m101: старт')
    print('Поис адресной строки и Вставка')
    if searchDrag('images/img_15.png'):
        print('Шаг m101: вставить найден')
    else:
        print('Шаг m101: не найден вставить')
        pyautogui.move(10, 10, 1)
        step_m100() # повторный вызав step_m100
        return
    pyautogui.click()    
    pyautogui.press('enter')
    print('Шаг m101: ок')
    pause()
    step_m102()


def step_m102():
    # step = 0
    print('\nШаг m102: старт')
    print('принять куки')
    if searchDrag('images/img_16.png'):
        print('Шаг m102: вставить Принять куки')
        global step
        step = 0
    else:
        # global step
        step = step + 1
        print('Шаг m102: не найден Принять куки, step: ' + str(step))
        if step == 50:
            print('Перезапуск цикла')
            # step_m100()
            global iterations
            iterations = iterations - 1
            step_12()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_m102() # повторный вызав step_m102
            return
    pyautogui.click()    
    # pyautogui.press('enter')
    print('Шаг m102: ок')
    pause()
    step_m103()


def step_m103():
    print('\nШаг m103: старт')
    print('расширить окно')
    if searchDrag('images/img_17.png'):
        print('Шаг m103: ..')
    else:
        print('Шаг m103: ..')
        pyautogui.move(10, 10, 1)
        step_m103() # повторный вызав step_m103
        return
    # pyautogui.click()    
    # pyautogui.press('enter')
    pyautogui.move(26, 0, 1)
    pyautogui.drag(100, 0, 1, button='left')
    print('Шаг m103: ок')
    pause()
    step_01()


# def step_m104():
#     print('\nШаг m104: старт')
#     print('расширить окно')
#     if searchDrag('images/img_18.png'):
#         print('Шаг m104: ..')
#     else:
#         print('Шаг m104: ..')
#         pyautogui.move(10, 10, 1)
#         step_m103() # повторный вызав step_m104
#         return
#     # pyautogui.click()    
#     # pyautogui.press('enter')
#     pyautogui.move(26, 0, 1)
#     pyautogui.drag(100, 0, 1, button='left')
#     print('Шаг m104: ок')
#     pause()



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
    elif searchDrag('images/img_18.png'):
        print('Шаг 1: логотип найден')
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
    pyautogui.scroll(-300)
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
        # step_05() # повторный вызао 2-г шага
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
    elif searchDrag('images/img_18.png'):
        print('Шаг 1: логотип найден')
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
    pyautogui.scroll(-300)
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
    step_10()


def step_10():
    print('\nШаг 10: старт')
    print('Едем на шапку(2) и прыгаем вправо')
    if searchDrag('images/img_05.png'):
        print('Шаг 10: логотип найден')
    else:
        print('Шаг 10: не найден логотип')
        pyautogui.move(10, 10, 1)
        step_10() # повторный вызав 10-г шага
        return
    pyautogui.move(100, 0, 1) # смешаем курсор вправо
    pyautogui.click()
    pyautogui.move(10, 300, 1) # смешаем курсор вниз
    print('Шаг 10: ок')
    step_11()


def step_11():
    print('\nШаг 11: старт')
    global sleep_time
    print('сон... ' + str(sleep_time))    
    time.sleep(sleep_time)
    print('Шаг 11: ок')
    step_12()


def step_12():
    print('\nШаг 12: старт')
    print('Ищем меню Тора и жмём')
    if searchDrag('images/img_17.png'):
        print('Шаг 12: 144 найден')
    else:
        print('Шаг 12: не найдена 144')
        pyautogui.move(5, 5, 1)
        pyautogui.move(-5, -5, 1)
        step_12() # повторный вызао 12-г шага
        return
    pyautogui.click()
    pause()
    print('Шаг 12: ок')
    step_13()


def step_13():
    print('\nШаг 13: старт')
    print('Ищем "Новая личность" и жмём')
    if searchDrag('images/img_22.png'):
        print('Шаг 13: "Новая личность" найден')
    else:
        print('Шаг 13: не найдена "Новая личность"')
        pyautogui.move(1, 1, 1)
        pyautogui.move(-1, -1, 1)
        step_12() # повторный вызао 13-г шага
        return
    pyautogui.click()
    print('Шаг 13: ок')
    pause()
    pause()
    pause()
    pause()
    pause()
    global iterations
    iterations = iterations + 1
    step_m100()

# def step_11():
#     print('\nШаг 11: старт')
#     print('Распознавание конца ролика')
#     if searchDrag('images/img_19.png'):
#         print('Шаг 11: конца ролика найден')
#     elif searchDrag('images/img_20.png'):
#         print('Шаг 11: конца ролика найден')
#     elif searchDrag('images/img_21.png'):
#         print('Шаг 11: "конца ролика" найден')
#     else:
#         print('Шаг 11: "конца ролика" не найдена')
#         pyautogui.move(5, 0, 0.25)
#         pyautogui.move(-5, 0, 0.25)
#         step_11() # повторный вызао 11-г шага
#         return
#     print('Шаг 11: ок')
#     pause()


def start():
    print('\nПрограмма автоматического простотра РуТуб v0.1')
    global sleep_time
    sleep_time = int(input('Сколько секунд ждать: '))
    step_m100()
    # step_11()
    print('\nЗавершение работы программы')


start()



