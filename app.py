from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("ck_form.html")

@app.route('/show_form_data', methods=['POST'])
def response():
    title   = request.form.get("title_field")
    content = request.form.get("content_field")
    return render_template("ck_form.html", field1=title, field2=content)
    
if __name__ == '__main__':
    app.run(debug=True)