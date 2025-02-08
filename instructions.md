# Technical Test

## **General Context**
You are a **Data Scientist Engineer** at an insurance company. Your mission is to develop a robust data pipeline and build predictive models that extract insights from customer and claims data to optimize risk assessment and pricing strategies.

This test is structured into four key exercises that evaluate your **data engineering skills, machine learning capabilities, and problem-solving mindset**.

---

## **Exercise 1: Data Pipeline & Processing (2 hours)**

### **Scenario:**
Your company collects data from multiple sources, including customer policies, claims history, and third-party risk indicators. The data arrives in JSON format via an API and needs to be processed into a structured format for analytics and modeling.

### **Goal:**
- Develop an **ETL pipeline** to ingest, clean, and store insurance-related data.
- Implement **data validation** and handle common data quality issues.
- Store the cleaned data in a **PostgreSQL or BigQuery** database.

### **Tasks:**
1. **Data Ingestion:** Write a Python script that fetches JSON data from a simulated API (or generate synthetic data for this step).
2. **Data Cleaning & Transformation:**
   - Handle missing or inconsistent values.
   - Standardize categorical fields (e.g., policy types, customer demographics).
   - Convert timestamps into a standardized format.
3. **Storage:** Load the processed data into PostgreSQL (or BigQuery if you prefer working with cloud storage).
4. **Data Quality Report:** Produce a summary of key data issues and how they were addressed.

### **Deliverables:**
- Python code implementing the pipeline.
- SQL schema for data storage.
- Brief documentation explaining your approach.

---

## **Exercise 2: Feature Engineering & Exploratory Data Analysis (EDA) (1.5 hours)**

### **Scenario:**
Your company wants to improve claim risk assessment. You need to analyze customer data and claims history to identify useful **features** for predictive modeling.

### **Goal:**
- Perform **exploratory data analysis (EDA)** on the processed dataset.
- Engineer **at least three new features** that could help predict claim probability.
- Visualize key insights using **Python (Matplotlib, Seaborn, or Plotly).**

### **Tasks:**
1. **Feature Engineering:** Create new variables that might be relevant, such as:
   - Customer risk score based on past claims.
   - Average claim amount per customer.
   - Time since last claim.
2. **EDA & Visualization:**
   - Plot the distribution of key variables.
   - Analyze correlations between features and claim occurrence.
   - Identify potential biases or anomalies in the data.

### **Deliverables:**
- Jupyter Notebook or Python script with EDA.
- At least three visualizations with explanations.
- A written summary of key insights and feature relevance.

---

## **Exercise 3: Predictive Modeling (1.5 hours)**

### **Scenario:**
Using the engineered dataset, you need to build a **classification model** to predict the likelihood of a customer filing a claim in the next 12 months.

### **Goal:**
- Train and evaluate a **machine learning model** for claim prediction.
- Optimize model performance using appropriate evaluation metrics.
- Compare at least **two different algorithms**.

### **Tasks:**
1. **Data Preparation:**
   - Split data into training and test sets.
   - Normalize numerical features and encode categorical variables.
2. **Model Training & Evaluation:**
   - Train two classification models (e.g., Logistic Regression, Random Forest, XGBoost, or Neural Network).
   - Evaluate performance using precision, recall, F1-score, and ROC-AUC.
3. **Hyperparameter Tuning:** Use **GridSearchCV or another tuning approach** to improve model performance.

### **Deliverables:**
- Python code for training and evaluating models.
- Comparison table of model performance.
- A brief discussion on which model you would recommend and why.

---

## **Exercise 4: External Data Integration & Business Recommendations (1 hour)**

### **Scenario:**
Your team believes that integrating **external data** (e.g., weather conditions, crime rates, economic indicators) could enhance claim prediction accuracy.

### **Goal:**
- Identify a relevant **external dataset** that could improve the model.
- Develop a Python script to fetch and integrate this data.
- Explain how this data could be used to improve risk assessment.

### **Tasks:**
1. **Data Identification:** Select an external data source and justify its relevance (e.g., crime rate API, historical weather data, financial indicators).
2. **Data Acquisition & Integration:**
   - Write a script to retrieve and merge this data with existing datasets.
   - Handle potential data mismatches and missing values.
3. **Business Impact Analysis:**
   - Explain how this additional data could enhance claim risk predictions.
   - Suggest two practical ways this data could be leveraged in marketing or risk mitigation strategies.

### **Deliverables:**
- Python script for external data retrieval.
- Explanation of how the data is integrated and its value.
- A short business proposal on how this data benefits insurance pricing or fraud detection.

---