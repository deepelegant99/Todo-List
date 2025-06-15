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
    return render_template("index.html", name=name)


@app.route("/hello")
def greet():
    name = request.args.get("name", "World")
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
