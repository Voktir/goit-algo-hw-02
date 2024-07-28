from queue import Queue
from time import sleep
import random

# Створити чергу заявок
queue = Queue()

queue_dict = {'id': 0}

def generate_request():
    # Створити нову заявку
    data = random.uniform(0, 999)
    req = {'id': queue_dict['id'], 'data': data}
    queue_dict['id'] += 1
    # Додати заявку до черги
    queue.put(req)
    print(f"З'явилась заявка {req["id"]} ")

def process_request():
    if not queue.empty():
        # Видалити заявку з черги
        req = queue.get()
        # Обробити заявку
        print(f'Обробка заявки № {req["id"]} з даними: {req["data"]}')
        queue.task_done()
    else:
        print('Черга заявок порожня, очікування...')

if __name__ == "__main__":
    try:
        queue_dict['id'] = 1
        process_request()
        sleep(2)
        while True:
            gen_proc = random.randint(0, 1)
            if gen_proc == 0:
                # Створення нових заявок
                generate_request()
                sleep(1)
            else:
                # Обробка заявок
                process_request()
                sleep(1)
    except KeyboardInterrupt:
        print("Користувач зупинив програму.")