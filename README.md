# Kalman Filter
![GitHub](https://img.shields.io/github/license/siaan/project-proposals-f2020?style=plastic)
[![Build Status](https://travis-ci.org/Siaan/kalmanfilter.svg?branch=master)](https://travis-ci.org/Siaan/kalmanfilter)
![Codecov](https://img.shields.io/codecov/c/gh/Siaan/kalmanfilter)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/siaan/kalmanfilter?style=flat-square)
[![Documentation Status](https://readthedocs.org/projects/kalmanfilter/badge/?version=latest)](https://kalmanfilter.readthedocs.io/en/latest/?badge=latest)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyth?style=flat-square)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Siaan/kalmanfilter?style=flat-square)

## Kalman Filter

Kalman Filter, also known as Hidden Markov Model, is a dimensionality reduction model which assumes that data follows an underlying latent linear dynamical system. It projects high dimensional data into a low dimensional represenation while preserving the main features/variables (better known as explanatory variables) which it believes explains the data well. 

## How it Works
Kalman Filter provides estimates of unknown variables given the measurements observed over time. There are two main steps:
1. Prediction Step:
  Given a current estimate of a measurement (for example position in the x axis) x_t, we can predict x_{t+1}
2. Update Step:
  We update our current estimates to be our predicted step, input more raw measurements from sensors and predict again.

Despite initial estimates or raw measurements, the Kalman Filter does a computationally efficient analysis of predicting values. 

## Demo
![](https://raw.githubusercontent.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/master/animations/05_dog_track.gif)


Since this project is created for use on http://neurocaas.org/ the demo is presented on that website. 
The user is only responsible for 1. data.csv 2. configuration.yaml. These two files are uploaded to the website and the code handles the rest. 


This project, as well as all my other research projects are mentioned on my website:  
https://siaan.github.io/research-projects/ 


