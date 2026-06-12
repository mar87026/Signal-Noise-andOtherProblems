import os
import re

# 設定目標目錄
current_dir = os.getcwd()
content_dir = os.path.join(current_dir, "content")


def deep_clean():
    if not os.path.exists(content_dir):
        print(content_dir)
        return

    
    # 儲存舊名到新名的映射，用於修復內容連結
    name_map = []

    # 階段 1: 建立對照表並修改檔案內容
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
                    if "%20" in new_content:
                        new_content = new_content.replace("%20", "_")

                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"已更新連結: {filename}")

    for root, dirs, files in os.walk(content_dir, topdown=False):
   
        for file in files:
            cut_name = file.split(' ')
            if len(cut_name) < 2:
                continue
            
            remove_target = os.path.splitext(cut_name[-1])[0]
            if remove_target in name_map:
                new_name = re.sub(remove_target, "", file)
                os.rename(os.path.join(root, file), os.path.join(root, new_name))

        # 改資料夾名 (Notion 匯出的圖片資料夾通常也帶 UUID)
        for name in dirs:
            cut_name = name.split(' ')
            remove_target = os.path.splitext(cut_name[-1])[0]            
            if remove_target in name_map:
                new_name = re.sub(remove_target, "", file)
                os.rename(os.path.join(root, file), os.path.join(root, new_name))


if __name__ == "__main__":
    deep_clean()
