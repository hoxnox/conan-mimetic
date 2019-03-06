from conans import ConanFile, CMake
import os

channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "hoxnox")

class FnvTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "mimetic/0.9.8@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        self.run('cmake "%s" %s' % (self.source_folder, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        os.chdir("bin")
        self.run(".%stestapp" % os.sep)
