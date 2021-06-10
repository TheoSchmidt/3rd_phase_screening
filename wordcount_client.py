####################################################################
# Word Counter Client                                              #
#                                                                  #
# USAGE: python3 wordcount_client.py -f document.txt               #
#                                                                  #
# By Theo Schmidt @2021-06-10                                      #
#    theo_schmidt@hotmail.com                                      #
#                                                                  #
####################################################################
import sys
import requests
 
n = len(sys.argv)

if n < 3:
    print("\n USAGE: python3 wordcount_client.py -f document.txt \n")
else:
    param = sys.argv[1]
    filename = sys.argv[2]

    if param == "-f":
        with open(filename) as f:
            data = f.read()
        req = requests.post('http://127.0.0.1:8090/', data)
        print(req.text.replace(',','').replace('"','').replace('{','').replace('}','').replace(':',''))
    else:
        print("\n USAGE: python3 wordcount_client.py -f document.txt \n")

