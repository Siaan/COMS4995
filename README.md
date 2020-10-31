# Kalman Filter
![GitHub](https://img.shields.io/github/license/siaan/project-proposals-f2020?style=plastic)
[![Build Status](https://travis-ci.org/Siaan/kalmanfilter.svg?branch=master)](https://travis-ci.org/Siaan/kalmanfilter)
![Codecov](https://img.shields.io/codecov/c/gh/Siaan/kalmanfilter)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/siaan/kalmanfilter?style=flat-square)


## Kalman Filter

Kalman Filter, also known as Hidden Markov Model, is a dimensionality reduction model which assumes that data follows an underlying latent linear dynamical system. It projects high dimensional data into a low dimensional represenation while preserving the main features/variables (better known as explanatory variables) which it believes explains the data well. 

## How it works
Kalman Filter provides estimates of unknown variables given the measurements observed over time. There are two main steps:
1. Prediction Step:
  Given a current estimate of a measurement (for example position in the x axis) x_t, we can predict x_{t+1}
2. Update Step:
  We update our current estimates to be our predicted step, input more raw measurements from sensors and predict again.

Despite initial estimates or raw measurements, the Kalman Filter does a computationally efficient analysis of predicting values. 

## Example
![](https://raw.githubusercontent.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python/master/animations/05_dog_track.gif)





