from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Muat model saat aplikasi dimulai
with open("scaler.pkl", "rb") as scaler_file:
    scaler_model = pickle.load(scaler_file)

with open("model.pkl", "rb") as model_file:
    prediction_model = pickle.load(model_file)

# =[Routing]=====================================
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/api/deteksi", methods=['POST'])
def apiDeteksi():
    if request.method == 'POST':
        # Ambil data dari formulir
        location = float(request.form.get('location'))
        cuisines = float(request.form.get('Cuisines'))
        minimum_order = float(request.form.get('minimum_order'))

        # Lakukan scaling pada input data
        input_data = [[location, cuisines, minimum_order]]
        scaled_data = scaler_model.transform(input_data)

        # Lakukan prediksi menggunakan model
        prediction = prediction_model.predict(scaled_data)

        # Tampilkan hasil prediksi
        return jsonify({
            'prediction': prediction[0]
        })

if __name__ == '__main__':
    app.run()
