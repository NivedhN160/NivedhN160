import os
import requests
import yaml
from datetime import datetime

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = 'NivedhN160'

def fetch_repos():
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&page={page}&sort=pushed"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Failed to fetch repos:", response.status_code)
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def main():
    try:
        with open('flagships.yml', 'r') as f:
            flagships_config = yaml.safe_load(f)
            flagships = flagships_config.get('flagships', [])
    except Exception as e:
        print(f"Error reading flagships: {e}")
        flagships = []

    repos = fetch_repos()
    
    # Filter: Exclude forks and the profile repo itself
    filtered_repos = [r for r in repos if not r['fork'] and r['name'] != USERNAME]
    
    # Find flagship repos
    flagship_repos = []
    for f in flagships:
        match = next((r for r in filtered_repos if r['name'].lower() == f.lower()), None)
        if match:
            flagship_repos.append(match)
            
    # Remove flagships from filtered
    remaining_repos = [r for r in filtered_repos if r['name'].lower() not in [f.lower() for f in flagships]]
    
    # Take top 5 recently pushed
    recent_repos = remaining_repos[:5]
    
    final_list = flagship_repos + recent_repos
    
    markdown_lines = []
    for r in final_list:
        desc = r.get('description', '') or ''
        name = r.get('name')
        url = r.get('html_url')
        lang = r.get('language') or 'Markdown'
        stars = r.get('stargazers_count', 0)
        
        star_str = f" ⭐ {stars}" if stars > 0 else ""
        badge = ""
        if next((f for f in flagships if f.lower() == name.lower()), None):
            badge = " 🎯 **Flagship** |"
            
        markdown_lines.append(f"- [**{name}**]({url}) {badge} {lang}{star_str}\n  <br/> {desc}\n")
        
    new_content = "\n".join(markdown_lines)
    
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
        
    start_marker = "<!-- AUTO-PROJECTS:START -->"
    end_marker = "<!-- AUTO-PROJECTS:END -->"
    
    if start_marker in readme and end_marker in readme:
        start_idx = readme.find(start_marker) + len(start_marker)
        end_idx = readme.find(end_marker)
        
        updated_readme = readme[:start_idx] + "\n" + new_content + "\n" + readme[end_idx:]
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(updated_readme)
        print("Updated README.md")
    else:
        print("Markers not found in README.md")

if __name__ == '__main__':
    main()
