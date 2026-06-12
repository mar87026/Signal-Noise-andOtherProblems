import os
import re

# 設定目標目錄
current_dir = os.getcwd()
content_dir = os.path.join(current_dir, "content")


def deep_clean():
    if not os.path.exists(content_dir):
        print(content_dir)
        return

    name_map = []

    # build up name_map and re-name setense within files
    for root, dirs, files in os.walk(content_dir):
        for filename in files:
            if filename.endswith(".md"):
                # 取得不帶副檔名的名稱
                old_name_no_ext = os.path.splitext(filename)[0]
                cut_name = old_name_no_ext.split(' ')
                if len(cut_name) < 2:
                    continue
                new_name_no_ext = re.sub(cut_name[-1], "", old_name_no_ext)
                if old_name_no_ext != new_name_no_ext:
                    name_map.append(cut_name[-1])
        #check index.md is exist
        if "index.md" in files:
            pass
        else:
            full_path = os.path.join(root, "index.md")
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write("---\n")
                f.write(f"title: {os.path.basename(root)}\n")
                f.write("---\n")
    #rename file
    for root, dirs, files in os.walk(content_dir):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_content = content
                for old_val in name_map:
                    if old_val in new_content:
                        new_content = new_content.replace(old_val, "")
                if '%20' in new_content:
                    new_content = new_content.replace('%20', "_")
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"update: {filename}")

    for root, dirs, files in os.walk(content_dir, topdown=False):
   
        for file in files:
            cut_name = file.split(' ')          
            if len(cut_name) < 2:
                continue
            #rename file
            remove_target = os.path.splitext(cut_name[-1])[0]
            new_name = file
            if remove_target in name_map:
                new_name = re.sub(remove_target, "", file)
            new_name = re.sub('\s+', '_', new_name)
            if new_name != file:
                os.rename(os.path.join(root, file), os.path.join(root, new_name))

        # rename folder
        for dir_name in dirs:
            cut_name = dir_name.split(' ')
            new_name = dir_name
           
            remove_target = os.path.splitext(cut_name[-1])[0]            
            if remove_target in name_map:
                new_name = re.sub(remove_target, "", dir_name)
            new_name = re.sub('\s+', "_", new_name) 
            if new_name != dir_name:
                os.rename(os.path.join(root, dir_name), os.path.join(root, new_name))


if __name__ == "__main__":
    deep_clean()
