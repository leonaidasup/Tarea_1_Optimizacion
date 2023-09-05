from matplotlib import pyplot as plt
from methods import NewthonRapshon, False_Position, Biseccion, Quadratic_Interpolation, Phi, Busca_Aleatoria


def f(x: float) -> float:
    return 3 * x ** 2 - 100 * x + 200


def df(x: float) -> float:
    return 6 * x - 100


def i_f(x: float) -> float:
    return x ** 3 - 50 * x ** 2 + 200 * x


def graf(lista: list) -> None:
    fig, ax = plt.subplots(nrows=len(lista), ncols=2, constrained_layout=True)
    for i, item in enumerate(lista):
        for j, y in enumerate(item.list_inc_e):
            ax[i, 0].plot(item.list_x, y, label=item.legend_names[j])
            ax[i, 0].set_title(item.name + ' error', fontweight='semibold')
        ax[i, 0].legend(loc='upper right')
        ax[i, 1].plot(item.list_x, item.list_inc_i, label=item.label)
        ax[i, 1].set_title(item.name + ' dif', fontweight='semibold')
        ax[i, 1].legend(loc='upper right')
    plt.show()


def main(fun, a: float, b: float, xr: float, error: int) -> None:
    graf([NewthonRapshon.newthon_rapshon(f=fun, df=df, xi=a, xr=xr, error=error),
          False_Position.false_position(f=fun, xl=a, xu=b, xr=xr, error=error),
          Biseccion.biseccion(f=fun, xl=a, xu=b, xr=xr, error=error),
          Quadratic_Interpolation.quadratic_interpolation(f=i_f, x1=a, x3=b, xr=xr, error=error),
          Phi.phi(f=i_f, xl=a, xu=b, xr=xr, error=error),
          Busca_Aleatoria.busca_aleatoria(f=i_f, xl=a, xu=b, xr=xr, error=error)])


if __name__ == '__main__':
    main(fun=f, a=0, b=4, xr=2.13700352153, error=6)
