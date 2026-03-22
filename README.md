# NBA Playoff Outcome Prediction using Linear Regression

A machine learning project that predicts NBA playoff outcomes based on historical team performance metrics. This project demonstrates the end-to-end implementation of a supervised regression model — from data preprocessing and exploratory analysis to model training and evaluation.

---

## 📖 Project Overview

This project leverages **Linear Regression** to analyze NBA team statistics and forecast the key factors that influence playoff success. By examining historical performance data, the model identifies which metrics most significantly impact a team's chances of advancing in the playoffs.

---

## 📂 Repository Structure

```
nba-playoff-prediction/
│
├── dataset/                        # Raw NBA team statistics dataset
│
├── notebooks/                      # Jupyter Notebooks for analysis and modeling
│   └── nba_playoff_prediction.ipynb
│
├── src/                            # Source scripts
│   ├── preprocessing.py            # Data cleaning and feature selection
│   ├── eda.py                      # Exploratory data analysis and visualizations
│   ├── train.py                    # Model training and evaluation
│
├── outputs/                        # Generated plots and result exports
│
├── README.md                       # Project overview and instructions
├── requirements.txt                # Python dependencies
└── .gitignore                      # Files excluded from version control
```

---

## 🔍 Dataset

The dataset contains NBA player and team statistics used to derive performance insights:

| Feature | Description |
|---------|-------------|
| `rank` | Player or team ranking |
| `player` | Player name |
| `position` | Playing position on the court |
| `total_games` | Total number of games played |
| `active_player` | Whether the player is currently active |
| `field_goals` | Number of field goals scored |
| `free_shots` | Number of free throws attempted/made |
| `three_point_goals` | Number of three-point goals scored |

---

## 🛠️ Technologies Used

| Category | Tools / Libraries |
|----------|-------------------|
| **Language** | Python 3.x |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn |

**Scikit-learn modules used:**
- `LinearRegression` — Core regression model
- `train_test_split` — Dataset splitting for training and testing
- `metrics` — Model performance evaluation

---

## 🚀 Implementation Steps

### 1. Data Preprocessing
- Handling missing and null values
- Feature selection based on correlation analysis
- Encoding categorical variables where required

### 2. Exploratory Data Analysis (EDA)
- Visualizing distributions of key features
- Identifying correlations between performance metrics and playoff outcomes
- Detecting and handling outliers

### 3. Model Training
- Splitting data into training and testing sets
- Fitting the **Linear Regression** model on training data
- Tuning feature selection for optimal performance

### 4. Model Evaluation
- Measuring model accuracy using **R² Score**
- Analyzing residuals and prediction error

---

## 📊 Results & Insights

- The model successfully identifies the key performance factors that influence playoff success
- Teams with higher values in the following metrics show a stronger likelihood of reaching and advancing in the playoffs:

| Metric | Impact on Playoff Success |
|--------|--------------------------|
| `field_goals` | High positive correlation |
| `free_shots` | Moderate positive correlation |
| `three_point_goals` | High positive correlation |

> These insights can assist coaching staff and analysts in prioritizing training focus areas for playoff preparation.

---

## 🏁 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/shreyaa-1702/nba-playoff-prediction.git
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook**
   ```bash
   jupyter notebook notebooks/nba_playoff_prediction.ipynb
   ```

---

## 📄 License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

---

## 🙋 Contributing

Contributions and suggestions are welcome. Feel free to open an issue or submit a pull request for any improvements or enhancements.
