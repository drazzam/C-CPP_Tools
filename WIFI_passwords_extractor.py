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
        # Get the output of the `netsh` command for this profile
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8')
        # Use regular expressions to extract the password
        password_match = re.search(r'(?:Key\s*Content\s*:\s)(.*)', output)
        # Check if the password was found
        if password_match is not None:
            # Print the WiFi network name and the password
            print(f'{profile}: {password_match.group(1)}')
    except CalledProcessError as e:
        # Print a message indicating that an error occurred
        print(f'An error occurred while getting the password for {profile}')
