from flask import Flask, render_template, request
from nietzsche import model
from pyngrok import conf, ngrok
import re


app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

conf.get_default().auth_token = "AUTH_TOKEN"
http_tunnel = ngrok.connect(5000)
tunnels = ngrok.get_tunnels()

def preprocess(prompt: str) -> str:
    """_prompt에서 태그를 제거하는 함수입니다._

    Args:
        prompt (str): _form request로 받은 prompt입니다._

    Returns:
        _str_: _정제한 prompt입니다._
    """
    prompt = prompt.replace("&nbsp;", '')
    return re.sub(r"\<[^)]*\>", '', prompt)

@app.route("/")
def index():
    https_url = tunnels[0].public_url # ngrok으로 생성된 https 주소를 넘겨줍니다.
    return render_template("index.html")

@app.route("/", methods=['POST'])
def result():
    if request.method == 'POST':
        set_lst: tuple[int, float] = (int(request.form.get('maxLength')), float(request.form.get('topP')))
        content: str = preprocess(request.form.get('prompt'))
        result: str = model.generate(content, set_lst)
        return render_template("index.html", content= content, result= result)
    