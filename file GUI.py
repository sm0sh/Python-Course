fp = open("geek.txt","w")
fp.write("text")
with open("geek.txt","r")as fp:
    con = fp.read()
    print(con)

fp.close()    
