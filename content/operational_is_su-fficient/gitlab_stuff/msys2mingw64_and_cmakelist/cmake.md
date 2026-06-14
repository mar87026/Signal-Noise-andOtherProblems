# CMAKE

```c
cmake_minimum_required(VERSION 3.15)
project(DEMO)

# 設定 C++ 標準
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 尋找 OpenCV (Conan 能確保它被找到)
find_package(OpenCV REQUIRED)

add_executable(main.c)

# 連結 OpenCV 函式庫
target_link_libraries(CamApp PRIVATE opencv_opencv)
```