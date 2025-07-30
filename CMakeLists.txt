cmake_minimum_required(VERSION 3.15)
project(CusADi)

# Enable and check for CUDA
include(CheckLanguage)
check_language(CUDA)
find_package(CUDAToolkit REQUIRED)

if(CMAKE_CUDA_COMPILER)
  enable_language(CUDA)
  include_directories(${CUDA_INCLUDE_DIRS})
  message("CUDA found")
endif()

# Set CUDA architectures if not defined
if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
  set(CMAKE_CUDA_ARCHITECTURES 75 86)
endif()
message("CUDA Architectures: ${CMAKE_CUDA_ARCHITECTURES}")

# Set compiler flags
set(CMAKE_CXX_STANDARD 11)
set(CUDA_NVCC_FLAGS ${CUDA_NVCC_FLAGS}; -O3 -arch=sm_86 --use_fast_math)

# Include current dir
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

# --- Auto-compile all codegen/*.cu files ---
file(GLOB CODEGEN_FILES "codegen/*.cu")

foreach(CU_FILE ${CODEGEN_FILES})
  get_filename_component(FN_NAME ${CU_FILE} NAME_WE)
  message(STATUS "Adding CUDA target: ${FN_NAME}")

  add_library(${FN_NAME} SHARED ${CU_FILE})
  set_target_properties(${FN_NAME} PROPERTIES LINKER_LANGUAGE CUDA)
endforeach()
