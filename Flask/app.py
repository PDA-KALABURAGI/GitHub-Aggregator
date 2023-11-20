from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        username = request.form.get('username')
        repository = request.form.get('repository')

        if not username or not repository:
            return render_template('index.html', error="Please enter both 'username' and 'repository'.")

       
        repo_url = f'https://api.github.com/repos/{username}/{repository}'
        contributors_url = f'{repo_url}/contributors'

        try:
            
            repo_info = requests.get(repo_url).json()
            is_private = repo_info.get('private', False)

           
            contributors = []
            page = 1

            while True:
                params = {'page': page}
                response = requests.get(contributors_url, params=params)
                response.raise_for_status()  

                page_contributors = response.json()
                contributors.extend(page_contributors)

                if len(page_contributors) < 30:
                    break  

                page += 1

            contributor_count = len(contributors)

        except requests.RequestException as e:
            return render_template('index.html', error=str(e))

       
        return render_template('index.html', contributor_count=contributor_count, contributors=contributors)

   
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


