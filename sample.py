import requests

output = requests.get("http://localhost:8080/job/python_script/lastBuild/consoleText")
print(output.text)

 github_pulls = requests.get(https://api.github.com/repos/Aishwarya-123-afk/Python_Demo/pulls)
 print("github_pulls")

filepath = ".github/pull_request_template.md"
with open(filepath,'a', newline = "") as fp:
    fp.write(output.text)
