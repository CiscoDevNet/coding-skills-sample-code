
project(coding210_parsing_json_cpp_activity_2)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")



# main-http
set(SOURCE_FILES
    main-http.cpp)

add_executable(coding210_2_main_http ${SOURCE_FILES})
target_link_libraries(coding210_2_main_http curl)


