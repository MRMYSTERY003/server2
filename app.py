from flask import Flask, request, jsonify
import requests
import ast




app = Flask(__name__)
i = 1


def vals(data = None, mode = 'read'):

    url = "https://sketchpy-95aa4-default-rtdb.firebaseio.com/keys.json"
    keys = requests.put(url,json=data).text
    print(keys)



def read():
    url = "https://sketchpy-95aa4-default-rtdb.firebaseio.com/keys.json"
    keys = requests.get(url).text
    result_list = ast.literal_eval(keys.replace(",null,", ""))
    return result_list
 

def write(data):
    url = "https://sketchpy-95aa4-default-rtdb.firebaseio.com/keys.json"
    res = read()

    data = {len(res) : data}
    res = requests.patch(url=url, json=data).text
    return res



def delete(data):
    url = f"https://sketchpy-95aa4-default-rtdb.firebaseio.com/keys.json"
    li = read()

    if data not in li:
        return -1
    li.pop(li.index(data))
    res = requests.put(url, json=li).text
    return res

@app.route("/", methods=["GET", "POST", "PUT"])
def home():
    return "ready to go!"


@app.route("/write", methods=["GET", "POST", "PUT"])
def write_data():
    try:
        val = int(request.args['val'])
        print(val)
        r = write(val)
        return r
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": f"Error: {str(e)}"})


@app.route("/read", methods=["GET", "POST", "PUT"])
def read_data():
    try:
        return read()
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": f"Error: {str(e)}"})



@app.route("/delete", methods=["GET", "POST", "PUT"])
def delete_data():
    try:
        val = int(request.args['val'])
        print(val)
        return delete(val)
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": f"Error: {str(e)}"})




if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0")
    app.run(debug=False, host="0.0.0.0")



# vals(data=[2,3,5,63,4])





