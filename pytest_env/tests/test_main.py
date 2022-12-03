import requests


def test_lambda_handler():
    response = requests.post(
        url="http://hello_world_lambda:8080/2015-03-31/functions/function/invocations",
        data="{}",
    )
    print(response.json())
    assert 1 == 2
