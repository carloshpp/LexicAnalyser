__author__ = 'Kaike'
from enum import Enum
import tokens as Token

class lexicAnalyser():

    def __init__(self):
        code = ""
        i = 0

    def setCode(self, _code):
        code = _code
        i = 0;

    def nextToken(self):
        while(lexicAnalyser.isSpace(nextChar)):
            nextChar = lexicAnalyser.readChar()

        if nextChar.isalpha():
            text = ""
            while True:
                text += nextChar
                nextChar = lexicAnalyser.readChar()
                if not lexicAnalyser.isalnum(nextChar) and nextChar != "_":
                    break

            token = Token.searchKeyWord(text)
            if(token == 'ID'):
                tokenSec = Token.searchName(text)

        elif lexicAnalyser.isNumeric(nextChar):
            num = ""
            while True:
                num += nextChar
                nextChar = lexicAnalyser.readChar()
                if not lexicAnalyser.isNumeric(nextChar):
                    break

            token = 'NUMERAL'
            tokenSec = lexicAnalyser.addIntConst(num)

        elif nextChar == '"':
            text = ""
            while True:
                text += nextChar
                nextChar = lexicAnalyser.readChar()
                if nextChar == '"':
                    break
            token = 'STRING'
            tokenSec = text
        else:
            if nextChar == '\'':
                nextChar = lexicAnalyser.readChar()
                token = 'CHARACTER'
                tokenSec = lexicAnalyser.addCharConst(nextChar)
                nextChar = lexicAnalyser.readChar()
                nextChar = lexicAnalyser.readChar()
            elif nextChar == ':':
                nextChar = lexicAnalyser.readChar()
                token = 'COLON'
            elif nextChar == '+':
                nextChar = lexicAnalyser.readChar()
                if nextChar == lexicAnalyser.readChar():
                    token = 'PLUS_PLUS'
                    nextChar = lexicAnalyser.readChar()
                else:
                    token = 'PLUS'
            else:
                token = 'UNKNOWN'
        return token


    def isSpace(self, char):
        return " " == char


    def readChar(self):
        lexicAnalyser.i += 1
        return lexicAnalyser.code[lexicAnalyser.i-1]

    def isNumeric(self,ch):
        try:
            float(ch)
            return True
        except ValueError:
            return False

    def addStringConst(self, string):
        return ""

    def addCharConst(self, ch):
        return ""

    def addIntConst(self,integer):
        return ""