# Versão mínima recomendada do CMake
cmake_minimum_required(VERSION 3.10)

# Nome do projeto e linguagem (CXX para C++)
project(ProjetoParte3 CXX)

# Especificar a versão do padrão C++ (ex: C++17)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Localizar a biblioteca Eigen3 instalada no sistema
find_package(Eigen3 REQUIRED)

# Definir o nome do executável e os ficheiros fonte associados
add_executable(parte3 parte3.cpp)

# Vincular a biblioteca Eigen3 ao executável (configura automaticamente os caminhos de include)
target_link_libraries(parte3 PRIVATE Eigen3::Eigen)