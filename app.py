from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return """
    <h1>RAL to Net Calculator</h1>
    <p>The application is running.</p>
    """
