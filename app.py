from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Add the custom filter to remove the 'answer' key and convert to JSON
def remove_answer_key(value):
    new_dict = {k: v for k, v in value.items() if k != 'answer'}
    return json.dumps(new_dict)

app.jinja_env.filters['remove_answer_key'] = remove_answer_key

QUESTIONS = [
    {
    'id': 1,
    'question': 'What type of lighting conditions does your space have?',
    'answers': [{
        'answer': 'Bright, direct sunlight',
        'zzplant': 2,
        'snake': 4,
        'croton': 5,
        'areca': 5,
        'string': 3
    },{
        'answer': 'Bright, indirect sunlight',
        'zzplant': 4,
        'snake': 5,
        'croton': 4,
        'areca': 4,
        'string': 4
    },{
        'answer': 'Partial shade or filtered light',
        'zzplant': 3,
        'snake': 3,
        'croton': 2,
        'areca': 2,
        'string': 5
    },{
        'answer': 'Low light or artificial light',
        'zzplant': 5,
        'snake': 3,
        'croton': 2,
        'areca': 2,
        'string': 5
    }]
    },
    {
    'id': 2,
    'question': 'How often would you like to water your houseplants?',
    'answers': [{
        'answer': 'Daily or every other day',
        'zzplant': 1,
        'snake': 1,
        'croton': 3,
        'areca': 5,
        'string': 1
    },{
        'answer': 'Once or twice a week',
        'zzplant': 2,
        'snake': 3,
        'croton': 5,
        'areca': 4,
        'string': 2
    },{
        'answer': 'Once every two weeks',
        'zzplant': 4,
        'snake': 5,
        'croton': 2,
        'areca': 2,
        'string': 4
    },{
        'answer': 'Once a month or less',
        'zzplant': 5,
        'snake': 4,
        'croton': 1,
        'areca': 1,
        'string': 3
    }]
    },
    {
    'id': 3,
    'question': 'How much space do you have for your houseplant?',
    'answers': [{
        'answer': 'A large area or floor space',
        'zzplant': 3,
        'snake': 4,
        'croton': 3,
        'areca': 5,
        'string': 1
    },{
        'answer': 'A medium-sized shelf or tabletop',
        'zzplant': 5,
        'snake': 5,
        'croton': 5,
        'areca': 3,
        'string': 2
    },{
        'answer': 'A small shelf or windowsill',
        'zzplant': 4,
        'snake': 3,
        'croton': 4,
        'areca': 1,
        'string': 4
    },{
        'answer': 'Minimal space or a hanging pot',
        'zzplant': 2,
        'snake': 2,
        'croton': 1,
        'areca': 1,
        'string': 5
    }]
    },
    {
    'id': 4,
    'question': 'What kind of foliage are you attracted to?',
    'answers': [{
        'answer': 'Large, dramatic leaves',
        'zzplant': 1,
        'snake': 2,
        'croton': 4,
        'areca': 5,
        'string': 1
    },{
        'answer': 'Colorful or variegated leaves',
        'zzplant': 2,
        'snake': 1,
        'croton': 5,
        'areca': 3,
        'string': 2
    },{
        'answer': 'Small, delicate leaves or vines',
        'zzplant': 1,
        'snake': 2,
        'croton': 3,
        'areca': 4,
        'string': 5
    },{
        'answer': 'Unusual or sculptural shapes',
        'zzplant': 3,
        'snake': 5,
        'croton': 2,
        'areca': 1,
        'string': 5
    }]
    },
    {
    'id': 5,
    'question': 'How experienced are you with houseplant care?',
    'answers': [{
        'answer': "Beginner - I'm new to houseplants",
        'zzplant': 5,
        'snake': 5,
        'croton': 1,
        'areca': 2,
        'string': 3
    },{
        'answer': "Intermediate - I've cared for a few houseplants",
        'zzplant': 4,
        'snake': 4,
        'croton': 3,
        'areca': 3,
        'string': 4
    },{
        'answer': 'Advanced - I have a green thumb and a large plant collection',
        'zzplant': 2,
        'snake': 3,
        'croton': 5,
        'areca': 4,
        'string': 2
    }]
    },
    {
    'id': 6,
    'question': 'What additional benefits are you looking for in a houseplant?',
    'answers': [{
        'answer': 'Air purification',
        'zzplant': 4,
        'snake': 5,
        'croton': 3,
        'areca': 2,
        'string': 1
    },{
        'answer': 'Humidity control',
        'zzplant': 3,
        'snake': 2,
        'croton': 1,
        'areca': 5,
        'string': 2
    },{
        'answer': 'Easy propagation for sharing with friends',
        'zzplant': 2,
        'snake': 3,
        'croton': 4,
        'areca': 1,
        'string': 5
    },{
        'answer': 'Pet-friendly and non-toxic',
        'zzplant': 5,
        'snake': 1,
        'croton': 1,
        'areca': 3,
        'string': 4
    }]
    },
    {
    'id': 7,
    'question': 'Are you open to dealing with potential pest issues or extra maintenance?',
    'answers': [{
        'answer': "Yes, I'm willing to invest time in maintaining my plant's health",
        'zzplant': 2,
        'snake': 3,
        'croton': 5,
        'areca': 4,
        'string': 2
    },{
        'answer': 'No, I prefer low-maintenance plants that are resistant to pests',
        'zzplant': 5,
        'snake': 5,
        'croton': 1,
        'areca': 2,
        'string': 4
    }]
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html', 
                           questions=QUESTIONS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)