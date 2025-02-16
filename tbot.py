#!/usr/bin/env python3
import logging
import sys
import os
from dotenv import load_dotenv
import google.generativeai as genai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# ---------------------------
# 1) 환경 변수 로드
# ---------------------------
load_dotenv()

# ---------------------------
# 2) 로그 설정 (옵션)
# ---------------------------
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ---------------------------
# 3) 환경 변수에서 API 키 불러오기
# ---------------------------
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GENAI_API_KEY = os.getenv("GENAI_API_KEY")

# ---------------------------
# 4) Gemini AI 설정 (하드코딩된 설정값 사용)
# ---------------------------
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# ---------------------------
# 초기 메시지(역할 지정)
# ---------------------------
chat_session = model.start_chat(
    history=[{
        "role": "user",
        "parts": [
            (
                "지금부터 너는 중국인과 한국인을 이어주는 번역봇이야. "
                "지금부터 내가 중국어를 말하면 한국어로 번역해서 딱 번역된 말만 출력하고, "
                "내가 한국어를 말하면 중국어로 번역해서 중국어만 출력하여 말해줘. "
                "그 외에 다른 기능을 수행해서는 안돼."
            )
        ],
    }, {
        "role": "model",
        "parts": ["알겠습니다.\n"],
    }]
)

# ---------------------------
# 5) 특정 채팅(방)만 허용
# ---------------------------
ALLOWED_CHAT_IDS = [int(chat_id) for chat_id in os.getenv("ALLOWED_CHAT_IDS", "").split(",") if chat_id]

# ---------------------------
# 6) 텔레그램 메시지 핸들러 함수
# ---------------------------
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id not in ALLOWED_CHAT_IDS:
        return

    user_text = update.message.text  
    response = chat_session.send_message(user_text)
    translated_text = response.text

    await update.message.reply_text(translated_text)

# ---------------------------
# 7) /start 명령어
# ---------------------------
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id not in ALLOWED_CHAT_IDS:
        return

    await update.message.reply_text("안녕! 번역해줄게.")

# ---------------------------
# 8) /chatid 명령어
# ---------------------------
async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"📌 이 채팅방(혹은 유저)의 ID: {chat_id}")

# ---------------------------
# 9) /restart 명령어
# ---------------------------
async def restart_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id not in ALLOWED_CHAT_IDS:
        return

    await update.message.reply_text("봇을 재시작합니다...")
    os.execl(sys.executable, sys.executable, *sys.argv)

# ---------------------------
# 10) /help 명령어
# ---------------------------
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat_id not in ALLOWED_CHAT_IDS:
        return

    help_text = (
        "🤖 *가능한 명령어 목록:*\n\n"
        "/start - 번역봇 소개\n"
        "/chatid - 현재 채팅방의 ID 확인\n"
        "/restart - 봇 재시작\n"
        "/help - 사용 가능한 명령어 목록 보기\n\n"
        "💬 *메시지를 입력하면 자동으로 번역됩니다!*"
    )

    await update.message.reply_text(help_text, parse_mode="Markdown")

# ---------------------------
# 11) 메인 함수 (핸들러 등록)
# ---------------------------
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("chatid", get_chat_id))
    app.add_handler(CommandHandler("restart", restart_command))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

# ---------------------------
# 12) 실행
# ---------------------------
if __name__ == "__main__":
    main()
