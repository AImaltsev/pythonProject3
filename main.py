import time

# Текущее время
current_time = time.localtime()
print("Текущее время:", time.strftime("%H:%M:%S", current_time))

# Только минуты
minutes = time.strftime("%M", current_time)
print("Текущие минуты:", minutes)

# Только дата
date = time.strftime("%d.%m.%Y", current_time)
print("Текущая дата:", date)

# Только месяц
month = time.strftime("%B", current_time)
print("Текущий месяц:", month)