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
    title = match.group(1)  # catch header
    path = match.group(2)  # catch path
    path_parts = path.split('/')
    cleaned_parts = [normalize_name(p, name_map) for p in path_parts]
    path_out = '/'.join(cleaned_parts)
    return f"[{title}]({path_out.lower()})"

def fix_notion_formatting(content):
    # 1. 統一顏色標籤格式
    content = re.sub(r'<mark style="background:(.*?);">(.*?)</mark>', r'<mark style="background:\1;">\2</mark>', content)

    # 2. 自動修復 Notion 表格內的異常換行 (緩衝區捕捉法)
    lines = content.split('\n')
    fixed_lines = []
    buffer = []
    in_broken_row = False
    
    for line in lines:
        stripped = line.strip()
        
        # 情況 A：如果目前正在收集中斷的表格列
        if in_broken_row:
            buffer.append(line)
            # 如果這行結尾終於出現了 '|'，代表這列結束了
            if stripped.endswith('|'):
                # 把緩衝區內收集到的所有斷行片段，用 <br> 完美縫合
                merged_row = " <br> ".join([b.strip() for b in buffer])
                fixed_lines.append(merged_row)
                
                # 清空緩衝區，準備迎接下一行
                buffer = []
                in_broken_row = False
            continue

        # 情況 B：如果目前不在中斷的列中
        if stripped.startswith('|'):
            if stripped.endswith('|'):
                # 正常的單行表格列，直接加入
                fixed_lines.append(line)
            else:
                # 開頭是 '|' 但結尾不是 '|'，這就是 Notion 斷行表格的開頭
                in_broken_row = True
                buffer.append(line)
        else:
            # 一般文字或空行，直接放行
            fixed_lines.append(line)
            
    return '\n'.join(fixed_lines)

def deep_clean():
    current_dir = os.getcwd()
    content_dir = os.path.join(current_dir, "content")
    if not os.path.exists(content_dir):
        print(content_dir)
        return
    
    name_map = []

    # build up name_map
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
    #refresh the path
    current_dir = os.getcwd()
    content_dir = os.path.join(current_dir, "content")            
    project_name = [f.name for f in Path(content_dir).iterdir() if f.is_file()][0]
    for root, dirs, files in os.walk(content_dir, topdown=False): 
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = fix_notion_formatting(content)
                for keys in name_map:
                    if keys in new_content:
                        new_content = new_content.replace('%20'+keys, '')
                
                def link_update(match):
                    text_content = match.group(1)
                    path_content = match.group(2)

                    # 1. 過濾掉空字串，避免絕對路徑開頭的 '/' 造成 target_dir 變成空字串
                    path_parts = [p for p in path_content.split("/") if p]
                    if not path_parts:
                        return match.group(0)

                    target_dir = path_parts[0]
                    new_name = normalize_name(target_dir, name_map)
                    
                    # 2. 檢查目標資料夾是否真實存在於「當前目錄」下
                    if os.path.exists(os.path.join(root, new_name)):
                        root_parts = root.replace("\\", "/").split("/")
                        try:
                            idx = root_parts.index('content')
                            prefix_parts = root_parts[idx+1:]
                            if project_name in path_content:
                                return match.group(0)
                        except ValueError:
                            prefix_parts = []
                         
                        prefix = "/" + "/".join(prefix_parts) + "/" if prefix_parts else "/"
                        # 使用過濾後的 path_parts 重組，避免結尾或開頭多出多餘斜線
                        cleaned_path = "/".join([normalize_name(p, name_map) for p in path_parts])

                        return f"[{text_content}]({prefix}{cleaned_path})"
                    
                    # 3. 如果是絕對路徑或其他狀況，直接清理並消除雙斜線 (//)
                    cleaned_path = "/".join([normalize_name(p, name_map) for p in path_content.split("/")])
                    cleaned_path = cleaned_path.replace("//", "/")
                    return f"[{text_content}]({cleaned_path})"
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                
                if Path(os.path.splitext(file_path)[0]).is_dir():
                    shutil.copyfile(
                    file_path, 
                    os.path.join(os.path.splitext(file_path)[0], 'index.md')) 
    
    if not os.path.exists(os.path.join(content_dir, 'index.md')):
        project_name = [f.name for f in Path(content_dir).iterdir() if f.is_file()][0]
        index_file = os.path.join(content_dir, project_name)
        os.rename(index_file, os.path.join(content_dir, 'index.md'))
if __name__ == "__main__":
    deep_clean()
