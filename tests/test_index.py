def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'モードを選択してください'.encode('utf-8') in response.data