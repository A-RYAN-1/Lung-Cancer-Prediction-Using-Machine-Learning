Lung Cancer Risk Predictor
==========================

This project is a web application that predicts the risk of lung cancer (Low, Medium, or High) based on user-provided health and environmental factors. It uses a machine learning model built with scikit-learn and a Flask-based web interface styled with Tailwind CSS for a modern, user-friendly experience.

Features
--------

*   **User-Friendly Interface**: Input health and environmental factors via a simple form with Yes/No radio buttons for most fields.
    
*   **Machine Learning Model**: Logistic Regression model trained on a dataset to predict lung cancer risk.
    
*   **Responsive Design**: Styled with Tailwind CSS for a clean, modern, and responsive UI.
    
*   **Scalable Backend**: Flask server handles predictions and serves the web interface.
    
*   **Data Preprocessing**: Includes scaling and oversampling to handle imbalanced datasets.
    

Prerequisites
-------------

*   Python 3.8+
    
*   pip (Python package manager)
    
*   Git (for cloning the repository)
    

Installation
------------

1.  git clone 
    
2.  python -m venv venvsource venv/bin/activate <br>
    On Windows: venv\\Scripts\\activate
    
4.  pip install -r requirements.txt <br>
    Ensure you have a requirements.txt file with the following:
    flask==2.0.1numpy==1.21.0pandas==1.3.0scikit-learn==0.24.2imblearn==0.8.0joblib==1.0.1
    
5.  **Prepare the Dataset**:
    
    *   Place the cancer\_data.csv file in the project root directory. This file should contain the dataset with columns like Age, Gender, Air Pollution, etc., and a Level column for risk labels (Low, Medium, High).
        
6.  **Train the Model** (if not using pre-trained models):
    
    *   python train\_and\_save\_model.py
        

Usage
-----

1.  python app.pyThis starts the Flask server in debug mode, typically accessible at http://127.0.0.1:5000.
    
2.  **Access the Web Interface**:
    
    *   Open a web browser and navigate to http://127.0.0.1:5000.
        
    *   Fill out the form with your details:
        
        *   **Age**: Enter your age (numeric).
            
        *   **Gender**: Select Male (1) or Female (2).
            
        *   Other fields (e.g., Air Pollution, Smoking): Select "Yes" (1) or "No" (0) via radio buttons.
            
    *   Click the "Predict" button to see the predicted lung cancer risk (Low, Medium, or High).
        
3.  **View Results**:
    
    *   The prediction will appear below the form, indicating the risk level.
        
How It Works
------------

*   **Frontend**: The index.html file provides a form where users input their data. Most fields use Yes/No radio buttons (mapped to 1/0) for simplicity, except for Age (numeric) and Gender (1 for Male, 2 for Female). Tailwind CSS ensures a responsive and modern design.
    
*   **Backend**: The Flask app (app.py) loads the pre-trained model and scaler, processes form inputs, scales the data, and predicts the risk level using the Logistic Regression model.
    
*   **Model Training**: The train\_and\_save\_model.py script loads the dataset, preprocesses it (encoding Gender, scaling features, balancing classes with RandomOverSampler), trains a Logistic Regression model, and saves the model and scaler as pickle files.
  
Contributing
------------

Contributions are welcome! Please:

1.  Fork the repository.
    
2.  Create a feature branch (git checkout -b feature/your-feature).
    
3.  Commit your changes (git commit -m 'Add your feature').
    
4.  Push to the branch (git push origin feature/your-feature).
    
5.  Open a pull request.
    
