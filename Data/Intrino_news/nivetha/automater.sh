files=$(ls .)
for file in $files
do
  echo $file
  atom $file &
  read dummy
done
