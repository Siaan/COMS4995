from tests import input_process, output_process, visualize
# from unittest import mock
# import scripts.main.clean_KF as KF
# from scripts.main import *

import numpy as np

#def test_process_data_file():
#    test_process  = np.array([5])
#    assert type(process_data_file('test.csv')) == type(test_process)

def test_inputprocess():
    test_array = np.array([5])
    assert input_process(5, 4) == test_array


def test_outputprocess():
    test_array = np.array([4])
    assert output_process(5, 4) == test_array


def test_visualize():
    assert isinstance(visualize(5, 4), str)


def test_visualize():  # noqa: F811
    result = "figure created"
    assert visualize(5, 6) == result


'''
@mock.patch("%s.visualise.plt" % __name__)
def test_visualise(mock_plt):
    x = np.arange(0,5,0.1)
    y = np.sin(x)
    x_messy = np.arange(0,5,0.1)
    visualise(x,y, x_messy)

    mock_plt.title.assert_called_once_with("RTS Smoother")
    assert mock_plt.figure.called
'''
