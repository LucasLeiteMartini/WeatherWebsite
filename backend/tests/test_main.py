"""TODO add comentários"""


def test_read_main(client):
    """TODO add comentários"""

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_search_location(client):
    response = client.post("/map/ufam")

    assert response.status_code == 200
    assert response.json() == {
        "address": "Federal Univ of Amazonas - Av. General Rodrigo Octavio Jordão Ramos, 1200 - Coroado I, Manaus - AM, 69067-005, Brazil",
        "lng": -59.9765378,
        "lat": -3.1002425,
    }
