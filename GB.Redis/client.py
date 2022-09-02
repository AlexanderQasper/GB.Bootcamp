import imp


import redis

with  redis.Redis() as redis_client:
    value = redis_client.brpop("queue")

# rpop - забираем значение из очереди с хвоста в голову, но если никого нет, то выдаёт пустую строку
# brpop - забираем только когда появляется, то есть клиент ждёт


print(int(value[1]))
# int и индекс массива добавлен, чтобы перевести из байтов в норм целое число и вывести только его