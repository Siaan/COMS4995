from scripts.main import visualise 
from unittest import mock
import scripts.main.clean_KF as KF

import numpy as np


@mock.patch("%s.KF.plt" % __name__)
def test_visualise(mock_plt):
    x = np.arange(0,5,0.1)
    y = np.sin(x)
    x_messy = np.arange(0,5,0.1)
    KF.visualise(x,y, x_messy)

    mock_plt.title.assert_called_once_with("RTS Smoother")
    assert mock_plt.figure.called

