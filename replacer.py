import re
import uploader


def replace_url(lines, dirpath):
    newlines = []
    for line in lines:
        print(line)
        # ![描述](图片url)
        # 判断是否是图片，如果是的话则将图片上传到github，然后替换成cdn的地址
        image = re.match('^!\[([\s\S]*?)]\(([\s\S]*?)\)', line, re.M | re.I)
        if image:
            filename = image.group(1)
            filepath = image.group(2)
            url = uploader.upload_file(filename, filepath, dirpath)
            line = "![" + filename + "](" + url + ")"
        newlines.append(line)

    return newlines
