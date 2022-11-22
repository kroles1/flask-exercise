from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import NotFound, InternalServerError, BadRequest

app = Flask(__name__)
CORS(app)

dogs = [
    {'id': 1, 'name': 'Doggo', 'age': 6},
    {'id': 2, 'name': 'Dolores', 'age': 2},
    {'id': 3, 'name': 'Darren', 'age': 1}
]

@app.route("/")
def hello_world():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route("/dogs", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify(dogs)
    elif request.method == "POST":
        data = request.json
        last_id = dogs[-1]['id']
        data['id'] = last_id + 1
        dogs.append(data)
        print(data)
        return f"{data['name']} was added to dogs", 201

@app.route('/dogs/<int:dog_id>', methods=["GET", "DELETE", "PATCH"])
def show(dog_id):
    try:
        if request.method == "GET":
            return next(dog for dog in dogs if dog['id'] == dog_id), 302
        elif request.method == "DELETE":
            dog = next(dog for dog in dogs if dog['id'] == dog_id)
            dogs.remove(dog)
            return dogs, 204
        elif request.method == "PATCH":
            dog = next(dog for dog in dogs if dog['id'] == dog_id)
            data = request.json
            print(data)
            for key, val in data.items():
                dog[key] = val
            return dog, 200
    except:
        raise BadRequest(f"We don't have that dog in dogs")

@app.errorhandler(NotFound)
def handle_404(err):
    return jsonify({"message": f'Not found {err}'}), 404

@app.errorhandler(InternalServerError)
def handle_500(err):
    return jsonify({"message" f"It's not you, it's me"}), 500

if __name__ == "__main__":
    app.run()
