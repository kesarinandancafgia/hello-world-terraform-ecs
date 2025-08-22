from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World - Terraform ECS Project</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 40px;
                background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);
                color: white;
                text-align: center;
            }}
            .container {{
                background: rgba(255,255,255,0.1);
                border-radius: 10px;
                padding: 40px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                border: 1px solid rgba(255,255,255,0.18);
                max-width: 600px;
                margin: 0 auto;
            }}
            h1 {{
                font-size: 3em;
                margin-bottom: 20px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }}
            .info {{
                background: rgba(50,50,255,0.2);
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
            }}
            .success {{
                color: red;
                font-weight: bold;
                font-size: 1.2em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Hello World! 🎉</h1>
            <div class="success">✅ Terraform + ECS + Docker Deployment Successful!</div>
            
            <div class="info">
                <h3>🚀 Application Details</h3>
                <p><strong>Hostname:</strong> Kesari Nandan</p>
                <p><strong>Timestamp:</strong> {timestamp}</p>
                <p><strong>Python Version:</strong> 3.9+</p>                
            </div>
            
            <div class="info">
                <h3>🏗️ Infrastructure</h3>
                <p><strong>Platform:</strong> AWS ECS with Fargate</p>
                <p><strong>Load Balancer:</strong> Application Load Balancer</p>
                <p><strong>Container Registry:</strong> Amazon ECR</p>
                <p><strong>CI/CD:</strong> GitHub Actions</p>
            </div>
            
            <div class="info">
                <h3>🎯 Project Status</h3>
                <p class="success">All systems operational! 🟢</p>
                <p>Your Terraform project is working perfectly!</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

@app.route('/health')
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname()
    }

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=False)