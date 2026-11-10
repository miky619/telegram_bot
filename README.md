🎬 Telegram Movie Bot

A Telegram bot built with Python that allows users to search for movies and retrieve movie information using the OMDb API.

📑 Table of Contents
Project Description
Overview
Key Features
Screenshots and Demo
Technologies Used
Project Architecture
Project Structure
Requirements and Prerequisites
Installation Guide
Virtual Environment Setup
Dependencies Installation
API Configuration
Environment Variables and Configuration Files
Running the Application
Available Commands
Usage Examples
How It Works
API Integration
Error Handling
Security Considerations
Troubleshooting
Current Limitations
Future Improvements
Contributing
License
Author
Contact and Repository
🎯 Project Description

Telegram Movie Bot is a Python-based Telegram bot designed to provide users with movie information through a simple conversational interface.

The bot integrates with the OMDb API to search for movies and retrieve information such as titles, release information, IMDb ratings, cast members, directors, and plot summaries.

The project uses the pyTelegramBotAPI library to handle Telegram interactions and requests to communicate with the external movie database.

📌 Overview

The application consists of two main Python modules:

app.py: Handles Telegram bot interactions, commands, messages, and inline keyboard callbacks.
app_api.py: Handles communication with the OMDb API and retrieves movie information.

A separate configuration module named base.py is required to provide the Telegram Bot Token and OMDb API Key.

✨ Key Features

The following features are implemented in the current source code:

Start the bot using the /start command.
Display usage instructions using /help.
Search for movies using /search.
Retrieve information about movies through the OMDb API.
Display a predefined list of five movie titles.
View movie details through Telegram inline keyboard buttons.
Retrieve IMDb ratings.
Display movie cast and director information.
Retrieve movie plot summaries.

Note: The predefined movie list is not a live ranking of the most popular movies. It consists of titles specified in the application code.

📸 Screenshots and Demo

Screenshots and demonstration videos have not yet been provided.

You can add screenshots here after capturing the bot's actual interface.

Suggested screenshot locations:

text
assets/
├── start-command.png
├── movie-search.png
└── movie-details.png

🛠 Technologies Used
Technology	Purpose
Python	Main programming language
pyTelegramBotAPI	Telegram Bot API integration
Requests	HTTP requests
OMDb API	Movie information retrieval
Telegram Bot API	User interaction
🏗 Project Architecture

The application follows a simple modular architecture.

text
             Telegram User
                   |
                   v
              Telegram API
                   |
                   v
                app.py
                   |
                   v
               app_api.py
                   |
                   v
                requests
                   |
                   v
                 OMDb API
                   |
                   v
            Movie Information

Main Components

1. Telegram Bot Module (app.py)

Responsible for:

Registering Telegram bot handlers.
Processing user commands.
Handling movie search interactions.
Managing inline keyboard callbacks.
Displaying movie information to users.

2. Movie API Module (app_api.py)

Responsible for:

Sending requests to the OMDb API.
Searching for movies.
Retrieving movie details.
Processing API responses.

3. Configuration Module (base.py)

Stores the credentials required by the application:

Telegram Bot Token.
OMDb API Key.

This file must be created locally before running the application.

📁 Project Structure

The confirmed repository structure includes the following:

text
telegram_bot/
│
├── src/
│   ├── app.py
│   ├── app_api.py
│   └── base.py          # Create this file locally
│
├── requirements.txt
├── .gitignore
└── README.md


The base.py entry represents the required local configuration file. Its presence in the public repository has not been verified.

📋 Requirements and Prerequisites

Before installing the project, make sure you have:

Python installed.
Git installed.
A Telegram account.
A Telegram Bot Token.
An OMDb API Key.
An internet connection.

Python package dependencies are listed in requirements.txt.

🚀 Installation Guide
1. Clone the Repository

Open Windows PowerShell or the VS Code terminal:

powershell
git clone https://github.com/miky619/telegram_bot.git


Navigate to the project directory:

powershell
cd telegram_bot

🐍 Virtual Environment Setup

Using a virtual environment is recommended to keep project dependencies isolated.

Windows PowerShell

Create a virtual environment:

powershell
python -m venv venv


Activate it:

powershell
.\venv\Scripts\Activate.ps1


If PowerShell prevents script execution, you can temporarily allow activation scripts for the current terminal session:

powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass


Then activate the environment again:

powershell
.\venv\Scripts\Activate.ps1

Linux and macOS

Create the environment:

bash
python3 -m venv venv


Activate it:

bash
source venv/bin/activate

📦 Dependencies Installation

Make sure your virtual environment is activated.

Upgrade pip:

powershell
python -m pip install --upgrade pip


Install the project dependencies:

powershell
pip install -r requirements.txt

🔑 API Configuration

The bot requires two credentials to communicate with Telegram and the OMDb API.

1. Create a Telegram Bot
Open Telegram.
Search for @BotFather.
Start a conversation using /start.
Send /newbot.
Follow the instructions to choose a bot name and username.
Copy the generated Telegram Bot Token.

Keep your token private.

2. Obtain an OMDb API Key
Visit the OMDb API website.
Choose an available API key plan.
Complete the registration process.
Obtain your API Key.

Keep your API key private as well.

3. Create the base.py File

Navigate to the src directory:

powershell
cd src


Create a new file named base.py:

powershell
New-Item -Name "base.py" -ItemType File


Open the file in VS Code:

powershell
code base.py


Add the following configuration:

python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
API_KEY = "YOUR_OMDB_API_KEY"


Replace the placeholder values with your own credentials.

For example:

TOKEN: The token generated by BotFather.
API_KEY: Your OMDb API key.

Important: Do not publish your actual credentials on GitHub.

Return to the project root before continuing:

powershell
cd ..

⚙️ Environment Variables and Configuration Files

The current application uses a Python configuration module named base.py.

Expected configuration:

python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
API_KEY = "YOUR_OMDB_API_KEY"


The application expects these configuration values to be available through the base module.

The project currently does not document an environment-variable-based configuration system.

Recommended .gitignore Configuration

Make sure your .gitignore file contains the following entries:

gitignore
# Local configuration and secrets
src/base.py

# Python cache
__pycache__/
*.py[cod]

# Virtual environments
venv/
.venv/

# IDE settings
.vscode/

# Operating system files
.DS_Store
Thumbs.db


If base.py has already been tracked by Git, adding it to .gitignore will not automatically remove it from Git tracking.

▶️ Running the Application

After completing the installation and configuration steps, open PowerShell in the project root.

Run:

powershell
python src/app.py


The bot should start if:

Python dependencies are installed.
src/base.py exists.
The Telegram Bot Token is valid.
The OMDb API Key is valid.
Internet access is available.

The application uses Telegram bot polling to receive user interactions.

💬 Available Commands
Command	Description
/start	Start interacting with the bot
/help	Display usage instructions
/search	Search for movies

The application also provides inline keyboard interactions for displaying movie details.

📖 Usage Examples
Start the Bot

Send:

text
/start


The bot responds with its welcome message.

Display Help

Send:

text
/help


The bot displays its usage instructions.

Search for a Movie

Send:

text
/search


Follow the bot's search interaction to request movie information.

View Movie Details

Use the available inline keyboard buttons to retrieve movie information.

Depending on the API response, the displayed information includes:

Movie title.
IMDb rating.
Director.
Cast.
Plot summary.
🔄 How It Works

The application follows this general workflow:

A user sends a command or interacts with the Telegram bot.
The Telegram bot module processes the interaction.
Movie-related requests are passed to the API module.
The API module sends an HTTP request to OMDb.
OMDb returns movie information.
The application processes the response.
The bot sends the resulting information back to the user.
🌐 API Integration
OMDb API

The project uses the OMDb API to retrieve movie information.

The API key is supplied through the local configuration module.

The application uses HTTP requests to communicate with the external service.

The retrieved information can include:

Movie title.
Release year.
IMDb rating.
Director.
Actors.
Plot summary.

Availability of individual fields depends on the API response.

Telegram Bot API

Telegram communication is handled through pyTelegramBotAPI.

This library provides the functionality required to:

Receive user messages.
Register command handlers.
Send messages.
Display inline keyboards.
Handle callback interactions.
⚠️ Error Handling

The current implementation includes basic API error handling.

The API module can return an "ERROR" result when a request does not produce the expected response.

However, error handling is limited and could be improved.

Potential failure scenarios include:

Invalid API credentials.
Movie not found.
Network connection problems.
Unexpected API responses.
Missing movie information.

More comprehensive exception handling and logging are recommended for future versions.

🔒 Security Considerations

Security is important when deploying a Telegram bot.

Follow these recommendations:

Never publish your Telegram Bot Token.
Never publish your OMDb API Key.
Keep src/base.py out of public Git commits.
Add configuration files containing secrets to .gitignore.
Never share credentials in screenshots or public issue reports.
Regenerate credentials immediately if they become exposed.
Review Git history if sensitive information has previously been committed.

Important: Removing a secret from the latest version of a repository does not remove it from previous commits.

If a Telegram Bot Token has been exposed, revoke or regenerate it through BotFather.

🧰 Troubleshooting
ModuleNotFoundError

If Python cannot find a required module, install the dependencies again:

powershell
pip install -r requirements.txt

Missing Configuration Module

If you encounter an error related to base, make sure the configuration file exists:

text
src/base.py


Also verify that it contains the expected TOKEN and API_KEY variables.

Telegram Bot Does Not Respond

Check the following:

Your Telegram Bot Token is valid.
The bot application is running.
Your internet connection is working.
Another running process is not already polling with the same bot token.
Movie Search Does Not Work

Check:

Your OMDb API Key.
Your internet connection.
The movie title spelling.
OMDb API availability and usage limits.
🚧 Current Limitations

The current implementation has several limitations:

Movie information depends on an external API.
The predefined movie list contains a fixed set of titles.
There is no documented database integration.
There is no documented persistent user-data storage.
API requests do not have an explicitly configured timeout.
Network and response error handling is limited.
Input validation could be improved.
The application has no documented automated test suite.

These limitations describe areas that could benefit from further development.

🔮 Future Improvements

Possible improvements for future versions include:

Environment-variable-based configuration.
More robust API error handling.
HTTP request timeouts and retry mechanisms.
Improved input validation.
Advanced movie filtering and search options.
Movie recommendations.
Database integration.
User search history.
Automated testing.
Logging and monitoring.
Docker support.
Continuous integration with GitHub Actions.

These are suggestions for future development, not features currently claimed to be implemented.

🤝 Contributing

Contributions and suggestions are welcome.

To contribute:

Fork this repository.
Create a new branch.
Make your changes.
Test your changes.
Submit a pull request.

Example:

bash
git checkout -b feature/new-feature
git commit -m "Add new feature"
git push origin feature/new-feature


For major changes, consider opening an issue first to discuss your proposal.

📄 License

No license file or confirmed license information has been provided.

A license should be selected and added to the repository before others are granted explicit permission to reuse, modify, or distribute this project.

👨‍💻 Author

GitHub: @miky619

📬 Contact and Repository
GitHub Repository: https://github.com/miky619/telegram_bot
Author: https://github.com/miky619

For questions, bug reports, or suggestions, please use the repository's GitHub Issues section.

⭐ If you find this project useful, consider giving the repository a star!

Built with Python and Telegram Bot API.
