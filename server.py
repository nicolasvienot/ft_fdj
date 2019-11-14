import threading
import time
from flask import render_template
from flask import Flask
import connexion

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')

def home():
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
