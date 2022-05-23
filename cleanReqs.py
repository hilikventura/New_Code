import sys
def main(path=""):
    if path!="":
        reqsList=[]
        with open(path,"rt") as f:
            reqsList=f.readlines()
        final=""
        for req in reqsList:
            final+= str(req).split("==")[0]+"\n"
        with open(path,"wt") as f:
            f.write(final)
        print("DONE")



if len(sys.argv) == 2 :
    main(list(sys.argv)[1])