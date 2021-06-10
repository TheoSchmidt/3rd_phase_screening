####################################################################
# Word Counter Server                                              #
#                                                                  #
# USAGE: python3 wordcount_server.py                                #
#                                                                  #
# By Theo Schmidt @2021-06-10                                      #
#    theo_schmidt@hotmail.com                                      #
#                                                                  #
####################################################################
import sys
import json
from collections import defaultdict
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def computation():
    data = request.get_data(as_text=True)
    words = data.split()
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    print("Data Processed!")
    return json.dumps(word_counts, indent=4, sort_keys=True)

app.run(host="127.0.0.1", port=8090)
