# Skin Cutter

Ember's tool for quickly cutting up character skin files.

# Introduction

This tool and README is a work in progress. Please leave any issues here on the repository.

This tool is intended to make custom skins an easier process. By cutting up any sized skin file, the results are pooped out into the active directory.

To use, simply type "python3 ./skin-cutter.py HumanMaleSkin00_00.png" and the resulting facial upper, lower, and pelvis files should be created.

This tool currently only handles PNGs. To bulk convert check out PNG2BLP.

You can use the find command in Linux to recursively run the skin-cutter.py script for all PNG files in the current directory and its subdirectories. Here's the command:

find . -type f -name "*.png" -exec python3 skin-cutter.py {} \;

