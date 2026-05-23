# Instagram Non-Followers Finder

A desktop application built using Python and Tkinter that helps Instagram users identify accounts they follow that do not follow them back.

This project uses Instagram's official account data export feature and performs all analysis locally on the user's machine. No login credentials are required, and no data is sent to any external server.

---

# Table of Contents

1. Project Overview
2. Features
3. How the Application Works
4. Prerequisites
5. Downloading Your Instagram Data
6. Extracting the Instagram Export
7. Project Setup
8. Folder Structure
9. Running the Application
10. Using the Application
11. Exporting Results
12. Screenshots
13. Troubleshooting
14. Technologies Used
15. Privacy and Security
16. Future Improvements
17. Author

---

# Project Overview

Instagram does not provide a built-in feature to identify users who do not follow you back.

This application solves that problem by comparing:

- Accounts following you
- Accounts you are following

and generating a list of users who do not follow you back.

The application provides a simple graphical user interface (GUI) where users can:

- Browse non-followers one by one
- Open profiles directly in Instagram
- Navigate through results
- Export results to CSV format

---

# Features

### Core Features

✔ Analyze Instagram follower data

✔ Find accounts that do not follow you back

✔ Display follower statistics

✔ Display following statistics

✔ Calculate non-followers automatically

✔ Browse accounts individually

✔ Open Instagram profiles directly from the application

✔ Export non-followers list to CSV

✔ User-friendly graphical interface

---

### Benefits

- No Instagram login required
- No password storage
- No browser automation
- No scraping
- Uses official Instagram export files
- Works completely offline

---

# How the Application Works

Instagram allows users to download a copy of their account data.

The exported data contains information such as:

- Followers
- Following
- Messages
- Stories
- Saved information
- Account activity

This project only uses:

```text
followers_1.json
following.json
```

The application performs the following operation:

```python
non_followers = following - followers
```

Example:

Followers:

```text
alice
bob
charlie
```

Following:

```text
alice
bob
charlie
david
emma
```

Result:

```text
david
emma
```

These users are being followed by you but are not following you back.

---

# Prerequisites

Before running the application, make sure you have:

- Python 3.10 or newer
- Instagram account
- Instagram data export files

Check your Python version:

```bash
python --version
```

Expected output:

```bash
Python 3.10.0
```

or higher.

---

# Downloading Your Instagram Data

The application requires Instagram export files.

Follow these steps carefully.

---

## Method 1 – Mobile Application

### Step 1

Open Instagram.

### Step 2

Tap your profile picture.

### Step 3

Tap:

```text
☰ Menu
```

### Step 4

Open:

```text
Settings and Privacy
```

### Step 5

Go to:

```text
Accounts Center
```

### Step 6

Select:

```text
Your Information and Permissions
```

### Step 7

Choose:

```text
Download Your Information
```

### Step 8

Select:

```text
Download or Transfer Information
```

### Step 9

Choose your Instagram account.

### Step 10

Select:

```text
Some of your information
```

### Step 11

Choose:

```text
Followers and Following
```

### Step 12

Continue.

### Step 13

Choose:

```text
Download to device
```

### Step 14

Select:

```text
Format: JSON
```

### Step 15

Submit request.

Instagram will prepare your data and send a download link.

This process may take several minutes or hours depending on account size.

---

# Extracting the Instagram Export

After downloading:

You will receive a ZIP archive similar to:

```text
instagram-data.zip
```

Extract it.

Inside the extracted folder, locate:

```text
connections/
```

Inside:

```text
connections/
├── followers_1.json
├── following.json
```

These are the files required by this project.

---

# Project Setup

## Step 1

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Instagram-NonFollowers-Finder.git
```

## Step 2

Navigate into the project folder:

```bash
cd Instagram-NonFollowers-Finder
```

## Step 3

Create a folder named:

```text
connections
```

if it does not already exist.

## Step 4

Copy:

```text
followers_1.json
following.json
```

from your Instagram export into the connections folder.

Example:

```text
Instagram-NonFollowers-Finder/
│
├── app.py
│
├── connections/
│   ├── followers_1.json
│   └── following.json
│
├── screenshots/
│   └── preview.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Running the Application

Open a terminal inside the project folder.

Run:

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

The graphical interface will open automatically.

---

# Using the Application

When the application starts:

### Dashboard

The application calculates:

- Total followers
- Total following
- Total non-followers

Example:

```text
Followers: 520
Following: 810
Non-Followers: 290
```

---

### Browsing Results

The application displays one username at a time.

Example:

```text
@example_username
```

---

### Open Profile

Click:

```text
Open Profile
```

The selected Instagram profile opens in your default browser.

---

### Next User

Click:

```text
Next
```

to view the next account.

---

### Previous User

Click:

```text
Previous
```

to return to the previous account.

---

# Exporting Results

Click:

```text
Export CSV
```

The application generates:

```text
non_followers.csv
```

Example:

```csv
Username
user1
user2
user3
```

This file can be opened in:

- Microsoft Excel
- Google Sheets
- LibreOffice Calc

---

# Screenshots

## Main Window

![Application Preview](screenshots/preview.png)

---

# Troubleshooting

## Error: File Not Found

Example:

```text
FileNotFoundError
```

Cause:

Instagram export files are missing.

Solution:

Verify:

```text
connections/followers_1.json
connections/following.json
```

exist inside the project.

---

## Error: JSON Decode Error

Cause:

Corrupted Instagram export.

Solution:

Download a fresh export from Instagram.

---

## Error: No Non-Followers Found

Cause:

Either:

- Everyone follows you back
- Incorrect export files were used

Verify the correct files were copied.

---

# Technologies Used

### Programming Language

- Python

### Libraries

- tkinter
- json
- csv
- webbrowser

### Data Format

- JSON

### Platform

- Windows
- Linux
- macOS

---

# Privacy and Security

This project was designed with privacy in mind.

The application:

✔ Does not require Instagram login

✔ Does not store passwords

✔ Does not send data to external servers

✔ Does not perform automated account actions

✔ Processes data entirely on the local machine

Users maintain full control over their information.

---

# Future Improvements

Planned features:

- Dark mode interface
- Profile picture preview
- Search functionality
- Excel export
- Advanced statistics
- Mutual followers analysis
- Followers-only analysis
- Interactive charts
- Account growth tracking

---

# Author

## Thamizhselvan M

Data Scientist

### Skills

- Python Development
- Artificial Intelligence
- Machine Learning
- Data Science
- Automation
- Web Development

---

If you found this project useful, consider giving it a ⭐ on GitHub.