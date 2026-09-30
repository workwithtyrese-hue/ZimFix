from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>ZimFix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background: #f5f5f5;
            color: #222;
        }

        .header {
            background: #111;
            color: white;
            padding: 35px 20px;
            text-align: center;
        }

        .logo {
            font-size: 42px;
            font-weight: bold;
        }

        .container {
            max-width: 650px;
            margin: 25px auto;
            padding: 15px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 18px;
            margin-bottom: 20px;
            box-shadow: 0 3px 12px rgba(0,0,0,0.08);
        }

        h2 {
            margin-top: 0;
        }

        input, select {
            width: 100%;
            padding: 14px;
            margin-top: 7px;
            border: 1px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-top: 18px;
        }

        button, .button {
            display: block;
            width: 100%;
            background: #111;
            color: white;
            border: none;
            padding: 16px;
            border-radius: 10px;
            font-size: 17px;
            margin-top: 22px;
            text-align: center;
            text-decoration: none;
        }

        .back {
            background: #eee;
            color: #111;
        }
    </style>
</head>

<body>

<div class="header">
    <div class="logo">🔧 ZimFix</div>
    <p>Find trusted service providers in Zimbabwe</p>
</div>

<div class="container">

    <div class="card">
        <h2>🔎 Need a Service?</h2>
        <p>Find a professional near you.</p>

        <a class="button" href="/request">
            Find a Service Provider
        </a>
    </div>

    <div class="card">
        <h2>👷 Are you a professional?</h2>
        <p>Join ZimFix and get customers looking for your services.</p>

        <a class="button" href="/provider">
            Join as a Provider
        </a>
    </div>

</div>

</body>
</html>
"""


@app.route("/provider", methods=["GET", "POST"])
def provider():

    if request.method == "POST":

        name = request.form.get("name")
        phone = request.form.get("phone")
        service = request.form.get("service")
        location = request.form.get("location")

        return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Provider Registered - ZimFix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }}

        .card {{
            max-width: 600px;
            margin: 40px auto;
            background: white;
            padding: 30px;
            border-radius: 18px;
            text-align: center;
        }}

        .button {{
            display: block;
            background: #111;
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-decoration: none;
            margin-top: 20px;
        }}
    </style>
</head>

<body>

<div class="card">

    <h1>🎉 Welcome to ZimFix!</h1>

    <p>Your provider profile has been received.</p>

    <hr>

    <p><strong>Name:</strong> {name}</p>
    <p><strong>Phone:</strong> {phone}</p>
    <p><strong>Service:</strong> {service}</p>
    <p><strong>Location:</strong> {location}</p>

    <a class="button" href="/">
        Back to ZimFix
    </a>

</div>

</body>
</html>
"""

    return """
<!DOCTYPE html>
<html>
<head>
    <title>Join ZimFix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            margin: 0;
            padding: 20px;
        }

        .card {
            max-width: 600px;
            margin: 20px auto;
            background: white;
            padding: 25px;
            border-radius: 18px;
        }

        h1 {
            margin-top: 0;
        }

        label {
            display: block;
            font-weight: bold;
            margin-top: 18px;
        }

        input, select {
            width: 100%;
            padding: 14px;
            margin-top: 7px;
            border: 1px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
        }

        button {
            width: 100%;
            background: #111;
            color: white;
            border: none;
            padding: 16px;
            border-radius: 10px;
            font-size: 17px;
            margin-top: 25px;
        }

        .back {
            display: block;
            text-align: center;
            margin-top: 20px;
            color: #555;
        }
    </style>
</head>

<body>

<div class="card">

    <h1>👷 Join ZimFix</h1>

    <p>Get customers looking for your services.</p>

    <form method="POST">

        <label>Your name or business name</label>

        <input
            type="text"
            name="name"
            placeholder="e.g. Tinashe Plumbing"
            required
        >

        <label>Phone number</label>

        <input
            type="tel"
            name="phone"
            placeholder="e.g. 0771234567"
            required
        >

        <label>What service do you provide?</label>

        <select name="service" required>

            <option value="">Choose your service</option>

            <option>🔧 Plumbing</option>
            <option>⚡ Electrical</option>
            <option>🚗 Mechanic</option>
            <option>🧱 Building</option>
            <option>🧹 Cleaning</option>
            <option>🌳 Gardening</option>
            <option>❄️ Appliance Repair</option>
            <option>🔨 General Handyman</option>
            <option>📸 Photography</option>
            <option>🎵 DJ / Events</option>

        </select>

        <label>Where do you operate?</label>

        <input
            type="text"
            name="location"
            placeholder="e.g. Bulawayo"
            required
        >

        <button type="submit">
            Create Provider Profile
        </button>

    </form>

    <a class="back" href="/">
        ← Back to ZimFix
    </a>

</div>

</body>
</html>
"""


@app.route("/request")
def request_page():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Find a Provider - ZimFix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }

        .card {
            max-width: 600px;
            margin: 20px auto;
            background: white;
            padding: 25px;
            border-radius: 18px;
        }

        .button {
            display: block;
            background: #111;
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            text-decoration: none;
            margin-top: 20px;
        }
    </style>
</head>

<body>

<div class="card">

    <h1>🔎 Find a Provider</h1>

    <p>
        The customer request system is already available
        from the previous version.
    </p>

    <a class="button" href="/">
        ← Back to ZimFix
    </a>

</div>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
