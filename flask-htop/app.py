import os
import platform
import time
import psutil
from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get user info
    full_name = "Sumanth Madala"  # Replace with your actual full name
    system_username = os.getlogin()

    # Get current time in IST (Indian Standard Time)
    ist_timezone = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist_timezone).strftime('%Y-%m-%d %H:%M:%S')

    # Get system stats like top command output
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent

    # Render the information
    return f"""
    <html>
    <head><title>System Information</title></head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {system_username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>

        <h2>Top Output (System Stats)</h2>
        <pre>
        CPU Usage: {cpu_percent}%
        Memory Usage: {memory_percent}%
        Disk Usage: {disk_percent}%
        </pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
