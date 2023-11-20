
from flask import Flask, render_template, jsonify
import requests
from config import GITHUB_TOKEN

app = Flask(__name__)

github_api_url = 'https://api.github.com'
repositories = ['PDA-KALABURAGI/GitHub-Aggregator', 'Sou26/test.Template'] 

@app.route('/')
def index():
    commits_data = get_recent_commits()
    return render_template('index.html', commits_data=commits_data)

def get_recent_commits():
    commits_data = []

    for repo in repositories:
        response = requests.get(f'{github_api_url}/repos/{repo}/commits',
                                headers={'Authorization': f'Bearer {GITHUB_TOKEN}'})
        commits_data.append({
            'repository': repo,
            'commits': response.json(),
        })

    return commits_data

if __name__ == '__main__':
    app.run(debug=True)

