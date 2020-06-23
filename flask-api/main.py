import random
import math
import copy
from flask import Flask, request
from flask_restful import Api, Resource
from flask import jsonify
from flask_restful.utils import cors
import json
from flask_cors import CORS

import pandas as pd
import neural_network
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

def to_dict(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))

lst = []

class Resultado():
    def __init__(self, res):
        self.res = res


class Prediccion(Resource):
    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def post(self):
        age = int(request.json['age'])
        sex = int(request.json['sex'])
        height = int(request.json['height'])
        weight = int(request.json['weight'])
        qrs_duration = int(request.json['qrs_duration'])
        pr_interval = int(request.json['pr_interval'])
        qt_interval = int(request.json['qt_interval'])
        t_interval = int(request.json['t_interval'])
        p_interval = int(request.json['p_interval'])
        qrs = int(request.json['qrs'])
        heart_rate = int(request.json['heart_rate'])
        q_wave = int(request.json['q_wave'])
        r_wave = int(request.json['r_wave'])
        s_wave = int(request.json['s_wave'])

        datos = []
        datos.append(age)
        datos.append(sex)
        datos.append(height)
        datos.append(weight)
        datos.append(qrs_duration)
        datos.append(pr_interval)
        datos.append(qt_interval)
        datos.append(t_interval)
        datos.append(p_interval)
        datos.append(qrs)
        datos.append(heart_rate)
        datos.append(q_wave)
        datos.append(r_wave)
        datos.append(s_wave)

        # leer archivos
        arch = pd.read_csv('dataset.csv', sep=';')
        # Columnas de dataset

        # quitar la columna diagnosis y qrs
        X = arch.drop(columns=['diagnosis'])

        # reemplazaremos el diagnostico con 0 y 1 (0 no esta enfermo, 1 esta enfermo)
        arch['diagnosis'] = arch['diagnosis'].replace(1, 0)
        arch['diagnosis'] = arch['diagnosis'].replace(2, 1)

        y_label = arch['diagnosis'].values.reshape(X.shape[0], 1)

        # estandarizar el dataset
        sc = StandardScaler()
        sc.fit(X)

        X = sc.transform(X)
        nn = neural_network.NeuralNet()
        nn.entrenar(X, y_label)

        test = []
        test.append(datos)

        # estandarizamos a la escala del dataset
        test_nn = sc.transform(test)

        pred = nn.predecir(test_nn)[0][0]

        resultado = Resultado(pred)

        lst.clear()

        lst.append(resultado)

        return jsonify(to_dict(resultado))

    @cors.crossdomain(origin='*',
                      methods={"HEAD", "OPTIONS", "GET", "POST"})
    def get(self):
        return jsonify(to_dict(lst))


api.add_resource(Prediccion, '/Prediccion')


if __name__ == '__main__':
    app.run(debug=True)