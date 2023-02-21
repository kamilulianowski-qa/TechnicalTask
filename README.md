# TechnicalTask

## Requirements:
- Python 3.10
- Virtualenv https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
- Chrome 109.0.5414.119
- Firefox 110.0 
- Allure commandline and java if you want to run reports -> https://www.npmjs.com/package/allure-commandline

## Installation: 
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run tests
Chrome: 
```
pytest --browser chrome --alluredir=allure_result
```
Firefox: 
```
pytest --browser firefox --alluredir=allure_result
```

## Reports:
```
Allure serve
```

![image](https://user-images.githubusercontent.com/121701119/220397385-2b3256c7-7311-4c92-abad-7371cf5bab6c.png)
