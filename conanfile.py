from conans import ConanFile, tools, os


class BoostLevel8GroupConan(ConanFile):
    name = "Boost.Level8Group"
    version = "1.64.0"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-boost-level8group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Generator/0.0.1@bincrafters/testing"
    lib_short_names = ["math", "lexical_cast"]
    requires = "Boost.Array/1.64.0@bincrafters/testing", \
               "Boost.Assert/1.64.0@bincrafters/testing", \
               "Boost.Atomic/1.64.0@bincrafters/testing", \
               "Boost.Concept_Check/1.64.0@bincrafters/testing", \
               "Boost.Container/1.64.0@bincrafters/testing", \
               "Boost.Config/1.64.0@bincrafters/testing", \
               "Boost.Core/1.64.0@bincrafters/testing", \
               "Boost.Detail/1.64.0@bincrafters/testing", \
               "Boost.Function/1.64.0@bincrafters/testing", \
               "Boost.Fusion/1.64.0@bincrafters/testing", \
               "Boost.Integer/1.64.0@bincrafters/testing", \
               "Boost.Lambda/1.64.0@bincrafters/testing", \
               "Boost.Mpl/1.64.0@bincrafters/testing", \
               "Boost.Numeric_Conversion/1.64.0@bincrafters/testing", \
               "Boost.Predef/1.64.0@bincrafters/testing", \
               "Boost.Range/1.64.0@bincrafters/testing", \
               "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
               "Boost.Static_Assert/1.64.0@bincrafters/testing", \
               "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
               "Boost.Tuple/1.64.0@bincrafters/testing", \
               "Boost.Type_Traits/1.64.0@bincrafters/testing", \
               "Boost.Utility/1.64.0@bincrafters/testing"

    # Math Dependencies
    # array3 assert1 atomic4 concept_check5 config0 core2 detail5 function5 fusion5 integer3
    # lambda6 lexical_cast8 mpl5 predef0 range7 smart_ptr4 static_assert1 throw_exception2 tuple4 type_traits3 utility5

    # Lexical_Cast Dependencies
    # array3 assert1 config0 container7 core2 integer3 math8 mpl5 numeric~conversion6 range7 static_assert1 throw_
    # exception2 type_traits3

    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/math"))

        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, "https://github.com/boostorg/lexical_cast"))
                 
    def build(self):
        boost_build = self.deps_cpp_info["Boost.Build"]
        b2_bin_name = "b2.exe" if self.settings.os == "Windows" else "b2"
        b2_bin_dir_name = boost_build.bindirs[0]
        b2_full_path = os.path.join(boost_build.rootpath, b2_bin_dir_name, b2_bin_name)

        toolsets = {
          'gcc': 'gcc',
          'Visual Studio': 'msvc',
          'clang': 'clang',
          'apple-clang': 'darwin'}

        b2_toolset = toolsets[str(self.settings.compiler)]
        
        self.run(b2_full_path + " -j4 -a --hash=yes toolset=" + b2_toolset)
        
    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(self.build_folder, lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)
        lib_dir = os.path.join(self.build_folder, "stage/lib")
        self.copy(pattern="*", dst="lib", src=lib_dir)
       
    def package_info(self):
        self.cpp_info.libs = ["boost_%s"%(lib_short_name) for lib_short_name in self.lib_short_names ]
