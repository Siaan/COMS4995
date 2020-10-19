import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


def input_process(x, y):
    return np.asarray([x])


def output_process(x, y):
    return np.asarray([y])


def visualize(x, y):
    output = "figure created"
    return output


def visualise(x, y, x_messy, x_real=None):
    '''

    :param x: filterd/smoothed data
    :param y: covariances
    :param x_real: real data
    :param x_messy: raw measurements from sensors
    :return: plot comparing raw data and smooth/filtered data
    '''
    plt.figure(figsize=(10, 10))  # noqa: F821
    plt.plot(range(1, len(x) + 1), x[:, 0], c='r', label='Smoothed data')  # noqa: F821, E501
    plt.plot(  # noqa: F821
        range(
            1,
            len(x_messy) +
            1),
        x_messy,
        '--o',
        c='g',
        label='Noisy Measurement')
    if x_real.all() is not None:
        plt.plot(  # noqa: F821
            range(
                1,
                len(x_real) + 1),
            x_real,
            '--o',
            c='royalblue',
            label='True position')
    # plt.plot(range(1, len(x)+1), cv, c='r', label='Smoothed data')

    plt.legend()  # noqa: F821
    plt.title('RTS Smoother')  # noqa: F821
    plt.show()  # noqa: F821
    output = "figure created"
    return output
