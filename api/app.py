from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
<h1>Sistema da Turma 3DSM</h1>
<p>oii</p>"""

app.run(host="0.0.0.0", port=5000)