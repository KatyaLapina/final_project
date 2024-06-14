## Machine Learning Model for Real Estate Listings
We have data from Yandex.Realty classified Yandex.Realty (https://realty.yandex.ru/) containing real estate listings for apartments in St. Petersburg and Leningrad Oblast from 2016 till the middle of August 2018. In this Lab, you'll learn how to apply machine learning algorithms to solve business problems. Accurate price prediction can help to find fraudsters automatically and help Yandex.Realty users make better decisions when buying and selling real estate.

The cleaned and prepared dataset contains the following features:

1. last_price
2. floor
3. rooms
4. area
5. renovation
6. year
7. month

## ML model
Decision Tree, Random Forest and XGboost were tested. As the best one XGboost was chosen.

## Metrics for final model
MAE: 7778.5174845588945

MSE: 234493011.7982312

RMSE: 15313.164656537565

MAPE: 0.22951383547115659

## Chosen Framework
Framework: xgboost
# Hyperparameters
n_estimators = 3000

learning_rate=0.02 

max_depth = 5 

## Installation and Running Instructions
To install and run the application in a virtual environment, follow these steps:

1. Download and install Visual Studio Code from the official website (https://code.visualstudio.com/).

2. Create and activate a virtual environment by running the following commands in your terminal:

 python3 -m venv env
 source env/bin/activate
3. Install the required libraries. The project uses several libraries, with a notable emphasis on the specific version of Scikit-learn. Install the dependencies using the following command:

 pip install -r requirements.txt
 
4. Run the application. Once the environment is set up and the dependencies are installed, you can run the Flask application using:

 python3 app.py
## Dockerfile information
A Dockerfile is available for supporting a containerized environment for the project. The Dockerfile includes the following parameters:

FROM ubuntu:22.04

MAINTAINER Ekaterina Lapina

RUN apt-get update -y

COPY . /opt/gsom_predictor

WORKDIR /opt/gsom_predictor

RUN apt install -y python3-pip

RUN pip3 install -r requirements.txt

CMD python3 app.py

## Port Configuration
The application uses port 7778. It can be changed in the last rows of the file.

## App via Docker
Use the following commands:

Run the Docker container:

sudo docker run —network host -d KatyaLapina/gsom_predictors:v.0.4
