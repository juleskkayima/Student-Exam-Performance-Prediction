# Student Exam Performance Prediction

## 📌 Problem Definition

Predicting student performance on exams is valuable for educators, parents, and students. Understanding the factors affecting student success can guide interventions and improve outcomes.

In this project, we treat it as a **machine learning regression problem**. Given student characteristics such as gender, ethnicity, parental education level, lunch type, test preparation course, and reading/writing scores, we aim to **predict the student’s mathematics score**.

This helps answer business questions like:

* Which student features most impact math performance?
* Can schools identify students at risk early?
* How do demographics and study habits correlate with success?


## 📊 Dataset

We use the Kaggle dataset:
**“Students Performance in Exams”** — [Kaggle link](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

### 🔍 About the Data

| Feature                       | Type        | Description                        |
| ----------------------------- | ----------- | ---------------------------------- |
| `gender`                      | Categorical | Male or Female                     |
| `race_ethnicity`              | Categorical | Ethnicity group (A–E)              |
| `parental_level_of_education` | Categorical | Parent’s education                 |
| `lunch`                       | Categorical | Type of lunch received             |
| `test_preparation_course`     | Categorical | Completed or not                   |
| `reading_score`               | Numerical   | Score in reading exam              |
| `writing_score`               | Numerical   | Score in writing exam              |
| `math_score`                  | Numerical   | Score in mathematics exam (target) |

**Data characteristics:**

* **Structured:** Tabular features.
* **Static:** Records collected at one point in time.
* **Supervised learning ready:** Inputs + target (`math_score`).


## 🧪 Evaluation

We measure model performance using:

* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **R² Score**

Goal: accurately predict math scores. A model with low error and high R² is considered good. For regression, accuracy is about prediction closeness, not a classification percentage.



## 🔎 Feature Analysis

We use all columns except `math_score` as features:

**Categorical:**

* Gender
* Race or ethnicity
* Parental level of education
* Lunch type
* Test preparation course

**Numerical:**

* Reading score
* Writing score

Categorical features are **one-hot encoded**. Numerical features are scaled as needed.


## 🤖 Modelling

Models explored:

* **Linear Regression**
* **Random Forest Regressor**
* **Gradient Boosting Regressor**
* **XGBoost Regressor**

**Modeling Steps:**

1. Train-test split
2. Preprocessing: One-hot encode categorical features, scale numerical features
3. Model training
4. Evaluation (MAE, MSE, R²)
5. Model selection based on validation performance

Tree-based models generally performed better than linear regression for this dataset.


## 🧪 Experimentation

Explored:

* Feature encoding strategies
* Model hyperparameters
* Different regression algorithms

**Next steps:**

* Cross-validation for robust performance estimation
* Hyperparameter tuning (GridSearchCV / Bayesian optimization)
* Feature importance and explainability (e.g., SHAP)
* Deep learning models (optional)


## 🚀 Deployment

The final model is deployed as:

* **Flask web app** — Users enter student details and see predicted math scores.

See `application.py` 


## 📁 Project Structure

```
📦 mlproject/
├── .ebextensions/           # AWS Elastic Beanstalk configuration
├── artifacts/               # Serialized model & preprocessor
│   ├── model.pkl
│   └── preprocessor.pkl
├── catboost_info/           # CatBoost metadata (optional)
├── notebook/                # Jupyter notebooks for exploration
├── src/                     # Source code
│   ├── pipeline/
│   │   ├── data_transformation.py
│   │   └── predict_pipeline.py
│   ├── exception.py
│   └── utils.py
├── templates/               # Flask HTML templates
│   └── index.html
├── application.py           # Flask app entry point
├── app_streamlit.py         # Streamlit app entry point
├── requirements.txt         # Dependencies
├── setup.py                 # Optional package setup
├── output.png               # Reference visualization or demo output
└── README.md
```


## 📌 How to Run

### 🐍 Flask App

```bash
pip install -r requirements.txt
python application.py
```

Open in browser:

```
http://127.0.0.1:5000/
```


## 👋 Credits & References

Dataset: [Kaggle — Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

ML concepts: scikit-learn and online resources
