# Предварительно запустить redis server в терминале командой redis-cli
import redis
import random

# конструкция with ... as позволяет закрыть поток, соединение если словим ошибку
with  redis.Redis() as redis_server:
    redis_server.lpush("queue", random.randint(0,5))

# lpush - добавляем значения в очередь, с головы в хвост.
# В терминале открываем сервер командой кли. Потом LRANGE queue (from where) 0 -1 (from start to finish)