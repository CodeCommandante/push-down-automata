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

#! /usr/bin/python3

import unittest
import machine 
import ui
import os

class Test_Finite_Automata(unittest.TestCase):

    def test_Finite_Automata_BadConstruction_1(self):
        try:
            M1 = machine.FiniteAutomata([],'',['q_0'])
            self.assertTrue(False)
            del M1
        except:
            self.assertTrue(True)
    
    def test_Finite_Automata_BadConstruction_2(self):
        try:
            M1 = machine.FiniteAutomata([],'q_0',[])
            self.assertTrue(False)
            del M1
        except:
            self.assertTrue(True)

    def test_Finite_Automata_BadConstruction_3(self):
        try:
            M1 = machine.FiniteAutomata([['q_0','1']],'q_0',['q_0'])
            self.assertTrue(False)
            del M1
        except:
            self.assertTrue(True)

    def test_Finite_Automata_BadConstruction_4(self):
        try:
            M1 = machine.FiniteAutomata([['q_0','1','q_1']],'q_0',['q_0',''])
            self.assertTrue(False)
            del M1
        except:
            self.assertTrue(True)
    
    def test_Finite_Automata_BadConstruction_5(self):
        try:
            M1 = machine.FiniteAutomata([['q_0','101','q_1']],'q_0',['q_1'])
            self.assertTrue(False)
            del M1
        except:
            self.assertTrue(True)
    
    def test_Finite_Automata_BadConstruction_6(self):
        try:
            M1 = machine.FiniteAutomata([['q_0','1','']],'q_0',['q_0'])
            self.assertTrue(False)
            del M1
        except:
            self.assertTrue(True)

    def test_Finite_Automata_run_1(self):
        M = machine.FiniteAutomata([['q_0','a','q_1']], 'q_0', ['q_0'])
        self.assertTrue(M.run(''))
        self.assertFalse(M.run('a'))
        self.assertFalse(M.run('aa'))
        del M

    def test_Finite_Automata_run_2(self):
        M = machine.FiniteAutomata([['q_0','b','q_1']], 'q_0', ['q_1'])
        self.assertFalse(M.run(''))
        self.assertTrue(M.run('b'))
        self.assertFalse(M.run('bb'))
        self.assertFalse(M.run('a'))
        del M

    def test_Finite_Automata_run_3(self):
        M = machine.FiniteAutomata([['q_0','0','q_0'],
                                    ['q_0','1','q_1'],
                                    ['q_1','0','q_0'],
                                    ['q_1','1','q_2'],
                                    ['q_2','0','q_2'],
                                    ['q_2','1','q_1']],
                                     'q_0', ['q_1'])
        self.assertFalse(M.run(''))
        self.assertTrue(M.run('01'))
        self.assertFalse(M.run('00'))
        self.assertTrue(M.run('101'))
        self.assertTrue(M.run('0111'))
        self.assertTrue(M.run('11001'))
        self.assertFalse(M.run('100'))
        self.assertFalse(M.run('1100'))
        del M
    
    def test_Finite_Automata_run_4(self):
        M = machine.FiniteAutomata([['q_0','a','q_0'],
                                    ['q_0','b','q_1'],
                                    ['q_1','a','q_2'],
                                    ['q_1','b','q_2'],
                                    ['q_2','a','q_2'],
                                    ['q_2','b','q_2']],
                                     'q_0', ['q_1'])
        self.assertFalse(M.run(''))
        self.assertTrue(M.run('b'))
        self.assertFalse(M.run('a'))
        self.assertTrue(M.run('ab'))
        self.assertTrue(M.run('aab'))
        self.assertFalse(M.run('bbb'))
        self.assertFalse(M.run('ba'))
        self.assertFalse(M.run('bb'))
        del M

    def test_Finite_Automata_run_5(self):
        M = machine.FiniteAutomata([['q_0','a','q_1'],
                                    ['q_0','b','q_3'],
                                    ['q_1','a','q_3'],
                                    ['q_1','b','q_2'],
                                    ['q_2','a','q_2'],
                                    ['q_2','b','q_2'],
                                    ['q_3','a','q_3'],
                                    ['q_3','b','q_3']],
                                     'q_0', ['q_2'])
        self.assertFalse(M.run(''))
        self.assertTrue(M.run('ab'))
        self.assertFalse(M.run('a'))
        self.assertTrue(M.run('abb'))
        self.assertTrue(M.run('aba'))
        self.assertFalse(M.run('aab'))
        self.assertFalse(M.run('ba'))
        self.assertFalse(M.run('bb'))
        del M
    
    def test_Finite_Automata_run_6(self):
        M = machine.FiniteAutomata([['L','1','L'],
                                    ['L','0','0'],
                                    ['0','1','L'],
                                    ['0','0','00'],
                                    ['00','0','00'],
                                    ['00','1','001'],
                                    ['001','0','001'],
                                    ['001','1','001']],
                                     'L', ['L','0','00'])
        self.assertTrue(M.run(''))
        self.assertTrue(M.run('1'))
        self.assertFalse(M.run('001'))
        self.assertTrue(M.run('101'))
        self.assertTrue(M.run('000'))
        self.assertFalse(M.run('0011'))
        self.assertFalse(M.run('0010'))
        self.assertFalse(M.run('1001'))

    def test_Finite_Automata_run_7(self):
        M = machine.FiniteAutomata([['q0','a','q2'],
                                    ['q0','b','q1'],
                                    ['q1','a','q1'],
                                    ['q1','b','q1'],
                                    ['q2','b','q2'],
                                    ['q2','a','q3'],
                                    ['q3','b','q2'],
                                    ['q3','a','q3']],
                                     'q0', ['q3'])
        self.assertFalse(M.run(''))
        self.assertTrue(M.run('abbbba'))
        self.assertFalse(M.run('bba'))
        self.assertTrue(M.run('aaaaa'))
        self.assertTrue(M.run('aaba'))
        self.assertFalse(M.run('babab'))
        self.assertFalse(M.run('abab'))
        self.assertFalse(M.run('abbbaab'))

    def test_Finite_Automata_run_8(self):
        M = machine.FiniteAutomata([['q0','a','q2'],
                                    ['q0','b','q1'],
                                    ['q1','a','q1'],
                                    ['q1','b','q1'],
                                    ['q2','b','q2'],
                                    ['q2','a','q3'],
                                    ['q3','b','q2'],
                                    ['q3','a','q4'],
                                    ['q4','b','q4'],
                                    ['q4','a','q5'],
                                    ['q5','b','q4'],
                                    ['q5','a','q5']],
                                     'q0', ['q5'])
        self.assertFalse(M.run(''))
        self.assertTrue(M.run('abbbaaba'))
        self.assertFalse(M.run('bba'))
        self.assertTrue(M.run('aaaaa'))
        self.assertTrue(M.run('aaabbba'))
        self.assertFalse(M.run('aabbab'))
        self.assertFalse(M.run('aaabbbab'))
        self.assertFalse(M.run('aabaababbb'))

class Test_Pushdown_Automata(unittest.TestCase):
    
    def test_Pushdown_Automata_BadConstruction_1(self):
        try:
            M = machine.PushdownAutomata([],'','0',['q_0'])
            self.assertTrue(False)
            del M
        except:
            self.assertTrue(True)

    def test_Pushdown_Automata_BadConstruction_2(self):
        try:
            M = machine.PushdownAutomata([],'q_0','0',[])
            self.assertTrue(False)
            del M
        except:
            self.assertTrue(True)

    def test_Pushdown_Automata_BadConstruction_3(self):
        try:
            M = machine.PushdownAutomata([['q_0','1']],'q_0','0',['q_0'])
            self.assertTrue(False)
            del M
        except:
            self.assertTrue(True)

    def test_Pushdown_Automata_BadConstruction_4(self):
        try:
            M = machine.PushdownAutomata([['q_0','1','0','q_2','']],'q_0','0',['q_0',''])
            self.assertTrue(False)
            del M
        except:
            self.assertTrue(True)
    
    def test_Pushdown_Automata_BadConstruction_5(self):
        try:
            M = machine.PushdownAutomata([['q_0','101','100','q_3','1']],'q_0','0',['q_1'])
            self.assertTrue(False)
            del M
        except:
            self.assertTrue(True)
    
    def test_Pushdown_Automata_BadConstruction_6(self):
        try:
            M = machine.PushdownAutomata([['q_0','1','4','','']],'q_0','0',['q_0'])
            self.assertTrue(False)
            del M
        except:
            self.assertTrue(True)

    def test_Pushdown_Automata_BadConstruction_7(self):
        try:
            M = machine.PushdownAutomata([['q_0','1','','q_1','']],'q_0','0',['q_0'])
            self.assertTrue(False)
            del M
        except:
            self.assertTrue(True)
    
    def test_Pushdown_Automata_BadConstruction_8(self):
        try:
            M = machine.PushdownAutomata([['q_0','1','0','q_1','']],'q_0','',['q_0'])
            self.assertTrue(False)
            del M
        except:
            self.assertTrue(True)

    def test_Pushdown_Automata_run_1(self):
        M = machine.PushdownAutomata([['q0','a','0','q1','10'],
                                      ['q1','a','1','q1','11'],
                                      ['q1','b','1','q2',''],
                                      ['q2','b','1','q2',''],
                                      ['q2','','0','q0','']],
                                       'q0','0',['q0'])
        self.assertTrue(M.run(''))
        self.assertTrue(M.run('ab'))
        self.assertTrue(M.run('aabb'))
        self.assertTrue(M.run('aaabbb'))
        self.assertTrue(M.run('aaaaabbbbb'))
        self.assertFalse(M.run('aabbab'))
        self.assertFalse(M.run('aaabbbab'))
        del M

class Test_UI(unittest.TestCase):

    def test_buildTransFA_1(self):
        T = 'q0,a -> q1'
        Trans = ui.buildTransFA(T)
        self.assertEqual(['q0','a','q1'],Trans)

    def test_buildTransFA_2(self):
        T = '(q0,a) -> q1'
        Trans = ui.buildTransFA(T)
        self.assertNotEqual(['q0','a','q1'],Trans)
        self.assertEqual(['(q0','a)','q1'],Trans)

    def test_buildTransFA_3(self):
        T = 'q_0, a  ->q1'
        Trans = ui.buildTransFA(T)
        self.assertEqual(['q_0','a','q1'],Trans)

    def test_buildTransFA_Except1(self):
        T = 'ere, hj = 567'
        try:
            Trans = ui.buildTransFA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildTransFA_Except2(self):
        T = 'q2 b - q1'
        try:
            Trans = ui.buildTransFA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildTransFA_Except3(self):
        T = 'q2 b 56 -> j'
        try:
            Trans = ui.buildTransFA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildTransFA_Except4(self):
        T = ''
        try:
            Trans = ui.buildTransFA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildTransFA_Except5(self):
        T = '->'
        try:
            Trans = ui.buildTransFA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildTransPDA_1(self):
        T = 'q__0, a, q_1 -> qq, 0'
        Trans = ui.buildTransPDA(T)
        self.assertEqual(['q__0','a','q_1','qq','0'],Trans)

    def test_buildTransPDA_2(self):
        T = '((q0, bg, q9) -> yip, 2'
        Trans = ui.buildTransPDA(T)
        self.assertEqual(['((q0','bg','q9)','yip','2'],Trans)

    def test_buildTransPDA_3(self):
        T = 'q1, ba, 09 -> q2, 09'
        Trans = ui.buildTransPDA(T)
        self.assertEqual(['q1','ba','09','q2','09'],Trans)

    def test_buildTransPDA_Except1(self):
        T = 'the, jkl 89 -> 890, i'
        try:
            Trans = ui.buildTransPDA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildTransPDA_Except2(self):
        T = 'q, w, e, = 45, 6'
        try:
            Trans = ui.buildTransPDA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildTransPDA_Except3(self):
        T = 'q__0, q, qwerty -> jk'
        try:
            Trans = ui.buildTransPDA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildTransPDA_Except4(self):
        T = ''
        try:
            Trans = ui.buildTransPDA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)
    
    def test_buildTransPDA_Except5(self):
        T = '->'
        try:
            Trans = ui.buildTransPDA(T)
            self.assertFalse(True)
        except:
            self.assertTrue(True)

    def test_buildFinals_1(self):
        F = 'q0,q1,q2'
        self.assertEqual(ui.buildFinals(F),['q0','q1','q2'])

    def test_buildFinals_2(self):
        F = ''
        self.assertEqual(ui.buildFinals(F),[''])

    def test_buildFinals_3(self):
        F = '  q0'
        self.assertEqual(ui.buildFinals(F),['q0'])

    def test_fileParse_FA_1(self):
        FILE_NAME = os.getcwd() + '/TestFiles/TestFA1.txt'
        transitions = ui.fileParse(FILE_NAME,'f')
        self.assertEqual(transitions,[[['q0','0','q0'],
                                        ['q1','0','q0'],
                                        ['q2','0','q2'],
                                        ['q0','1','q1'],
                                        ['q1','1','q2'],
                                        ['q2','1','q1']],'q0',['q1']])

    def test_fileParse_FA_2(self):
        FILE_NAME = os.getcwd() + '/TestFiles/TestFA2.txt'
        transitions = ui.fileParse(FILE_NAME,'f')
        self.assertEqual(transitions,[[['q0','a','q1'],
                                      ['q0','b','q3'],
                                      ['q3','b','q3'],
                                      ['q3','a','q3'],
                                      ['q3','b','q3'],
                                      ['q1','a','q3'],
                                      ['q1','b','q2'],
                                      ['q2','a','q2'],
                                      ['q2','b','q2']],'q0',['q2']])                             
    
    def test_fileParse_FA_3(self):
        FILE_NAME = os.getcwd() + '/TestFiles/TestFA3.txt'
        transitions = ui.fileParse(FILE_NAME,'f')
        self.assertEqual(transitions,[[['L','1','L'],
                                     ['L','0','0'],
                                     ['0','1','L'],
                                     ['0','0','00'],
                                     ['00','0','00'],
                                     ['00','1','001'],
                                     ['001','0','001'],
                                     ['001','1','001']],'L',['L','0','00']])        

    def test_fileParse_PDA_1(self):
        FILE_NAME = os.getcwd() + '/TestFiles/TestPDA1.txt'
        transitions = ui.fileParse(FILE_NAME,'p')
        self.assertEqual(transitions,[[['q0','a','0','q1','10'],
                                        ['q1','a','1','q1','11'],
                                        ['q1','b','1','q2',''],
                                        ['q2','b','1','q2',''],
                                        ['q2','','0','q0','']],'q0','0',['q0']])

if __name__ == '__main__':
    unittest.main()