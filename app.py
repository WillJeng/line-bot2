from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('YnI9d/5kyp5rNuqSc1jMXuLjq4Ox/6BvbVLeQPclBN/H0ivnb5g3DAdvRA4MnbEG/5He4B1vFH+UZo1hYrHotbpSN96QuRY8yyGz7HGWB+YeL9sSHW6VC1Fbnpd4Q1unUGfLl+zAq+Fgg3EzIMEIpwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('afe5918f8ca8abae3d188c722b0eb2f2')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="工三小"))


if __name__ == "__main__":
    app.run()