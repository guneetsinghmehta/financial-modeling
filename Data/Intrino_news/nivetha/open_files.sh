python file_order_opener.py
file_name=$(cat read_order)
for file in $file_name
do
  atom $file
  echo $file | cat >> done_files.txt
  read dummy
done
