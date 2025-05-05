def test_register_owner_get(client):
    response = client.get('/register_owner')
    assert response.status_code == 200


def test_register_owner_post(client):
    response = client.post('/register_owner', data={
        'store_name': 'テスト店',
        'address': 'テスト住所',
        'business_hours': '10:00-20:00'
    }, follow_redirects=True)
    assert response.status_code == 200