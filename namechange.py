import os
import re
import shutil
from pathlib import Path

current_dir = os.getcwd()
content_dir = os.path.join(current_dir, "content")
replace_to_baseline = ['%20', '%E2%80%99', ' ', "'"]
def to_lower_path(match):
    title = match.group(1)  # 抓取 [標題]
    path = match.group(2)  # 抓取 (路徑)
    pattern = '|'.join(map(re.escape, replace_to_baseline))
    path_out = re.sub(pattern, '_', path)
    return f"[{title}]({path_out.lower()})"
# 3. 使用正則表達式物理匹配所有的 [文字](路徑) 格式
# \[([^\]]+)\]  -> 匹配 [中括號內的任意文字]
# \(([^)]+)\)    -> 匹配 (小括號內的路徑)

def deep_clean():
    if not os.path.exists(content_dir):
        print(content_dir)
        return
    
    name_map = []

    # build up name_map and check index.md
    for root, dirs, files in os.walk(content_dir):
        for filename in files:
            if filename.endswith(".md"):
                # get filename
                old_name_no_ext = os.path.splitext(filename)[0]
                cut_name = old_name_no_ext.split(' ')
                if len(cut_name) < 2:
                    continue
                name_map.append(cut_name[-1])

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
                        new_content = new_content.replace('%20'+keys, '')
                
                def link_update(match):
                    text_content = match.group(1)
                    path_content = match.group(2)
                    root_parts = root.replace("\\", "/").split("/")

                    target_dir = path_content.split("/")[0]

                    if os.path.exists(os.path.join(root.replace("\\", "/"), target_dir)):
                        idx = root_parts.index('content')
                        prefix_parts = root_parts[idx+1:]

                        if prefix_parts:
                            prefix = "/" + "/".join(prefix_parts) + "/"
                        else:
                            prefix = "/"

                        return f"[{text_content}]({prefix}{path_content})"
                    return match.group(0)

                new_content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_update, new_content)
                new_content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", to_lower_path, new_content)             
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:                
                        f.write(new_content)

    for root, dirs, files in os.walk(content_dir, topdown=False):
   
        for file in files:
            cut_name = os.path.splitext(file)[0].split(' ')
            if len(cut_name) < 2:
                continue
            #rename file
            remove_target = cut_name[-1]
            new_name = file
            if remove_target in name_map:
                new_name = re.sub(' ' + remove_target, '', file)
            new_name = new_name.lower()
            new_name = re.sub(' ', '_', new_name)
            new_name = re.sub("’", '_', new_name)
            if new_name != file:
                os.rename(os.path.join(root, file), os.path.join(root, new_name))

        # rename folder
        for dir_name in dirs:
            cut_name = dir_name.split(' ')
            new_name = dir_name
           
            remove_target = cut_name[-1]            
            if remove_target in name_map:
                new_name = re.sub(remove_target, '', dir_name)
            new_name = new_name.lower()
            new_name = re.sub(' ', '_', new_name)
            new_name = re.sub("’", '_', new_name)
            if new_name != dir_name:
                os.rename(os.path.join(root, dir_name), os.path.join(root, new_name))
            if os.path.exists(os.path.join(root, new_name+'.md')):
                shutil.copyfile(os.path.join(root, new_name+'.md'), os.path.join(root, new_name, 'index.md'))
    
    
    project_name = [f.name for f in Path(content_dir).iterdir() if f.is_file()][0]
    index_file = os.path.join(content_dir, project_name)
    os.rename(index_file, os.path.join(content_dir, 'index.md'))
    
if __name__ == "__main__":
    deep_clean()
