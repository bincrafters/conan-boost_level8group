from conans import ConanFile, tools, os


class BoostLevel8GroupConan(ConanFile):
    name = "Boost.Level8Group"
    version = "1.64.0"
    generators = "txt"
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/conan-boost-level8group"
    description = "Special package with all members of cyclic dependency group"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Build/1.64.0@bincrafters/testing"
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
                 
    def package(self):
        math_dir = os.path.join(self.build_folder, "math", "include")
        self.copy(pattern="*", dst="include", src=math_dir)

        lexical_cast_dir = os.path.join(self.build_folder, "lexical_cast", "include")
        self.copy(pattern="*", dst="include", src=lexical_cast_dir)


