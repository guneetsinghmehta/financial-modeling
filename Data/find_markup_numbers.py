import glob
import re
#indir = '/Users/nehamittal/github/financial-modeling/Data/Intrino_news/nivetha/done_files/*.txt'
indir = 'Intrino_news/nivetha/output_files/test/*.txt'
def find_all(a_str, sub):
    start = 0
    ans=0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return ans
        ans=ans+1
        start += len(sub) # use start += 1 to find overlapping matches

markups=0
fileList=glob.glob(indir)
for f in fileList:
  fileHandle=open(f)
  pattern="<strong>"
  for line in fileHandle:
    markups=markups+find_all(line,pattern)

print(markups)
