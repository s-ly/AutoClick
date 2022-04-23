import pyautogui # основной модуль
import time

iterations = 1
time_sleep = 0
####################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
# Шаги
####################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
def step_adres():
    log('Поис адресной строки')
    if searchDrag('images/img_14.png') == False:
        return False
    pyautogui.move(300, 0, 1) # смешаем курсор вправо
    pyautogui.click(button='right')
    return True


def step_paste():
    log('Вставить')
    if searchDrag('images/img_15.png') == False:
        return False
    pyautogui.click()    
    pyautogui.press('enter')
    return True


def step_cuc():
    log('принять куки')
    if searchDrag('images/img_16.png') == False:
        return False
    pyautogui.click()
    return True


def step_winsiz():
    log('расширить окно')
    if searchDrag('images/img_17.png') == False:
        return False
    pyautogui.move(26, 0, 1)
    pyautogui.drag(120, 0, 1, button='left')
    return True


def step_logo():
    log('Едем на шапку и прыгаем вниз')
    if searchDrag('images/img_05.png') == False:
        return False
    pyautogui.move(10, 300, 1) # смешаем курсор вниз
    return True


def step_ses():
    log('Ищем шестерёнку и жмём')
    if searchDrag('images/img_04.png')  == False:        
        if searchDrag('images/img_18.png') == False:
            return False
    pyautogui.click()
    return True


def step_speed():
    log('Ищем скорость и жмём')
    if searchDrag('images/img_08.png') == False:
        return False
    pyautogui.click()
    return True


def step_sc_speed():
    log('Ищем 0.25x потом скролим')
    if searchDrag('images/img_12.png') == False:
        return False
    pyautogui.scroll(-300)
    return True


def step_two_speed():
    log('Ищем 2x потом нажимаем')
    if searchDrag('images/img_09.png') == False:
        return False
    pyautogui.click()
    return True


def step_sis_m():
    log('Ищем шестерёнку и отводим к ней')
    if searchDrag('images/img_04.png')  == False:        
        if searchDrag('images/img_18.png') == False:
            return False
    return True


def step_kat():
    log('Ищем качество и жмём')
    if searchDrag('images/img_10.png') == False:
        return False
    pyautogui.click()
    return True


def step_1080():
    log('Ищем 1080 и скрол')
    if searchDrag('images/img_13.png') == False:
        return False
    pyautogui.scroll(-300)
    return True


def step_144():
    log('Ищем 144 и жмём')
    if searchDrag('images/img_11.png') == False:
        return False
    pyautogui.click()
    return True


def step_logo2():
    log('Едем на шапку(2) и прыгаем вправо')
    if searchDrag('images/img_05.png') == False:
        return False
    pyautogui.move(100, 0, 1) # смешаем курсор вправо
    pyautogui.click()
    pyautogui.move(10, 300, 1) # смешаем курсор вниз
    return True


def step_sleep_show():
    log('просмотр')
    global time_sleep
    log('сон... ' + str(time_sleep))    
    i = time_sleep
    while i > 0:
        log(str(i))
        time.sleep(1)
        i = i - 1

    log('Шаг 11: ок\n')
    return True


def step_tor_menu():
    log('Ищем меню Тора и жмём')
    if searchDrag('images/img_17.png') == False:
        return False
    pyautogui.click()
    return True


def step_new():
    log('Ищем "Новая личность" и жмём')
    if searchDrag('images/img_22.png') == False:
        return False
    pyautogui.click()
    return True

####################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
def log(mess):
    global iterations
    print('Цикл: ' + str(iterations) + ' - ' + mess)


def searchDrag(img):
    """ Ищет изображение и подводитк нему курсор. """
    speedMove = 0.5
    # confidence=0.9 - погрешность поиска
    img_location = pyautogui.locateOnScreen(img, confidence=0.9) 
    if img_location != None:
        img_center = pyautogui.center(img_location)
        pyautogui.moveTo(img_center.x, img_center.y, speedMove)
        return True
    else:        
        log('No found: ' + img)
        return False


def step(f):
    """Отработка попыток шагов"""
    popitki = 35
    i = True
    while i:
        func_run = f()
        if func_run:
            log('УДАЧНЫЙ шаг')
            time.sleep(0.75)
            return True
        else:
            popitki = popitki - 1
            if popitki != 0:
                log('попытка шага: ' + str(popitki))      
                pyautogui.move(10, 10, 1)
                pyautogui.move(-10, -10, 1)          
            else:
                log('кончилиси попытки шага')
                return False


def main_cicle():
    """главный цикл"""
    global iterations
    global time_sleep
    print('\nПрограмма автоматического простотра РуТуб v0.3')
    time_sleep = int(input('Сколько секунд ждать: '))
    
    while True:    
        if step(step_tor_menu) != True: continue
        if step(step_new) != True: continue

        if step(step_adres) != True: continue
        if step(step_paste) != True: continue
        if step(step_cuc) != True: continue
        if step(step_winsiz) != True: continue
        if step(step_logo) != True: continue
        if step(step_ses) != True: continue
        if step(step_speed) != True: continue
        if step(step_sc_speed) != True: continue
        if step(step_two_speed) != True: continue
        if step(step_sis_m) != True: continue
        if step(step_kat) != True: continue
        if step(step_1080) != True: continue
        if step(step_144) != True: continue
        if step(step_logo2) != True: continue
        if step(step_sleep_show) != True: continue
        # if step(step_tor_menu) != True: continue
        # if step(step_new) != True: continue

        log('Глобальный перезапуск цикла, сон 15 сек.')
        time.sleep(15)
        iterations = iterations + 1
###################################################################################################


main_cicle()