from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        service = request.form.get("service")
        location = request.form.get("location")
        description = request.form.get("description")
        phone = request.form.get("phone")

        message = f"""
        <div class="success">
            <h2>✅ Request received!</h2>
            <p>We're looking for a <strong>{service}</strong> provider for you.</p>
            <p><strong>Location:</strong> {location}</p>
            <p>Providers will be able to contact you at <strong>{phone}</strong>.</p>
        </div>
        """

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>ZimFix - Find Local Services</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            background: #f5f5f5;
            color: #222;
        }}

        .header {{
            background: #111;
            color: white;
            padding: 35px 20px;
            text-align: center;
        }}

        .logo {{
            font-size: 42px;
            font-weight: bold;
        }}

        .header p {{
            font-size: 18px;
            margin-bottom: 0;
        }}

        .container {{
            max-width: 650px;
            margin: 25px auto;
            padding: 15px;
        }}

        .card {{
            background: white;
            padding: 25px;
            border-radius: 18px;
            margin-bottom: 20px;
            box-shadow: 0 3px 12px rgba(0,0,0,0.08);
        }}

        h2 {{
            margin-top: 0;
        }}

        label {{
            display: block;
            font-weight: bold;
            margin-top: 18px;
            margin-bottom: 7px;
        }}

        select,
        input,
        textarea {{
            width: 100%;
            padding: 14px;
            border: 1px solid #ddd;
            border-radius: 10px;
            font-size: 16px;
        }}

        textarea {{
            min-height: 120px;
            resize: vertical;
        }}

        .button {{
            width: 100%;
            background: #111;
            color: white;
            border: none;
            padding: 16px;
            border-radius: 10px;
            font-size: 17px;
            margin-top: 22px;
            cursor: pointer;
        }}

        .services {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-top: 15px;
        }}

        .service {{
            background: #f2f2f2;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
        }}

        .success {{
            background: #e8f7e8;
            border: 1px solid #9ad29a;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
        }}

        .provider {{
            text-align: center;
        }}

        .provider-button {{
            display: block;
            background: #111;
            color: white;
            text-decoration: none;
            padding: 15px;
            border-radius: 10px;
            margin-top: 15px;
        }}
    </style>
</head>

<body>

<div class="header">
    <div class="logo">🔧 ZimFix</div>
    <p>Find trusted service providers in Zimbabwe</p>
</div>

<div class="container">

    {message}

    <div class="card">
        <h2>🔎 Find a Service Provider</h2>
        <p>Tell us what you need and where you need it.</p>

        <form method="POST">

            <label>What service do you need?</label>

            <select name="service" required>
                <option value="">Choose a service</option>
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

            <label>Where are you located?</label>

            <input
                type="text"
                name="location"
                placeholder="e.g. Hillside, Bulawayo"
                required
            >

            <label>Describe the job</label>

            <textarea
                name="description"
                placeholder="Tell the provider what needs to be done..."
                required
            ></textarea>

            <label>Your phone number</label>

            <input
                type="tel"
                name="phone"
                placeholder="e.g. 0771234567"
                required
            >

            <button class="button" type="submit">
                Find Me a Provider
            </button>

        </form>
    </div>

    <div class="card">
        <h2>🛠️ Popular Services</h2>

        <div class="services">
            <div class="service">🔧 Plumbing</div>
            <div class="service">⚡ Electrical</div>
            <div class="service">🚗 Mechanics</div>
            <div class="service">🧹 Cleaning</div>
            <div class="service">🌳 Gardening</div>
            <div class="service">🧱 Building</div>
            <div class="service">📸 Photography</div>
            <div class="service">🎵 Events</div>
        </div>
    </div>

    <div class="card provider">
        <h2>👷 Are you a professional?</h2>
        <p>Get customers looking for your services.</p>

        <a class="provider-button" href="#">
            Join ZimFix as a Provider
        </a>
    </div>

</div>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
