from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'USD 70,000'
    },
    {
        'id': 2,
        'title': 'Front-end Engineer',
        'location': 'Pleasant Grove, UT',
        'salary': 'USD 75,000'
    },
    {
        'id': 3,
        'title': 'Back-end Engineer',
        'location': 'Phoenix, AZ',
        'salary': 'USD 80,000'
    },
    {
        'id': 4,
        'title': 'Full-stack Engineer',
        'location': 'Portland, OR',
        'salary': 'USD 85,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)