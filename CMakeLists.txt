cmake_minimum_required( VERSION 2.8)
set(CMAKE_CXX_FLAGS "-std=c++11")
project(enhance)

find_package(OpenCV REQUIRED)
find_package(Boost COMPONENTS program_options filesystem python REQUIRED)

find_package (Python3 COMPONENTS Interpreter Development NumPy  REQUIRED)
if (Python3_FOUND)
  message("python version= ${Python3_VERSION}  ${Python3_INCLUDE_DIRS}")
endif()

include_directories(
  ${PROJECT_SOURCE_DIR}/include
  ${PROJECT_SOURCE_DIR}/include/incCn
  ${OpenCV_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIR}
  ${Python3_INCLUDE_DIRS}
  ${Python3_NumPy_INCLUDE_DIRS}
  )


add_subdirectory(${PROJECT_SOURCE_DIR}/src)
