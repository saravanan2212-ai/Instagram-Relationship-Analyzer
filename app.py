import json
import tkinter as tk
from tkinter import messagebox
import webbrowser
import csv

# -----------------------
# Load Instagram Data
# -----------------------

with open("connections/followers_1.json", "r", encoding="utf-8") as f:
    followers_data = json.load(f)

with open("connections/following.json", "r", encoding="utf-8") as f:
    following_data = json.load(f)

followers = set()

for item in followers_data:
    followers.add(
        item["string_list_data"][0]["value"].lower()
    )

following = set()

for item in following_data["relationships_following"]:
    following.add(
        item["title"].lower()
    )

non_followers = sorted(
    list(following - followers)
)

# -----------------------
# GUI Logic
# -----------------------

current_index = 0


def update_display():
    global current_index

    if len(non_followers) == 0:
        username_label.config(text="No non-followers found")
        counter_label.config(text="")
        return

    username = non_followers[current_index]

    username_label.config(
        text="@" + username
    )

    counter_label.config(
        text=f"{current_index + 1} / {len(non_followers)}"
    )


def next_user():
    global current_index

    if current_index < len(non_followers) - 1:
        current_index += 1
        update_display()


def previous_user():
    global current_index

    if current_index > 0:
        current_index -= 1
        update_display()


def open_profile():
    username = non_followers[current_index]

    webbrowser.open(
        f"https://www.instagram.com/{username}/"
    )


def export_csv():

    with open(
        "non_followers.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(["Username"])

        for user in non_followers:
            writer.writerow([user])

    messagebox.showinfo(
        "Success",
        "Saved as non_followers.csv"
    )


# -----------------------
# Window
# -----------------------

root = tk.Tk()

root.title(
    "Instagram Non-Followers Manager"
)

root.geometry("550x350")

# Title

title_label = tk.Label(
    root,
    text="Instagram Non-Followers",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=15)

# Statistics

stats_label = tk.Label(
    root,
    text=f"Followers: {len(followers)}   |   Following: {len(following)}   |   Non-Followers: {len(non_followers)}",
    font=("Arial", 10)
)

stats_label.pack()

# Username

username_label = tk.Label(
    root,
    text="",
    font=("Arial", 24, "bold")
)

username_label.pack(pady=30)

# Counter

counter_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)

counter_label.pack()

# Buttons

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

prev_btn = tk.Button(
    btn_frame,
    text="◀ Previous",
    command=previous_user,
    width=12
)

prev_btn.grid(row=0, column=0, padx=5)

open_btn = tk.Button(
    btn_frame,
    text="Open Profile",
    command=open_profile,
    width=15
)

open_btn.grid(row=0, column=1, padx=5)

next_btn = tk.Button(
    btn_frame,
    text="Next ▶",
    command=next_user,
    width=12
)

next_btn.grid(row=0, column=2, padx=5)

# Export Button

export_btn = tk.Button(
    root,
    text="Export CSV",
    command=export_csv,
    width=20
)

export_btn.pack(pady=15)

update_display()

root.mainloop()