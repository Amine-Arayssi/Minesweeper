#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:25:26 2020

@author: aminearayssi
"""
import numpy as np
import pandas as pd

def mines_generator():
  level=str(input('Level of Difficulty --> Easy(e), Medium(m), Hard(h): '))
  assert level=='e' or level=='m' or level=='h','ONLY INPUT e,m,or h'
  if level=='e':
    nb_of_mines=np.random.randint(12,18)
  elif level=='m':
    nb_of_mines=np.random.randint(18,24)
  elif level=='h':
    nb_of_mines=np.random.randint(24,36)
  mines_loc=[]
  for i in range(nb_of_mines):
    x=np.random.randint(0,12)
    y=np.random.randint(0,12)
    loc=[x,y]
    if loc not in mines_loc:
      mines_loc.append(loc)
    else:
      nb_of_mines+=1 
  return mines_loc 
    
def map_gen():
  mappa=pd.DataFrame(index=[i for i in range(12)],columns=[i for i in range(12)])
  mines_loc=mines_generator()
  for i in mines_loc:
    mappa[i[0]][i[1]]='*'
  for x in range(0,12):
    for y in range(0,12):
      counter=0
      for w in [-1,0,1]:
        for v in[-1,0,1]:
          if (x+w>=0 and y+v>=0) and (x+w<12 and y+v<12):
            if mappa[x][y]!='*'and mappa[x+w][y+v]=='*':
              counter+=1
      if mappa[x][y]!='*' and counter!=0:
        mappa[x][y]=counter
      elif mappa[x][y]!='*' and counter==0:
        mappa[x][y]='-'
  return mappa

def blank_gen():
  blank=pd.DataFrame(index=[i for i in range(12)],columns=[i for i in range(12)])
  for i in blank.index:
    for j in blank.columns:
      blank[i][j]=' '
  return blank

def assert_true(row,column):
  assert type(row)==int and type(column)==int,'BAD INPUT!'
  if int(row)>=0 and int(row)<12:
    if int(column)>=0 and int(column)<12:
      return True
  else: 
    return False

  
def input_pos():
  inp=str(input('Input column,row position(eg: 1,4):'))
  row=int(inp.split(',')[0])
  column=int(inp.split(',')[1])
  assert assert_true(row,column)==True,'Bad Input!'
  return row,column

def game():
  original=map_gen()
  blank=blank_gen()
  print(blank)
  x,y=input_pos()
  while original[x][y]!='*':
      if blank[x][y]==' ':
          blank[x][y]=original[x][y]
          for v in [-1,0,1]:
              for w in [-1,0,1]:
                  if (x+v>=0 and y+w>=0) and (x+v<12 and y+w<12):
                      if original[x+v][y+w]!='*':
                          if np.random.randint(1,3)==1:
                              blank[x+v][y+w]=original[x+v][y+w]
          print(blank)
          x,y=input_pos()
      elif blank[x][y]!=' ':
          x,y=input_pos()
  if original[x][y]=='*':
    print('\n\nGAME OVER!!','\n\n',original)


game()











    