from app import app

def test_index():
    res = app.test_client().get("/")
    assert res.status_code == 200