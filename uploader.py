import requests
import base64
import json
import configparser

config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")


# 读取文件
def open_file(file_path):
    with open(file_path, 'rb+') as f:
        return f.read()


# 将文件转换为base64编码，上传文件必须将文件以base64格式上传
def file_base64(data):
    data_b64 = base64.b64encode(data).decode('utf-8')
    return data_b64


# 上传文件
# https://developer.github.com/v3/repos/contents/
# V4：https://developer.github.com/v4/
def do_upload_file(file_data, filename, dirname):
    # 文件名称
    file_name = filename
    token = config.get('github', 'token')
    user = config.get('github', 'user')
    repo = config.get('github', 'repo')
    path = dirname

    url = "https://api.github.com/repos/" + user + "/" + repo + "/contents/" + path + "/" + file_name  # 用户名、库名、路径
    headers = {"Authorization": "token " + token}
    content = file_base64(file_data)
    data = {
        "message": "for_upload_img",
        "committer": {
            "name": "[wangxt]",
            "email": "1471520488@qq.com"
        },
        "content": content
    }
    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)
    print(re_data)

    # https://github.com/wxt2rr/images/blob/main/hexo/aa.jpg
    # https://cdn.jsdelivr.net/gh/wxt2rr/images@main/hexo/aa.jpg
    cdn_url = "https://cdn.jsdelivr.net/gh/" + user + "/" + repo + "@main/" + path + "/" + file_name
    print(cdn_url)
    return cdn_url


# eg:
#   'C:\\Users\\wxt\\Desktop\\cc.png'
def upload_file(filename, filepath, dirname):
    # 读取img文件
    image = open_file(filepath)
    # 上传img文件到github，并返回cdn地址
    cdn_url = do_upload_file(image, filename, dirname)
    return cdn_url
