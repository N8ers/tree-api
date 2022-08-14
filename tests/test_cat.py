import json

# dummy_cat_data = [
#     {
#         "name": "Whiskey",
#         "size": "small n tuff",
#         "color": "orange"
#     },
#     {
#         "name": "Skittles",
#         "color": "rainbow",
#         "size": "very small"
#     }
# ]


def test_get_cats(client):
    response = client.get('/cat/')
    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert response_data == [
        {"color": "black", "name": "Tsuki", "size": "This big"}
    ]


def test_create_cat(client):
    response = client.post(
        '/cat/',
        data=json.dumps({
            "name": "Whiskey",
            "size": "small n tuff",
            "color": "orange"
        })
    )

    assert response.status_code == 201
    response_data = response.data.decode("utf-8")
    assert response_data == 'Whiskey was created.'


def test_delete_cat(client):
    # Create cat
    post_response = client.post(
        '/cat/',
        data=json.dumps({
            "name": "Skittles",
            "color": "rainbow",
            "size": "very small"
        })
    )

    assert post_response.status_code == 201
    response_data = post_response.data.decode("utf-8")
    assert response_data == 'Skittles was created.'

    # Delete cat - this is not a good test
    response = client.get('/cat/')
    response_length_before_delete = len(json.loads(response.data))

    delete_response = client.delete('/cat/2')
    assert delete_response.status_code == 200

    response = client.get('/cat/')
    response_length_after_delete = len(json.loads(response.data))

    assert response_length_before_delete == response_length_after_delete + 1
