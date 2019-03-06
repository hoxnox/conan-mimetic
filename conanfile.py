from nxtools import NxConanFile
from conans import tools, AutoToolsBuildEnvironment


class MimeticConan(NxConanFile):
    name = "mimetic"
    version = "0.9.8"
    url = "http://www.codesink.org/mimetic_mime_library.html"
    settings = "os", "compiler", "build_type", "arch"
    description = "Email library (MIME)"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    license = "http://en.wikipedia.org/wiki/MIT_License"

    def do_source(self):
        self.retrieve("3a07d68d125f5e132949b078c7275d5eb0078dd649079bd510dd12b969096700",
                [
                    "vendor://codesink.org/mimetic/mimetic-{v}.tar.gz".format(v=self.version),
                    "http://www.codesink.org/download/mimetic-{v}.tar.gz".format(v=self.version)
                ], "mimetic-{v}.tar.gz".format(v=self.version))

    def do_build(self):
        tools.untargz("mimetic-{v}.tar.gz".format(v=self.version))
        env_build = AutoToolsBuildEnvironment(self)
        with tools.environment_append(env_build.vars):
            with tools.chdir(self.name + "-{v}".format(v=self.version)):
                self.run("./configure prefix=\"{staging}\"".format(staging=self.staging_dir))
                self.run("make install")

    def do_package_info(self):
        self.cpp_info.libs = ["mimetic"]

