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
include Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/depend.make

# Include the progress variables for this target.
include Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/progress.make

# Include the compile flags for this target's objects.
include Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/flags.make

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o: Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/flags.make
Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o: Demos/DoublePrecisionDemo/DoublePrecisionDemo.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o -c /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo/DoublePrecisionDemo.cpp

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.i"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo/DoublePrecisionDemo.cpp > CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.i

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.s"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo/DoublePrecisionDemo.cpp -o CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.s

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o.requires:
.PHONY : Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o.requires

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o.provides: Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o.requires
	$(MAKE) -f Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/build.make Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o.provides.build
.PHONY : Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o.provides

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o.provides.build: Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o

# Object files for target AppDoublePrecisionDemo
AppDoublePrecisionDemo_OBJECTS = \
"CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o"

# External object files for target AppDoublePrecisionDemo
AppDoublePrecisionDemo_EXTERNAL_OBJECTS =

Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: Demos/OpenGL/libOpenGLSupport.a
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: src/BulletDynamics/libBulletDynamics.a
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: src/BulletCollision/libBulletCollision.a
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: src/LinearMath/libLinearMath.a
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: /usr/lib/libglut.so
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: /usr/lib/i386-linux-gnu/libGL.so
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: /usr/lib/i386-linux-gnu/libGLU.so
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/build.make
Demos/DoublePrecisionDemo/AppDoublePrecisionDemo: Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable AppDoublePrecisionDemo"
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/AppDoublePrecisionDemo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/build: Demos/DoublePrecisionDemo/AppDoublePrecisionDemo
.PHONY : Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/build

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/requires: Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DoublePrecisionDemo.o.requires
.PHONY : Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/requires

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/clean:
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo && $(CMAKE_COMMAND) -P CMakeFiles/AppDoublePrecisionDemo.dir/cmake_clean.cmake
.PHONY : Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/clean

Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/depend:
	cd /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613 /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613 /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo /home/gao/Desktop/test/fuzzylite-1.03/bullet-2.81-rev2613/Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Demos/DoublePrecisionDemo/CMakeFiles/AppDoublePrecisionDemo.dir/depend

