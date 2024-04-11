#!/bin/bash
echo "File name?"
read file
echo -e "#!/usr/bin/python3\n# $file" > $file
chmod u+x $file
vim $file
