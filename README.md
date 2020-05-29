# bot

Web automation examples

### Prerequisites

1. Python3, Pipenv and Geckodriver for .py
```
cd bot
pipenv install
./download-geckodriver-for-windows.sh
```

2. Nodejs and Chromium for .js
```
cd bot
npm install
```

### Usage
```
cp env-example .env
pipenv run python facebook_login.py
node facebook-login.js
```
