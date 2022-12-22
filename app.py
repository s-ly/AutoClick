from ssl import VERIFY_CRL_CHECK_LEAF
import pyautogui # основной модуль
import pyperclip # буфер обмена
import time
import log_app # мой модуль логирования
import random # для перемешивание url

# popitki = 3
iterations = 1
time_sleep = 0

retina = 1 # коэфф смещения карсора для дисплеев retina

# флаг, нужен ли переход с ВК. 1 - нет, 2 - да, нужен переход.
vk_post_flag = 1 

# Используется для парсинга строки для url.
# 57 - прямая ссылке РуТуб
# 33 - ссылка на пост ВК
url_parser_index = 57

url_1 = None
url_2 = None
url_3 = None


# суперфлаг инициализации управляющих флагов.
# При сбое, когда попытки шага кончились, мы запускаем цикл по новой.
# Нужно обнулить все управляющие флаги.
# Она находится в True в начале, для первой инициации, далее, переводим его 
# в True только при сбое, тоесть когда кончились попытки шагов  и нужно всё перезапустить.
superflag_init = True

# popitki = 43
reset = 0


####################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
# Шаги
####################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
def restart_browser():
    """Перезапуск Браузера если вышло сообщение: Что-то пошло не так."""
    log('Возможно упал Тор')    
    if searchDrag('images/error1.png') == False:
        return False
    log('Ошибка: Что-то пошло не так!!!')
    log('Перезагрузка браузера.')
    
    log('(restart) Ищем кнопку меню Тора')
    if searchDrag('images/img_17.png') == False:
        if searchDrag('images/img_28.png') == False:
            if searchDrag('images/img_29.png') == False:
                return False
    pyautogui.click() 
    
    log('(restart) Ищем Выход')
    if searchDrag('images/exit1.png') == False:
        return False
    pyautogui.click() 
    time.sleep(3) # что-бы Тор успел выключится

    log('(restart) Ищем значёк Тора')
    if searchDrag('images/tor_start.png') == False:
        return False
    pyautogui.click() 
    time.sleep(3) # что-бы Тор успел включится
    
    return True


def step_adres():
    """Поис адресной строки"""
    log('Поис адресной строки')
    if searchDrag('images/img_14.png') == False:
        if searchDrag('images/img_24.png') == False:
            return False
    pyautogui.move(300 * retina, 0, 1) # смешаем курсор вправо
    pyautogui.click(button='right')
    return True


def step_paste():
    """Вставить - контекстное меню"""
    log('Вставить')
    if searchDrag('images/img_15.png') == False:
        return False
    pyautogui.click()    
    pyautogui.press('enter')
    return True



# def step_cuc():
#     """
#     Жмёт на куки двух видов.
#     """
#     log('принять куки')
#     if searchDrag('images/img_16.png') == False:
#         if searchDrag('images/img_30.png') == False:
#             return False
#     pyautogui.click()
#     return True

def step_cuc():
    """
    Жмёт на куки двух видов.
    """
    global reset
    # log('10 ^')
    # time.sleep(10) # ТЕХНИЧЕСКА

    # суперфлаг инициализации управляющих флагов.
    # global superflag_init

    # Флаг для определения нашли куки или "Ошибку"
    if_flag = 0

    log('принять куки')
    if searchDrag('images/img_16.png') == False:
        if searchDrag('images/img_30.png') == False:
            if searchDrag('images/error1.png') == False:
                if searchDrag('images/error2.png') == False:
                    if searchDrag('images/error3.png') == False:
                        return False
                else:
                    # найдена "ОШИБКА"
                    if_flag = 1
            else:
                # найдена "ОШИБКА"
                if_flag = 1
    
    if if_flag == 0:
        pyautogui.click()
        return True
    else:
        # нужен рестарт Браузера
        log('Перезагрузка браузера.')
    
        log('(restart) Ищем кнопку меню Тора')
        if searchDrag('images/img_17.png') == False:
            if searchDrag('images/img_28.png') == False:
                if searchDrag('images/img_29.png') == False:
                    return False
        
        
        
        
        
        
        
        
        # time.sleep(1)
        pyautogui.move(0, -30, 1)
        pyautogui.click() 
        
        # log('(restart) Ищем Выход')
        # if searchDrag('images/exit1.png') == False:
        #     return False
        # time.sleep(1)
        # pyautogui.click() 
        # time.sleep(3) # что-бы Тор успел выключится

        log('(restart) Ищем значёк Тора')
        if searchDrag('images/tor_start.png') == False:
            return False
        time.sleep(1)
        pyautogui.click() 
        time.sleep(5) # что-бы Тор успел включится

        # log('10 ^^')
        # time.sleep(10) # ТЕХНИЧЕСКА
        
        # superflag_init = True
        # reset = 1
        return False


def step_winsiz():
    """
    Расширяет окно. Оринтируется на три вида кнопок меню Тора.
    Обычный, с точкой, с зелёной точкой.
    """
    log('расширить окно')
    if searchDrag('images/img_17.png') == False:
        if searchDrag('images/img_28.png') == False:
            if searchDrag('images/img_29.png') == False:
                return False
    pyautogui.move(26 * retina, 0, 1)
    pyautogui.drag(120 * retina, 0, 1, button='left')
    return True


def step_logo():
    """Едем на шапку и прыгаем вниз.
    
    На этом шаге иногда появляется сообщение об утечке данных,
    тогда жмём Ввод."""
    # pyautogui.press('enter')
    log('Едем на шапку и прыгаем вниз (с проверкой утечки)')
    
    if searchDrag('images/img_33_data_leak.png') == True:
        log('Обнаружено сообщение утечки данных.')
        pyautogui.press('enter')

    if searchDrag('images/img_05.png') == False:
        if searchDrag('images/logo_v2.png') == False:
            if searchDrag('images/logo_v3.png') == False:
                return False
    pyautogui.move(10 * retina, 300 * retina, 1) # смешаем курсор вниз
    return True


def step_ses():
    log('Ищем шестерёнку и жмём')
    if searchDrag('images/img_04.png')  == False:        
        if searchDrag('images/img_18.png') == False:
            if searchDrag('images/img_18v2.png') == False:
                if searchDrag('images/img_18v3.png') == False:
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
            if searchDrag('images/img_18v2.png') == False:
                if searchDrag('images/img_18v3.png') == False:
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
        if searchDrag('images/logo_v2.png') == False:
            if searchDrag('images/logo_v3.png') == False:
                return False
    pyautogui.move(100 * retina, 0, 1) # смешаем курсор вправо
    # pyautogui.click()
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
    """
    Ищет меню тора или меню тора с точкой,
    или с зелёной точкой (если окно в фокусе).
    """
    log('Ищем меню Тора и жмём')
    if searchDrag('images/img_17.png') == False:
        if searchDrag('images/img_28.png') == False:
            if searchDrag('images/img_29.png') == False:
                return False
    pyautogui.click()
    return True


def step_new():
    """Ищем "Новая личность" и жмём"""
    log('Ищем "Новая личность" и жмём')
    if searchDrag('images/img_22.png') == False:
        return False
    pyautogui.click()
    log('2 секунда задержка')
    time.sleep(2) # что-бы Тор успел перезапустится
    return True


def step_new_tab():
    """Ищем новую вкладку и жмём"""
    log('Ищем новую вкладку и жмём')
    if searchDrag('images/img_23.png') == False:
        return False
    pyautogui.click()
    return True


def step_vk_post():
    """Ищем ссылку в посте в ВК и жмём"""
    log('Ищем новую вкладку и жмём')
    if searchDrag('images/img_32_vk_post.png') == False:
        if searchDrag('images/img_32_vkm_post.png') == False:
            if searchDrag('images/img_32_tikm_post.png') == False:
                if searchDrag('images/img_vk_post2.png') == False:
                    if searchDrag('images/img_mvk_post2.png') == False:
                        return False
    time.sleep(2) # с сылкой что-то происходит
    pyautogui.click()
    return True


def step_play():
    """
    Нажатие play если он есть, иначе едем дальше.
    """
    # иногда плей включается не сразу и мы подождём
    log('Ищем кнопку play и жмём, но в начале подождём 8 сек')
    time.sleep(8)
    pyautogui.move(10, 10, 1)
    pyautogui.move(-10, -10, 1) 

    if searchDrag('images/img_25.png') == False:
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


def step(f, reset = 0):
    """Отработка попыток шагов. В случае глобального сбоя (кончильсь попытки)
    включает суперФлаг инициации управляющих флагов."""
    # суперфлаг инициализации управляющих флагов.
    global superflag_init
    # global popitki
    
    popitki = 43
    # if reset == 1:
    #     popitki = 0
    # log('reset ' + str(reset))
    # log('pop ' + str(popitki))
    # popitki = 5
    i = True
    while i:
        func_run = f()
        if func_run:
            log('шаг -> ок')
            time.sleep(0.75)
            return True
        else:
            log('шаг -> ошибка')
            popitki = popitki - 1
            if popitki != 0:
                log('Осталось попыток: ' + str(popitki))      
                pyautogui.move(10, 10, 1)
                pyautogui.move(-10, -10, 1)          
            else:
                log('Кончилиси попытки шага !!!')
                log('Включаю суперФлаг иницилизации')
                superflag_init = True
                return False


def read_url ():
    """Читаем 3 url из файла"""
    global url_1
    global url_2
    global url_3
    global url_parser_index

    url_fileName = ''
    url_fileName = input('Введите имя файла с url. Если просто Ввод, то будет "url.txt": ') or 'url.txt'

    with open(url_fileName, "r") as file:
        
        print ('Загрузка url:')
        url_1_note = file.readline()
        url_1 = file.readline()
        url_2_note = file.readline()
        url_2 = file.readline()
        url_3_note = file.readline()
        url_3 = file.readline()

        # убираем в конце знак переноса строки
        url_1 = url_1[:-1]
        url_2 = url_2[:-1]
        url_3 = url_3[:-1]
        url_1_note = url_1_note[:-1]
        url_2_note = url_2_note[:-1]
        url_3_note = url_3_note[:-1]

        print(url_1_note + ': ' + url_1)
        print(url_2_note + ': ' + url_2)
        print(url_3_note + ': ' + url_3)

        # убираем описание из url-строки
        # url_1 = url_1[0:url_parser_index]
        # url_2 = url_2[0:url_parser_index]
        # url_3 = url_3[0:url_parser_index]


def random_url():
    """Перемешивает url адреса"""
    global url_1
    global url_2
    global url_3

    urls = []
    urls.append(url_1)
    urls.append(url_2)
    urls.append(url_3)

    random.shuffle(urls) # перемешиваем

    # распределяем перемешанные url
    url_1 = urls[0]
    url_2 = urls[1]
    url_3 = urls[2]

    print("Перемешиваем ссылки:")
    print(url_1)
    print(url_2)
    print(url_3)


###################################################################################################
# Главный цикл
###################################################################################################
def main_cicle():
    """главный цикл"""
    # global retina
    global vk_post_flag
    global iterations
    global time_sleep
    global url_1
    global url_2
    global url_3
    global url_parser_index

    # суперфлаг инициализации управляющих флагов.
    global superflag_init

    global reset

    # log('Запуск \n', True)
    log_app.log_message('Запуск', True)
    print('\nПрограмма автоматического просмотра РуТуб v0.67')
    print('\nВНИМАНИЕ!!! если есть ссылки на TikTok, то Tor в обычном (не мобильном) режиме.')
    # print('Если экран retina, то подмени картинки в папке images на картинки с retina!')

    while True:
        vk_post_flag_input = input('Нужен переход с ВК? ' +
        'Если ДА введите 2 и нажмите Ввод, если обычный то 1: ')
        # retina_input = input('Нужен переход с ВК? Если ДА введите 2 и нажмите Ввод, если обычный то 1: ')
        # if retina_input == '1' or retina_input == '2':
        #     retina_input = int(retina_input)
        #     retina = retina_input
        #     break
        if vk_post_flag_input == '1':
            vk_post_flag = 1
            break

        if vk_post_flag_input == '2':
            vk_post_flag = 2
            url_parser_index = 33  # ссылки для постов ВК
            break

    read_url()


    # url_1 = input('Вставьте ссылку 1: ')
    # url_2 = input('Вставьте ссылку 2: ')
    # url_3 = input('Вставьте ссылку 3: ')
    # pyperclip.copy(url_1) # копируем в буфер обмена

    time_sleep = int(input('Сколько секунд ждать: '))    



    # Флаги управления циклом
    # flag_new_tab = True # нужна ли новая вкладка
    # flag_new = True # нужна ли новая личность
    # flag_cuc = True # нужно ли куки и расширить окно
    # flag_play = False # нужно ли нажимать на play (нужно на второй и третьей вкладке)
    # flag_url = False # нужно ли url_2
    # flag_url_3 = False # нужна ли URL 3

    while True:   
        # СуперИнициализация управляющих флагов ---------------------------------------------------
        if superflag_init == True:  

            # Флаги управления циклом
            flag_new_tab = True # нужна ли новая вкладка
            flag_new = True # нужна ли новая личность
            flag_cuc = True # нужно ли куки и расширить окно
            flag_play = False # нужно ли нажимать на play (нужно на второй и третьей вкладке)
            flag_url = False # нужно ли url_2
            flag_url_3 = False # нужна ли URL 3
            
            # Закрываем суперфлаг
            superflag_init = False
        # -----------------------------------------------------------------------------------------


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


        #VK ---------------------------------------------------------------------------------------
        # Если нужен ВК
        # if vk_post_flag == 2:
        #     if step(step_adres) != True: continue        
        #     if step(step_paste) != True: continue
        #     if step(step_vk_post) != True: continue
            
        #VK ---------------------------------------------------------------------------------------


        if step(step_adres) != True: continue        
        if step(step_paste) != True: continue

        # Если нужен ВК
        if vk_post_flag == 2:
            if step(step_vk_post) != True: continue


        if flag_cuc == True:
            # if step(step_cuc, reset) != True: continue
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
        random_url() # перемешиваем url
        reset = 0
###################################################################################################


main_cicle()