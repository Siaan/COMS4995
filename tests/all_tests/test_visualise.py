from tests import input_process, output_process, visualize
# from unittest import mock
# import scripts.main.clean_KF as KF
from scripts.main import process_data_file # noqa: F401
from scripts.main import process_output
import pandas as pd
import numpy as np
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

'''
def test_process_data_file():
    test_process  = np.array([5])
    file = pd.read_csv('test.csv'
    assert type(process_data_file(file)) == type(test_process)
'''

def test_process_output():
    '''
    :param x: filterd/smoothed data
    :param p: covariances_
    :return: dataframe of processed results
    '''

    x = [[5,6]]
    x = np.asarray(x)
    p = np.array([5])
    df = pd.DataFrame()
    assert type(process_output(x, p, THIS_DIR)) == type(df)

def test_inputprocess():
    '''
    :param x: raw observations
    :return: all input re-formatted into numpy arrays
    '''
    test_array = np.array([5])
    assert input_process(5, 4) == test_array


def test_outputprocess():
    '''
    :param x: mediary values
    :return: numpy array
    '''
    test_array = np.array([4])
    assert output_process(5, 4) == test_array


def test_visualize():
    '''
    :param x: filterd/smoothed data
    :param p: covariances
    :return: plotting of  processed results
    '''
    assert isinstance(visualize(5, 4), str)


def test_visualize():  # noqa: F811
    '''
    :param x: filterd/smoothed data
    :param p: covariances
    :return: ensures visuals are returned
    '''

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
