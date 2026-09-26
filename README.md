[README.md](https://github.com/user-attachments/files/32679323/README.md)
# ❤️ ViharaTech Heart Disease Prediction

A Machine Learning based **Heart Disease Prediction Web Application** developed using **Python, OOP concepts, Scikit-learn, Flask, HTML/CSS**, and deployed on **Render**.

The project takes seven patient-related input features — `age`, `sex`, `cp`, `thalach`, `oldpeak`, `slope`, and `thal` — and uses a trained machine learning model to predict the presence of heart disease.

---

## 📌 Project Overview

This project was developed as a complete end-to-end Machine Learning project.

The workflow starts with the **Heart Disease dataset**, followed by data understanding, null-value checking, data cleaning, feature preparation, feature selection, scaling, model training and evaluation. The final trained model and scaler are integrated into a **Flask web application**.

The complete project was developed in **PyCharm using Object-Oriented Programming (OOP) concepts**. The main workflow includes data cleaning, null-value checking, data balancing, feature processing, and scaling of values before model training. The completed project was uploaded to **GitHub** and deployed on **Render**.

---

## 🎯 Objectives

- Analyze the Heart Disease dataset.
- Check and handle missing/null values.
- Clean and preprocess the dataset.
- Select the required features.
- Scale numerical input values.
- Train and evaluate Machine Learning models.
- Save the trained model using Pickle.
- Build a Flask-based prediction application.
- Create a user-friendly web interface.
- Upload the complete project to GitHub.
- Deploy the application on Render.

---

## 🧠 Input Features

The application uses the following 7 input features:

| Feature | Description |
|---|---|
| `age` | Age of the patient |
| `sex` | Sex of the patient |
| `cp` | Chest pain type |
| `thalach` | Maximum heart rate achieved |
| `oldpeak` | ST depression value |
| `slope` | Slope of the peak exercise ST segment |
| `thal` | Thalassemia-related encoded value |

> The categorical values and numerical encoding used by the application should match the encoding used while training the model.

---

## 🔄 Project Workflow

```text
Heart Disease Dataset
        ↓
Data Loading
        ↓
Data Understanding
        ↓
Check Dataset Information
        ↓
Check Null Values
        ↓
Data Cleaning
        ↓
Data Preprocessing
        ↓
Check / Handle Null Values
        ↓
Data Cleaning
        ↓
Data Balancing
        ↓
Feature Selection
        ↓
Feature Transformation
        ↓
Scale Down / Feature Scaling
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Save Model (.pkl)
        ↓
Save Scaler (.pkl)
        ↓
Flask Application
        ↓
HTML User Interface
        ↓
GitHub
        ↓
Render Deployment
```

---

## 🧹 Data Preprocessing

The project performs the required preprocessing steps before model training.

### Steps include:

1. Load the Heart Disease dataset.
2. Inspect rows and columns.
3. Check data types.
4. Check null/missing values.
5. Clean the dataset where required.
6. Separate input features and target variable.
7. Balance the data to handle class imbalance.
8. Perform feature selection.
9. Apply feature transformation where required.
10. Scale down/standardize the feature values.
11. Use the processed data for Machine Learning model training.

The data balancing and scaling workflow is handled as part of the main project processing in `main.py`.

The trained scaler is saved as `scaled.pkl` and reused during prediction so that new user inputs are transformed consistently with the training data.

---

## ⚙️ Object-Oriented Programming

The project is organized using **OOP concepts** to make the Machine Learning workflow structured and reusable.

The project separates responsibilities such as:

- Data loading
- Data preprocessing
- Feature selection
- Model training
- Model evaluation
- Model saving/loading
- Prediction

This makes the project easier to maintain, debug, and extend.

---

## 🤖 Machine Learning

The project contains model-training and model-selection components.

The trained model is saved as:

```text
model.pkl
```

The scaler used for preprocessing is saved as:

```text
scaled.pkl
```

During prediction:

```text
User Input
    ↓
7 Features
    ↓
scaled.pkl
    ↓
Scaled Input
    ↓
model.pkl
    ↓
Prediction
```

---

## 🌐 Web Application

The web application is developed using **Flask**.

The user enters:

- Age
- Sex
- Chest Pain Type
- Maximum Heart Rate
- Oldpeak
- Slope
- Thal

The Flask application receives the input, applies the saved scaler, sends the transformed values to the trained model, and displays the prediction on the webpage.

---

## 🎨 User Interface

The frontend is created using:

- HTML5
- CSS3
- Responsive design
- Flask Jinja templates

The application includes:

- ViharaTech branding
- ViharaTech logo
- `Learn • Intern • Get Placed` tagline
- Heart Disease Prediction title
- Patient input form
- Prediction result section
- Project information section
- Developer credit

---

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── .venv/
│
├── logs/
│   ├── all_models.log
│   ├── fea_sel.log
│   ├── main.log
│   └── vt_yeo.log
│
├── static/
│   └── viharatech_logo.png
│
├── templates/
│   └── index.html
│
├── all_models.py
├── app.py
├── feature_selection.py
├── heart.csv
├── log.py
├── main.py
├── model.pkl
├── profile
├── requirements.txt
├── scaled.pkl
└── variable_transform.py
```

---

## 📄 Important Files

### `heart.csv`

Original Heart Disease dataset used for the project.

### `main.py`

Main Machine Learning workflow and project execution. It includes the overall data-processing pipeline, including data cleaning, data balancing, feature processing, and scaling of values before model training.

### `all_models.py`

Used for model training/comparison and model-related processing.

### `feature_selection.py`

Contains feature-selection related processing.

### `variable_transform.py`

Contains feature transformation/preprocessing operations.

### `model.pkl`

Saved trained Machine Learning model.

### `scaled.pkl`

Saved scaler generated from the training preprocessing pipeline. It is used to scale the seven user-input values before they are passed to the trained model.

### `app.py`

Flask backend responsible for:

- Loading the model.
- Loading the scaler.
- Receiving user input.
- Scaling input data.
- Generating predictions.
- Sending results to the HTML page.

### `templates/index.html`

Frontend interface for entering patient information and displaying the prediction.

### `static/viharatech_logo.png`

ViharaTech project logo used in the web application.

### `requirements.txt`

Contains the Python dependencies required to run the project.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| Pickle | Model and scaler serialization |
| Flask | Backend web framework |
| HTML5 | Frontend structure |
| CSS3 | Frontend design |
| PyCharm | Development environment |
| Git | Version control |
| GitHub | Source-code hosting |
| Render | Cloud deployment |

---

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

Open the project in **PyCharm** or VS Code.

### 3. Create/activate virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Flask

```bash
python app.py
```

### 6. Open the application

```text
http://127.0.0.1:5000/
```

---

## 🚀 GitHub Upload

The complete project is maintained in a GitHub repository.

Repository:

**YOUR_GITHUB_REPOSITORY_URL**

Replace the above placeholder with your actual GitHub repository URL.

---

## ☁️ Render Deployment

The Flask application is deployed on Render.

### Live Application

**RENDER_LIVE_LINK**

Replace `RENDER_LIVE_LINK` with your actual Render URL after deployment.

Example:

```text
https://your-heart-disease-project.onrender.com
```

---

## 📋 Render Deployment Steps

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

Make sure `gunicorn` is included in `requirements.txt`.

Example:

```text
Flask
numpy
pandas
scikit-learn
gunicorn
```

If your saved model was trained with a particular Scikit-learn version, use a compatible version in `requirements.txt` to avoid model-loading errors after deployment.

---

## 🔮 Prediction Process

During training, the data is cleaned, balanced, processed, and scaled. The resulting scaler is saved as `scaled.pkl`.

During prediction, the same preprocessing scale is applied to the seven user inputs.

```text
Training Dataset
       ↓
Data Cleaning
       ↓
Data Balancing
       ↓
Feature Processing
       ↓
Scale Down Values
       ↓
Model Training
       ↓
Save model.pkl
       ↓
Save scaled.pkl


User enters 7 values
       ↓
Flask receives input
       ↓
Convert input to numerical array
       ↓
Load scaled.pkl
       ↓
Scale input
       ↓
Load model.pkl
       ↓
Model prediction
       ↓
Display result
```

---

## 📊 Example Input

Example values:

```text
Age       : 55
Sex       : 1
CP        : 1
Thalach   : 150
Oldpeak   : 1.2
Slope     : 1
Thal      : 2
```

The values are passed through the saved scaler and then to the trained model.

---

## 👨‍💻 Developer

**👨‍💻 P. Venkata Siva Sai**

Heart Disease Prediction Project

**ViharaTech**

**Learn • Intern • Get Placed**

---

## ⚠️ Disclaimer

This project is developed for **educational, learning, and project demonstration purposes**. The prediction generated by this application should not be considered a medical diagnosis or a substitute for professional medical advice.

---

## ⭐ Acknowledgement

Developed as a Machine Learning project with **ViharaTech** using Python, OOP concepts, Scikit-learn, Flask, GitHub, and Render.

If you find this project useful, consider giving the repository a ⭐ on GitHub.
