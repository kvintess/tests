# -*- coding: utf-8 -*-

# Отладка программ
#
# В коде всегда есть ошибки - это аксиома. Особенно если код развивается
# и добавляются новый функционал.
# Как обнаружить ошибку? Есть несколько методик и одна из них - отладка.
#
# Самый простой случай отладки - трассировка кода. Для этого надо
# в интересующих местах выполнения расставить print() с выводом
# ключевых значений (или логировать в файл, см. 4й часть урока)


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        # print(f'number {number}')
        for prime in prime_numbers:
            if number % prime == 0:
                # print(f'делится на {prime}')
                break
        else:
            prime_numbers.append(number)
            yield number
    # print(prime_numbers)


for prime in prime_numbers_generator(100):
    print(f'Простое из генераторв {prime}')


# Трассировка позволяет увидеть весь ход выполнения кода.
# Преимущества трассировки
#  - позволяет вычленять места изменения значений в разные моменты
#       времени выполнения кода
#  - применима в сложных условиях (нет дебаггера,
#       нет доступа к запуску программы,
#       невозможно смоделировать поведение пользователя, етс)
# Недостатки:
#  - приходится писать много кода в print()
#  - замедляет выполнение программы
#  - сложно переключать режимы отладка vs продакшн

# Другой способ отладки - дебаггинг с помощью отладчика.

# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#
#
# for prime in prime_numbers_generator(100):
#     print(prime)

# Это наиболее распространенный способ отладки кода программистом
# при разработке. Но программа-отладчик может запускаться и без pycharm,
# например на удаленных серверах - обратите внимание как pycharm
# запускает код в режиме отладки.

# Преимущества дебаггинга:
#  - полный контроль и анализ состояния программы в момент точки останова
#  - возможность следить за ходом выполнения алгоритма
# Недостатки:
#  - иногда сложно поймать необходимое состояние программы
#       (скажем, большой массив входных данных, а ошибка возникает
#       только в одном случае)


# Наиболее употребимые приемы работы с отладчиком
# 1) Условные точки останова
# 2) Наблюдение за переменными
# 3) Интерактивное изменение значений переменных

# from family import emulate_life
#
# emulate_life(num_cats=2)
