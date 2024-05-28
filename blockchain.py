from hashlib import sha256

def updateHash(*args):
    hashingText = ""; h = sha256()
    for arg in args:
        hashingText += str(args)
    
    h.update(hashingText.encode("utf-8"))
    return h.hexdigest()

class Block():
    data = None
    hash = None
    nonce = 0
    previousHash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number
    
    def hash(self):
       return updateHash(self.previousHash, self.number, self.data, self.nonce)

class Blockchain():
    pass

def main():
    block = Block("Hello world", 1)
    print(block.hash())

if __name__ == "__main__":
    main()
