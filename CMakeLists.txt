cmake_minimum_required(VERSION 3.25.0)
project(cMake_project LANGUAGES C)

# ${PROJECT_SOURCE_DIR} is where CMakeLists.txt is located

# In this project the files are located in different subdirectories, we will see how to include those as well
# list of files to be built are main.cpp, foo.cpp, foo2.cpp, foo_test.cpp, foo.h, foo2.h and foo_test.h

if (${BUILD_TYPE_CONFIG} MATCHES "EXEC_BUILD")
    set(src_lib "SRC_LIBR")
    set(project_name "exe")
    add_library(${src_lib} src/local_library.c)
    # we defined the c++ files above but we need to tell the CMake where the header files are located which is
    # done in the line below. The "target", which is the library needs to include the header file directory.
    # check here for more example https://pabloariasal.github.io/2018/02/19/its-time-to-do-cmake-right/
    target_include_directories(${src_lib} 
                                PUBLIC 
                                $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/lib>
                                $<INSTALL_INTERFACE:lib>)

    # $<INSTALL_INTERFACE:lib>
    add_executable(${project_name}  src/main.c)

    # once we have defined the project target we need to then link the library to the target. This happens in the line below
    target_link_libraries(${project_name} PUBLIC ${src_lib})
endif()
# add_executables creates an .exe file make sure to include all the header files used in the main.cpp file

if (${BUILD_TYPE_CONFIG} MATCHES "EMULATOR_BUILD")
    set(src_lib "SRC_LIBR")
    set(project_name "pyTest")
    add_library(${src_lib} src/local_library.c)
    target_include_directories(${src_lib} 
                                PUBLIC 
                                $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/lib>)

    add_library(${project_name} SHARED src/testDll.c)
    target_link_libraries(${project_name} PUBLIC ${src_lib})
endif()

# in CLI type cmake -S <source directory of CMakeLists.txt> -B <build directory> -D <variable name>=<variable value> 
# the variable name mentioned above can be directly used inside the CMakeLists.txt file
# the above line will only generate the build system to actually build the software type the below line in CLI
# make sure you are in the build directory cmake --build . note the end period is also part of the command