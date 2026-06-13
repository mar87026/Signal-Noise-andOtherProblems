# msys2mingw64 and cmakelist

一個是管理與編譯外部、另一個是管理自己與連結外部

當然可以完全用cmakelist，但是每次專案重新編譯都會很久，明明沒有換第三方卻也要rebuild
以下以加入opencv為示範，盡量用命令提示字元操作，因為power shell常誤以為cmake是變數
因為不喜歡依賴ide、reproducible、portable，會用msys2mingw64做開發

# msys2mingw64

```c
pacman -s mingw-w64-x86_64-toolchain
pacman -s mingw-w64-x86_64-cmake
pacman -s mingw-w64-x86_64-ninja
pacman -s mingw-w64-x86_64-ntldd

```

> 'cmake' is not recognized as an internal or external command,

operable program or batch file. 
//means cmake is not ready, check the installing
> 

step3. compile with “ninja”

```c

cmake -g "ninja" -b build -s .
cmake --build build
```

cmakelist 

```c
cmake_minimum_required(version 3.15)
project(videotool cxx)

set(cmake_cxx_standard 17)
set(cmake_cxx_standard_required on)

find_package(opencv required)

add_executable(${project_name} main.cpp)

target_link_libraries(${project_name} private opencv_core opencv_imgproc)

if(mingw)
    target_link_options(videotool private -static-libgcc -static-libstdc++ -static)
endif()
```

[cmake](msys2mingw64%20and%20cmakelist/cmake.md)