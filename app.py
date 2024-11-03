from flask import Flask, render_template_string
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    html_content = """
    <html>
        <head>
            <title>N3TWork</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #e0f7fa; color: #333; margin: 0; padding: 0; }
                .container { max-width: 600px; margin: 50px auto; padding: 20px; background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); text-align: center; }
                h1 { color: #007acc; font-size: 2em; margin-bottom: 10px; }
                .info-box { display: flex; align-items: center; justify-content: center; padding: 15px; margin: 10px 0; border: 1px solid #ddd; border-radius: 8px; transition: box-shadow 0.3s ease; }
                .info-box:hover { box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15); }
                .icon { font-size: 1.8em; color: #007acc; margin-right: 10px; }
                .info { font-size: 1.2em; color: #333; }
                footer { margin-top: 30px; font-size: 0.9em; color: #888; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Server Information</h1>
                <div class="info-box">
                    <span class="icon">🖥️</span><span class="info">Hostname: {{ hostname }}</span>
                </div>
                <div class="info-box">
                    <span class="icon">🌐</span><span class="info">IP Address: {{ ip_address }}</span>
                </div>
            </div>
        </body>
    </html>
    """
    return render_template_string(html_content, hostname=hostname, ip_address=ip_address)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
