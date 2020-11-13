import hashlib
import time
import itertools

# a class of password generator
# used to generate file "hashes.txt", for specific usage info, checkout the comment section in main()
# can generate a file of MD5 hashes based on the user input password
class pwdGenerator:
    def __init__(self):
        pass
    def GenerateHashFile(self, fileName):
        symbols_input = input("Enter password to generate MD5 hashes (separated by space): ");
        symbols = symbols_input.split();
        file_to_generate = open(fileName, "w");
        
        for s in symbols:
            result = hashlib.md5(s.encode());
            file_to_generate.write(str(result.hexdigest()))
            if symbols.index(s) != len(symbols) - 1:
                file_to_generate.write("\n")
            print(result.hexdigest())
        
        file_to_generate.close();

# a class of password cracker
# checkout main() for specific usage info
# after creating a pwdCracker instance, call member function CrackHashFile(fileName) to crack passwords. 
# fileName is the file containing password MD5 hashes
class pwdCracker:
    def __init__(self):
        self.charset = [char for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@"]
        self.listofHashes = []

    #helper function to crack the password. Will try to crack password represnted by hashVal
    def CheckHash(self, hashVal):
        pwdLen = 1;
        while pwdLen <= len(self.charset):
            print("curr len testing: " + str(pwdLen))
            #generate a combination of length pwdLen from charset, then compare it with hash
            for comb in itertools.permutations(self.charset, pwdLen):
                string = ""
                for c in comb:
                    string += str(c)
         
                result = hashlib.md5(string.encode())
                resulthex = str(result.hexdigest())

                #check agianst the hashVal
                if resulthex == hashVal:
                    return string
            pwdLen = pwdLen + 1

        return False
    
    def CrackHashFile(self, fileName):
        startTime = time.time()
        file_to_read = open(fileName, "r");

        for line in file_to_read:
            newLine = line.replace('\n', '')
            self.listofHashes.append(newLine);
        for hashVal in self.listofHashes:
            password = self.CheckHash(hashVal)
            endTime = time.time()
            if(password != False):
                print(password + '\t' + str(endTime - startTime))
            else:
                print("No password can be cracked from the existing character set, sorry")



def main():
    #To generate a new file containing the MD5 hashes of the password inputed by user, uncomment the line below
    """
    test_g = pwdGenerator();
    test_g.GenerateHashFile("hashes.txt");
    """
    print("   ")
    print("ITP125 Python Brute-force Hash-Cracker")
    print("You can create a file of MD5 hashes with user input")
    print("And you can run the password cracker against that file")
    print("Format: cracked password       cracktime")
    print("\n")
    
    test = pwdCracker()
    test.CrackHashFile("hashes.txt")


main()




