
import logging
import socket


log_format = '%(asctime)s %(name)s: %(levelname)s: %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
log_name = "echo_client"
logging.basicConfig(
    format=log_format, level=logging.INFO, datefmt=date_format)


logger = logging.getLogger(log_name)

server, port = "localhost", 9090

sock = socket.socket()
sock.connect((server, port))
logger.info(f"Подключение к серверу {server} по порту {port}.")

while True:
    data = input('Пользователь: ')

    if data == "exit":
        sock.close()
        logger.info(f"Отключение от сервера {server}.")

        break

    if not data:
        print("Введите сообщение!")

        continue

    sock.send(str.encode(data))
    logger.info(f"Отправлены данные на сервер {server}.")

    data = sock.recv(1024)
    logger.info(f"Получены данные от сервера{server}.")

    print(data)