#!/usr/bin/env bash
echo "Enter file name:"
read file_nm
echo "#!/usr/bin/env bash" > $file_nm
chmod u+x $file_nm
echo "File created"
vi $file_nm
