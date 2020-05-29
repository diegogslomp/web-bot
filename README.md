# bot

Web automation examples

### Prerequisites

1. Python3, Pipenv and Geckodriver for .py
```
cd bot
cp env-example .env
pipenv install
./download-geckodriver-for-windows.sh
```

2. Nodejs and Chromium for .js
```
cd bot
cp env-example .env
npm install
```

### Usage
```
pipenv run python facebook_login.py
node facebook-login.js
```
