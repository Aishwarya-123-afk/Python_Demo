# import requests

# output = requests.get("http://localhost:8080/job/python_script/lastBuild/consoleText")
# print(output.text)

# github_pulls = requests.get("https://api.github.com/repos/Aishwarya-123-afk/Python_Demo/pulls")
# print("github_pulls")

# filepath = ".github/pull_request_template.md"
# with open(filepath,'a', newline = "") as fp:
#     fp.write(output.text)

import subprocess

jenkins_url = 'http://192.168.1.6:8080/job/checklist/build'

# Construct the curl command
curl_command = ['curl', '-X', 'POST', jenkins_url]

# Execute the curl command using subprocess
subprocess.run(curl_command)
