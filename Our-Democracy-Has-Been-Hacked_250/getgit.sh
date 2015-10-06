#!/bin/bash

# Curls the generic files within a .git folder for structure
mkdir -p .git/
cd .git/;
mkdir -p {hooks,info,objects/{info,pack},refs/{heads,tags}};
for file in HEAD config description info/exclude refs/heads/master; do
    curl "http://54.152.37.157/.git/${file}" > "${file}";
done;
cd ..;
