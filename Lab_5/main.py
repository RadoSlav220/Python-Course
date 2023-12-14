from argparse import ArgumentError
import sys
from source.JsonConverter import *
from source.requester import requestData
from source.CsvConverter import *

if __name__ == "__main__":
  if len(sys.argv) != 4:
    raise ArgumentError("Invalid number of args")

  mediaCollection = requestData(sys.argv[1], sys.argv[2])

  if sys.argv[3] == "json":
    print(convertMediaListToJSON(mediaCollection))
  elif sys.argv[3] == "csv":
    print(convertMediaListToCSV(mediaCollection))
  



  

  
  
