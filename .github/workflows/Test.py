import subprocess

jenkins_url = 'http://192.168.1.6:8080/job/checklist/build'
username = 'Aishwarya'
password = '11ffbd89d6a2b90e0abb9ecb0cf6d991f0'

# Construct the curl command with username and password
curl_command = ['curl', '-X', 'POST', jenkins_url, '--user', f'{username}:{password}']

# # Construct the curl command
# curl_command = ['curl', '-X', 'POST', jenkins_url]

# Execute the curl command using subprocess
subprocess.run(curl_command)
