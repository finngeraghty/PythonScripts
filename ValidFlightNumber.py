import re
###
flight = raw_input('what is flight number')

#####REGEX HERE TO PARSE AND VALIDATE FLIGHT NUMBER AND EXIT ON FAILURE for SECURITY
test1 = flight
###Referencelink: http://academe.co.uk/2014/01/validating-flight-codes/
#Do not fuck up trailing strings
p = re.compile(r'^([a-z][a-z]|[a-z][0-9]|[0-9][a-z])[a-z]?[0-9]{1,4}[a-z]?$')
m = p.search(test1)  # p.match() to find from start of string only

if m:
    pass
else:
    print('[error],[bad flight number],[flightNumber error]'),quit()

a = re.compile(r'^([a-z][a-z]|[a-z][0-9]|[0-9][a-z])([a-z]?[0-9]{1,4}[a-z]?)$')

#####SECOND REGEG TO FIND THE CARRIER CODE PORTION OF STING

b = p.findall(test1)
if b:
    pass
else:
    print('[error],[bad flight number][carrierCode error]'),quit()

###SECOND REGEX RETURNS LIST b[0] FOR FIRST GROUP IN REGEX

ccode = (b[0])
ccodes = str(ccode)
fcode = str(test1)
fcodes = str.replace(fcode,ccodes,"")

print('valid flight code: ') + flight
