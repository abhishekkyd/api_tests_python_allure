## Sample REST API tests for (gorest)(https://gorest.co.in/)
Used packages: Requests + Pytest + Allure2

## Requirements:
1. Python 3.7.3
2. [Allure2 report generator](https://github.com/allure-framework/allure2#download) (add allure to PATH variables)

## Setup and Run:
(Terminal from root project folder)
1. Install Python dependencies `pipenv install --three --ignore-pipfile`
2. Get token [here](https://gorest.co.in/access-token)
3. Set it in environment variable: `export TOKEN='your_token'`
4. Run tests `pipenv run python -m pytest tests -l -v -vv -s`
5. Get report `allure serve allure-results`
