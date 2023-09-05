from grafClass import graphics


def newthon_rapshon(f, df, xi: float, xr: float, error: int) -> object:
    e: float = 10 ** -error
    inc_e: float = abs(xr - xi)
    inc_i: float = abs(xr - xi)
    list_inc_e: list = [inc_e]
    list_inc_i: list = [abs(inc_i)]
    while inc_e > e:
        xi = xi - inc_i
        inc_e = abs(xr - xi)
        inc_i = f(xi) / df(xi)
        list_inc_e.append(inc_e)
        list_inc_i.append(abs(inc_i))
    return graphics(name='(Newthon-Rapshon)', label='|x(i+1) - x(i)|',
                    legend_names=['|' + str(xr)[:6] + ' - x(i)|'],
                    list_x=[i for i in range(len(list_inc_e))],
                    list_inc_e=[list_inc_e], list_inc_i=list_inc_i)
