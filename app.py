from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def rajak_number_api():
    number = request.args.get('num')
    
    if not number:
        return jsonify({
            'error': 'Number parameter is required',
            'example': '/?num=9876543210',
            'developer': 'https://t.me/rajakkhan4x'
        }), 400
    
    try:
        # Call original happy API
        response = requests.get(f'https://happy-api-app.vercel.app/?num={number}')
        original_data = response.json()
        
        # Rajak modified response
        rajak_data = {
            **original_data,
            'dev': 'https://t.me/rajakkhan4x',
            'developer': 'Rajak Khan',
            'credit': 'Rajak Number Info API',
            'telegram': 'https://t.me/rajakkhan4x',
            'website': 'https://t.me/rajakkhan4x'
        }
        
        return jsonify(rajak_data)
        
    except Exception as e:
        return jsonify({
            'error': 'Failed to fetch number information',
            'dev': 'https://t.me/rajakkhan4x',
            'contact': 'https://t.me/rajakkhan4x'
        }), 500

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'active',
        'service': 'Rajak Number Info API',
        'developer': 'https://t.me/rajakkhan4x'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)