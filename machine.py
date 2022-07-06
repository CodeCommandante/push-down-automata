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

class FiniteAutomata:
    __finalStates = []
    __startState = ""
    __transGraph = []

    def __init__(self,transitions: list,sState: str,fStates: list):
        self.__checkBadInput(transitions,sState,fStates)
        self.__startState = sState
        self.__finalStates = fStates.copy()
        self.__transGraph = transitions.copy()

    def __del__(self):
        self.__finalStates.clear()
        self.__transGraph.clear()

    def __checkBadInput(self,transitions: list, sState: str, fStates: list):
        if len(sState) < 1:
            raise Exception('There must be a starting state for the machine')
        if len(fStates) < 1:
            raise Exception('There must be at least one final state in the machine')
        for t in transitions:
            if not (len(t) == 3):
                raise Exception('Transitions must be on the form (state,symbol,state)')
            if (len(t[0]) < 1) or (len(t[2]) < 1):
                raise Exception('Invalid state found in transition definition')
            if (len(t[1]) < 1) or (len(t[1]) > 1):
                raise Exception('Invalid symbol found in transition definition')
        for f in fStates:
            if len(f) < 1:
                raise Exception('Invalid state found in final states definition')
    
    def __isFinalState(self,state: str) -> bool:
        for s in self.__finalStates:
            if state == s:
                return True
        return False
    
    def __nextState(self,currState: str, sym: str) -> str:
        for t in self.__transGraph:
            if (currState == t[0]) and (sym == t[1]):
                return t[2]
        return None

    def listTransitions(self):
        for t in self.__transGraph:
            print(t)

    def run(self,word: str,showWalk=False) -> bool:
        Walk = []
        Walk.append(self.__startState)
        currState = self.__startState
        for sym in word:
            nextState = self.__nextState(currState,sym)
            if (nextState == None):
                return False
            else:
                Walk.append(nextState)
                currState = nextState
        if showWalk:
            for w in Walk:
                print(w)
        return self.__isFinalState(currState)

class PushdownAutomata:
    __finalStates = []
    __theStack = []
    __stackStart = ""
    __startState = ""
    __transGraph = []

    def __init__(self,transitions: list,sState: str,stackSyms: str,fStates: list):
        self.__checkBadInput(transitions,sState,stackSyms,fStates)
        self.__startState = sState
        self.__stackStart = stackSyms
        self.__stackPut(stackSyms)
        self.__finalStates = fStates.copy()
        self.__transGraph = transitions.copy()

    def __del__(self):
        self.__finalStates.clear()
        self.__transGraph.clear()
        self.__theStack.clear()

    def __checkBadInput(self,transitions: list, sState: str, stackSyms: str, fStates: list):
        if len(sState) < 1:
            raise Exception('There must be a starting state for the machine')
        if len(fStates) < 1:
            raise Exception('There must be at least one final state in the machine')
        if len(stackSyms) < 1:
            raise Exception('The stack must have starting symbol(s)')
        for t in transitions:
            if not (len(t) == 5):
                raise Exception('Transitions must be on the form (state,symbol,topStack,state,topStack)')
            if (len(t[0]) < 1) or (len(t[1]) > 1) or not (len(t[2]) == 1) or (len(t[3]) < 1):
                raise Exception('Invalid state found in transition definition')
        for f in fStates:
            if len(f) < 1:
                raise Exception('Invalid state found in final states definition')
    
    def __isFinalState(self,state: str) -> bool:
        for s in self.__finalStates:
            if state == s:
                return True
        return False
    
    def __nextState(self,currState: str, sym: str) -> str:
        Dest = None
        for t in self.__transGraph:
            if not self.__stackEmpty() and (currState == t[0]) and (sym == t[1]) and (t[2] == self.__stackPeek()):
                self.__stackPop()
                self.__stackPut(t[4])
                Dest = t[3]
        if (Dest == None):
            for u in self.__transGraph:
                if not self.__stackEmpty() and (currState == t[0]) and ('' == t[1]) and (t[2] == self.__stackPeek()):
                    self.__stackPop()
                    self.__stackPut(t[4])
                    Dest = self.__nextState(t[3],sym)
        return Dest

    def __stackEmpty(self):
        if len(self.__theStack) == 0:
            return True
        return False

    def __stackPeek(self) -> str:
        if self.__stackEmpty():
            raise Exception('The stack was exhausted')
        return self.__theStack[len(self.__theStack) - 1]

    def __stackPop(self) -> str:
        if self.__stackEmpty():
            raise Exception('The stack was exhausted')
        return self.__theStack.pop()

    def __stackPut(self,syms: str):
        Syms = list(syms)
        while len(Syms) > 0:
            self.__theStack.append(Syms.pop())

    def __stackReset(self):
        self.__theStack.clear()
        self.__stackPut(self.__stackStart)

    def listTransitions(self):
        for t in self.__transGraph:
            print(t)

    def run(self,word: str,showWalk=False) -> bool:
        Walk = []
        Walk.append(self.__startState)
        currState = self.__startState
        for sym in word:
            nextState = self.__nextState(currState,sym)
            if (nextState == None):
                self.__stackReset()
                return False
            else:
                Walk.append(nextState)
                currState = nextState
        if not self.__isFinalState(currState):
            nextState = self.__nextState(currState,'')
            if (nextState == None):
                self.__stackReset()
                return False
            else:
                Walk.append(nextState)
                currState = nextState
        if showWalk:
            for w in Walk:
                print(w)
        self.__stackReset()
        return self.__isFinalState(currState)
