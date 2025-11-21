import timeit
import numpy as np


# def soma1 ():
#     lista =  list(range(1,2000))
#     print(lista)
#     return lista


# soma1()
# time = timeit.timeit(soma1, number=10)
# print('função1', time)


def soma2():
    aleatorio1 =  np.arange(1,2000)
    # soma2  =  np.sum(aleatorio1)
    print(aleatorio1)
    return soma2


time = timeit.timeit(soma2, number=10)
print('função2', time)

