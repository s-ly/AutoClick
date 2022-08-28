import pyautogui # основной модуль
import pyperclip # буфер обмена
import time
import log_app # мой модуль логирования

# popitki = 3
iterations = 1
time_sleep = 0

retina = 1 # коэфф смещения карсора для дисплеев retina

url_1 = None
url_2 = None
url_3 = None
####################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
# Шаги
####################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
def step_adres():
    log('Поис адресной строки')
    if searchDrag('images/img_14.png') == False:
        if searchDrag('images/img_24.png') == False:
            return False
    pyautogui.move(300 * retina, 0, 1) # смешаем курсор вправо
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
    pyautogui.move(26 * retina, 0, 1)
    pyautogui.drag(120 * retina, 0, 1, button='left')
    return True


def step_logo():
    log('Едем на шапку и прыгаем вниз')
    if searchDrag('images/img_05.png') == False:
        return False
    pyautogui.move(10 * retina, 300 * retina, 1) # смешаем курсор вниз
    return True


def step_ses():
    log('Ищем шестерёнку и жмём')
    if searchDrag('images/img_04.png')  == False:        
        if searchDrag('images/img_18.png') == False:
            return False
    time.sleep(5) # из-за рекламы нужно подождать с нажатием
    pyautogui.move(10, 10, 1)
    pyautogui.move(-10, -10, 1) 
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
    pyautogui.scroll(-300 * retina)
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
    log('Ищем 1080 или 720 и скрол')
    if searchDrag('images/img_13.png') == False:
        if searchDrag('images/img_27.png') == False:
            return False
    pyautogui.scroll(-300 * retina)
    return True


def step_144():
    log('Ищем 144(240) и жмём')
    if searchDrag('images/img_11(240).png') == False:
        return False
    pyautogui.click()
    return True


def step_logo2():
    log('Едем на шапку(2) и прыгаем вправо')
    if searchDrag('images/img_05.png') == False:
        return False
    pyautogui.move(100 * retina, 0, 1) # смешаем курсор вправо
    pyautogui.click()
    pyautogui.move(10 * retina, 300 * retina, 1) # смешаем курсор вниз
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

    log('Шаг 11 (сон): ок')
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


def step_new_tab():
    log('Ищем новую вкладку и жмём')
    if searchDrag('images/img_23.png') == False:
        return False
    pyautogui.click()
    return True


def step_play():
    """нажатие play"""
    # иногда плей включается не сразу и мы подождём
    log('Ищем кнопку play или pause, жмём толоко на play, но в начале подождём 8 сек')
    time.sleep(8)
    pyautogui.move(10, 10, 1)
    pyautogui.move(-10, -10, 1) 

    if searchDrag('images/img_25.png') == False:
        if searchDrag('images/img_26.png') == False:
            return False
        else:
            return True
    pyautogui.click()
    return True

####################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
def log(mess, wr = False):
    global iterations
    log_mess = 'Цикл: ' + str(iterations) + ' - ' + mess
    # print('Цикл: ' + str(iterations) + ' - ' + mess)
    log_app.log_message(log_mess, wr)


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


def read_url ():
    """Читаем 3 url из файла"""
    global url_1
    global url_2
    global url_3

    with open("url.txt", "r") as file:
        
        print ('Загрузка url:')
        url_1 = file.readline()
        url_2 = file.readline()
        url_3 = file.readline()

        print(url_1)
        print(url_2)
        print(url_3)


def main_cicle():
    """главный цикл"""
    global retina
    global iterations
    global time_sleep
    global url_1
    global url_2
    global url_3

    # log('Запуск \n', True)
    log_app.log_message('Запуск', True)
    print('\nПрограмма автоматического простотра РуТуб v0.44')
    print('Если экран retina, то подмени картинки в папке images на картинки с retina!')

    while True:
        retina_input = input('У вас ретина? Если ДА введите 2 и нажмите Ввод, если обычный то 1: ')
        if retina_input == '1' or retina_input == '2':
            retina_input = int(retina_input)
            retina = retina_input
            break

    read_url()


    # url_1 = input('Вставьте ссылку 1: ')
    # url_2 = input('Вставьте ссылку 2: ')
    # url_3 = input('Вставьте ссылку 3: ')
    # pyperclip.copy(url_1) # копируем в буфер обмена

    time_sleep = int(input('Сколько секунд ждать: '))    
    flag_new_tab = True # нужна ли новая вкладка
    flag_new = True # нужна ли новая личность
    flag_cuc = True # нужно ли куки и расширить окно
    flag_play = False # нужно ли нажимать на play (нужно на второй и третьей вкладке)
    flag_url = False # нужно ли url_2
    flag_url_3 = False # нужна ли URL 3

    while True:   
        if flag_url_3 == True:
            pyperclip.copy(url_3) # копируем в буфер обмена url 3
        elif flag_url == True:
            pyperclip.copy(url_2) # копируем в буфер обмена второй url
        else:
            pyperclip.copy(url_1) # копируем в буфер обмена            

        # ели True, то новую личность
        if flag_new == True:   
            if step(step_tor_menu) != True: continue
            if step(step_new) != True: continue

        if step(step_adres) != True: continue        
        if step(step_paste) != True: continue

        if flag_cuc == True:
            if step(step_cuc) != True: continue
            if step(step_winsiz) != True: continue

        if step(step_logo) != True: continue
        if step(step_ses) != True: continue

        # временно отлючил изменение скорости
        # if step(step_speed) != True: continue
        # if step(step_sc_speed) != True: continue
        # if step(step_two_speed) != True: continue

        if step(step_sis_m) != True: continue
        if step(step_kat) != True: continue
        if step(step_1080) != True: continue
        if step(step_144) != True: continue
        if step(step_logo2) != True: continue

        if flag_play == True:   
            if step(step_play) != True: continue




        # ели True, то открываем новую вкладку
        if flag_new_tab == True:
            if flag_url == False:
                # flag_new_tab = False
                flag_new = False 
                flag_cuc = False
                flag_play = True # на второй вкладке нужно нажать play
                flag_url = True # понадобится второй url
                if step(step_new_tab) == True: continue

        # ели True, то открываем новую вкладку
        if flag_new_tab == True:
            if flag_url_3 == False:
                flag_new_tab = False
                flag_new = False 
                flag_cuc = False
                flag_play = True # на второй вкладке нужно нажать play
                flag_url_3 = True # понадобится url 3
                flag_url = False # url 2 не нужен
                if step(step_new_tab) == True: continue


        

        if step(step_sleep_show) != True: continue
        flag_new_tab = True # нужна ли новая вкладка
        flag_new = True # понадобится новая личность
        flag_cuc = True # нужно ли куки и расширить окно
        flag_play = False # нужно ли нажимать на play (нужно на второй вкладке)
        flag_url = False # нужно ли url_2
        flag_url_3 = False # нужна ли URL 3

        log('Цикл завершён --------------------------', True)
        print()
        print('Глобальный перезапуск цикла, сон 15 сек.\n')
        # log('Глобальный перезапуск цикла, сон 15 сек.')
        time.sleep(15)
        iterations = iterations + 1
###################################################################################################


main_cicle()