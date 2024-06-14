from flask import Flask, request
import numpy
import joblib
MODEL_PATH ='/home/lapina/mlmodel/finalized_model.sav' 
app = Flask(__name__)

model = joblib.load(MODEL_PATH)
@app.route('/predict_price', methods = ['GET'])
def predict():
    args = request.args
    rooms = args.get('rooms', default = -1, type = int)
    area  = args.get('area', default = -1, type = float)
    rennovation = args.get('rennovation', default = -1, type = int)
    floor = args.get('floor', default = -1, type = int)
    x = numpy.array([rooms, area, rennovation, floor]).reshape(1,-1)

    result = model.predict(x)
    result = result.reshape(1,-1)
    return str(result[0][0])
if __name__ == '__main__':
    app.run(debug=True, port=7778, host='0.0.0.0')
