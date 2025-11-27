Log Filter Web Application
A Flask-based web application that allows users to upload log files and filter content using regular expressions (Regex) with a graphical interface. This project is designed to be deployed on an Apache2 server using mod_wsgi.

Features
Drag & Drop Upload: Easy log file submission.

Multi-Keyword Filtering: Support for multiple regex filters (AND logic).

Live Preview: View filtered results instantly with line numbers.

Sub-directory Deployment: configured to run under /log_filter.

# Installation Guide
This guide is designed for Ubuntu / Debian systems (or WSL).

## Step 1: Install System Dependencies
On a fresh machine, install Apache, the Python WSGI module, and Git.

```
sudo apt update
sudo apt install apache2 libapache2-mod-wsgi-py3 python3-venv git -y
```

## Step 2: Clone the Repository
It is recommended to clone the project directly into /var/www/.

```
cd /var/www
```

Replace the URL below with your actual GitHub repository URL

```
sudo git clone [https://github.com/guanweichiang/log_filter_remake.git](https://github.com/guanweichiang/log_filter_remake.git) log_filter
```

## Step 3: Setup Python Virtual Environment
We need to install the required Python packages. (Note: We temporarily change permissions to the current user to run pip without issues.)

### 1. Temporarily take ownership of the directory
```
sudo chown -R $USER:$USER /var/www/log_filter
```
### 2. Enter the directory
```
cd /var/www/log_filter
```
### 3. Create the virtual environment
```
python3 -m venv venv
```
### 4. Activate venv and install dependencies
```
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

## Step 4: Configure app.wsgi (⚠️ Important)
Apache uses this file to launch your Python application. You must verify your Python version.

Check the Python version inside your virtual environment:

```
ls /var/www/log_filter/venv/lib/
# You will see a folder name like 'python3.10' or 'python3.12'
```

Edit the app.wsgi file:

```
nano app.wsgi
```

Ensure the path matches your Python version (Update python3.x accordingly):

```
import sys
import site

# CHANGE 'python3.12' below to match the folder name found in step 1
site.addsitedir('/var/www/log_filter/venv/lib/python3.12/site-packages')

sys.path.insert(0, '/var/www/log_filter')

from myapp import app as application
```

## Step 5: Configure Apache VirtualHost
Create a configuration file for the site.

Create the file:

```
sudo nano /etc/apache2/sites-available/log_filter.conf
```
Paste the following configuration:


```
<VirtualHost *:80>
    # Use 'localhost' for local testing, or your domain/IP for production
    ServerName localhost

    # WSGI Daemon Process configuration
    WSGIDaemonProcess log_filter python-home=/var/www/log_filter/venv python-path=/var/www/log_filter
    WSGIProcessGroup log_filter

    # Mount the application at /log_filter
    WSGIScriptAlias /log_filter /var/www/log_filter/app.wsgi

    # Directory permissions
    <Directory /var/www/log_filter>
        Require all granted
    </Directory>

    # Static files alias
    Alias /log_filter/static /var/www/log_filter/static
    <Directory /var/www/log_filter/static/>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

Enable the site and reload Apache:

```
sudo a2ensite log_filter.conf
# Optional: Disable the default Apache welcome page
sudo a2dissite 000-default.conf
```

## Step 6: Finalize Permissions (🚀 Crucial)
For Apache to function correctly and handle file uploads, ownership must be transferred to the www-data user.

```
# 1. Create the uploads directory (if it wasn't cloned)
sudo mkdir -p /var/www/log_filter/uploads

# 2. Transfer ownership to Apache
sudo chown -R www-data:www-data /var/www/log_filter

# 3. Grant write permissions to the uploads folder
sudo chmod -R 777 /var/www/log_filter/uploads

# 4. Restart Apache to apply changes
sudo systemctl restart apache2
```

# Verification & Troubleshooting
Accessing the App
Open your browser and visit: http://localhost/log_filter (Or http://<YOUR_SERVER_IP>/log_filter)

Common Errors
1. 500 Internal Server Error This usually indicates a Python version mismatch or missing packages. Check the error log:


```
sudo tail -n 20 /var/log/apache2/error.log
```
Solution: Check if ModuleNotFoundError appears. If so, fix the path in app.wsgi or run pip install again.

2. 403 Forbidden The server does not have permission to read the files.

Solution: Re-run the chown and chmod commands in Step 6.

3. Upload Failed / File Not Found

Solution: Ensure myapp.py uses an absolute path for UPLOAD_FOLDER (e.g., /var/www/log_filter/uploads) instead of /tmp.