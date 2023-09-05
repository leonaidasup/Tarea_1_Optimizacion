from grafClass import graphics


def comparator(f, xl: float, xu: float, xr: float) -> tuple:
    return (xl, xr) if f(xl) * f(xr) < 0 else (xr, xu)


def biseccion(f, xl: float, xu: float, xr: float, error: int) -> object:
    e: float = 10 ** - error
    inc_i: float = abs(xl - xu)
    list_inc_e_xl: list = [abs(xr - xl)]
    list_inc_e_xu: list = [abs(xr - xu)]
    list_inc_i: list = [inc_i]
    while inc_i > e:
        (xl, xu) = comparator(f=f, xl=xl, xu=xu, xr=(xl + xu) / 2)
        inc_i = abs(xl - xu)
        list_inc_e_xl.append(abs(xr - xl))
        list_inc_e_xu.append(abs(xr - xu))
        list_inc_i.append(inc_i)
    return graphics(name='(Biseccion)', label='|x(u) - x(l)|',
                    legend_names=['|' + str(xr)[:6] + ' - x(u)|', '|' + str(xr)[:6] + ' - x(l)|'],
                    list_x=[i for i in range(len(list_inc_i))],
                    list_inc_e=[list_inc_e_xu, list_inc_e_xl], list_inc_i=list_inc_i)
