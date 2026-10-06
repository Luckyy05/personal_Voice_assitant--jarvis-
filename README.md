# Jarvis Voice Assistant

AI-powered voice assistant that processes natural language commands using Groq, stores simple user memories, fetches news updates, and controls music playback through voice interaction.

## Features

* **Voice Recognition**: Converts speech to text for command processing
* **AI Responses**: Integrates Groq API for intelligent conversation
* **Memory System**: Stores and retrieves user memories using a local JSON file
* **News Updates**: Retrieves and reads latest headlines
* **Music Control**: Plays songs from your music library via voice interaction
* **Website Control**: Opens websites such as Google, Facebook, YouTube, and LinkedIn
* **Text-to-Speech**: Responds audibly to user queries

## Tech Stack

* **Python 3.x**
* **Groq API** - Natural language understanding and AI responses
* **SpeechRecognition** - Voice input processing
* **pyttsx3** - Text-to-speech output
* **NewsAPI** - Real-time news fetching
* **JSON** - Local memory storage
* **python-dotenv** - Environment variable management

## Project Structure

```text
personal_Voice_assitant--jarvis-/
├── main.py              # Application entry point and command processing
├── speech.py            # Text-to-speech functionality
├── groqai.py            # Groq API integration
├── memory.py            # Memory storage and retrieval
├── news.py              # News fetching logic
├── musiclibrary.py      # Music library management
└── requirements.txt     # Dependencies
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Luckyy05/personal_Voice_assitant--jarvis-.git
cd personal_Voice_assitant--jarvis-
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure API keys:

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

4. Run the assistant:

```bash
python main.py
```

## Usage

Once running, speak commands like:

* "What's the weather today?"
* "Tell me the latest news"
* "Play [song name]"
* "Remember my favourite language is Python"
* "What is my favourite language?"
* "What is [query]?"

The assistant will process the speech, execute the command, access saved memories when required, and respond verbally.

## Memory System

Jarvis can store simple information provided through voice commands.

For example:

```text
"Remember my favourite language is Python"
```

The information is stored locally in `memory.json`.

Later, you can ask:

```text
"What is my favourite language?"
```

Jarvis searches the saved memories and returns the matching information.

> `memory.json` is a local file and should not be uploaded to GitHub because it may contain personal information.

## Learning Outco
