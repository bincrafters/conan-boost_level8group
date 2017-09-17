## This repository holds a conan recipe for a cyclic dependency group featuring multiple libraries.

[Conan.io](https://conan.io) package for [Boost.Level8Group](http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm) 

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/Boost.Level8Group%3Abincrafters).

## For Users

### Do not consume this package directly.  It is intended for use only within other boost packages.

### Basic setup for using with other Boost packages

    $ conan install Boost.Level8Group/1.65.1@bincrafters/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Boost.Level8Group/1.65.1@bincrafters/testing

    [generators]
    txt

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they shoudl not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This package contains header-only libraries, so nothing needs to be built.

## Package 

    $ conan create bincrafters/testing
	
## Add Remote

	$ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload --all --remote bincrafters Boost.Level8Group/1.65.1@bincrafters/testing

### License
[Boost](LICENSE)
