.DEFAULT_GOAL := app

app: install test run deploy

install:
	@pip install pipenv
	@pipenv --python 3.8
	@pip install requests
	@pip install pytest

test:
	@pipenv run pytest tests/tests.py | tee results.txt

run:
	@pipenv run python3 app.py | tee -a results.txt
	
deploy:
	@git add results.txt
	@git commit -m "зміни в роботі"
@git push origin master 
