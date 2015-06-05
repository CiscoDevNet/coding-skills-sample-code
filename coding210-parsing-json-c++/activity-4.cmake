
project(coding210_parsing_json_cpp_activity_4)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

include_directories("rapidjson/include")

# main-http
set(SOURCE_FILES
    main-json-lib.cpp)

add_executable(coding210_4_main_json_lib ${SOURCE_FILES})
target_link_libraries(coding210_4_main_json_lib curl)


