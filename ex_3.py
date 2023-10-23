import datetime
import time

# Получаем текущее время
current_time = datetime.datetime.now()

end_time = current_time + datetime.timedelta(seconds=5)
# Запускаем цикл, который будет выполняться в течение 5 секунд
while datetime.datetime.now() < end_time:
    current_time = datetime.datetime.now()
    print(current_time.strftime("%H:%M:%S"))
    time.sleep(1)  # Подождать 1 секунду перед следующим выводом

print("Программа завершена.")
