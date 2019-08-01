import pdal
import os

class Compress:
    def __init__(self):
        self.__encodeStr = """{
        "pipeline":[
        {
            "type" : "readers.las",
            "filename" : "input.las"
        },
        {
            "type" : "writers.las",
            "compression":"laszip",
            "filename" : "output.laz",
            "forward" : ["scale", "offset"]
        }
        ]
        }"""
        self.__decodeStr = """{
        "pipeline":[
        {
            "type" : "readers.las",
            "filename" : "input.laz"
        },
        {
            "type" : "writers.las",
            "filename" : "output.las",
            "forward" : ["scale", "offset"]
        }
        ]
        }"""

    def Encode(self, file):
        self.__encodeStr, bkp = self.SetCode(file, self.__encodeStr)
        self.RunProcess(self.__encodeStr)
        self.__encodeStr = bkp

    def Decode(self, file):
        self.__decodeStr, bkp = self.SetCode(file, self.__decodeStr)
        self.RunProcess(self.__decodeStr)
        self.__decodeStr = bkp

    def RunProcess(self, json):
        pipeline = pdal.Pipeline(json)
        count = pipeline.execute()
        print("done Process")
    
    def SetCode(self, file, codeStr):
        bkp = codeStr
        name, _, = os.path.splitext(file) 
        codeStr = codeStr.replace("input", name)
        codeStr = codeStr.replace("output", name)
        print(codeStr)
        return codeStr, bkp

def Main():

    compress = Compress()
    compress.Encode("scans/test2.las")
    compress.Decode("scans/test2.laz")


# Run main...
if __name__ == '__main__':
    Main()
