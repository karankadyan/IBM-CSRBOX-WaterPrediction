# IBM-CSRBOX-WaterPrediction
# Water Quality Prediction App

This Streamlit application predicts the quality of water based on various chemical and biological parameters. It uses a pre-trained deep learning model to classify water as either 'safe' or 'unsafe' for consumption.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Input Parameters](#input-parameters)
- [EDA Section](#eda-section)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/karankadyan/IBM-CSRBOX-WaterPrediction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd water-quality-prediction
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the necessary model and scaler files in the project directory:
    - `water_quality_model.h5`
    - `scaler.pkl`
    - `waterQuality1.csv`
2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Features

- **Water Quality Prediction:** Predicts if the water is safe or unsafe based on the given parameters.
- **Feature Distribution:** Visual representation of the input feature values.
- **Exploratory Data Analysis (EDA):** Provides an in-depth analysis of the dataset using pandas profiling.

## Description
All attributes are numeric variables and they are listed bellow:

- aluminium - dangerous if greater than 2.8

- ammonia - dangerous if greater than 32.5

- arsenic - dangerous if greater than 0.01

- barium - dangerous if greater than 2

- cadmium - dangerous if greater than 0.005

- chloramine - dangerous if greater than 4

- chromium - dangerous if greater than 0.1

- copper - dangerous if greater than 1.3

- flouride - dangerous if greater than 1.5

- bacteria - dangerous if greater than 0

- viruses - dangerous if greater than 0

- lead - dangerous if greater than 0.015

- nitrates - dangerous if greater than 10

- nitrites - dangerous if greater than 1

- mercury - dangerous if greater than 0.002

- perchlorate - dangerous if greater than 56

- radium - dangerous if greater than 5

- selenium - dangerous if greater than 0.5

- silver - dangerous if greater than 0.1

- uranium - dangerous if greater than 0.3

- is_safe - class attribute {0 - not safe, 1 - safe}

## Input Parameters

The following parameters can be adjusted using the sliders in the sidebar:

- Aluminium
- Ammonia
- Arsenic
- Barium
- Cadmium
- Chloramine
- Chromium
- Copper
- Flouride
- Bacteria
- Viruses
- Lead
- Nitrates
- Nitrites
- Mercury
- Perchlorate
- Radium
- Selenium
- Silver
- Uranium

## EDA Section

The EDA section provides a detailed analysis of the dataset used for training the model. It includes:
- Overview of the dataset
- Detailed statistics
- Distribution of features
- Correlation matrix
- And more...

## Model Details

- The model used for prediction is a deep learning model saved in the `water_quality_model.h5` file.
- The input features are scaled using the scaler saved in the `scaler.pkl` file.
- Model accuracy: **94.5%**

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
