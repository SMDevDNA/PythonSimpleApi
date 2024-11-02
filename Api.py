from flask import Flask, jsonify, request

app = Flask(__name__)

items = {
    "apple": "A fresh red apple",
    "banana": "A ripe yellow banana",
    "orange": "A juicy orange",
    "grapes": "A bunch of green grapes"
}


@app.route('/items/<string:name>', methods=['GET'])
def get_item(name):
    item = items.get(name)
    if item is not None:
        return jsonify({name: item}), 200
    else:
        return jsonify({'error': 'No item'}), 404

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    name = data.get('name')
    value = data.get('value')

    if name in items:
        return jsonify({'error': 'Item already exists'}), 400

    items[name] = value
    return jsonify({name: value}), 201

@app.route('/items/<string:name>', methods=['DELETE'])
def delete_item(name):
    if name in items:
        del items[name]
        return jsonify({'message': 'Deleted'}), 200
    else:
        return jsonify({'error': 'No item'}), 404

if __name__ == '__main__':
    app.run(debug=True)