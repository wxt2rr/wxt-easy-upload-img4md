import reader
import replacer

if __name__ == '__main__':
    # md文件路径（需要使用绝对路径）
    path = "E:\\my-project\\static\\blog\\source\\_posts\\auto_replace_img_url_for_md.md"
    # 目标md文件路径
    tar_path = "E:\\my-project\\static\\blog\\source\\_posts\\auto_replace_img_url_for_md.md"
    # 上传到github的根路径
    dir_path = "hexo/" + "auto_replace_img_url_for_md_file"

    # 读取md文件
    lines = reader.read_md(path)

    # 检索md文件中的图片，并替换url
    new_lines = replacer.replace_url(lines, dir_path)

    # 替换md文件
    reader.write_md(tar_path, new_lines)
