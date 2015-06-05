
project(coding210_parsing_json_cpp_activity_5)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

include_directories("rapidjson/include")

# main
set(SOURCE_FILES
    main.cpp)

add_executable(coding210_5_main ${SOURCE_FILES})
target_link_libraries(coding210_5_main curl)
