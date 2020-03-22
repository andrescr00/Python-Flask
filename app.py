from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)
#lista de Prod
@app.route('/products', methods=['GET'])
def hello():
    return jsonify({"message": "Productos", "List":products})
#Buscando
@app.route('/products/<string:product_name>', methods=['GET'])
def get_Prod(product_name):
    Found = [p for p in products if p['name']==product_name]
    return jsonify({"Producto": Found[0]})
#Ingreso datos
@app.route('/products', methods=['POST'])
def add():
    addp = {
        "name": request.json['name'],
        "price":request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(addp)
    return jsonify({"message": "added", "New list": products})
@app.route('/products/<string:changeP>', methods=['PUT'])
def upd(changeP):
    Found = [prod for prod in products if prod['name']==changeP]
    if(len(Found)>0):
        Found[0]['name'] = request.json['name'],
        Found[0]['price'] = request.json['price'],
        Found[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "updated",
            "new list": products
        })

if __name__ == '__main__':
    app.run(debug=True)
