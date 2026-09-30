from flask import Flask

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
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background: #f5f5f5;
                color: #222;
            }

            .header {
                background: #111;
                color: white;
                padding: 25px;
                text-align: center;
            }

            .container {
                max-width: 600px;
                margin: 30px auto;
                padding: 20px;
            }

            .card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                margin-bottom: 15px;
                box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            }

            h1 {
                margin-bottom: 5px;
            }

            .button {
                display: block;
                background: #111;
                color: white;
                text-decoration: none;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                margin-top: 15px;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <h1>🔧 ZimFix</h1>
            <p>Find trusted service providers in Zimbabwe</p>
        </div>

        <div class="container">

            <div class="card">
                <h2>Need a service?</h2>
                <p>Find a trusted professional near you.</p>

                <a class="button" href="#">
                    Find a Service Provider
                </a>
            </div>

            <div class="card">
                <h2>Are you a professional?</h2>
                <p>Get customers looking for your services.</p>

                <a class="button" href="#">
                    Join as a Provider
                </a>
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
