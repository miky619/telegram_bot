🎬 Telegram Movie Bot

A Python-based Telegram bot that allows users to search for movies, explore selected popular titles, and retrieve detailed movie information directly through Telegram.

The bot integrates with the OMDb API to fetch movie data and uses pyTelegramBotAPI to handle Telegram interactions.

---

✨ Features

🔍 Movie Search

- Search for movies by entering their titles.
- Retrieve matching movie results.
- Display up to five search results.
- Select a movie using interactive inline buttons.

🔥 Popular Movies

- Browse a curated list of popular movie titles.
- Quickly access movie information through interactive buttons.

🎥 Movie Details

Get detailed information about selected movies, including:

- Movie Title
- Release Year
- IMDb Rating
- Runtime
- Genre
- Director
- Cast
- Full Plot Overview

💬 Interactive Telegram Interface

- Welcome message and main menu.
- Custom reply keyboard.
- Inline movie selection buttons.
- Help command with usage instructions.

---

🛠️ Technologies Used

Technology| Purpose
Python| Main programming language
pyTelegramBotAPI| Telegram Bot integration
Requests| HTTP requests
OMDb API| Movie information provider
IMDb| Movie identification and ratings

---

📁 Project Structure

telegram_bot/
│
├── src/
│   ├── app.py
│   ├── app_api.py
│   └── base.py
│
├── requirements.txt
├── .gitignore
└── README.md

File Description

- "app.py": Main application containing Telegram bot commands, message handlers, keyboards, and callback handlers.
- "app_api.py": Handles communication with the OMDb API and retrieves movie information.
- "base.py": Stores configuration values and API credentials.
- "requirements.txt": Contains the project's Python dependencies.
- ".gitignore": Excludes sensitive and unnecessary files from version control.

---

⚙️ Requirements

Before running the project, make sure you have:

- Python installed.
- A Telegram Bot Token.
- An OMDb API Key.
- An active internet connection.

---

🚀 Installation

1. Clone the Repository

git clone https://github.com/miky619/telegram_bot.git

2. Navigate to the Project Directory

cd telegram_bot

3. Create a Virtual Environment

python -m venv .venv

4. Activate the Virtual Environment

Windows (PowerShell):

.venv\Scripts\Activate.ps1

Linux / macOS:

source .venv/bin/activate

5. Install Dependencies

pip install -r requirements.txt

---

🔑 Configuration

The project requires two credentials:

1. Telegram Bot Token
2. OMDb API Key

Create a "base.py" file inside the "src" directory and configure it as follows:

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

API_KEY = "YOUR_OMDB_API_KEY"

Replace the placeholder values with your actual credentials.

Security Notice: Never upload your real API keys or Telegram Bot Token to GitHub.

Add the following entry to ".gitignore":

src/base.py

---

▶️ Running the Bot

After installing the dependencies and configuring your credentials, run:

python src/app.py

The bot uses Telegram polling to receive and process incoming messages.

Once the application starts, open your Telegram bot and send:

/start

---

📱 Available Commands

Command| Description
"/start"| Start the bot and display the main menu
"/help"| Display usage instructions
"/search"| Search for a movie
"/popular"| Display selected popular movies

Users can also interact with the bot through its reply keyboard.

---

🔄 How It Works

1. The user sends a command or selects an option from the Telegram keyboard.
2. The bot processes the incoming message.
3. For movie searches, the application sends a request to the OMDb API.
4. The API returns matching movie information.
5. The bot displays movie results using inline keyboard buttons.
6. When a user selects a movie, the bot retrieves its detailed information.
7. The selected movie's information is displayed directly in the Telegram chat.

---

🌐 API Integration

This project uses the OMDb API to retrieve movie information.

The API is used for:

- Searching movies by title.
- Retrieving detailed information using IMDb IDs.
- Accessing movie ratings and descriptions.

Official API documentation:

https://www.omdbapi.com/

---

🔒 Security

- API credentials should remain private.
- Configuration files containing secrets should not be committed.
- The ".gitignore" file should exclude sensitive files and virtual environments.

---

🚧 Future Improvements

Potential improvements for future versions include:

- Advanced movie filtering.
- Search by genre and release year.
- More comprehensive error handling.
- Movie recommendations.
- User favorites and watchlists.
- Movie poster previews.
- Database integration for storing user preferences.

---

👩‍💻 Author

Miky

GitHub: https://github.com/miky619

---

📄 License

This project is available for educational and personal development purposes.

A formal open-source license can be added to define permissions for reuse and distribution.
