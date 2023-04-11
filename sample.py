import requests

output = requests.get("http://localhost:8080/job/python_script/lastBuild/consoleText")
print(output.text)

filepath = ".github/pull_request_template.md"
with open(filepath,'a', newline = "") as fp:
    fp.write(output.text)
