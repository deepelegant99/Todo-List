from flask import Flask, render_template, request   


app = Flask(__name__)

@app.route("/")
def home():
    # name = request.args["name"]

    # A better version of the above code:
    # if "name" in request.args:
    #     name = request.args["name"]
    # else:
    #     name = "World"
    # The best version of the above code:

    # The / route should render index.html
    return render_template("index.html")

# @app.route("/hello", methods=["GET"])
@app.route("/hello", methods=["GET","POST"])
def greet():

    if request.method == "GET":
        # For GET requests, we can use request.args
        name = request.args.get("name", "World")
        age = request.args.get("age", 0)
        print(f"GET request: name={name}, age={age}")
    else:
        # For POST requests, we can use request.form
        name = request.form.get("name", "World")
        age = request.form.get("age", 0)
        print(f"POST request: name={name}, age={age}")
    
    return render_template("hello.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
