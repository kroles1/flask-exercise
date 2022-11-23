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
        outputs = map(lambda p: {"name": p.name, "age": p.age, "id": p.id}, dogs)
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

# @main_routes.route('/dogs/<string:dog_name>', methods=["GET", "DELETE", "PATCH"])
# def show(dog_name, dog):
#     if request.method == "GET":
#         try:
#             foundDog = Dog.query.filter_by(name=str(dog_name)).first()
#             output = {"name": foundDog.name, "age": foundDog.age}
#             return output, 302
#         except:
#             raise BadRequest(f"We do not have a dog with that name: {dog_name}")
#     elif request.method == "DELETE":
#         try:
#             foundDog = Dog.query.filter_by(name=str(dog_name)).first()
#             db.session.delete(foundDog)
#             db.session.commit()
#             return "deleted", 204
#         except:
#             raise BadRequest(f"failed to delete dog with that name: {dog_name}")
    # elif request.method == "PATCH":
    #     try:
    #         db.session.query(Dog).filter(Dog.dog_name == dog_name).update(request.json)
    #         db.session.commit()
    #         return request.json, 200
    #     except:
    #         raise BadRequest(f"We're not able to edit this dog {dog_name}")
            
            
@main_routes.route('/dogs/<int:dog_id>', methods=["GET", "DELETE", "PATCH"])
def show(dog_id):
    if request.method == "GET":
        try:
            foundDog = Dog.query.filter_by(id=int(dog_id)).first()
            output = {"name": foundDog.name, "age": foundDog.age, "id": foundDog.id}
            return output, 302
        except:
            raise BadRequest(f"We do not have a dog with that id: {dog_id}")
    elif request.method == "DELETE":
        try:
            foundDog = Dog.query.filter_by(id=int(dog_id)).first()
            db.session.delete(foundDog)
            db.session.commit()
            return "deleted", 204
        except:
            raise BadRequest(f"failed to delete dog with that name: {dog_id}")
    elif request.method == "PATCH":
        try:
            foundDog = Dog.query.filter_by(id=int(dog_id)).first()
            if request.json.get("name") != None:
                foundDog.name = request.json["name"]
            if request.json.get("age") != None:
                foundDog.age = request.json["age"]
            db.session.commit()
            return "updated", 200
        except:
            raise BadRequest(f"We're not able to edit this dog {dog_id}")
