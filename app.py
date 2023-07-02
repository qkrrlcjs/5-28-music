from flask import render_template, request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        year = request.form.get('year')
        genre = request.form.get('genre')
        if year and genre:
            return render_template('list.html')
        else:
            error_message = "연도와 장르 모두 선택해주세요."
            return render_template('main.html',error_message = error_message)
        
@app.route('/lyrics')
def lyrics():
    return render_template('lyrics.html')

if __name__ == '__main__':
    app.run(debug=True)