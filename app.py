import pandas as pd
import pickle
import os
import csv
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

model_path = 'model_mental_health.pkl'
history_file = 'riwayat_prediksi.csv'

# Load Model
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Error: File .pkl tidak ditemukan.")

mappings = {
    'Gender': {'Female': 0, 'Male': 1},
    'Country': {
        'Australia': 0, 'Belgium': 1, 'Bosnia and Herzegovina': 2, 'Brazil': 3, 
        'Canada': 4, 'Colombia': 5, 'Costa Rica': 6, 'Croatia': 7, 
        'Czech Republic': 8, 'Denmark': 9, 'Finland': 10, 'France': 11, 
        'Georgia': 12, 'Germany': 13, 'Greece': 14, 'India': 15, 
        'Ireland': 16, 'Israel': 17, 'Italy': 18, 'Mexico': 19, 
        'Moldova': 20, 'Netherlands': 21, 'New Zealand': 22, 'Nigeria': 23, 
        'Philippines': 24, 'Poland': 25, 'Portugal': 26, 'Russia': 27, 
        'Singapore': 28, 'South Africa': 29, 'Sweden': 30, 'Switzerland': 31, 
        'Thailand': 32, 'United Kingdom': 33, 'United States': 34
    },
    'Occupation': {'Business': 0, 'Corporate': 1, 'Housewife': 2, 'Others': 3, 'Student': 4},
    'self_employed': {'No': 0, 'Yes': 1},
    'family_history': {'No': 0, 'Yes': 1},
    'Days_Indoors': {
        '1-14 days': 0, '15-30 days': 1, '31-60 days': 2, 
        'Go out Every day': 3, 'More than 2 months': 4
    },
    'Growing_Stress': {'Maybe': 0, 'No': 1, 'Yes': 2},
    'Changes_Habits': {'Maybe': 0, 'No': 1, 'Yes': 2},
    'Mental_Health_History': {'Maybe': 0, 'No': 1, 'Yes': 2},
    'Mood_Swings': {'High': 0, 'Low': 1, 'Medium': 2},
    'Coping_Struggles': {'No': 0, 'Yes': 1},
    'Work_Interest': {'Maybe': 0, 'No': 1, 'Yes': 2},
    'Social_Weakness': {'Maybe': 0, 'No': 1, 'Yes': 2},
    'mental_health_interview': {'Maybe': 0, 'No': 1, 'Yes': 2},
    'care_options': {'No': 0, 'Not sure': 1, 'Yes': 2}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard_view.html')

@app.route('/predict', methods=['GET'])
def predict_form():
    return render_template('predict.html')

@app.route('/predict_process', methods=['POST'])
def predict_process():
    if request.method == 'POST':
        try:
            form_data = request.form.to_dict()
            
            input_encoded = {}
            for col, mapping_dict in mappings.items():
                user_input = form_data.get(col)
                input_encoded[col] = mapping_dict.get(user_input, 0)
            
            cols_order = [
                'Gender', 'Country', 'Occupation', 'self_employed', 'family_history',
                'Days_Indoors', 'Growing_Stress', 'Changes_Habits', 'Mental_Health_History',
                'Mood_Swings', 'Coping_Struggles', 'Work_Interest', 'Social_Weakness',
                'mental_health_interview', 'care_options'
            ]
            
            data_values = [[input_encoded[col] for col in cols_order]]
            df_input = pd.DataFrame(data_values, columns=cols_order)
            
            prediction = model.predict(df_input)[0]
            
            if prediction == 1:
                result_text = "Disarankan Mencari Perawatan (YES)"
                result_class = "danger" # Untuk styling merah
            else:
                result_text = "Kondisi Mental Stabil (NO)"
                result_class = "success" # Untuk styling hijau
            
            if not os.path.exists(history_file):
                with open(history_file, mode='w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Timestamp'] + cols_order + ['Prediction'])
            
            with open(history_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                row_to_write = [datetime.now()] + data_values[0] + [result_text]
                writer.writerow(row_to_write)

            return render_template('predict_view.html', 
                                   result=result_text, 
                                   result_class=result_class,
                                   data=form_data)
                                   
        except Exception as e:
            return f"Terjadi Kesalahan: {e}"

if __name__ == "__main__":
    app.run(debug=True)