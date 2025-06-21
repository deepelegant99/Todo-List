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
        print(f"GET request")
        return render_template("hello.html", name=request.args.get("name"), age=request.args.get("age"))
    else:
        # For POST requests 
        print(f"POST request")
        return render_template("hello.html", name=request.form.get("name"), age=request.form.get("age"))
    
   # return render_template("hello.html", name=name, age=age)

if __name__ == "__main__":
    app.run(debug=True)
