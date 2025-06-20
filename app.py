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
@app.route("/hello", methods=["POST"])
def greet():
    # name = request.args.get("name", "World")
    # age = request.args.get("age", 0)
    name = request.form.get("name", "World")
    age = request.form.get("age", 0)
    
    return render_template("hello.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
