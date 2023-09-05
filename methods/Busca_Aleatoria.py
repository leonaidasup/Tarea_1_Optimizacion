from grafClass import graphics
from random import random


def busca_aleatoria(f, xl: float, xu: float, xr: float, error: float) -> object:
    e: float = 10 ** - error
    xi: float = xl
    xc: float = xi
    inc_i: float = abs(xr - xi)
    list_inc_e: list = [abs(xr - xi)]
    list_inc_i: list = [inc_i]
    for _ in range(100):
        if inc_i <= e:
            break
        xi = xl + (xu - xl) * random()
        inc_i = abs(xc - xi)
        list_inc_e.append(abs(xr - xc))
        list_inc_i.append(inc_i)
        if f(xi) > f(xc):
            xc = xi
    return graphics(name='(Busqueda Aleatoria n=100)', label='|x(u) - x(l)|',
                    legend_names=['|' + str(xr)[:6] + ' - x(i)|'],
                    list_x=[i for i in range(len(list_inc_i))],
                    list_inc_e=[list_inc_e], list_inc_i=list_inc_i)