from flask import Flask, render_template, url_for, send_file
import pdfkit
from data import inputs

app = Flask(__name__, static_url_path='/static')

@app.context_processor
def inject_dict_for_all_templates():
    global_ = {'last name': inputs['last name']}
    return dict(global_=global_)

@app.route('/')
def index():
    return render_template('index.html', data=inputs)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=inputs)

@app.route('/download_cv_pdf')
def download_cv_pdf():
    cv_path = 'static\cv_llamoja.pdf'
    return send_file(cv_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
