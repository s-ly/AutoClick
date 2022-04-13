""" Программа для автоматического простотра Ютуб. Главный модуль."""

import pyautogui # основной модуль
import time


sleep_time = 1
iterations = 1
step = 0
step_sum = 25 # попытки


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
        # print('No found: ' + img)
        log('No found: ' + img)
        return False


def global_reset():
    """Глобальная перезагрузка цикла"""
    global step
    # global step_sum
    global iterations
    log('Глобальный перезапуск цикла, сон 15 сек.')
    time.sleep(15)
    step = 0
    iterations = iterations - 1
    step_12()


def log(mess):
    global iterations
    print('Цикл: ' + str(iterations) + ' - ' + mess)


###################################################################################################
# Шаги
###################################################################################################
def step_m100():
    global step
    global step_sum

    log('Шаг m100: старт')
    log('Поис адресной строки')
    if searchDrag('images/img_14.png'):
        log('Шаг m100: адресная строка найден')
    else:
        step = step + 1
        log('Шаг m100: не найден адресная строка' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_m100() # повторный вызав step_m100
            return
    pyautogui.move(300, 0, 1) # смешаем курсор вправо
    pyautogui.click(button='right')
    log('Шаг m100: ок\n')
    step_m101()


def step_m101():
    global step
    global step_sum

    log('Шаг m101: старт')
    log('Поис адресной строки и Вставка')
    if searchDrag('images/img_15.png'):
        log('Шаг m101: вставить найден')
    else:
        step = step + 1
        log('Шаг m101: не найден вставить' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_m100() # повторный вызав step_m100
            return
    pyautogui.click()    
    pyautogui.press('enter')
    log('Шаг m101: ок\n')
    time.sleep(0.75)
    step_m102()


def step_m102():
    log('Шаг m102: старт')
    log('принять куки')
    global step
    global step_sum

    if searchDrag('images/img_16.png'):
        log('Шаг m102: НАЙДЕН Принять куки')
    else:
        step = step + 1
        log('Шаг m102: не найден Принять куки, step: ' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(5, 5, 1)
            step_m102() # повторный вызав step_m102
            return
    pyautogui.click()    
    log('Шаг m102: ок\n')
    time.sleep(0.75)
    step_m103()


def step_m103():
    global step
    global step_sum

    log('Шаг m103: старт')
    log('расширить окно')
    if searchDrag('images/img_17.png'):
        log('Шаг m103: ..')
    else:
        step = step + 1
        log('Шаг m103: ..' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_m103() # повторный вызав step_m103
            return
    # pyautogui.click()    
    # pyautogui.press('enter')
    pyautogui.move(26, 0, 1)
    pyautogui.drag(100, 0, 1, button='left')
    log('Шаг m103: ок\n')
    time.sleep(0.75)
    step_01()


def step_01():
    global step
    global step_sum

    log('Шаг 1: старт')
    log('Едем на шапку и прыгаем вниз')
    if searchDrag('images/img_05.png'):
        log('Шаг 1: логотип найден')
    else:
        step = step + 1
        log('Шаг 1: не найден логотип' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_01() # повторный вызав 1-г шага
            return
    pyautogui.move(10, 300, 1) # смешаем курсор вниз
    log('Шаг 1: ок\n')
    step_02()


def step_02():
    global step
    global step_sum

    log('Шаг 2: старт')
    log('Ищем шестерёнку и жмём')
    if searchDrag('images/img_04.png'):
        log('Шаг 2: шестерёнка найден')
    elif searchDrag('images/img_18.png'):
        log('Шаг 1: логотип найден')
    else:
        step = step + 1
        log('Шаг 2: не найдена шестерёнка' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_02() # повторный вызао 2-г шага
            return
    pyautogui.click()
    log('Шаг 2: ок\n')
    time.sleep(0.75)
    step_03()


def step_03():
    global step
    global step_sum
    
    log('Шаг 3: старт')
    log('Ищем скорость и жмём')
    if searchDrag('images/img_08.png'):
        log('Шаг 3: скорость найден')
    else:
        step = step + 1
        log('Шаг 3: не найдена скорость' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            log('Шаг 3: повторный вызов шага 2')
            step_02() # повторный вызао 2-г шага
            return
    pyautogui.click()
    log('Шаг 3: ок\n')
    time.sleep(0.75)
    step_04()


def step_04():
    global step
    global step_sum

    log('Шаг 4: старт')
    log('Ищем 0.25x потом скролим')
    if searchDrag('images/img_12.png'):
        log('Шаг 4: 0.25x найден')
    else:
        log('Шаг 4: не найдена 0.25x' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            log('Шаг 4: повторный вызов шага 2')
            step_02() # повторный вызао 2-г шага
            return
    pyautogui.scroll(-300)
    log('Шаг 4: ок\n')
    time.sleep(0.75)
    step_05()


def step_05():
    global step
    global step_sum
    global iterations

    log('Шаг 5: старт')
    log('Ищем 2x потом нажимаем')
    if searchDrag('images/img_09.png'):
        log('Шаг 5: 2x найден')
    else:
        step = step + 1
        log('Шаг 5: не найдена 2x' + str(step))
        if step > step_sum:
            log('Глобальный перезапуск цикла')
            step = 0
            iterations = iterations - 1
            step_12()
            return
        else:
            pyautogui.move(10, 10, 1)
            log('Шаг 5: повторный вызов шага 2')
            step_02() # повторный вызао 2-г шага
            return
    pyautogui.click()
    log('Шаг 5: ок\n')
    time.sleep(0.75)
    step_06()


def step_06():
    global step
    global step_sum

    log('Шаг 6: старт')
    log('Ищем шестерёнку и отводим к ней')
    if searchDrag('images/img_04.png'):
        log('Шаг 2: шестерёнка найден')
    elif searchDrag('images/img_18.png'):
        log('Шаг 1: логотип найден')
    else:
        log('Шаг 2: не найдена шестерёнка' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_06() # повторный вызао 6-г шага
            return
    log('Шаг 6: ок\n')
    time.sleep(0.75)
    step_07()


def step_07():
    global step
    global step_sum

    log('Шаг 7: старт')
    log('Ищем качество и жмём')
    if searchDrag('images/img_10.png'):
        log('Шаг 7: качество найден')
    else:
        step = step + 1
        log('Шаг 7: не найдена качество' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_06() # повторный вызао 6-г шага
            return
    pyautogui.click()
    log('Шаг 7: ок\n')
    time.sleep(0.75)
    step_08()


def step_08():
    global step
    global step_sum

    log('Шаг 8: старт')
    log('Ищем 1080 и скрол')
    if searchDrag('images/img_13.png'):
        log('Шаг 8: 1080 найден')
    else:
        step = step + 1
        log('Шаг 8: не найдена 1080' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_06() # повторный вызао 6-г шага
            return
    pyautogui.scroll(-300)
    time.sleep(0.75)
    log('Шаг 8: ок\n')
    step_09()


def step_09():
    global step
    global step_sum

    log('Шаг 9: старт')
    log('Ищем 144 и жмём')
    if searchDrag('images/img_11.png'):
        log('Шаг 9: 144 найден')
    else:
        step = step + 1
        log('Шаг 9: не найдена 144' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_06() # повторный вызао 6-г шага
            return
    pyautogui.click()
    time.sleep(0.75)
    log('Шаг 9: ок\n')
    step_10()


def step_10():
    global step
    global step_sum

    log('Шаг 10: старт')
    log('Едем на шапку(2) и прыгаем вправо')
    if searchDrag('images/img_05.png'):
        log('Шаг 10: логотип найден')
    else:
        step = step + 1
        log('Шаг 10: не найден логотип' + str(step))
        if step > step_sum:
            global_reset()
            return
        else:
            pyautogui.move(10, 10, 1)
            step_10() # повторный вызав 10-г шага
            return
    pyautogui.move(100, 0, 1) # смешаем курсор вправо
    pyautogui.click()
    pyautogui.move(10, 300, 1) # смешаем курсор вниз
    log('Шаг 10: ок\n')
    step_11()


def step_11():
    log('Шаг 11: старт')
    global sleep_time
    log('сон... ' + str(sleep_time))    
    i = sleep_time
    while i > 0:
        log(str(i))
        time.sleep(1)
        i = i - 1

    log('Шаг 11: ок\n')
    step_12()


def step_12():
    log('Шаг 12: старт')
    log('Ищем меню Тора и жмём')
    if searchDrag('images/img_17.png'):
        log('Шаг 12: 144 найден')
    else:
        log('Шаг 12: не найдена 144')
        pyautogui.move(5, 5, 1)
        pyautogui.move(-5, -5, 1)
        step_12() # повторный вызао 12-г шага
        return
    pyautogui.click()
    time.sleep(0.75)
    log('Шаг 12: ок\n')
    step_13()


def step_13():
    log('Шаг 13: старт')
    log('Ищем "Новая личность" и жмём')
    if searchDrag('images/img_22.png'):
        log('Шаг 13: "Новая личность" найден')
    else:
        log('Шаг 13: не найдена "Новая личность"')
        pyautogui.move(1, 1, 1)
        pyautogui.move(-1, -1, 1)
        step_12() # повторный вызао 13-г шага
        return
    pyautogui.click()
    log('Шаг 13: ок\n')
    log('Сон между циклами 5 сек (штатный)')
    time.sleep(5)
    global iterations
    iterations = iterations + 1
    step_m100()


def start():
    print('\nПрограмма автоматического простотра РуТуб v0.2')
    global sleep_time
    sleep_time = int(input('Сколько секунд ждать: '))
    step_m100()
    # step_11()
    print('\nЗавершение работы программы\n')


start()



