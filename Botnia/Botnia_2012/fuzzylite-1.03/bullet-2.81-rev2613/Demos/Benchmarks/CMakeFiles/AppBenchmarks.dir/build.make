# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613

# Include any dependencies generated for this target.
include Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/depend.make

# Include the progress variables for this target.
include Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/progress.make

# Include the compile flags for this target's objects.
include Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/flags.make

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/flags.make
Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o: Demos/Benchmarks/main.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/AppBenchmarks.dir/main.o -c /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks/main.cpp

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/AppBenchmarks.dir/main.i"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks/main.cpp > CMakeFiles/AppBenchmarks.dir/main.i

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/AppBenchmarks.dir/main.s"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks/main.cpp -o CMakeFiles/AppBenchmarks.dir/main.s

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o.requires:
.PHONY : Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o.requires

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o.provides: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o.requires
	$(MAKE) -f Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/build.make Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o.provides.build
.PHONY : Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o.provides

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o.provides.build: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/flags.make
Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o: Demos/Benchmarks/BenchmarkDemo.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o -c /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks/BenchmarkDemo.cpp

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.i"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks/BenchmarkDemo.cpp > CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.i

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.s"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks/BenchmarkDemo.cpp -o CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.s

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o.requires:
.PHONY : Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o.requires

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o.provides: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o.requires
	$(MAKE) -f Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/build.make Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o.provides.build
.PHONY : Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o.provides

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o.provides.build: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o

# Object files for target AppBenchmarks
AppBenchmarks_OBJECTS = \
"CMakeFiles/AppBenchmarks.dir/main.o" \
"CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o"

# External object files for target AppBenchmarks
AppBenchmarks_EXTERNAL_OBJECTS =

Demos/Benchmarks/AppBenchmarks: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o
Demos/Benchmarks/AppBenchmarks: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o
Demos/Benchmarks/AppBenchmarks: Demos/OpenGL/libOpenGLSupport.a
Demos/Benchmarks/AppBenchmarks: src/BulletDynamics/libBulletDynamics.a
Demos/Benchmarks/AppBenchmarks: src/BulletCollision/libBulletCollision.a
Demos/Benchmarks/AppBenchmarks: src/LinearMath/libLinearMath.a
Demos/Benchmarks/AppBenchmarks: /usr/lib/libglut.so
Demos/Benchmarks/AppBenchmarks: /usr/lib/i386-linux-gnu/libGL.so
Demos/Benchmarks/AppBenchmarks: /usr/lib/i386-linux-gnu/libGLU.so
Demos/Benchmarks/AppBenchmarks: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/build.make
Demos/Benchmarks/AppBenchmarks: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable AppBenchmarks"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/AppBenchmarks.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/build: Demos/Benchmarks/AppBenchmarks
.PHONY : Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/build

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/requires: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/main.o.requires
Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/requires: Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/BenchmarkDemo.o.requires
.PHONY : Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/requires

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/clean:
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks && $(CMAKE_COMMAND) -P CMakeFiles/AppBenchmarks.dir/cmake_clean.cmake
.PHONY : Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/clean

Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/depend:
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613 /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613 /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Demos/Benchmarks/CMakeFiles/AppBenchmarks.dir/depend

