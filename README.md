# package-status-web
[![Build Status](https://travis-ci.org/hd4niel/package-status-web.svg?branch=master)](https://travis-ci.org/hd4niel/package-status-web)
[![Coverage Status](https://coveralls.io/repos/github/hd4niel/package-status-web/badge.svg?branch=master)](https://coveralls.io/github/hd4niel/package-status-web?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

Expose key information about packages in /var/lib/dpkg/status via an HTML interface

## Docker

Pull the image:

    docker pull hd4niel/package-status-web

Run using the default status.real file:

    docker run -p 5000:5000 hd4niel/package-status-web

Run using a package status file from your local filesystem:

    docker run -v /var/lib/dpkg/status:/mnt/status -p 5000:5000 hd4niel/package-status-web /mnt/status

The last command makes for a nice shell alias eg. pkgstatus
