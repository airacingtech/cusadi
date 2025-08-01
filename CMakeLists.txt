cmake_minimum_required(VERSION 3.15)
project(CusADi)

# Find CUDA package
include(CheckLanguage)
check_language(CUDA)
find_package(CUDAToolkit REQUIRED)
if(CMAKE_CUDA_COMPILER)
enable_language(CUDA)
include_directories(${CUDA_INCLUDE_DIRS})
message("CUDA found")
endif()
if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
    set(CMAKE_CUDA_ARCHITECTURES 75 86)
endif()
message(${CMAKE_CUDA_ARCHITECTURES})

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)

# Set CUDA flags
set(CUDA_NVCC_FLAGS ${CUDA_NVCC_FLAGS}; -O3 -arch=sm_86 --use_fast_math)  # Adjust architecture as needed

set(DYNAMICS_DOUBLE_TRACK_SX_SOURCE codegen/dynamics_double_track_sx.cu)
set(DYNAMICS_BICYCLE_SX_SOURCE codegen/dynamics_bicycle_sx.cu)
set(TRACTION_CONSTRAINT_SX_SOURCE codegen/traction_constraint_sx.cu)
set(BOUNDARY_CONSTRAINT_SX_SOURCE codegen/boundary_constraint_sx.cu)

# Include directories for your header files
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_library(dynamics_double_track_sx SHARED ${DYNAMICS_DOUBLE_TRACK_SX_SOURCE})
set_target_properties(dynamics_double_track_sx PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(dynamics_double_track_sx)
add_library(dynamics_bicycle_sx SHARED ${DYNAMICS_BICYCLE_SX_SOURCE})
set_target_properties(dynamics_bicycle_sx PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(dynamics_bicycle_sx)
add_library(traction_constraint_sx SHARED ${TRACTION_CONSTRAINT_SX_SOURCE})
set_target_properties(traction_constraint_sx PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(traction_constraint_sx)
add_library(boundary_constraint_sx SHARED ${BOUNDARY_CONSTRAINT_SX_SOURCE})
set_target_properties(boundary_constraint_sx PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(boundary_constraint_sx)
