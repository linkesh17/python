import re

num1 = "5234567890"

num2 = "7010141655"

num3 ="134135"

matchObj = re.match( r'^[6-9][0-9]{9}', num2)

if matchObj :

  print "Valid"


else:

  print "Invalid!!"
