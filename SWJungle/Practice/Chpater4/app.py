# flask 시작 코드

from flask import Flask, render_template # html 파일 불러올 시 사용해줘야함.
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html') # html파일 불러오는 구문

@app.route('/mypage')
def mypage():  
   return 'This is My Page!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)

# 파일 이름은 아무렇게나 해도 상관없지만,
# 통상적으로 flask 서버를 돌리는 파일은 app.py라고 이름 짓는다.