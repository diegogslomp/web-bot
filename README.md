# bot

Web automation examples

### Prerequisites

1. Python3, Pipenv and Geckodriver for .py
2. Nodejs and Chromium for .js

### Install

```
# For .py script
git clone https://github.com/diegogslomp/bot.git
cd bot
cp env-example .env
pipenv install
./download-geckodriver-for-windows.sh
```

```
# For .js script
npm install
```

### Usage

```
pipenv run python facebook_login.py
node facebook-login.js
```
