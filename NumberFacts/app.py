from flask import Flask, render_template, url_for, request, math
app = Flask(__name__)

@app.route("/")
def number_form():
    return render_template("NumberForm.html")

@app.route("/NumberFormRedirect")
def handle_number_form():
    submittedNumberInput = request.args.get("number_input", 100)
    render_dictionary = {
        "number" : submittedNumberInput
        "isInt" : isinstance(submittedNumberInput, int)
        "isPerfectSquare" : (math.sqrt(submittedNumberInput) % 1 == 0)
        "squareRoot" : (math.sqrt(submittedNumberInput))
        "square" : submittedNumberInput ** 2
        "isEven" : (int(submittedNumberInput) % 2 == 0)
        "numberPlus1" : submittedNumberInput + 1
        "numberMinus1" : submittedNumberInput - 1
    }

    return render_template("NumberFacts.html", num = number)