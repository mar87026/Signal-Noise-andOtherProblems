import os
import re
import shutil
# 設定目標目錄
current_dir = os.getcwd()
content_dir = os.path.join(current_dir, "content")
def to_lower_path(match):
    title = match.group(1)  # 抓取 [標題]
    path = match.group(2)  # 抓取 (路徑)
    path_out = re.sub('%20', '_', path)
    return f"[{title}]({path_out.lower()})"


# 3. 使用正則表達式物理匹配所有的 [文字](路徑) 格式
# \[([^\]]+)\]  -> 匹配 [中括號內的任意文字]
# \(([^)]+)\)    -> 匹配 (小括號內的路徑)


def deep_clean():
    if not os.path.exists(content_dir):
        print(content_dir)
        return
    
    name_map = {}

    # build up name_map and check index.md
    for root, dirs, files in os.walk(content_dir):
        for filename in files:
            if filename.endswith(".md"):
                # get filename
                old_name_no_ext = os.path.splitext(filename)[0]
                cut_name = old_name_no_ext.split(' ')
                if len(cut_name) < 2:
                    continue
                new_name_no_ext = re.sub(' '+cut_name[-1], "", old_name_no_ext)
                if old_name_no_ext != new_name_no_ext:
                    new_name_no_ext = re.sub(' ', '_', new_name_no_ext)
                    new_name_no_ext = new_name_no_ext.lower()
                    name_map[old_name_no_ext] = new_name_no_ext
                    old_name_no_ext = re.sub(' ', '%20', old_name_no_ext)
                    name_map[old_name_no_ext] = new_name_no_ext
        """
        if not os.path.exists(os.path.join(root, 'index.md')):
            with open(os.path.join(root, 'index.md'), 'w', encoding='utf-8') as f:
                pass
                """
    
    #rename content
    for root, dirs, files in os.walk(content_dir): 
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = content
                for keys in name_map:
                    if keys in new_content:
                        new_content = new_content.replace(keys, name_map[keys])
                new_content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", to_lower_path, new_content)
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:                
                        f.write(new_content)

    for root, dirs, files in os.walk(content_dir, topdown=False):
   
        for file in files:
            cut_name = file.split(' ')          
            if len(cut_name) < 2:
                continue
            #rename file
            remove_target = os.path.splitext(file)[0]
            new_name = file
            if remove_target in name_map:
                new_name = re.sub(remove_target, name_map[remove_target], file)
            new_name = new_name.lower()
            if new_name != file:
                os.rename(os.path.join(root, file), os.path.join(root, new_name))

        # rename folder
        for dir_name in dirs:
            cut_name = dir_name.split(' ')
            new_name = dir_name
           
            remove_target = os.path.splitext(dir_name)[0]            
            if remove_target in name_map:
                new_name = re.sub(remove_target, name_map[remove_target], dir_name)
            new_name = new_name.lower()
            new_name = re.sub(' ', '_', new_name)
            if new_name != dir_name:
                os.rename(os.path.join(root, dir_name), os.path.join(root, new_name))


if __name__ == "__main__":
    deep_clean()
