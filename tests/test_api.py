import requests

def test_predict():
    sample_input = [[0.1, 0.2, 0.3, 0.4]]  # Adjust dimensions
    response = requests.post("http://localhost:5000/predict", json=sample_input)
    assert response.status_code == 200