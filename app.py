from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), "iris_model.pkl")
model = pickle.load(open(model_path, "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        sl = float(request.form["sl"])
        sw = float(request.form["sw"])
        pl = float(request.form["pl"])
        pw = float(request.form["pw"])

        prediction = model.predict([[sl, sw, pl, pw]])

        if prediction[0] == 0:
            result = "Setosa 🌼"
        elif prediction[0] == 1:
            result = "Versicolor 🌺"
        else:
            result = "Virginica 🌸"

    except:
        result = "Invalid Input ❌"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

# ===========================================================================================
# ===========================================================================================
# ===========================================================================================

# from flask import Flask, request, jsonify
# import pickle
# import os

# app = Flask(__name__)

# model_path = os.path.join(os.path.dirname(__file__), "iris_model.pkl")
# model = pickle.load(open(model_path, "rb"))

# @app.route("/")
# def home():
#     return "🌸 Iris ML API is running!"

# # 🔥 JSON API Endpoint
# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()

#     sl = float(data["sl"])
#     sw = float(data["sw"])
#     pl = float(data["pl"])
#     pw = float(data["pw"])

#     prediction = model.predict([[sl, sw, pl, pw]])

#     if prediction[0] == 0:
#         result = "Setosa 🌼"
#     elif prediction[0] == 1:
#         result = "Versicolor 🌺"
#     else:
#         result = "Virginica 🌸"

#     return jsonify({
#         "prediction": result
#     })

# if __name__ == "__main__":
#     app.run(debug=True)