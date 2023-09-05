from grafClass import graphics


def comparator(f, x1: float, x2: float, x3: float, x4: float) -> list:
    if x4 > x2:
        nueva_lista = [x2, x4, x3]
    else:
        nueva_lista = [x1, x4, x2]
    return nueva_lista


def quadratic_interpolation(f, x1: float, x3: float, xr: float, error: int) -> object:
    e: float = 10 ** - error
    x2: float = (x1 + x3) / 2
    inc_i: float = abs(x1 - x3)
    list_inc_e_x1: list = [abs(xr - x1)]
    list_inc_e_x2: list = [abs(xr - x2)]
    list_inc_e_x3: list = [abs(xr - x3)]
    list_inc_i: list = [inc_i]
    while inc_i > e:
        (x1, x2, x3) = comparator(f=f, x1=x1, x2=x2, x3=x3,
                                  x4=(f(x1) * (x2 ** 2 - x3 ** 2) + f(x2) * (x3 ** 2 - x1 ** 2) + f(x3) * (
                                          x1 ** 2 - x2 ** 2)) /
                                     (2 * (f(x1) * (x2 - x3) + f(x2) * (x3 - x1) + f(x3) * (x1 - x2))))

        inc_i = abs(x1 - x3)
        list_inc_e_x1.append(abs(xr - x1))
        list_inc_e_x2.append(abs(xr - x2))
        list_inc_e_x3.append(abs(xr - x3))
        list_inc_i.append(inc_i)
    return graphics(name='(Quadratic Interpolation)', label='|x1 - x3|',
                    legend_names=['|' + str(xr)[:6] + ' - x1|', '|' + str(xr)[:6] + ' - x2|',
                                  '|' + str(xr)[:6] + ' - x3|'],
                    list_x=[i for i in range(len(list_inc_i))],
                    list_inc_e=[list_inc_e_x1, list_inc_e_x2, list_inc_e_x3], list_inc_i=list_inc_i)
