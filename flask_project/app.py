from flask import Flask, render_template, request, redirect, url_for
from io import BytesIO
import base64
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/payment')
def payment():
    service = request.args.get('service')
    total_price = float(request.args.get('total_price'))
    reward = float(request.args.get('reward'))
    transaction_fee = float(request.args.get('transaction_fee'))

    qr_code_data = f"http://192.168.0.34:5000/processing?service={service}&total_price={total_price}&reward={reward}&transaction_fee={transaction_fee}"
    img = qrcode.make(qr_code_data)

    buffered = BytesIO()
    img.save(buffered, format="PNG")
    qr_code_b64 = base64.b64encode(buffered.getvalue()).decode()

    return render_template("payment.html", qr_code_b64=qr_code_b64, total=total_price, reward=reward, transaction_fee=transaction_fee)

@app.route('/generate_qr_code_request/<service>', methods=['POST'])
def generate_qr_code_request(service):
    services = {
        "chiropractic": {
            "price": 100,
            "reward": 28,
            "transaction_fee": 1
        },
        "acupuncture": {
            "price": 120,
            "reward": 33.5,
            "transaction_fee": 1.5
        },
        "massage": {
            "price": 50,
            "reward": 14.5,
            "transaction_fee": 0.5
        }
    }

    service_info = services.get(service)

    if not service_info:
        return redirect(url_for('index'))

    total_price = service_info['price']
    reward = service_info['reward']
    transaction_fee = service_info['transaction_fee']

    return redirect(url_for('payment', service=service, total_price=total_price, reward=reward, transaction_fee=transaction_fee))

@app.route('/processing')
def processing():
    service = request.args.get('service')
    total_price = float(request.args.get('total_price'))
    reward = float(request.args.get('reward'))
    transaction_fee = float(request.args.get('transaction_fee'))

    return render_template("processing.html", service=service, total=total_price, reward=reward, transaction_fee=transaction_fee)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
