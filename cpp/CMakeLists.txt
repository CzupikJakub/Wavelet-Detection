cmake_minimum_required(VERSION 3.20)
project(WaveletDetection)

set(CMAKE_CXX_STANDARD 17)

# Szukaj OpenCV (jeœli nie znajdzie, poka¿e b³¹d)
find_package(OpenCV REQUIRED)

# Dodaj pliki Ÿród³owe
add_executable(${PROJECT_NAME} 
    src/main.cpp
)

# Pod³¹cz OpenCV
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})