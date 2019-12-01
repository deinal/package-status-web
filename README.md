# package-status-web
[![Build Status](https://travis-ci.org/hd4niel/package-status-web.svg?branch=master)](https://travis-ci.org/hd4niel/package-status-web)
[![Coverage Status](https://coveralls.io/repos/github/hd4niel/package-status-web/badge.svg?branch=master)](https://coveralls.io/github/hd4niel/package-status-web?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

Expose key information about packages in /var/lib/dpkg/status via an HTML interface

Live at: https://pkg-status.herokuapp.com/

---

* Name: Package name
* Dependencies: Names of the packages the current package depends on
* Alternatives: Alternative dependencies without an entry in the status file
* Description: Package description
* Need me: Names of the packages that depend on the current package

---

## Run locally

Python version: 3.7.3, should not be too strict though as long as it is python 3.x.

    git clone https://github.com/hd4niel/package-status-web.git
    cd package-status-web/
    pip install -r requirements.txt
    python main.py

Runs on http://0.0.0.0:5000/

By default status.real is read as package info file, but it is possible to give your own files as command line arguments:

    python main.py /var/lib/dpkg/status    

## Docker

Pull the image:

    docker pull hd4niel/package-status-web

Run using the default status.real file:

    docker run -p 5000:5000 hd4niel/package-status-web

Run using a package status file from your local filesystem:

    docker run -v /var/lib/dpkg/status:/mnt/status -p 5000:5000 hd4niel/package-status-web /mnt/status

The last command makes for a nice shell alias eg. pkgstatus
