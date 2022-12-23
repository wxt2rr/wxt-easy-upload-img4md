# 读取md文件
def read_md(path):
    mdfile = open(path, "r", encoding="utf-8")
    return mdfile.readlines()


# 更新md文件
def write_md(path, lines):
    mdfile = open(path, "w+", encoding="utf-8")
    for line in lines:
        mdfile.write(line + "\n")
