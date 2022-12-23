# wxt-easy-upload-img4md
快速上传md文件中的img到指定图床，并替换url地址，方便需要每次进行手动进行上传的操作。

# 食用方式
## 申请github token
因为目前使用的图床是github，所以需要使用github的token通过API进行文件上传。
* 登录github，然后访问https://github.com/settings/tokens
* 点击Generate new token
* 输入github登录密码
* 设置token的信息
  * Note：token名称，比如我们是为了上传图片，我设置成了for_upload_img
  * Expiration：过期时间，根据自己情况设置
  * Select scopes：权限设置，我们只需要仓库的权限

## 配置token
打开项目的config.ini配置文件，设置对应的配置参数
~~~python
[github]
token = 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
user = wxt2rr
repo = images
~~~
启动程序
找到main.py，修改需要替换url的文件路径，执行程序即可
~~~python
if __name__ == '__main__':
    # md文件路径（需要使用绝对路径）
    path = "C:\\Users\\wxt\\Desktop\\test_1223_1735.md"
    # 目标md文件路径
    tar_path = "C:\\Users\\wxt\\Desktop\\test_1223_1735_new.md"
    # 上传到github的根路径
    dir_path = "hexo/" + "test_1223_1735_new"

    # 读取md文件
    lines = reader.read_md(path)

    # 检索md文件中的图片，并替换url
    new_lines = replacer.replace_url(lines, dir_path)

    # 替换md文件
    reader.write_md(tar_path, new_lines)
~~~
