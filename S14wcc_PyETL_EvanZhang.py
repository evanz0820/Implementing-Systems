### S14_PyMT_StarterFile.py  v3c
#  K.Schmitz (c) 2022, 2023
#  Starter File for CIS2010 Session 14, Structured Query Language
##################Initialization information, do not modify ################
from cis2010utils4 import StartHere, EndHere, runsql 
#from colorama import Fore
import pandas as pd
import sqlite3
############################################################################
# Open up the database  ########## Do not modify these instructions#########
db_name =  "irs18.db"
db_conn = sqlite3.connect(db_name)
sqltxt = "SELECT COUNT(zipcode) FROM irsz" ; zz = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of zipcodes\n", zz)
sqltxt = "pragma table_info('irsz')" ; t1 = pd.read_sql(sqltxt, db_conn) ; print("irsz table\n", t1)
sqltxt = "pragma table_info('zco')" ; t2 = pd.read_sql(sqltxt, db_conn) ; print("zco table\n", t2)
############################################################################
#
# Task 2a
StartHere( "Evan Zhang", "S14", "Fall 2023")
#
# Task w2b
sqlw2b = """
SELECT state, zipcode, n1 FROM irsz
"""
w2b = runsql( sqlw2b, db_conn)

# Task w2c
sqlw2c = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000,
schf FROM irsz
"""
w2c = runsql( sqlw2c, db_conn)

# Task w2d
sqlw2d = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000,
schf, a06500*1000, a19700*1000 FROM irsz
"""
w2d = runsql( sqlw2d, db_conn)


# Task w3a
w2d.to_csv( 'x2d.csv', sep=',')
# Workshop END
#
###########################################################
# Collaboration Challenge
#
# S14ccq Q4
#StartHere( "", "S14", "CC")

# S14ccq Q5
sqlcc5 = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000,
schf, a06500*1000, a19700*1000 FROM irsz
WHERE zipcode > 1000 and zipcode < 99999
"""
cc5 = runsql( sqlcc5, db_conn)


# S14ccq Q6
sqlcc6 = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000,
schf, a06500*1000, a19700*1000 FROM irsz
WHERE zipcode > 1000 and zipcode < 99999 and state = "GA"
"""
cc6 = runsql( sqlcc6, db_conn)

# S14ccq Q7
sqlcc7 = """
SELECT state, zipcode, n1, n2, numdep, a00100*1000,
schf, a06500*1000, a19700*1000, elderly FROM irsz
WHERE zipcode > 1000 and zipcode < 99999 and state = "GA"
"""
cc7 = runsql( sqlcc7, db_conn)

cc7.to_csv("cc7.csv", sep=',')
#Collaboration Challenge: Cleanup, Save and End
db_conn.close()
EndHere( globals())
#db_conn.close(); exit()
###########################################################
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$)'YJ[FS%_MFSLM}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
