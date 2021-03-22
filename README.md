# find-dead-links

This is a repository for Assignment A6 in BVU's CMSC 190 DevOps course (Spring 2021).

# Dependencies

This assumes you have `virtualenv` and `python3` installed.

# Installation

Typing `make install` installs `find-dead-links` to `~/bin`.

To install to another directory, type `make install INSTALL_DIR=<DIRECTORY>` where `<DIRECTORY>` is your chosen directory.

# Running

`find-dead-links <url>` - Finds all dead links in the given URL.

`find-dead-links -<levels> <url>` - Finds all dead links in the given URL, and recursively searches for dead links in all accessible URLs in the specified URL.
It continues this for `<levels>` levels.
