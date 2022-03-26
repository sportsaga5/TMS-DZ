import time
from datetime import datetime

# задание 1
x = input("Введите длину списка: ")
print([i for i in range(1, x+1)])

# задание 2 
def get_numbers_list(x: int) -> list:
    return [i for i in range(1, x+1)]
print(get_numbers_list(x))

# задание 3
def current_time():
    time.sleep(1)
    now = datetime.now()
    return now.strftime("%H:%M:%S")

print([current_time() for i in range(5)])
    

