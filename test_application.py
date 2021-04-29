from application import application
with application.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello World! Welcome to CI/CD Deploy'
    assert response.status_code == 200
