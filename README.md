# Jarvis Voice Assistant

AI-powered voice assistant that processes natural language commands using Google Gemini, fetches news updates, and controls music playback through voice interaction.

## Features

- **Voice Recognition**: Converts speech to text for command processing
- **AI Responses**: Integrates Google Gemini API for intelligent conversation
- **News Updates**: Retrieves and reads latest headlines
- **Music Control**: Plays songs from your music library via voice commands
- **Text-to-Speech**: Responds audibly to user queries

## Tech Stack

- **Python 3.x**
- **Google Gemini API** - Natural language understanding
- **SpeechRecognition** - Voice input processing
- **pyttsx3** - Text-to-speech output
- **NewsAPI** - Real-time news fetching

## Project Structure

```
personal_Voice_assitant--jarvis-/
├── main.py              # Application entry point
├── speech.py            # Speech recognition and synthesis
├── geminiai.py          # Gemini API integration
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
```
GEMINI_API_KEY=your_gemini_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

4. Run the assistant:
```bash
python main.py
```

## Usage

Once running, speak commands like:
- "What's the weather today?"
- "Tell me the latest news"
- "Play [song name]"
- "What is [query]?"

The assistant will process your speech, execute the command, and respond verbally.

## Learning Outcomes

This project helped me understand:
- Integrating multiple APIs into a cohesive system
- Managing asynchronous operations (speech input/output, API calls)
- Modular code architecture for maintainability
- Error handling in real-time voice applications

## Future Improvements

- [ ] Add weather integration
- [ ] Support for calendar/reminders
- [ ] Multi-language support
- [ ] Improve response latency
- [ ] Add conversation context memory

## Requirements

- Python 3.8+
- Microphone for voice input
- Internet connection for API access
- Valid API keys for Gemini and NewsAPI

## License

MIT

---

**Note**: This is a learning project. API keys are required and not included. Response quality depends on internet connection and API availability.
