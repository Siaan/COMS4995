# Welcome to  kalmanfilter's documentation!
==========================================

## What is Kalman Filter?

Kalman Filter, also known as Hidden Markov Model, is a dimensionality reduction model which assumes that data follows an underlying latent linear dynamical system. It projects high dimensional data into a low dimensional represenation while preserving the main features/variables (better known as explanatory variables) which it believes explains the data well.

This project is integrated with an open source platform for neural data analysis called NeuroCAAS. We aim to separate the engineer from the scientist. Hence the only thing users will have to implement are the common paramters for kalman filter such as:

 - Data collected (observations) 
 - Transition matrix: A
 - Noise Covariance: P
 - Input control: B
 - Control Input Noise Covar : U
 - Sensor Measurement: H
 - Sensor Noise Covar: R

The input will be in the form of two files. An input file for the observations and a yaml file for configurations.


```eval_rst
.. toctree::
    :maxdepth: 2
    :caption: Contents:

    modules

.. note::
    The documentation for kalmanfilter cotinuously being updated.
```

