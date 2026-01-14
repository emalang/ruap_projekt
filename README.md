# 🍄 Can I Eat This Mushroom?
 
Web application for classifying mushrooms as **edible** or **poisonous** based on their physical characteristics, using a **machine learning model deployed on Azure**.
 
The goal of this project is to demonstrate an **end-to-end ML system**, from data analysis and model training to deployment and user-facing web application.
 
---
 
## Project Overview
 
This application allows users to enter key observable features of a mushroom (such as odor, cap color, gill color, etc.) and receive a prediction on whether the mushroom is safe to eat.
 
The system consists of:
- a **machine learning model** trained on the Mushroom Classification dataset
- a **REST API endpoint** deployed using Azure Machine Learning
- a **Django web application** that communicates with the deployed model
 
---
 
## Dataset
 
- **Source:** UCI / Kaggle – Mushroom Classification Dataset  
- **Samples:** 8124  
- **Features:** 22 categorical attributes  
- **Target:**  
  - `e` – edible  
  - `p` – poisonous  
 
For usability reasons, the web interface focuses on the **8 most informative features**.
 
---
 
## Machine Learning Model
 
- **Algorithm:** Logistic Regression  
- **Preprocessing:** One-Hot Encoding
- **Accuracy:** ~99% on test data  
- **Deployment:** Azure Machine Learning – Managed Online Endpoint  
 
---
 
## Web Application
 
- **Framework:** Django (Python)
- **Frontend:** HTML + CSS (minimal, user-friendly design)

---
 
## Instructions
<ol>
  <li>Install <a href="https://docs.djangoproject.com/en/5.0/howto/windows/#install-python">Python</a></li>
  <li>Clone this repository</li>
  <li>In git bash, go to project repository:</li>
 
  ```
  cd backend/
  ```
 
  <li>Then, copy the following line:</li>
 
  ```
  python -m venv env
  ```
 
  <li>When that is done, copy this:</li>
 
  ```
  source env/Scripts/activate
  ```
 
  <li>Then, install required tools:</li>
 
  ```
  pip install -r requirements.txt
  ```
  
  <li>And finally, run the solution:</li>
 
  ```
  winpty python manage.py runserver
  ```
 
  <li>You can now see it in your browser:</li>
 
  ```
  localhost:8000
  ```
 
</ol>
