# Lung Cancer Prediction Project

This project focuses on analyzing and predicting the risk levels of lung cancer using machine learning techniques. The dataset contains various features related to health, habits, and environmental factors.

## Project Overview

- **Goal**: To classify the lung cancer risk level (`Low`, `Medium`, `High`) using various classification algorithms.
- **Dataset Source**: The dataset was loaded from a CSV file stored in Google Drive.
- **Tools Used**: Python, Google Colab, Pandas, Seaborn, Matplotlib, Scikit-learn.

## Features of the Dataset

The dataset contains features such as:
- **Environmental factors**: Air Pollution, Occupational Hazards, etc.
- **Lifestyle factors**: Smoking, Alcohol use, Balanced Diet, etc.
- **Genetic and health risks**: Genetic Risk, Obesity, Chronic Lung Disease, etc.
- **Target Variable**: `Level` (Low, Medium, High)

## Data Analysis and Visualization

1. **Class Distribution**:
   - The target variable (`Level`) is well-balanced, with an almost equal distribution of classes.
   
2. **Heatmap of Features**:
   - Visualized correlations between health risk factors, showing significant relationships.

3. **Exploratory Plots**:
   - Histograms, count plots, and box plots were used to study feature distributions and relationships with the target variable.

## Data Preprocessing

- **Feature Engineering**:
  - Removed irrelevant columns like `index` and `Patient Id`.
  - Encoded the `Level` column into numerical values: 0 (Low), 1 (Medium), 2 (High).
  
- **Correlation Analysis**:
  - Calculated and visualized feature correlations to understand dependencies.

- **Mutual Information**:
  - Evaluated features using mutual information to capture linear and non-linear relationships.

- **Train-Test Split**:
  - Split the data into training (75%) and testing (25%) sets for model evaluation.

## Machine Learning Models

The following models were implemented and evaluated:

1. **K-Nearest Neighbors (KNN)**:
   - Achieved high accuracy on both training and testing datasets.
   
2. **Decision Tree Classifier**:
   - Showed strong training performance but lower testing accuracy due to overfitting.

3. **Random Forest Classifier**:
   - Achieved perfect scores in both training and testing, indicating excellent generalization.

4. **AdaBoost Classifier**:
   - Similar to Random Forest, performed exceptionally well with perfect metrics.

## Results

| Model                  | Training Accuracy | Testing Accuracy |
|------------------------|-------------------|------------------|
| KNN                   | High             | High            |
| Decision Tree          | High             | Medium          |
| Random Forest          | Perfect          | Perfect         |
| AdaBoost               | Perfect          | Perfect         |

## Confusion Matrices

Confusion matrices were plotted for all models to analyze predictions on both training and testing datasets.

## Conclusion

- **Best Performers**: Random Forest and AdaBoost classifiers achieved perfect scores, showcasing excellent generalization.
- **KNN Performance**: KNN was also a strong performer, generalizing the data extremely well.
- **Decision Tree Limitations**: The Decision Tree classifier overfitted the data, resulting in lower testing accuracy.

## Key Learnings

- The importance of balanced datasets in classification problems.
- The effectiveness of ensemble methods like Random Forest and AdaBoost for robust classification.
- The impact of overfitting in simpler models like Decision Trees.

# Write the content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)

print("README.md file created successfully.")
