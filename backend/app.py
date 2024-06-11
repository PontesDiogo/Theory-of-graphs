from flask import Flask, request, jsonify, render_template
from dijkstra import dijkstra

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')

# Grid estático para fins de exemplo
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shortest-path', methods=['POST'])
def shortest_path():
    data = request.get_json()
    start = tuple(data['start'])
    goal = tuple(data['goal'])
    
    paths = dijkstra(grid, start, goal)
    
    return jsonify({'paths': paths})

if __name__ == '__main__':
    app.run(debug=True)
