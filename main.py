__author__ = 'Kaike'

import lexic_analyser

filename = "Code.txt"

code = open(filename,'r')

analyser = lexic_analyser.lexicAnalyser()

analyser.compile(code.read())


