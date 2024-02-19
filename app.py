from flask import Flask, request, jsonify
import requests
import ast
import os


URL = os.environ.get('URL')



app = Flask(__name__)
i = 1




def read():
    url =URL
    keys = requests.get(url).text
    result_list = ast.literal_eval(keys.replace(",null,", ""))
    return result_list
 

def write(data):
    url =URL
    res = read()

    data = {len(res) : data}
    res = requests.patch(url=url, json=data).text
    return res



def delete(data):
    url = URL
    li = read()

    if data not in li:
        return -1
    li.pop(li.index(data))
    res = requests.put(url, json=li).text
    return res

@app.route("/", methods=["GET", "POST", "PUT"])
def home():
    return "ready to go!"


@app.route("/write0", methods=["GET", "POST", "PUT"])
def write_data():
    try:
        val = int(request.args['val'])
        print(val)
        r = write(val)
        return r
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": f"Error: {str(e)}"})


@app.route("/read0", methods=["GET", "POST", "PUT"])
def read_data():
    try:
        return read()
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": f"Error: {str(e)}"})



@app.route("/delete0", methods=["GET", "POST", "PUT"])
def delete_data():
    try:
        val = int(request.args['val'])
        print(val)
        return delete(val)
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": f"Error: {str(e)}"})

@app.route("/check", methods=["GET", "POST", "PUT"])
def check():
    try:
        val = int(request.args['val'])
        print(val)
        keys = read()
        if val in keys:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": f"Error: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    # app.run(debug=False, host="0.0.0.0")






