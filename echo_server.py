
import logging
import socket

#параметры

log_format = '%(asctime)s %(name)s: %(levelname)s: %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
log_name = "echo_server"
logging.basicConfig(
    format=log_format, level=logging.INFO, datefmt=date_format)


logger = logging.getLogger(log_name)

logger.info("Сервер запущен!")

# ip/tcp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 9090))
logger.info("Подключение по порту 9090")

sock.listen(1)

while True:
    conn, addr = sock.accept()
    if not conn:
        continue

    logger.info(f"Пользователь {addr[0]}:{addr[1]} подключился.")
    while True:
        data = conn.recv(1024)
        logger.info(f"Получено 1024 байт от пользователя {addr[0]}:{addr[1]}.")
        if not data:
            logger.info(f"Пользователь {addr[0]}:{addr[1]} отключился.")
            break
        conn.send(data)
        logger.info(f"Отправлены данные пользователя {addr[0]}:{addr[1]}.")
    conn.close()

logger.info("Сервер остановлен.")