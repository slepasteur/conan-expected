#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibnameConan(ConanFile):
    name = "expected"
    version = "0.3"
    description = "C++11/14/17 std::expected with functional-style extensions"
    topics = ("expected", "outcome")
    url = "https://github.com/bincrafters/conan-libname"
    homepage = "https://github.com/TartanLlama/expected"
    author = "Simon Lepasteur <slepasteur@gmail.com>"
    license = "CC0-1.0"
    exports = ["LICENSE.md"]
    _source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/TartanLlama/expected"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version), sha256="18103ac213b3a7e5740bee754c9a5f96a4cee0ead1f2f7670775efc467b56ac3")
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*.h", dst=os.path.join("include", "tl"), src=os.path.join(self._source_subfolder, "tl"))
        self.copy(pattern="*.hpp", dst=os.path.join("include", "tl"), src=os.path.join(self._source_subfolder, "tl"))

    def package_info(self):
        self.info.header_only()
