#!/bin/bash
echo "Enter file name:"
read file_nm
echo "#!/bin/bash" > $file_nm
chmod u+x $file_nm
echo "File created"
vi $file_nm
