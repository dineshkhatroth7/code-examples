from flask import Flask,jsonify

app=Flask(__name__)


users = [
    {"id":1,"name":"sara","age":26},
     {"id":2,"name":"sam","age":25},
      {"id":3,"name":"santa","age":23},
   
]

@app.route("/")
def get_users():
    return jsonify(users)

@app.route("/age",methods=["GET"])
def get_age():
    ages = [{ "age": user["age"]} for user in users]
    return jsonify(ages)

@app.route("/names",methods=["POST"])
def get_name():
    names = [{ "name": user["name"]} for user in users]
    return jsonify(names)


@app.route("/id_num",methods=["GET"])
def id_num():
    id_num=[{"id":user["id"]} for user in users]
    return jsonify(id_num)




if __name__ =="__main__":
    app.run(debug=True ,port=8000)
    
     