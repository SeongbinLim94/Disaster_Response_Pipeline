# Disasters Response Projects
This project is to create disasters response pipeline for Udacity D.S course project.

## Contents
This repository contains three folders.

1. **Data**   
In `data` folder, two csv files which store raw data of messages and categories are contained. These files are processed with ETL pipeline, which can be excecuted by `process_data.py` file.

2. **Models**   
In `models` folder, a python script, `train_classifier.py`, is contained. This python script executes ML pipeline that holds CountVectorizer, TF-IDF models and Random Forest classifier.

3. **App**   
In `app` folder, `run.py` python script is contained. This script runs web app to deploy the results of two pipelines above.

## Instruction
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database   
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves   
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.   
    `python run.py`

3. Go to http://0.0.0.0:3001/

## Acknowledgements
The `run.py` python file is scripted based on templates provided by Udacity.
