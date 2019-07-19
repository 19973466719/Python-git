import requests
GetCodeApi = "https://api.github.com/search/code?q="
GetRepoApi ="https://api.github.com/search/repositories?q=language:python"
def get_code(language, size, repo):
    url = GetCodeApi +"language:" + language + "+size:" + size +"+repo:" + repo
    # 访问GitHub接口
    info =requests.get(url).json()
    if 'items' in info:
        for i in info['items']: print(i['html_url'])
def get_project(FindTime):
    info = requests.get(GetRepoApi).json()
    for i in info['items']:
        created_time =i['created_at']
        if created_time >FindTime:
            language ="python"
            size ="<200"
            repo =i['html_url'].replace("https://github.com/", "")
            get_code(language,size, repo)
