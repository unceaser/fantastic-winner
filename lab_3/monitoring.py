import requests
import json
import logging
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    ser_work = "\nServer в роботі :)\n"
    ser_down = "\nВиникла наступна помилка: \n"
    try:
        r = requests.get(url)
        data = json.loads(r.content)
    except Exception as e:
        print(ser_down, e, flush=True)
        logging.error("%s %s",ser_down, e)
    else:
        print(ser_work, flush=True)
        logging.warning("%s", ser_work)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])


if __name__ == '__main__':
    while True:
        main("http://localhost:8000/health")
        time.sleep(60)
<<<<<<< HEAD

=======
>>>>>>> d992fed42fd4cee8fee93736f64f64dd63e6d891
