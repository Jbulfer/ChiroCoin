<!DOCTYPE html>
<html>
<head>
    <title>Processing Payment</title>
</head>
<body>
    <h1>Processing Payment</h1>
    <p>Total Price: {{ total }}</p>
    <p>Reward: {{ reward }}</p>
    <p>Transaction Fee: {{ transaction_fee }}</p>
    <button id="connect-wallet">Connect XUMM Wallet</button>
    
    <script src="{{ url_for('static', filename='xumm.js') }}"></script>
</body>
</html>
