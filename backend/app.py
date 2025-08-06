import os
import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This allows the frontend to talk to the backend

def get_db_connection():
    conn = psycopg2.connect(
        host="poll-db", # This is the service name of our database in Docker Compose
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
    return conn

@app.route('/poll', methods=['GET'])
def get_poll():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, option_name, votes FROM polls ORDER BY id;')
    poll_results = cur.fetchall()
    cur.close()
    conn.close()
    # Format the results as a list of dictionaries
    results = [{'id': row[0], 'option': row[1], 'votes': row[2]} for row in poll_results]
    return jsonify(results)

@app.route('/poll/<int:option_id>', methods=['POST'])
def vote(option_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE polls SET votes = votes + 1 WHERE id = %s;', (option_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'success', 'message': f'Voted for option {option_id}'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)