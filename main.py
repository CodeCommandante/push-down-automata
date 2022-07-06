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

import machine
import argparse
import ui

def main():
    parser = argparse.ArgumentParser(description='Program that checks user input strings against a defined machine and indicates whether the string is in the Language, L(M).')
    parser.add_argument('-F','--FA',action='store_true',help='the machine description file is a Finite Acceptor')
    parser.add_argument('-P','--PDA',action='store_true',help='the machine description file is a PushDown Automata')
    parser.add_argument('Machine',action='store',type=str,help='the file describing the machine (FA or PDA)')
    args = parser.parse_args()

    if not args.FA and not args.PDA:
        print('Program requires three arguments to run')
        print('         ./main.py [-F,-P] [file]')
    elif args.FA:
        params = ui.fileParse(str(args.Machine),'f')
        ui.runNAProgram(params)
        print('Goodbye!')
    elif args.PDA:
        params = ui.fileParse(str(args.Machine),'p')
        ui.runPDAProgram(params)
        print('Goodbye!')
    return 0

main()