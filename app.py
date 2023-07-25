# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the GeoLite2-ASN database
import geoip2.database
reader = geoip2.database.Reader('GeoLite2-ASN.mmdb')

@app.route('/geolocate', methods=['GET'])
def geolocate_by_ip():
    try:
        ip_address = request.args.get('ip')

        if not ip_address:
            return jsonify({'error': 'Please provide an IP address.'})

        # Perform geolocation lookup by IP address
        response = reader.asn(ip_address)
        return jsonify(response.raw)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
