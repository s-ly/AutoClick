import logging # модуль логирования



# Настройка логирования.
# Справка: https://webdevblog.ru/logging-v-python/
# level - уровень регистрации,
# filename - файл вывода,
# format - добавим дату и время.

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    format='%(asctime)s - %(message)s')

# logging.basicConfig(level=logging.INFO, filename='app.log')



# async def log_message(message):
#     """
#     Вывод (запись в файл) сообщения лога и на экран.
#     """
#     print(message)
#     logging.info(message)

def log_message(message, wr = False):
    """
    Вывод (запись в файл) сообщения лога и на экран.
    wr - необязательный, если True, то пишем в файл.
    """
    if wr == False:
        print(message)
        # logging.info(message)
    else:
        print(message)
        logging.info(message)