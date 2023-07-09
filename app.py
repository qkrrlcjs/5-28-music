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
        song_list = [{'title':'아름다운 이별','singer':'김건모'},
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
                     {'title':'벌써 일년','singer':'브라운 아이즈'},
                     {'title':'거리에서','singer':'성시경'},
                     {'title':'추억은 사랑을 닮아','singer':'박효신'},
                     {'title':'내게 오는 길','singer':'성시경'},
                     {'title':'보고 싶다','singer':'김범수'},
                     {'title':'사랑합니다','singer':'팀'},
                     {'title':'발자국','singer':'먼데이키즈'},
                     {'title':'그 남자 그 여자','singer':'바이브'},
                     {'title':'가지마..가지마..가지마..','singer':'원티드,이정'},
                     {'title':'오늘 헤여졌어요','singer':'윤하'},
                     {'title':'sk8er boy','singer':'Avril Lavigne'},
                     {'title':'Juliet (Single Edit)','singer':'LMNT'},
                     {'title':'Uptown Girl (Radio Edit) ','singer':'Westlife'},
                     {'title':'Year 3000','singer':'Busted'}
                     {'title':'Upside Down','singer':'A-Teens'},
                     {'title':'Geek In The Pink','singer':'Jason Mraz'},
                     {'title':'We belong Together','singer':'Mariah Carey'},
                     {'title':'Wherever You Will Go','singer':'The calling'},
                     {'title':'This Love','singer':'Maroon 5'},
                     {'title':'Umbrella ','singer':'Rihanna'},
                     {'title':'자옥아','singer':'박상철'},
                     {'title':'동반자','singer':'태진아'},
                     {'title':'사랑의 밧줄','singer':'김용인'},
                     {'title':'태클을 걸지마','singer':'진성'},
                     {'title':'만약에','singer':'조항조'},
                     {'title':'둠바 둠바','singer':'진시몬'},
                     {'title':'어머나!','singer':'장윤정'},
                     {'title':'사랑의 배터리','singer':'홍진영'},
                     {'title':'일편단심','singer':'금잔디'},
                     {'title':'시계바늘','singer':'신유'},
                     {'title':'죽일 놈','singer':'다이나믹듀오'},
                     {'title':'LOVE LOVE LOVE','singer':'에픽하이'},
                     {'title':'외톨이','singer':'아웃사이더'},
                     {'title':'눈물샤워','singer':'배치기'},
                     {'title':'우산','singer':'에픽하이'},
                     {'title':'HEARTBREAKER','singer':'지드래곤'},
                     {'title':'하루에 시간이 주어진다면','singer':'바이브'},
                     {'title':'아이스크림','singer':'MC몽'},
                     {'title':'마법의성','singer':'MC 스나이퍼'},
                     {'title':'고백','singer':'다이나믹듀오'},
                     {'title':'Tell Me','singer':'원더걸스'},
                     {'title':'Gee','singer':'소녀시대'},
                     {'title':"I Don't Care",'singer':'2NE1'},
                     {'title':'핫이슈','singer':'포미닛'},
                     {'title':'거짓말','singer':'빅뱅'},
                     {'title':'소원을 말해봐','singer':'소녀시대'},
                     {'title':'붉은 노을','singer':'빅뱅'},
                     {'title':'하루하루','singer':'빅뱅'},
                     {'title':'Wedding Dress','singer':'태양'},
                     {'title':'Again&Again','singer':'2PM'},]
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