from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    # Add code to render the home page
    return render_template('animehtml.html')

# Example of serving static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
