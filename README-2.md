# MicroTwin AI

**An AI-powered digital twin for microgreens farming.** Experiment on the twin, not the crop.

Live demo: https://srimathisamynathan.github.io/MicroTwin-AI/

## Problem statement

Microgreens grow in only 7 to 10 days, so a small mistake in watering, humidity, light or airflow can spoil a whole batch. Small growers still depend on manual checks and fixed schedules. They usually notice a problem only after the crop is affected, and they cannot test a change without risking real plants.

**How can we create an AI-powered digital twin that predicts microgreen growth problems early and lets growers test decisions virtually before applying them to the real crop?**

## Solution

MicroTwin AI keeps a live digital copy of every microgreen tray. The grower tests changes to water, light, temperature and airflow on the copy first. The system predicts yield, resource use and mold risk for each option, recommends the best action, and applies it to the real farm only after the grower approves.

## Working process

1. **Sense:** sensors (temperature, humidity, light, moisture, water level) and a camera collect tray data.
2. **Collect:** an ESP32 or Raspberry Pi sends the data to a database.
3. **Analyze:** a growth model predicts yield and harvest day, computer vision measures canopy, and a risk model flags mold and stress.
4. **Mirror:** the digital twin updates live to match the real tray.
5. **Simulate:** the what-if engine compares actions on yield, water, energy and risk.
6. **Recommend:** the optimizer picks the best action.
7. **Approve:** the grower approves or rejects it.
8. **Act and learn:** approved actions run the fan, pump or light. Results and stem and root measurements recalibrate the twin.

## Features

- Live digital twin of a tray, real vs. twin values
- What-if simulator with five controls and four compared scenarios
- Crop selector: radish, mustard, sunflower, pea
- 24-hour live monitor with safe ranges, sensor health and alert center
- 9-day demo: manual tray vs. MicroTwin tray, with savings and a counterfactual replay
- Farm overview of all trays
- Plant growth records with stem and root analysis (three records)
- Growth curve, prediction accuracy panel and canopy photo analyzer
- Cost and profit calculator, harvest calendar, action log and CSV batch report
- Ask the twin: a chat that answers from the tray data
- Tamil and English toggle, dark and light theme, guided tour

## Tech stack

- Website: HTML, CSS and JavaScript in a single file, no build step
- Planned AI: XGBoost for yield prediction, OpenCV for vision
- Planned hardware: ESP32, DHT22, moisture, light and water-level sensors, camera, relay, pump, fan, LED grow light
- Planned dashboard backend: Streamlit or FastAPI

## Run the website

Open `index.html` in a browser, or use the Live Server extension in VS Code.

## Stem and root analysis

`analyze_growth.py` measures stem and root length from a side-on photo of seedlings.

```
pip install opencv-python numpy
python analyze_growth.py photo.jpg --cm-per-px 0.02 --seed-line-y 400 --day 6
```

Take the photo against a plain background with a 5 cm marker in the frame. Roots must be visible, and the color thresholds in the script may need tuning for your lighting.

## Project structure

```
MicroTwin-AI/
  index.html          website and simulator
  analyze_growth.py   stem and root measurement
  README.md
```

## Current status and limits

- Numbers on the website (sensor values, trends, farm trays, accuracy batches, growth records) are **sample data** until real measurements are connected.
- Growth records use placeholder values. Replace the `records` list in `index.html` with measured averages.
- Predictions need many growth cycles per crop to be reliable, and crops behave differently.
- Cheap sensors drift, so they need calibration.
- Image checks are early warnings, not diagnoses.

## Roadmap

- Now: two-tray prototype with sensors, camera and one yield model
- Next: connect real sensor data through a backend, calibrate the twin with more growth cycles
- Later: many trays and crops, phone alerts, approved automatic control

## Author

Built by Srimathi Samynathan.
