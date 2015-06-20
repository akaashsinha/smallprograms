# This calculates the game score for a starting pitcher. Originally created by Bill James
# Starting score is always 50
game_score = 50
# Gets the components of the stat
outs = input("How many outs were recorded: ")
strike_outs = input("How many strike outs were recorded: ")
hits = input("How many hits were given up: ")
ER = input("How many earned runs were given up: ")
r = input("How many unearned runs were given up: ")
bb = input("How many walks were given: ")
# For every inning completed after the 4th, 2 points are added
if outs > 12:
	if outs == 15:
		game_score = game_score + 2
	if outs == 18:
		game_score = game_score + 4
	if outs == 21:
		game_score = game_score + 6
	if outs == 24:
		game_score = game_score + 8
	if outs == 27:
		game_score = game_score + 10

game_score = game_score + outs
game_score = game_score + strike_outs
game_score = game_score - (2 * hits)
game_score = game_score - (4 * ER)
game_score = game_score - (2 * r)
game_score = game_score - bb

print "The game score is %i" % game_score