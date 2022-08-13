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
