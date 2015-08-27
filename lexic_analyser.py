__author__ = 'Kaike'
import tokens

# add comments do the project
class lexicAnalyser():

    def __init__(self):
        self.code = ""
        self.i = 0
        #TO DO: save consts and sec tokens
        self.names = []
        self.Consts = []

    def setCode(self, _code):
        code = _code
        i = 0;

    def compile(self):
        self.nextToken()

    def nextToken(self):
        # TO DO: loop to compile the whole code
        nextChar = ''
        while(self.isSpace(nextChar)):
            nextChar = self.readChar()

        if nextChar.isalpha():
            text = ""
            while True:
                text += nextChar
                nextChar = self.readChar()
                if (not self.isalnum(nextChar)) and nextChar != "_":
                    break

            token = tokens.searchKeyWord(text)
            # TO DO: save the secundary token
            if(token == -1):
                tokenSec = tokens.searchName(text)

        elif self.isNumeric(nextChar):
            num = ""
            while True:
                num += nextChar
                nextChar = self.readChar()
                if not self.isNumeric(nextChar):
                    break

            token = tokens.Tokens.Numeral.value
            tokenSec = self.addIntConst(num)

        elif nextChar == '"':
            text = ""
            while True:
                text += nextChar
                nextChar = self.readChar()
                if nextChar == '"':
                    break
            token = tokens.Tokens.STRING.value
            tokenSec = text
        else:
            if nextChar == '\'':
                nextChar = self.readChar()
                token = tokens.Tokens.CHARACTER.value
                tokenSec = self.addCharConst(nextChar)
                nextChar = self.readChar()
                nextChar = self.readChar()
            elif nextChar == ':':
                nextChar = self.readChar()
                token = tokens.Tokens.COLON.value
            elif nextChar == '+':
                nextChar = self.readChar()
                if nextChar == self.readChar():
                    token = tokens.Tokens.PLUS_PLUS.value
                    nextChar = self.readChar()
                else:
                    token = tokens.Tokens.PLUS.value
            else:
                token = tokens.Tokens.UNKNOWN.value
        return token


    def isSpace(self, char):
        return " " == char


    def readChar(self):
        self.i += 1
        if self.i-1 <= len(self.code):
            return lexicAnalyser.code[lexicAnalyser.i-1]
        return "\0"

    def isNumeric(self,ch):
        try:
            float(ch)
            return True
        except ValueError:
            return False

    # TO DO: Not Implement Yet
    def addStringConst(self, string):
        return ""

    # TO DO: Not Implement Yet
    def addCharConst(self, ch):
        return ""

    # TO DO: Not Implement Yet
    def addIntConst(self,integer):
        return ""