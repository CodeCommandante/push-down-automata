"""    
    Program simulating PushDown Automata.
    Copyright (C) 2021  Jim Leon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import machine

InputExceptionMessage = 'The input file is in an incorrect format or contains syntax errors'

def buildFinals(string: str) -> list:
    Finals = []
    parts = string.split(',')
    for fs in parts:
        Finals.append(fs.strip())
    return Finals

def buildTransFA(transition: str) -> list:
    parts = transition.split('->')
    if not len(parts) == 2:
        raise Exception(InputExceptionMessage)
    leftSide = parts[0].strip()
    rightSide = parts[1].strip()
    leftSplit = leftSide.split(',')
    totalBuild = []
    if len(leftSplit) == 1:
        totalBuild.append(leftSplit[0].strip())
        totalBuild.append('')
        totalBuild.append(rightSide)
    elif len(leftSplit) == 2:
        totalBuild.append(leftSplit[0].strip())
        totalBuild.append(leftSplit[1].strip())
        totalBuild.append(rightSide)
    else:
        raise Exception(InputExceptionMessage)
    return totalBuild

def buildTransPDA(transition: str) -> list:
    parts = transition.split('->')
    if not len(parts) == 2:
        raise Exception(InputExceptionMessage)
    leftside = parts[0].strip()
    rightside = parts[1].strip()
    leftSplit = leftside.split(',')
    if not len(leftSplit) == 3:
        raise Exception(InputExceptionMessage)
    rightSplit = rightside.split(',')
    totalBuild = []
    if len(rightSplit) == 1:
        totalBuild.append(leftSplit[0].strip())
        totalBuild.append(leftSplit[1].strip())
        totalBuild.append(leftSplit[2].strip())
        totalBuild.append(rightSplit[0].strip())
        totalBuild.append('')
    elif len(rightSplit) == 2:
        totalBuild.append(leftSplit[0].strip())
        totalBuild.append(leftSplit[1].strip())
        totalBuild.append(leftSplit[2].strip())
        totalBuild.append(rightSplit[0].strip())
        totalBuild.append(rightSplit[1].strip())
    else:
        raise Exception(InputExceptionMessage)
    return totalBuild

def fileParse(fileName: str, machType: str) -> list:
    fin = open(fileName, 'r')
    params = []
    if machType == 'f':
        fileRead = fin.readlines()
        transGraph = []
        if len(fileRead) < 3:
            raise Exception(InputExceptionMessage)
        for t in range(len(fileRead) - 2):
            transition = fileRead[t].strip()
            transGraph.append(buildTransFA(transition))
        params.append(transGraph)
        params.append(fileRead[len(fileRead)-2].strip())
        params.append(buildFinals(fileRead[len(fileRead)-1]))
    elif machType == 'p':
        fileRead = fin.readlines()
        transGraph = []
        if len(fileRead) < 4:
            raise Exception(InputExceptionMessage)
        for t in range(len(fileRead) - 3):
            transition = fileRead[t].strip()
            transGraph.append(buildTransPDA(transition))
        params.append(transGraph)
        params.append(fileRead[len(fileRead)-3].strip())
        params.append(fileRead[len(fileRead)-2].strip())
        params.append(buildFinals(fileRead[len(fileRead)-1]))
    fin.close()
    return params

def runNAProgram(params: list):
    print('Enter strings to check if they are in the language on the machine, L(M).')
    print('When you are finished, enter \'quit\'')
    M = machine.FiniteAutomata(params[0],params[1],params[2])
    userIn = input()
    while not userIn == 'quit':
        if M.run(userIn):
            print(userIn,'is in the language!')
        else:
            print(userIn,'is not in the language!')
        userIn = input()
    return 

def runPDAProgram(params: list):
    print('Enter strings to check if they are in the language on the machine, L(M).')
    print('When you are finished, enter \'quit\'')
    M = machine.PushdownAutomata(params[0],params[1],params[2],params[3])
    userIn = input()
    while not userIn == 'quit':
        if M.run(userIn):
            print(userIn,'is in the language!')
        else:
            print(userIn,'is not in the language!')
        userIn = input()
    return