from transform import FourierTransform
import numpy as np
import matplotlib.pyplot as plt

N = 8


def y_fun(x):
    return np.cos(x)


def z_fun(x):
    return np.sin(x)


def convolution(sig1, sig2):
    return list(map(lambda x, y: x * y, sig1, sig2))


def correlation(sig1, sig2):
    return list(map(lambda x, y: x.conjugate() * y, sig1, sig2))


def _main():
    y_values = FourierTransform._function_values(y_fun, 2 * np.pi, N)
    z_values = FourierTransform._function_values(z_fun, 2 * np.pi, N)

    ty_values = FourierTransform._fft(FourierTransform, y_values, 1)
    tz_values = FourierTransform._fft(FourierTransform, z_values, 1)

    x = np.linspace(0.0, np.pi / 4, 8)
    correl_values = correlation(ty_values, tz_values)
    conv_values = convolution(ty_values, tz_values)
    icorrel_values = FourierTransform._fft(FourierTransform, correl_values, -1)
    iconv_values = FourierTransform._fft(FourierTransform, conv_values, -1)

    f, axarr = plt.subplots(2, 2, figsize=(8, 6))
    plt.tight_layout()

    axarr[0, 0].plot(x, y_values)
    axarr[0, 0].set_title('y = cos(x)')
    axarr[0, 0].grid(True)

    axarr[0, 1].plot(x, z_values)
    axarr[0, 1].set_title('z = sin(x)')
    axarr[0, 1].grid(True)

    axarr[1, 0].plot(x, iconv_values)
    axarr[1, 0].set_title('Результат свертки')
    axarr[1, 0].grid(True)

    axarr[1, 1].plot(x, icorrel_values)
    axarr[1, 1].set_title('Результат корреляции')
    axarr[1, 1].grid(True)

    plt.show()


if __name__ == "__main__":
    _main()
