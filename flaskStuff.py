from flask import Flask
app = Flask(__name__)

@app.route("goLeft")
def _():
    return "Done L"

@app.route("goRight")
def _():
    return "Done R"

if __name__ == "__main__":
    app.run()









