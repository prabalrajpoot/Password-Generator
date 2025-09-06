from flask import Flask, jsonify
import time, random

app = Flask(__name__)

@app.route('/health')
def health():
    delay = random.uniform(0.05,0.6); time.sleep(delay)
    if random.random() < 0.05: return jsonify({'status':'error'}), 500
    return jsonify({'status':'ok','delay':delay})

if __name__ == '__main__': app.run(port=5000)
