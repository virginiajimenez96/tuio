# Instructions to run each exercise

## Initial steps

1. Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```

2. Start jupyter:

```
jupyter notebook
```

## Exercise 1

1. Generate fake data

```
python3 exercise1/generate_data.py
```

It will generate four json files: claims.json, customers.json, policies.json and risk_indicators.json

2. Configure your PostgreSQL credentials in `config.json`.
3. Run data processing: ingestion, cleaning and storage.

```
python3 exercise1/data_processing.py
```

4. Read the report in `exercise1/etl.md`.

## Exercise 2

1. Go through `exercise2/eda.ipynb` and find comments in each of the sections.
2. Go through `exercise2/new_feautures.ipynb` adn find comments explaining each of the sections.

## Exercise 3

1. Go through `exercise3/exercise3.ipynb` and find the code and the steps.
2. Read the summary report in `exercise3/modelos.md`.

## Exercise 4

1. Go through `exercise4/external_data.ipynb` and find the code together with the report.

