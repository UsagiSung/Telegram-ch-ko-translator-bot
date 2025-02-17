Telegram CH-KO Translator Bot

[Korean] 📌 텔레그램 한중 번역 봇

이 텔레그램 봇은 실시간으로 한국어와 중국어 간의 메시지를 번역합니다.

한국어 메시지를 보내면 자동으로 중국어로 번역합니다.

중국어 메시지를 보내면 자동으로 한국어로 번역합니다.

Google의 Gemini AI를 사용하여 빠르고 문화적 차이와 맥락을 고려한 번역을 수행합니다.

🚨 봇을 사용하려면 채팅방의 ID를 환경 변수(.env)에 등록해야 합니다!

🚨채팅방에서 /chatid 명령어를 입력하여 ID를 확인 후 .env 파일에 추가하세요.

======= 🚀 설치 및 실행 방법 =======

1️⃣ 필수 패키지 설치

pip install -r requirements.txt

✅ 위 명령어를 실행하면 필요한 모든 패키지가 자동으로 설치됩니다. (python-dotenv)

2️⃣ 텔레그램 봇 생성 (BotFather 이용)

Step 1. BotFather로 봇 만들기

텔레그램에서 @BotFather 검색 후 시작합니다.

/newbot 명령어를 입력합니다.

봇의 이름(Name)을 입력합니다. (예: MyTranslatorBot)

봇 사용자명(Username)을 입력합니다. (username_bot 형식)

봇이 생성되면 API 토큰이 제공됩니다.

✅ 이 API 토큰을 .env 파일의 TELEGRAM_TOKEN 값으로 저장하세요.

Step 2. 텔레그램에서 봇 활성화

텔레그램 앱에서 방금 만든 봇을 검색하세요.

/start를 입력하여 봇을 활성화합니다.

.env 파일에 BotFather가 제공한 API 키 (TELEGRAM_TOKEN) 를 저장해야 합니다.

3️⃣ Google Gemini API 키 등록

Google AI Studio로 이동합니다.

https://aistudio.google.com/app/apikey

Get API Key 버튼을 클릭하여 새 API 키를 생성합니다.

생성된 API 키를 .env 파일의 GENAI_API_KEY 값으로 저장하세요.

4️⃣ .env 파일 생성 및 설정

프로젝트 폴더(Telegram-ch-ko-translator-bot)에 .env 파일을 만들고 아래 내용을 추가하세요.

echo TELEGRAM_TOKEN=your-telegram-bot-token > .env

echo GENAI_API_KEY=your-gemini-api-key >> .env

echo ALLOWED_CHAT_IDS=your-chat-id >> .env

또는 .env 파일을 수동으로 생성하여 아래와 같이 입력하세요.

TELEGRAM_TOKEN=your-telegram-bot-token

GENAI_API_KEY=your-gemini-api-key

ALLOWED_CHAT_IDS=your-chat-id

✅ 전부 실제 API 키, chat ID로 변경하세요.

✅ ALLOWED_CHAT_IDS는 번역을 수행할 채팅방에서 /chatid 명령어를 입력하면 알 수 있습니다.

5️⃣ 봇 실행

python tbot.py

✅ 서버에서 Python을 실행하면 번역 봇이 동작합니다. 🚀

💡 사용 가능한 명령어

/start

봇을 시작하고 설명을 표시합니다.

/chatid

현재 채팅방 ID를 확인합니다.

/restart

봇을 재시작합니다.

/help

사용 가능한 명령어 목록을 표시합니다.

⚠️ Gemini Flash 모델 특성상 번역이 누적되면 이상한 결과가 나올 수 있습니다. 주기적으로 /restart를 실행하여 번역 정확도를 유지하세요.

======= 🎯 최종 정리 =======

✅ @BotFather로 텔레그램 봇 생성 → TELEGRAM_TOKEN 얻기

✅ Gemini AI에서 API 키 생성 → GENAI_API_KEY 얻기

✅ .env 파일에 API 키 저장 (TELEGRAM_TOKEN, GENAI_API_KEY)

✅ pip install -r requirements.txt 실행하여 패키지 설치

✅ python tbot.py 실행 후 번역 테스트 🚀

===============================================================================================

[Chinese] 📌 Telegram 韩中翻译机器人

本 Telegram 机器人可以实时翻译韩语和中文之间的消息。

发送韩语消息后，机器人会自动翻译成中文。

发送中文消息后，机器人会自动翻译成韩语。

本翻译机器人使用 Google Gemini AI 进行翻译，能够快速提供考虑到文化差异和上下文的精准翻译。

🚨 要使用机器人，必须在环境变量（.env）中注册聊天 ID！

🚨 在聊天中输入 /chatid 命令获取 ID，并将其添加到 .env 文件中。

🚀 安装与运行方法

1️⃣ 安装必要的依赖包

运行以下命令安装所有必需的依赖项：

pip install -r requirements.txt

✅ 上述命令将自动安装所有必需的 Python 包（如 python-dotenv）。

2️⃣ 创建 Telegram 机器人（使用 BotFather）

Step 1: 通过 BotFather 创建机器人

在 Telegram 中搜索 @BotFather 并开始对话。

输入 /newbot 命令。

按提示输入机器人的名称（例如：MyTranslatorBot）。

按提示输入机器人的用户名（格式：username_bot）。

机器人创建成功后，BotFather 将提供一个 API 令牌（TOKEN）。

✅ 请将此 API 令牌存储到 .env 文件中的 TELEGRAM_TOKEN 变量。

Step 2: 在 Telegram 上启用机器人

在 Telegram 应用中搜索刚刚创建的机器人。

发送 /start 命令以激活机器人。

确保 .env 文件中已保存 BotFather 提供的 API 令牌（TELEGRAM_TOKEN）。

3️⃣ 注册 Google Gemini API 密钥

访问 Google AI Studio。

点击 “Get API Key” 按钮生成新的 API 密钥。

将生成的 API 密钥存储到 .env 文件的 GENAI_API_KEY 变量中。

4️⃣ 创建 .env 文件并进行配置

在项目目录 (Telegram-ch-ko-translator-bot) 中创建 .env 文件，并添加以下内容：

echo TELEGRAM_TOKEN=your-telegram-bot-token > .env

echo GENAI_API_KEY=your-gemini-api-key >> .env

echo ALLOWED_CHAT_IDS=your-chat-id >> .env

或者手动创建 .env 文件并输入以下内容：

TELEGRAM_TOKEN=your-telegram-bot-token

GENAI_API_KEY=your-gemini-api-key

ALLOWED_CHAT_IDS=your-chat-id

✅ 请务必将 your-telegram-bot-token、your-gemini-api-key 和 your-chat-id 替换为实际的值！

✅ 在需要使用翻译功能的聊天群中输入 /chatid 命令，以获取 ALLOWED_CHAT_IDS 的正确值。

5️⃣ 运行机器人

运行以下命令启动机器人：

python tbot.py

✅ 在服务器上运行 Python 代码后，翻译机器人即可开始工作！ 🚀

💡 可用命令

/start	启动机器人并显示说明信息。

/chatid	获取当前聊天的 ID。

/restart	重新启动机器人。

/help	显示可用命令列表。

⚠️ 由于 Gemini Flash 模型的特性，翻译内容可能会因累计处理而出现异常情况。建议定期运行 /restart 命令，以保持翻译准确性。

🎯 最终总结

✅ 使用 @BotFather 创建 Telegram 机器人 → 获取 TELEGRAM_TOKEN

✅ 在 Gemini AI 生成 API 密钥 → 获取 GENAI_API_KEY

✅ 在 .env 文件中保存 API 密钥（TELEGRAM_TOKEN、GENAI_API_KEY）

✅ 运行 pip install -r requirements.txt 安装依赖

✅ 运行 python tbot.py 并进行翻译测试 🚀
