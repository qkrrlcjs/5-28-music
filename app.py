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
        song_list = [{'title':'벌써 일년','singer':'이적'},
                     {'title':'아름다운 이별','singer':'김건모'},
                     {'title':'송인','singer':'쿨'},
                     {'title':'회상','singer':'터보'},
                     {'title':'눈물','singer':'리아'},
                     {'title':'시작','singer':'박기영'},
                     {'title':'괜찮아','singer':'비쥬'},
                     {'title':'첫사랑','singer':'임현정'},
                     {'title':'귀거래사','singer':'김신우'},
                     {'title':'사랑의 서약','singer':'한동준'},
                     {'title':'너를 보내고','singer':'윤도현'},
                     {'title':'Good bye','singer':'Jessica'},
                     {'title':'Because You Loved Me','singer':'Celine Dion'},
                     {'title':'Without you','singer':'Mariah Carey'},
                     {'title':'I Want It That Way','singer':'Back street Boys'},
                     {'title':'Now and forever','singer':'Richard Marx'},
                     {'title':"I'll Be Missing You",'singer':'Puff Daddy'},
                     {'title':'I Swear','singer':'All-4-One'},
                     {'title':'When a man loves a woman','singer':'Michael Bolton'},
                     {'title':"You're Still the One",'singer':'Shania Twain'},
                     {'title':'as long as you love me','singer':'Back street boys'},
                     {'title':'신사동 그사람','singer':'주현미'},
                     {'title':'사랑이 뭐길래','singer':'한혜진'},
                     {'title':'비나리','singer':'심수봉'},
                     {'title':'아미새','singer':'현철'},
                     {'title':'차표한장','singer':'송대관'},
                     {'title':'다함께 차차차','singer':'설운도'},
                     {'title':'당신','singer':'김정수'},
                     {'title':'누이','singer':'설운도'},
                     {'title':'애모','singer':'김수희'},
                     {'title':'환상 속의 그대','singer':'서태지와 아이들'},
                     {'title':'흐린 기억 속의 그대','singer':'현진영'},
                     {'title':'하여가','singer':'서태지와 아이들'},
                     {'title':'약한 남자','singer':'듀스'},
                     {'title':'나를 돌아봐','singer':'듀스'},
                     {'title':'발해를 꿈꾸며','singer':'서태지와 아이들'},
                     {'title':'다시 만나줘','singer':'업타운'},
                     {'title':'필승','singer':'서태지와 아이들'},
                     {'title':'머피의 법칙','singer':'DJ DOC'},
                     {'title':'Festival','singer':'엄정화'},
                     {'title':'애상','singer':'쿨'},
                     {'title':'헤라의 질투','singer':'손상미'},
                     {'title':'순정','singer':'코요태'},
                     {'title':'부담','singer':'백지영'},
                     {'title':'유혹','singer':'이재영'},
                     {'title':'장미의 미소','singer':'신인수'},
                     {'title':'뿌요뿌요','singer':'UP'},
                     {'title':'가까이','singer':'샵'},
                     ]
        if year and genre:
            return render_template('list.html', year=year, genre=genre, song_list=song_list)
        else:
            error_message = "연도와 장르 모두 선택해주세요."
            return render_template('main.html',error_message = error_message)
        
@app.route('/lyrics')
def lyrics():
    return render_template('lyrics.html')

if __name__ == '__main__':
    app.run(debug=True)