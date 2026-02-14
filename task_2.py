import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('C:\\').percent

print("Мониторинг загрузки CPU:", cpu, "%")
print("Мониторинг оперативной памяти:", memory, "%")
print("Процентное загруженности диска:", disk, "%")