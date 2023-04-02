# Flash web app with API call

This is a simple flashcard game that helps users learn French or Spanish using the 100 most commonly used words in French. The app makes use of a REST API to provide users with a new word to guess each time they play.
I used automatic translation to get the spanish one. Some words translation may not be so accurate.

I did this in order to practice: 
* SQL databases
* Flask application
* Python
* REST API
* Cypress
* HTML/CSS
* Docker

## TODO
* Create a Docker compose and run the app on `gunicorn` and `nginx` proxy

## Table of Contents

- [Installation](#%EF%B8%8F-installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Author](#-author)
    
## 🛠️ Installation
To run this app on your local machine, you'll need to have Python 3 installed.

1. Clone the repository:

```bash
git clone https://github.com/your-username/flashcard-game.git
cd flashcard-game
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv
```

3. Install the dependencies
```bash
pip3 install -r requirements.txt
```

## Usage
To start the app, run the following command:
```bash
python3 main.py
```
Then open a web browser and go to <http://127.0.0.1:5000> to play the game.

Alternatively, you can use Docker to run the app:
```bash
sudo docker run -p 80:5000 jonathananguise/flashcardgame:latest
```
Then open a web browser and go to <http:127.0.0.1:80> to play the game.

## API Reference

The API provides users with a new word to guess each time they play. To get a new word, send a GET request to the following endpoint:

```http
GET /get-words
```
The response will be a JSON object that contains the word and its translation:
```json
{
  "word": "bureau",
  "word_translation": "despacho"
}
```

## 🙇 Author
#### Jonathan Anguise
- Github: [@jonathanAnguise](https://github.com/jonathanAnguise)
