import pytest
import json
import requests
import os
import time

BASE_URL = "http://localhost:5000"

# Load data from JSON file (for POST/PUT requests)
def load_request_data():
    file_path = os.path.join('src', 'db.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    print(data["users"][1])
    return data["users"][1]


#-----------------------------------------------GET-5--------------------------------------------------
# def test_status_code_get():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    assert response.status_code == 200

def test_response_time_get():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    assert response.elapsed.total_seconds() * 1000 < 300

# Test for the presence of Content-Type header
def test_content_type_is_present_get():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    assert "Content-Type" in response.headers

# Test if response body is a non-empty array
def test_response_body_is_non_empty_array_get():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    json_data = response.json()
    assert isinstance(json_data, list)
    assert len(json_data) > 0

# Test if response is an array
def test_response_is_array_get():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    json_data = response.json()
    assert isinstance(json_data, list)

#-----------------------------------------------DELETE-5--------------------------------------------------

# Test for a successful DELETE request
def test_successful_delete_request():
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url)
    assert response.status_code in [200, 202, 204]


# Test for response time being less than 300ms
def test_response_time_delete():
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url)
    assert response.elapsed.total_seconds() * 1000 < 300


# Test for the response body being a success message
def test_response_body_is_success_message_delete():
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url)
    response_json = response.json()
    expected_response = {
        "message": "Post deleted",
        "status": "success"
    }
    assert response_json == expected_response, f"Expected {expected_response}, but got {response_json}"


# Test for the presence of Content-Type header
def test_content_type_is_present_delete():
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url)
    assert "Content-Type" in response.headers


# Test for verifying that the post is actually deleted (404 for a non-existing post)
def test_post_is_deleted():
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url)
    assert response.status_code in [200, 202, 204]  # Make sure the DELETE request was successful
    response = requests.get(url)
    assert response.status_code == 404, f"Expected 404, but got {response.status_code}. Response body: {response.text}"


#---------------------------------------PUT--------------------------------------------

# Test for a successful PUT request
def test_successful_put_request():
    url = f"{BASE_URL}/posts/1"  
    payload = load_request_data() 
    response = requests.put(url, json=payload)
    assert response.status_code in [200, 201, 204]

# Test for a successful PUT request
def test_successful_put_request():
    url = f"{BASE_URL}/posts/1"  
    payload = load_request_data()
    response = requests.put(url, json=payload)
    assert response.status_code == 200  

# Test for status code 200 with PUT request
def test_status_code_put():
    url = f"{BASE_URL}/posts/1"  
    payload = load_request_data()
    response = requests.put(url, json=payload)
    assert response.status_code == 200  

# Test for correct response body when updating a resource
def test_response_body_put():
    url = f"{BASE_URL}/posts/1"  
    payload = load_request_data()
    response = requests.put(url, json=payload)
    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert response_data["id"] == 1
    assert "title" in response_data  

# Test for failed PUT request (e.g., invalid data)
def test_failed_put_request():
    url = f"{BASE_URL}/posts/1"  
    invalid_payload = {"title": "Updated Post"} 
    response = requests.put(url, json=invalid_payload)
    assert response.status_code == 400  

#Test for the presence of Content-Type header
def test_content_type_is_present_put():
    url = f"{BASE_URL}/posts/1"
    payload = load_request_data()  
    response = requests.put(url, json=payload)
    assert "Content-Type" in response.headers



#---------------------------------------POST--------------------------------------------

# Test for a successful POST request
def test_successful_post_request():
    url = f"{BASE_URL}/posts"
    payload = load_request_data()  
    response = requests.post(url, json=payload)
    assert response.status_code in [200, 201]

# Test for status code 201
def test_status_code_post():
    url = f"{BASE_URL}/posts"
    payload = load_request_data()  
    response = requests.post(url, json=payload)
    assert response.status_code == 201

# Test for presence of Content-Type header
def test_content_type_header_post():
    url = f"{BASE_URL}/posts"
    payload = load_request_data() 
    response = requests.post(url, json=payload)
    assert "Content-Type" in response.headers

# Test for correct response body when posting data
def test_response_body_post():
    url = f"{BASE_URL}/posts"
    payload = load_request_data()
    response = requests.post(url, json=payload)
    assert response.status_code in [200, 201]
    response_data = response.json()
    assert "id" in response_data
    assert "title" in response_data

# Test for failed POST request (e.g., invalid data)
def test_failed_post_request():
    url = f"{BASE_URL}/posts"
    invalid_payload = {"title": "Test Post"}  
    response = requests.post(url, json=invalid_payload)
    assert response.status_code == 400  