names = ["libquadmath0", "libssl1.0.0"]
status = {"libquadmath0":
          {"Name": "libquadmath0",
           "Dependencies": ["gcc-5-base", "libc6"],
           "Description": "GCC Quad-Precision Math Library<br/> A library, which provides quad-precision mathematical functions on targets<br/> supporting the __float128 datatype. The library is used to provide on such<br/> targets the REAL(16) type in the GNU Fortran compiler.<br/>",
           "Need me": ["libssl1.0.0"]},
          "libssl1.0.0":
          {"Name": "libssl1.0.0",
           "Dependencies": ["libc6", "zlib1g", "libquadmath0"],
           "Description": "SSL shared libraries<br/> libssl and libcrypto shared libraries needed by programs like<br/> apache-ssl, telnet-ssl and openssh.<br/> .<br/> It is part of the OpenSSL implementation of SSL.<br/>",
           "Alternatives": ["debconf"]}
          }
unsure = {"libssl1.0.0": [" debconf (>= 0.5) ", " libquadmath0\n"]}
before_alt = {"libquadmath0":
              {"Name": "libquadmath0",
               "Dependencies": ["gcc-5-base", "libc6"],
               "Description": "GCC Quad-Precision Math Library<br/> A library, which provides quad-precision mathematical functions on targets<br/> supporting the __float128 datatype. The library is used to provide on such<br/> targets the REAL(16) type in the GNU Fortran compiler.<br/>"},
              "libssl1.0.0":
              {"Name": "libssl1.0.0",
                  "Dependencies": ["libc6", "zlib1g"],
                  "Description": "SSL shared libraries<br/> libssl and libcrypto shared libraries needed by programs like<br/> apache-ssl, telnet-ssl and openssh.<br/> .<br/> It is part of the OpenSSL implementation of SSL.<br/>"}
              }
before_need = {"libquadmath0":
               {"Name": "libquadmath0",
                "Dependencies": ["gcc-5-base", "libc6"],
                "Description": "GCC Quad-Precision Math Library<br/> A library, which provides quad-precision mathematical functions on targets<br/> supporting the __float128 datatype. The library is used to provide on such<br/> targets the REAL(16) type in the GNU Fortran compiler.<br/>"},
               "libssl1.0.0":
               {"Name": "libssl1.0.0",
                   "Dependencies": ["libc6", "zlib1g", "libquadmath0"],
                   "Description": "SSL shared libraries<br/> libssl and libcrypto shared libraries needed by programs like<br/> apache-ssl, telnet-ssl and openssh.<br/> .<br/> It is part of the OpenSSL implementation of SSL.<br/>"}
               }
lines = ["Package: libquadmath0\n",
         "Status: install ok installed\n",
         "Priority: optional\n", "Section: libs\n",
         "Installed-Size: 265\n",
         "Maintainer: Ubuntu Core developers <ubuntu-devel-discuss@lists.ubuntu.com>\n",
         "Architecture: amd64\n", "Multi-Arch: same\n",
         "Source: gcc-5\n", "Version: 5.4.0-6ubuntu1~16.04.12\n",
         "Depends: gcc-5-base (= 5.4.0-6ubuntu1~16.04.12), libc6 (>= 2.23)\n",
         "Description: GCC Quad-Precision Math Library\n",
         " A library, which provides quad-precision mathematical functions on targets\n",
         " supporting the __float128 datatype. The library is used to provide on such\n",
         " targets the REAL(16) type in the GNU Fortran compiler.\n",
         "Homepage: http://gcc.gnu.org/\n",
         "Original-Maintainer: Debian GCC Maintainers <debian-gcc@lists.debian.org>\n",
         "\n",
         "Package: libssl1.0.0\n",
         "Status: install ok installed\n",
         "Multi-Arch: same\n",
         "Priority: important\n",
         "Section: libs\n",
         "Installed-Size: 2836\n",
         "Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>\n",
         "Architecture: amd64\n",
         "Source: openssl\n",
         "Version: 1.0.1-4ubuntu5.5\n",
         "Depends: libc6 (>= 2.14), zlib1g (>= 1:1.1.4), debconf (>= 0.5) | libquadmath0\n",
         "Pre-Depends: multiarch-support\n",
         "Breaks: openssh-client (<< 1:5.9p1-4), openssh-server (<< 1:5.9p1-4)\n",
         "Description: SSL shared libraries\n",
         " libssl and libcrypto shared libraries needed by programs like\n",
         " apache-ssl, telnet-ssl and openssh.\n",
         " .\n",
         " It is part of the OpenSSL implementation of SSL.\n",
         "Original-Maintainer: Debian OpenSSL Team <pkg-openssl-devel@lists.alioth.debian.org>\n",
         "\n"]
