# Log Filter Viewer

A simple and lightweight web-based tool built with Python and Flask to filter specific lines in log files using multiple keywords and regular expressions.

---

## Overview

`log_filter` allows users to upload `.log` or `.txt` files through a browser interface and instantly filter log content based on:

- One or more keywords
- Regular expression (regex) queries
- Toggleable filters for real-time control

This tool is especially useful for debugging or analyzing large log files efficiently.

---

## Features

- Filter log files by multiple keywords
- Toggle individual filters on or off in real-time
- Supports regular expressions (regex)
- Drag & drop file upload
- Clean and responsive web interface
- Results update immediately as filters are applied

---

## Installation

### Requirements

- Python 3.8 or higher
- Flask

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/guanweichiang/log_filter.git
   cd log_filter
   ```

2. Install Flask:

   ```bash
   pip install Flask
   ```

3. Usage

   1.Run the app:

   ```bash
   python app.py
   ```
   2.Open your browser and go to the address shown in the terminal
   (usually http://127.0.0.1:5000)
   
   3.Upload your .log or .txt file via the drag & drop area
   
   4.Enter one or more keywords or regular expressions into the filter list
   
   5.Toggle filters on or off to dynamically update the displayed results 

4. Development Environment
   
   Language: Python 3.x
   Framework: Flask