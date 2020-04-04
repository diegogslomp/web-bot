# bot

Web automation with Selenium and Python

### Prerequisites

- [Firefox geckodriver](https://github.com/mozilla/geckodriver/releases) executable inside this repo folder or path in .env

- Python3 and Pipenv for Selenium virtual environment

### Install

```
git clone https://github.com/diegogslomp/bot.git
cd bot
pipenv install
```

### Usage

```
./facebook-bot --help
Loading .env environment variables…
usage: facebook_bot.py [-h] [--email EMAIL] [--password PASSWORD] task

positional arguments:
  task                  login

optional arguments:
  -h, --help            show this help message and exit
  --email EMAIL, --user EMAIL, -u EMAIL
  --password PASSWORD, -p PASSWORD
```
