# Flood Hazard Risk Predictor

This project is a Streamlit web application for predicting flood hazard categories based on district-level flood indicators. It uses a machine learning model trained on real flood data from Uttar Pradesh, India.

## Features
- User-friendly web interface built with Streamlit
- Predicts flood hazard category using:
  - Flood Hazard Index
  - Inundated Area (Ha)
  - Flood Hazard (%)
- Displays sample data and prediction results

## Project Structure
```
├── app.py                      # Streamlit app
├── flood_hazard_predection (1).py  # Data processing and model training script
├── new_cleaned_flood_data.csv  # Cleaned dataset used for prediction
├── requirements.txt            # Python dependencies
├── flood_app/
│   └── flood_hazard_model.pkl  # Trained ML model
```

## Getting Started

### 1. Clone the repository
```
git clone https://github.com/yourusername/flood-hazard-prediction.git
cd flood-hazard-prediction
```

### 2. Install dependencies
It is recommended to use Anaconda:
```
conda install --file requirements.txt
```
Or use pip:
```
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```
streamlit run app.py
```

The app will be available at `http://localhost:8501`.

## Usage
- Adjust the sliders in the sidebar to set flood indicators.
- The app will predict and display the flood hazard category.
- Expand the sample data section to view example records.

## Model Training
The script `flood_hazard_predection (1).py` contains code for data cleaning, feature engineering, and model training. The trained model is saved as `flood_app/flood_hazard_model.pkl`.

## License
This project is for educational and research purposes only.

---

**Developed by [Your Name]**
