import re
from functools import reduce
from collections import defaultdict


with open('./challenges/day_2/input.txt', 'r') as file:
  data = file.readlines()
  games = [re.sub(r'^.*:', '', line) for line in data]
  powers_of_min_colors = []
  legal_game_ids = []
  for idx, game in enumerate(games):
    pulls = game.split(';')
    legal = True
    min_color = defaultdict(int)
    for pull in pulls:
      color_combos = pull.split(',')    
      pull = defaultdict(int)
      for color_combo in color_combos:
        [quantity, color] = color_combo.strip().split(' ')
        pull[color] = int(quantity)
        min_color[color] = max(min_color[color], int(quantity))
      
      if pull['red'] > 12 or pull['green'] > 13 or pull['blue'] > 14:
        legal = False
    if legal:
      legal_game_ids.append(idx+1)
    powers_of_min_colors.append(reduce(lambda x, y: x * y, min_color.values()))
  
print(f'Part 1: {sum(legal_game_ids)}')

print(f'Part 2: {sum(powers_of_min_colors)}')