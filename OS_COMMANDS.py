import commands


f = open("abcde", 'r' )
f2 = f.read().splitlines()
for str1 in f2:
  cmd2 = "| awk '{if ($1/1024/1024 > 10) print $1,$2; else print 'OKAY' }'"
  cmd = "du -s " + str1 + cmd2
  #print (cmd)
  A = commands.getoutput(cmd)
  if A != OKAY:
