from flask import Flask, request

app = Flask(__name__)

@app.route('/predict_price', methods = ['GET'])
def predict():
    args = request.args
    open_plan  =  args.get('open_plan', default = -1, type = int)
    rooms = args.get('rooms', default = -1, type = int)
    area  = args.get('area', default = -1, type = float)
    rennovation = args.get('rennovation', default = -1, type = int)

    response = "open plan {}, rooms:{}, area:{}, rennovation:{}".format(open_plan, rooms, area, rennovation)

    return response
if __name__ == '__main__':
    app.run(debug=True, port=5444, host='0.0.0.0')
