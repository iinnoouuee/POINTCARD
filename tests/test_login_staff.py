def test_login_staff_success(client):
    response = client.post('/login_staff', data={
        'email': 'staff@example.com',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200


def test_login_staff_fail(client):
    response = client.post('/login_staff', data={
        'email': 'wrong@example.com',
        'password': 'wrongpass'
    })
    assert response.status_code == 401