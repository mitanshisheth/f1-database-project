# 🏎️ Formula 1 Data Analytics Pipeline (1950–2024)

## 📌 Overview
This project builds an end-to-end data analytics pipeline on a real-world Formula 1 dataset (1950–2024) sourced from Kaggle.  
It covers data ingestion, cleaning, transformation, relational database design, and exploratory data analysis (EDA) to extract meaningful racing insights.

---

## 🚀 Key Features
- Built a complete **ETL pipeline** using Python (Pandas) and MySQL  
- Cleaned and transformed raw CSV data (handled `\N`, inconsistent formats, missing values)  
- Designed a **normalized relational database schema** with multiple linked tables  
- Performed **feature engineering** (e.g., age calculation, lap time conversion to milliseconds)  
- Conducted **EDA and visualization** to analyze driver and team performance  

---

## 🛠️ Tech Stack
- **Python**: Pandas, NumPy  
- **Database**: MySQL  
- **Visualization**: Matplotlib, Seaborn  
- **Tools**: Jupyter Notebook  

---

## 📂 Dataset
- Source: Kaggle (Formula 1 World Championship Dataset, 1950–2024)  
- Contains data on:
  - Drivers  
  - Constructors (Teams)  
  - Races  
  - Results  
  - Lap Times  
  - Pit Stops  
  - Qualifying Sessions  

---

## ⚙️ Pipeline Workflow

### 1️⃣ Data Ingestion
- Loaded raw CSV files using Pandas  
- Automated pipeline for multiple tables  

### 2️⃣ Data Cleaning
- Converted `\N` → NULL values  
- Fixed inconsistent date formats  
- Converted string-based time fields into numeric (milliseconds)  
- Removed redundant columns  

### 3️⃣ Feature Engineering
- Created `name` column from first and last names  
- Derived `age` from date of birth  
- Converted qualifying times (`q1`, `q2`, `q3`) to milliseconds  

### 4️⃣ Database Design
- Designed normalized schema with relationships:
  - `drivers`, `constructors`, `races`, `results`, etc.  
- Implemented:
  - Primary Keys  
  - Foreign Keys  
- Ensured referential integrity

## Exploratory Data Ananlysis
-- under process 

## 🧠 Key Learnings
-under process
---
## 👨‍💻 Author
Mitanshi Sheth  
Electronics & Communication Engineering (ECE) Student  
Aspiring Data Science & ML Engineer
