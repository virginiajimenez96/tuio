# Instructions to run each exercise

1. Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```

## Exercise 1

1. Generate fake data

```
python3 exercise1/generate_data.py
```

It will generate four json files: claims.json, customers.json, policies.json and risk_indicators.json

2. Configure your PostgreSQL credentials in config.json
3. Run data processing: ingestion, cleaning and storage.

````
python3 exercise1/data_processing.py
```

TODO: ADD RESULTS!
TODO: ADD REPORT!