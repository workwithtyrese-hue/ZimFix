from flask import Flask, request
import os
import psycopg2

app = Flask(__name__)


def get_db():
    return psycopg2.connect(os.environ["DATABASE_URL"])


def setup_database():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS providers (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            service TEXT NOT NULL,
            location TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id SERIAL PRIMARY KEY,
            service TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT NOT NULL,
            phone TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id SERIAL PRIMARY KEY,
            job_id INTEGER REFERENCES jobs(id),
            provider_id INTEGER REFERENCES providers(id),
            amount NUMERIC NOT NULL,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ZimFix</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial;
                background: #f5f5f5;
                margin: 0;
            }

            .header {
                background: #111;
                color: white;
                text-align: center;
                padding: 35px 20px;
            }

            .logo {
                font-size: 40px;
                font-weight: bold;
            }

            .container {
                max-width: 600px;
                margin: 25px auto;
                padding: 15px;
            }

            .card {
                background: white;
                padding: 25px;
                border-radius: 18px;
                margin-bottom: 20px;
            }

            .button {
                display: block;
                background: #111;
                color: white;
                padding: 16px;
                border-radius: 10px;
                text-align: center;
                text-decoration: none;
                margin-top: 15px;
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
                <h2>🔎 Need a service?</h2>
                <p>Find a professional near you.</p>
                <a class="button" href="/request">
                    Find a Service Provider
                </a>
            </div>

            <div class="card">
                <h2>👷 Are you a professional?</h2>
                <p>Get customers looking for your services.</p>
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

        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO providers
            (name, phone, service, location)
            VALUES (%s, %s, %s, %s)
        """, (name, phone, service, location))

        conn.commit()
        cur.close()
        conn.close()

        return """
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {
                    font-family: Arial;
                    background: #f5f5f5;
                    padding: 20px;
                }

                .card {
                    max-width: 600px;
                    margin: 40px auto;
                    background: white;
                    padding: 30px;
                    border-radius: 18px;
                    text-align: center;
                }

                a {
                    display: block;
                    background: #111;
                    color: white;
                    padding: 15px;
                    border-radius: 10px;
                    text-decoration: none;
                    margin-top: 20px;
                }
            </style>
        </head>

        <body>
            <div class="card">
                <h1>🎉 Welcome to ZimFix!</h1>
                <p>Your provider profile has been saved.</p>
                <p>We'll use your profile to connect you with customers.</p>

                <a href="/">
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
            body {
                font-family: Arial;
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
                box-sizing: border-box;
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

            a {
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

                <label>Name or business name</label>
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

                <label>Service</label>

                <select name="service" required>
                    <option value="">Choose your service</option>
                    <option>Plumbing</option>
                    <option>Electrical</option>
                    <option>Mechanic</option>
                    <option>Building</option>
                    <option>Cleaning</option>
                    <option>Gardening</option>
                    <option>Appliance Repair</option>
                    <option>General Handyman</option>
                    <option>Photography</option>
                    <option>DJ / Events</option>
                </select>

                <label>Location</label>

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

            <a href="/">← Back to ZimFix</a>

        </div>

    </body>
    </html>
    """


@app.route("/request", methods=["GET", "POST"])
def job_request():

    if request.method == "POST":

        service = request.form.get("service")
        location = request.form.get("location")
        description = request.form.get("description")
        phone = request.form.get("phone")

        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO jobs
            (service, location, description, phone)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (service, location, description, phone))

        job_id = cur.fetchone()[0]

        conn.commit()
        cur.close()
        conn.close()

        return f"""
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {{
                    font-family: Arial;
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

                a {{
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
            <h1>✅ Request Submitted!</h1>

            <p>Your job request has been saved.</p>

            <p><strong>Request #{{job_id}}</strong></p>

            <p>We'll use this request to connect you with service providers.</p>

            <a href="/">
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
        <title>Find a Provider</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            body {
                font-family: Arial;
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

            label {
                display: block;
                font-weight: bold;
                margin-top: 18px;
            }

            input, select, textarea {
                width: 100%;
                padding: 14px;
                margin-top: 7px;
                border: 1px solid #ddd;
                border-radius: 10px;
                font-size: 16px;
                box-sizing: border-box;
            }

            textarea {
                min-height: 120px;
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

            a {
                display: block;
                text-align: center;
                margin-top: 20px;
                color: #555;
            }
        </style>
    </head>

    <body>

    <div class="card">

        <h1>🔎 Find a Provider</h1>

        <form method="POST">

            <label>What service do you need?</label>

            <select name="service" required>
                <option value="">Choose a service</option>
                <option>Plumbing</option>
                <option>Electrical</option>
                <option>Mechanic</option>
                <option>Building</option>
                <option>Cleaning</option>
                <option>Gardening</option>
                <option>Appliance Repair</option>
                <option>General Handyman</option>
                <option>Photography</option>
                <option>DJ / Events</option>
            </select>

            <label>Location</label>

            <input
                type="text"
                name="location"
                placeholder="e.g. Hillside, Bulawayo"
                required
            >

            <label>Describe the job</label>

            <textarea
                name="description"
                placeholder="Tell us what needs to be done..."
                required
            ></textarea>

            <label>Phone number</label>

            <input
                type="tel"
                name="phone"
                placeholder="e.g. 0771234567"
                required
            >

            <button type="submit">
                Submit Request
            </button>

        </form>

        <a href="/">← Back to ZimFix</a>

    </div>

    </body>
    </html>
    """


# Create database tables when the app starts
try:
    setup_database()
except Exception as e:
    print("Database setup error:", e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
