# webbot

Boilerplate for web automation with Selenium, Python and Bash

### Prerequisites

- Firefox geckodriver executable in PATH or path in .env

- Python3 and Pipenv for Selenium virtual environment

```
git clone https://github.com/diegogslomp/webbot.git
cd webbot
pipenv install 
# Edit .env with gecko path and user info
cp env-example .env
pipenv run bash scripts\facebook-login
```
