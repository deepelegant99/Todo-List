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
    name = request.args.get("name", "World")
    age = request.args.get("age", 0)
    return render_template("index.html", name=name, age=age)


@app.route("/hello")
def greet():
    name = request.args.get("name", "World")
    age = request.args.get("age", 0)
    print(request.args)
    return f"Hello, {name}! You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True)
