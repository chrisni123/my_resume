from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    courses = [
        ['BUAD475', 'International Marketing',
           'Learning about Marketing, using international regulations and bylaws'],
        ['MISY160', 'Introduction to Excel and Access',
            'Learning how to apply MS applications to databases'],
        ['BUAD302', 'Marketing Research',
           'Learning how to implement Market Research'],
        ['Buad306', 'Introduction to Operational Management',
            'Learns how to improve operational skills within corporations']
    ]
    return render_template('courses.html', courses=courses)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
