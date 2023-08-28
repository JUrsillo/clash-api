from flask import Flask, jsonify
import requests
app = Flask(__name__)
data = []

def get_person():
    global data
    url = 'https://api.clashofclans.com/v1/players/%238YLJRVGG'
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjJlNTNkOGNkLWNlM2ItNGVmNS04MTlmLWJjZjQ4ZmNjZGM4YiIsImlhdCI6MTY5MzE3Mjg5OSwic3ViIjoiZGV2ZWxvcGVyL2UwZjdlMzQxLTdmOWQtZWE5Ny01MzgwLWJhYTY5OGIxZWNjNSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc2LjEwMi41Mi4xODMiXSwidHlwZSI6ImNsaWVudCJ9XX0.PrLszp1wPcT8ZBLkVnLpSbTJNLubPYqirH5Dcs-temvG5OSXMB7Io2mmxm-qLvMd8gxJiSH7jDGN2BHxzb_4kw',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("Response data:", data)
    else:
        print("Request failed with status code:", response.status_code)


# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Route to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/api/clash/person', methods=['GET'])
def api_get_person():
    get_person()
    return jsonify(data)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)