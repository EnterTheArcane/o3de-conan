from conan import ConanFile


class TestPackage(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "VirtualBuildEnv"
    test_type = "explicit"

    def build_requirements(self):
        self.tool_requires(self.tested_reference_str)

    def build(self):
        pass

    def test(self):
        self.run("jom /VERSION")
