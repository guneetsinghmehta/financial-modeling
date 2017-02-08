contents=open('getCompanyDataYahoo2.py','r')
with open("getCompanyDataYahoo2.html", "w") as e:
    for lines in contents.readlines():
        e.write("<pre>" + lines + "</pre>\n")
