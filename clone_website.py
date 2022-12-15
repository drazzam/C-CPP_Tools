# Install libraries
pip install requests zipfile

# Load the libraries
import requests
import os
import zipfile

# URL of the website that you want to clone
url = input("Enter the URL of the website that you want to clone: ")

# Send a GET request to the website and save the response
response = requests.get(url)

# Create a new directory to store the cloned website
os.mkdir("cloned_website")

# Save the HTML of the website in a file called "index.html"
with open("cloned_website/index.html", "w") as file:
    file.write(response.text)

# Clone all of the website's assets (e.g. CSS, JavaScript, images)
for asset in response.iter_content(chunk_size=128):
    # Save each asset in a separate file
    with open("cloned_website/" + asset.name, "wb") as file:
        file.write(asset.content)

# Compress the cloned website into a ZIP file
zip_file = zipfile.ZipFile("cloned_website.zip", "w")
for root, dirs, files in os.walk("cloned_website"):
    for file in files:
        zip_file.write(os.path.join(root, file))
zip_file.close()

print("Website cloned and compressed successfully!")
