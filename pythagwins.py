import math

runs_scored = input("Insert how many runs scored ")
runs_allowed = input("Insert how many runs were allowed ")
runs_scored_squared = (runs_scored * runs_scored) 
runs_allowed_squared = (runs_allowed * runs_allowed)

print float(runs_scored_squared) / float(runs_scored_squared + runs_allowed_squared)