📌 Telegram CH-KO Translator Bot (텔레그램 한중 번역 봇)

이 텔레그램 봇은 한국어 ↔ 중국어 메시지를 실시간 번역합니다.
한국어 메시지를 보내면 자동으로 중국어 메시지로 번역해주고,
중국어 메시지를 보내면 자동으로 한국어 메시지로 번역합니다.
Gemini AI (Google AI)를 사용하여 빠르고 정확하며 문화적 차이, 맥락을 고려한 번역을 제공합니다.

무분별한 타인의 사용을 막기 위해 사용할 채팅방에서
/chatid를 입력하시고, 채팅방 id를 환경변수(env)에 꼭 등록하세요.
그래야 번역기가 작동합니다.

1️⃣ 필수 패키지 설치
pip install -r requirements.txt
✅ 위 명령어를 실행하면 필요한 모든 패키지가 설치됩니다.

2️⃣ 텔레그램 봇 생성 (BotFather 이용)
텔레그램에서 @BotFather 검색 후 시작합니다.
/newbot 명령어를 입력합니다.
봇의 이름(Name)을 입력합니다. (예: MyTranslatorBot)
봇 사용자명(Username)을 입력합니다. (username_bot 형식)
봇이 생성되면, API 토큰이 제공됩니다.
✅ 이 토큰을 .env 파일의 TELEGRAM_TOKEN 값으로 저장하세요!

Step 2. Telegram에서 Bot을 활성화
텔레그램 앱에서 방금 만든 봇을 검색하세요.
/start를 입력하여 봇을 활성화합니다.
📌 결과: BotFather가 제공한 API 키(TELEGRAM_TOKEN)를 .env 파일에 저장해야 합니다.

3️⃣ Google Gemini API 키 등록법
Step 1. Google ai스튜디오 API 키 발급
https://aistudio.google.com/app/prompts/new_chat?hl=ko로 이동합니다.
"Get API Key" 버튼을 클릭하여 새 API 키를 생성합니다.
생성된 API 키를 .env 파일의 GENAI_API_KEY 값으로 저장하세요!
📌 결과: Google Gemini API 키를 발급받아 .env 파일에 추가해야 합니다.

4️⃣ .env 파일 생성 및 설정
프로젝트 폴더(Telegram-ch-ko-translator-bot)에 .env 파일을 만들고 아래 내용을 추가하세요.

echo TELEGRAM_TOKEN=your-telegram-bot-token > .env
echo GENAI_API_KEY=your-gemini-api-key >> .env
echo ALLOWED_CHAT_IDS=-1001888990306,5058173161 >> .env

📌 또는 직접 .env 파일을 생성 후, 아래와 같이 내용을 입력하세요:
TELEGRAM_TOKEN=your-telegram-bot-token
GENAI_API_KEY=your-gemini-api-key
ALLOWED_CHAT_IDS=채팅ID

✅ your-telegram-bot-token과 your-gemini-api-key를 실제 API 키로 변경하세요.

5️⃣ 봇 실행 방법

python tbot.py

✅ 서버에서 파이썬을 돌리세요. 이제 봇이 실행됩니다. 🚀

💡 사용 가능한 명령어

/start 봇을 시작하고 설명을 표시합니다.
/chatid 현재 채팅방 ID를 확인합니다.
/restart 봇을 재시작합니다.
/help 사용 가능한 명령어 목록을 표시합니다.

또한, Gemini Flash 모델 특성상 번역이 누적되면 이상한 말을 번역하는 등
오류가 발생할 확률이 높아지기 때문에 주기적으로 /restart를 하여
번역기를 재시작해주는게 좋습니다.

🎯 최종 정리 | Summary
1️⃣ @BotFather로 텔레그램 봇 생성 → TELEGRAM_TOKEN 얻기
2️⃣ Gemini AI에서 API 키 생성 → GENAI_API_KEY 얻기
3️⃣ .env 파일에 API 키 저장 (TELEGRAM_TOKEN, GENAI_API_KEY)
4️⃣ pip install -r requirements.txt 로 패키지 설치
5️⃣ python tbot.py 실행 후 번역 테스트 🚀

=============================================

📌 Telegram CH-KO Translator Bot (텔레그램 한중 번역 봇 | 韩中翻译机器人)

This Telegram bot instantly translates messages between Korean and Chinese in real time.
If you send a message in Korean, it will be automatically translated into Chinese.
If you send a message in Chinese, it will be automatically translated into Korean.
It uses Gemini AI (Google AI) to provide fast, accurate translations while considering cultural and contextual nuances.

To prevent unauthorized use, enter /chatid in the chat room where you want to use the bot
and register the chat ID in the .env file.
The translator will only work if the chat ID is registered.

1️⃣ Install Required Packages
pip install -r requirements.txt
✅ Running this command will install all necessary dependencies.

2️⃣ Create a Telegram Bot (Using BotFather)
Step 1. Create a Bot with BotFather
Open Telegram and search for @BotFather, then start the chat.
Enter the command /newbot.
Enter the bot's name (Name) (e.g., MyTranslatorBot).
Enter the bot's username (Username) in the format username_bot.
Once the bot is created, an API token will be provided.
✅ Save this token as TELEGRAM_TOKEN in the .env file!
Step 2. Activate the Bot in Telegram
Search for the bot you just created in the Telegram app.
Enter /start to activate the bot.
3️⃣ Obtain a Google Gemini API Key
Step 1. Generate an API Key from Google AI Studio
Go to Google AI Studio API Key Page
Click the "Get API Key" button to generate a new API key.
Save the generated API key as GENAI_API_KEY in the .env file.
📌 Result: You must add the Google Gemini API key to the .env file.

4️⃣ Create and Configure .env File
Create a .env file inside your project folder (Telegram-ch-ko-translator-bot) and add the following:

echo TELEGRAM_TOKEN=your-telegram-bot-token > .env
echo GENAI_API_KEY=your-gemini-api-key >> .env
echo ALLOWED_CHAT_IDS=-1001888990306,5058173161 >> .env
Alternatively, you can manually create the .env file and enter the following:

TELEGRAM_TOKEN=your-telegram-bot-token
GENAI_API_KEY=your-gemini-api-key
ALLOWED_CHAT_IDS=your-chat-id
✅ Replace your-telegram-bot-token and your-gemini-api-key with the actual API keys.

5️⃣ Run the Bot
python tbot.py
✅ Run Python on your server, and the bot will start running. 🚀

💡 Available Commands
/start - Start the bot and display a description.
/chatid - Check the current chat room ID.
/restart - Restart the bot.
/help - Display the list of available commands.

Since the Gemini Flash model may degrade over time and start producing incorrect translations,
it is recommended to periodically restart the bot using /restart to maintain translation accuracy.

🎯 Summary
1️⃣ Create a Telegram bot using @BotFather → Obtain TELEGRAM_TOKEN
2️⃣ Generate a Gemini AI API key → Obtain GENAI_API_KEY
3️⃣ Save API keys in the .env file (TELEGRAM_TOKEN, GENAI_API_KEY)
4️⃣ Install required packages using pip install -r requirements.txt
5️⃣ Run python tbot.py to start the bot 🚀

✅ Now, anyone can easily create and run this Telegram translation bot! 😎🔥

=============================================

中文

这个 Telegram 机器人 可以实时翻译韩语和中文消息。
如果您发送 韩语消息，它会自动翻译成中文。
如果您发送 中文消息，它会自动翻译成韩语。
它使用 Gemini AI（Google AI） 提供 快速、准确的翻译，并考虑文化差异和语境。

为了防止未经授权的使用，请在要使用机器人的聊天群中输入 /chatid，
然后 将该聊天 ID 注册到 .env 文件中。
只有注册了聊天 ID，翻译功能才能正常工作。

1️⃣ 安装必需的软件包
pip install -r requirements.txt
✅ 运行此命令将安装所有必需的依赖项。

2️⃣ 创建 Telegram 机器人（使用 BotFather）
步骤 1. 通过 BotFather 创建机器人
在 Telegram 中搜索 @BotFather，然后开始聊天。
输入命令 /newbot。
输入 机器人的名称（Name）（例如：MyTranslatorBot）。
输入 机器人的用户名（Username）（格式：username_bot）。
创建机器人后，系统会提供 API 令牌（Token）。
✅ 将此令牌保存到 .env 文件中的 TELEGRAM_TOKEN！
步骤 2. 在 Telegram 中激活机器人
在 Telegram 应用中搜索刚刚创建的机器人。
输入 /start 来激活机器人。
3️⃣ 获取 Google Gemini API 密钥
步骤 1. 通过 Google AI Studio 生成 API 密钥
访问 Google AI Studio API 密钥页面
点击 "获取 API 密钥（Get API Key）" 按钮生成新的 API 密钥。
将生成的 API 密钥保存到 .env 文件的 GENAI_API_KEY 中。
📌 结果：您必须将 Google Gemini API 密钥添加到 .env 文件中。

4️⃣ 创建和配置 .env 文件
在您的项目文件夹 (Telegram-ch-ko-translator-bot) 内创建 .env 文件，并添加以下内容：

echo TELEGRAM_TOKEN=your-telegram-bot-token > .env
echo GENAI_API_KEY=your-gemini-api-key >> .env
echo ALLOWED_CHAT_IDS=-1001888990306,5058173161 >> .env
或者，您可以手动创建 .env 文件，并输入以下内容：

TELEGRAM_TOKEN=your-telegram-bot-token
GENAI_API_KEY=your-gemini-api-key
ALLOWED_CHAT_IDS=your-chat-id
✅ 请将 your-telegram-bot-token 和 your-gemini-api-key 替换为您的实际 API 密钥。

5️⃣ 运行机器人
python tbot.py
✅ 在服务器上运行 Python，机器人就会开始运行 🚀

💡 可用命令
/start - 启动机器人并显示描述。
/chatid - 检查当前聊天群 ID。
/restart - 重新启动机器人。
/help - 显示可用命令列表。

由于 Gemini Flash 模型可能随着时间的推移而产生错误，
建议定期使用 /restart 重新启动机器人 以保持翻译准确性。

🎯 总结
1️⃣ 使用 @BotFather 创建 Telegram 机器人 → 获取 TELEGRAM_TOKEN
2️⃣ 生成 Gemini AI API 密钥 → 获取 GENAI_API_KEY
3️⃣ 在 .env 文件中保存 API 密钥 (TELEGRAM_TOKEN, GENAI_API_KEY)
4️⃣ 运行 pip install -r requirements.txt 安装依赖项
5️⃣ 运行 python tbot.py 启动机器人 🚀

✅ 现在，任何人都可以轻松创建和运行这个 Telegram 翻译机器人！ 😎🔥
