from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app, title='Calculadora', version='1.0', description='API de calculadora', doc='/swagger')

operator_ns = api.namespace('/', description='Operadores disponiveis para calcular')

operator_model = operator_ns.model('BinaryOperator', {
    'a': fields.Fixed(decimals=3),
    'b': fields.Fixed(decimals=3)
})

@operator_ns.route('/')
@operator_ns.doc(description='Health check')
class HealthCheck(Resource):
        def get(self):
            return {'message': 'I am alive'}

@operator_ns.route('/soma')
@operator_ns.doc(description='Soma dois números')
class Soma(Resource):

    def post(self):
        a = api.payload['a']
        b = api.payload['b']
        return {'message': a + b}

@operator_ns.route('/multiplicacao')
@operator_ns.doc(description='Multiplica dois números')


    def post(self):
        a = api.payload['a']
        b = api.payload['b']
        return {'message': a * b}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
  
