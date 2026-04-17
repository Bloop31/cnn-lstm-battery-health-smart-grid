## CNN-LSTM Battery Health Prediction for Smart Grid

This project implements a deep learning–based system to predict the **State of Health (SOH)** and **Remaining Useful Life (RUL)** of lithium-ion batteries using operational sensor data.
The predicted battery health is used to generate **adaptive charging recommendations** to support smart grid stability and efficient energy management.

A CNN-LSTM fusion model for accurate State of Health (SOH) estimation and Remaining Useful Life (RUL) prediction of lithium-ion batteries, a thermal-aware closed-loop charging controller that adjusts charging rates based on real-time temperature and battery health feedback, and  a grid-aware adaptive charging module based on Model Predictive Control (MPC) that dynamically schedules EV charging to reduce peak demand and maintain grid stability.

## Features

* Battery capacity degradation modelling
* SOH and RUL prediction using **CNN-LSTM**
* Health status and charging decision engine
* Visualization of degradation and prediction results
* Integration-ready design for smart charging systems

## Tech Stack

Python, TensorFlow/Keras, Scikit-learn, Pandas, NumPy, Matplotlib

## Dataset

Processed version of the **NASA Lithium-Ion Battery Aging Dataset** (Kaggle) and B000X battery dataset.

## Application

Supports intelligent EV charging control, peak load reduction, and predictive battery maintenance in smart grid environments. 

**Author:** Prajjit Basu
