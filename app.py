from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    return render_template(
        'itemsPage.html',
        username='B76',
        items=[ "Assignments complete","Project planning","Submit project","Prepare presentation","Testing and Debugging","Final review meeting"]
    )

if __name__ == '__main__':
    app.run(debug=True)
