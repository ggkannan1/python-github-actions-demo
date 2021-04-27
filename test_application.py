from application import application
with application.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello World! Welcome to Devops 2021!'
    assert response.status_code == 200
