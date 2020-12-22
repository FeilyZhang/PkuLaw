from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<page>')
def visit_page(page):
    return render_template(page + '.html')

@app.route('/')
def visit_home():
    return render_template('line.html')

if __name__ == '__main__':
    app.run()