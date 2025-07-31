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

set(MIN_TIME_COST_SOURCE codegen/min_time_cost.cu)
set(BOUNDARY_CONSTRAINT_SOURCE codegen/boundary_constraint.cu)
set(TRACTION_CONSTRAINT_SOURCE codegen/traction_constraint.cu)
set(DYNAMICS_DOUBLE_TRACK_SOURCE codegen/dynamics_double_track.cu)
set(FN_HEAVY_DEMO_SOURCE codegen/fn_heavy_demo.cu)
set(INERTIAL_QUANTITIES_SOURCE codegen/inertial_quantities.cu)

# Include directories for your header files
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_library(min_time_cost SHARED ${MIN_TIME_COST_SOURCE})
set_target_properties(min_time_cost PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(min_time_cost)
add_library(boundary_constraint SHARED ${BOUNDARY_CONSTRAINT_SOURCE})
set_target_properties(boundary_constraint PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(boundary_constraint)
add_library(traction_constraint SHARED ${TRACTION_CONSTRAINT_SOURCE})
set_target_properties(traction_constraint PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(traction_constraint)
add_library(dynamics_double_track SHARED ${DYNAMICS_DOUBLE_TRACK_SOURCE})
set_target_properties(dynamics_double_track PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(dynamics_double_track)
add_library(fn_heavy_demo SHARED ${FN_HEAVY_DEMO_SOURCE})
set_target_properties(fn_heavy_demo PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(fn_heavy_demo)
add_library(inertial_quantities SHARED ${INERTIAL_QUANTITIES_SOURCE})
set_target_properties(inertial_quantities PROPERTIES LINKER_LANGUAGE CUDA)
target_link_libraries(inertial_quantities)
