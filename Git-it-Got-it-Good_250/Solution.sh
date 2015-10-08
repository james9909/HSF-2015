#!/bin/bash

cd git-it-got-it-good
git checkout master

for i in `seq 1 7`;
do
    git checkout HEAD~1
    cat s3cr3t >> ../s3cr3t
done

# With a little bit of reconstruction and knowledge about memes, we can reconstruct s3cr3t

# And his name is flag{JO0O0HHHNNNN_CEEENNNNA4A4A}
