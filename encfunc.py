class Msg:
    def __init__(self):
        self.__msg=input("Enter the message to encode: ")
        self.__enc=[]
        self.__dec=[]
    def encode(self,msg=None):
        if msg is None:
            msg=self.__msg
        for x in msg:
            y=ord(x)
            y=2*y+3
            y=chr(y)
            self.__enc.append(y)
        return "".join(self.__enc)
    def decode(self,msg=None):
        if msg is None:
            msg=self.__enc
        for x in self.__enc:
            a=ord(x)
            a-=3
            a=int(a/2)
            a=chr(a)
            self.__dec.append(a)
        return "".join(self.__dec)
def main():
    code1=Msg()
    print("The encoded message is: ",code1.encode())
    print("If the encoded message is decoded we get: ",code1.decode())
if __name__=="__main__":
    main()
