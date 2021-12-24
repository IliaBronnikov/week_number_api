from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_week_number():
    response = client.get("/", params={"date": "2020-11-25"})

    assert response.status_code == 200
    assert response.json() == {"week_number": 48, "date": "2020-11-25"}
