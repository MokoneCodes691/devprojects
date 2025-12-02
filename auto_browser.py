import webbrowser

websites = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.github.com",
    "https://www.chat.openai.com"
]

for site in websites:
    webbrowser.open(site)

print("All websites opened successfully!")