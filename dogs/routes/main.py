from flask import Blueprint, request, jsonify
# from ..database.dogs import dogs
from ..model.dogs import Dog
from ..database.db import db 
from werkzeug.exceptions import BadRequest

main_routes = Blueprint("main", __name__)

@main_routes.route("/dogs", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        dogs = Dog.query.all()
        print(dogs)
        outputs = map(lambda p: {"name": p.name, "age": p.age}, dogs)
        print(outputs)
        usable_outputs = list(outputs)
        print(usable_outputs)
        return jsonify(usable_outputs), 200
    elif request.method == "POST":
        pData = request.json
        print(pData)
        new_dog = Dog(name=pData["name"], age=pData["age"])
        print(new_dog)
        db.session.add(new_dog)
        db.session.commit()
        return jsonify(pData), 201

@main_routes.route('/dogs/<string:dog_name>', methods=["GET", "DELETE", "PATCH"])
def show(dog_name):
    if request.method == "GET":
        try:
            foundDog = Dog.query.filter_by(name=str(dog_name)).first()
            output = {"name": foundDog.name, "age": foundDog.age}
            return output, 302
        except:
            raise BadRequest(f"We do not have a dog with that name: {dog_name}")
    elif request.method == "DELETE":
        try:
            foundDog = Dog.query.filter_by(name=str(dog_name)).first()
            db.session.delete(foundDog)
            db.session.commit()
            return "deleted", 204
        except:
            raise BadRequest(f"failed to delete dog with that name: {dog_name}")
    elif request.method == "PATCH":
        try:
            foundDog = Dog.query.filter_by(name=str(dog_name)).first()
            db.session.update(foundDog)
            db.session.commit()
            return "dog updated", 200
        except:
            raise BadRequest(f"We're not able to edit this dog {dog_name}")
            
            
        #     pData = request.json
        # print(pData)
        # new_dog = Dog(name=pData["name"], age=pData["age"])
        # print(new_dog)
        # db.session.add(new_dog)
        # db.session.commit()
        # return jsonify(pData), 201

        #     dog = next(dog for dog in dogs if dog['id'] == dog_id)
        #     data = request.json
        #     print(data)
        #     for key, val in data.items():
        #         dog[key] = val
        #     return dog, 200

