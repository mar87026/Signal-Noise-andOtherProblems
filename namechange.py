import os
import re
import shutil
from pathlib import Path


replace_to_baseline = ['%20', '%E2%80%99', ' ', "'", "’"]

def normalize_name(name, name_map_list):

    for key in name_map_list:
        name = name.replace('%20' + key, '').replace(' ' + key, '').replace(key, '')

    pattern = '|'.join(map(re.escape, replace_to_baseline))
    name = re.sub(pattern, '_', name)
    

    return name.lower()


def to_lower_path(match, name_map):
    title = match.group(1)  # 抓取 [標題]
    path = match.group(2)  # 抓取 (路徑)
    path_parts = path.split('/')
    cleaned_parts = [normalize_name(p, name_map) for p in path_parts]
    path_out = '/'.join(cleaned_parts)
    return f"[{title}]({path_out.lower()})"
# 3. 使用正則表達式物理匹配所有的 [文字](路徑) 格式
# \[([^\]]+)\]  -> 匹配 [中括號內的任意文字]
# \(([^)]+)\)    -> 匹配 (小括號內的路徑)

def deep_clean():
    current_dir = os.getcwd()
    content_dir = os.path.join(current_dir, "content")
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

    #get new folder name, rename content
    for root, dirs, files in os.walk(content_dir, topdown=False):
        for file in files:
            cut_name = os.path.splitext(file)[0].split(' ')
            if len(cut_name) < 2:
                continue

            new_name = normalize_name(file, name_map)
            if new_name != file:
                os.rename(os.path.join(root, file), os.path.join(root, new_name))

        # rename folder
        for dir_name in dirs:

            new_name = normalize_name(dir_name, name_map)
            
            if new_name != dir_name:
                os.rename(os.path.join(root, dir_name), os.path.join(root, new_name))
    
    current_dir = os.getcwd()
    content_dir = os.path.join(current_dir, "content")            

    for root, dirs, files in os.walk(content_dir, topdown=False): 
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

                    target_dir = path_content.split("/")[0]
                    
                    new_name = normalize_name(target_dir, name_map)
                    if os.path.exists(os.path.join(root, new_name)):
                        root_parts = root.replace("\\", "/").split("/")
                        try:
                            idx = root_parts.index('content')
                            prefix_parts = root_parts[idx+1:]
                        except ValueError:
                            prefix_parts = []

                        prefix = "/" + "/".join(prefix_parts) + "/" if prefix_parts else "/"

                        cleaned_path = "/".join([normalize_name(p, name_map) for p in path_content.split("/")])

                        return f"[{text_content}]({prefix}{cleaned_path})"
                    return match.group(0)

                new_content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_update, new_content)
                new_content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m :to_lower_path(m , name_map), new_content)
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                
                if Path(os.path.splitext(file_path)[0]).is_dir():
                    shutil.copyfile(
                    file_path, 
                    os.path.join(os.path.splitext(file_path)[0], 'index.md'))
    
      
    
    project_name = [f.name for f in Path(content_dir).iterdir() if f.is_file()][0]
    index_file = os.path.join(content_dir, project_name)
    os.rename(index_file, os.path.join(content_dir, 'index.md'))
if __name__ == "__main__":
    deep_clean()
