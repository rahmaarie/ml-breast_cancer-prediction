from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load Model
model = joblib.load('breast_cancer_model.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction_text=None, input_values={})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil data input dari form
        features = {f'feature{i+1}': request.form[f'feature{i+1}'] for i in range(29)}

        # Konversi input ke array numpy untuk prediksi
        final_features = np.array([float(v) for v in features.values()]).reshape(1, -1)

        # Prediksi
        prediction = model.predict(final_features)
        output = "Tumor Ganas" if prediction[0] == 1 else "Tumor Jinak"

        return render_template('index.html', prediction_text=f'Hasil Prediksi: {output}', input_values=features)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
