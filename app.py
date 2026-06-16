from flask import Flask, render_template, request, redirect

app = Flask(__name__)

comments = []

@app.route('/')
def home():
    return render_template('index.html', comments=comments)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.form['comment']
    comments.append(comment)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)