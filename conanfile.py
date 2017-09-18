from conans import ConanFile, tools, os


class BoostLevel8GroupConan(ConanFile):
    name = "Boost.Level8Group"
    version = "1.65.1"
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-level8group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Generator/1.64.0@bincrafters/testing"
    lib_short_names = ["math", "lexical_cast"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = "Boost.Array/1.65.1@bincrafters/testing", \
               "Boost.Assert/1.65.1@bincrafters/testing", \
               "Boost.Atomic/1.65.1@bincrafters/testing", \
               "Boost.Concept_Check/1.65.1@bincrafters/testing", \
               "Boost.Container/1.65.1@bincrafters/testing", \
               "Boost.Config/1.65.1@bincrafters/testing", \
               "Boost.Core/1.65.1@bincrafters/testing", \
               "Boost.Detail/1.65.1@bincrafters/testing", \
               "Boost.Function/1.65.1@bincrafters/testing", \
               "Boost.Fusion/1.65.1@bincrafters/testing", \
               "Boost.Integer/1.65.1@bincrafters/testing", \
               "Boost.Lambda/1.65.1@bincrafters/testing", \
               "Boost.Mpl/1.65.1@bincrafters/testing", \
               "Boost.Numeric_Conversion/1.65.1@bincrafters/testing", \
               "Boost.Predef/1.65.1@bincrafters/testing", \
               "Boost.Range/1.65.1@bincrafters/testing", \
               "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
               "Boost.Static_Assert/1.65.1@bincrafters/testing", \
               "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
               "Boost.Tuple/1.65.1@bincrafters/testing", \
               "Boost.Type_Traits/1.65.1@bincrafters/testing", \
               "Boost.Utility/1.65.1@bincrafters/testing"

    # Math Dependencies
    # array3 assert1 atomic4 concept_check5 config0 core2 detail5 function5 fusion5 integer3
    # lambda6 lexical_cast8 mpl5 predef0 range7 smart_ptr4 static_assert1 throw_exception2 tuple4 type_traits3 utility5

    # Lexical_Cast Dependencies
    # array3 assert1 config0 container7 core2 integer3 math8 mpl5 numeric~conversion6 range7 static_assert1 throw_
    # exception2 type_traits3

    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def build(self):
        self.run(self.deps_user_info['Boost.Generator'].b2_command)

    def package(self):
        self.copy(pattern="*", dst="lib", src="stage/lib")
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)

    def package_info(self):
        self.user_info.lib_short_names = ",".join(self.lib_short_names)
        self.cpp_info.libs = self.collect_libs()
        self.cpp_info.defines.append("BOOST_ALL_NO_LIB=1")

