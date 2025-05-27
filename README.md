# Internet of Things: Smart Greenhouse

This repository contains the code for the IoT course of SJTU. The goal is to create a working prototype of a smart greenhouse.

## Details

The smart greenhouse will be able to monitor both temperature and humidity with sensors. Another sensor checks the current level of the water tank. This data will be sent to the main server for visualization and analysis. For instance,
- when the temperature is too high, windows on the side of the greenhouse will automatically open
- when the temperature is too low, windows will close and a heater will be power on
- if the humidity is not right, humidifiers will be accordingly powered on or off
- when the water level is too low, refill it


## Architecture

Thingsboard Server
Python to simulate sensors and actuators

## Todo

1. Thingsboard unifié
2. Code python qui gère la température
3. Code python qui gère l'humidité
