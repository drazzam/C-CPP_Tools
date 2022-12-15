# Load the libraries
import subprocess
import re

# Get the list of all saved WiFi profiles
output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')
profiles = re.findall(r'(?:Profile\s*:\s)(.*)', output)

# Iterate over each profile and get its password
for profile in profiles:
    # Remove any newline characters from the profile name
    profile = profile.strip()
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8')
        password = re.search(r'(?:Key\s*Content\s*:\s)(.*)', output)
        # Check if the password was found
        if password is not None:
            print(f'{profile}: {password.group(1)}')
    except CalledProcessError as e:
        # Handle the error here
        print(e)

# Use regular expressions to extract the password
password = re.search(r'(?:Key\s*Content\s*:\s)(.*)', output)

# Print the WiFi network name and the password
print(f'{profile}: {password.group(1)}')
