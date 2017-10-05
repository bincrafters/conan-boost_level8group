## This repository holds a conan recipe for a cyclic dependency group featuring multiple libraries.

[![Build status](https://ci.appveyor.com/api/projects/status/8o42w7lw2rxmllx0/branch/stable/1.65.1?svg=true)](https://ci.appveyor.com/project/BinCrafters/conan-boost-level8group/branch/stable/1.65.1)
[![Travis Status](https://travis-ci.org/bincrafters/conan-boost-level8group.svg?branch=stable%2F1.65.1)](https://travis-ci.org/bincrafters/conan-boost-level8group)
[![Download](https://api.bintray.com/packages/bincrafters/public-conan/Boost.Level8Group%3Abincrafters/images/download.svg?version=1.65.1%3Astable) ](https://bintray.com/bincrafters/public-conan/Boost.Level8Group%3Abincrafters/1.65.1%3Astable/link)

[Conan.io](https://conan.io) package for [Boost.Level8Group](http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm) 

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/Boost.Level8Group%3Abincrafters).

## For Users

### Do not consume this package directly.  It is intended for use only within other boost packages.

### Basic setup for using with other Boost packages

    $ conan install Boost.Level8Group/1.65.1@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Boost.Level8Group/1.65.1@bincrafters/stable

    [generators]
    txt

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This package contains header-only libraries, so nothing needs to be built.

## Package 

    $ conan create bincrafters/stable
	
## Add Remote

	$ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload --all --remote bincrafters Boost.Level8Group/1.65.1@bincrafters/stable

### License
[Boost](www.boost.org/LICENSE_1_0.txt)
