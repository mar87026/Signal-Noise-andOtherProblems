# MSYS2MINGW64 and CMakeList

一個是管理與編譯外部、另一個是管理自己與連結外部

當然可以完全用CMakeList，但是每次專案重新編譯都會很久，明明沒有換第三方卻也要rebuild
以下以加入Opencv為示範，盡量用命令提示字元操作，因為power shell常誤以為cmake是變數
因為不喜歡依賴IDE、reproducible、portable，會用MSYS2MINGW64做開發

# MSYS2MINGW64

```c
pacman -S mingw-w64-x86_64-toolchain
pacman -S mingw-w64-x86_64-cmake
pacman -S mingw-w64-x86_64-ninja
pacman -S mingw-w64-x86_64-ntldd

```

> 'cmake' is not recognized as an internal or external command,

operable program or batch file. 
//means cmake is not ready, check the installing
> 

Step3. compile with “Ninja”

```c

cmake -G "Ninja" -B build -S .
cmake --build build
```

CMakeList 

```c
cmake_minimum_required(VERSION 3.15)
project(VideoTool CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME} PRIVATE opencv_core opencv_imgproc)

if(MINGW)
    target_link_options(VideoTool PRIVATE -static-libgcc -static-libstdc++ -static)
endif()
```

[CMAKE](msys2mingw64%20and%20cmakelist/cmake.md)