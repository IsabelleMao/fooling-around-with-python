import random
tries = 10000 #more = more accurate = slower

wins_when_switched = 0
wins_when_kept = 0

for x in range(tries):
  #Assignments
  picked_door = random.randint(1, 3)
  good_door = random.randint(1, 3) #could be picked door
  a_bad_door = random.randint(1, 3)
  while a_bad_door == good_door or a_bad_door == picked_door:
    a_bad_door = random.randint(1, 3) #until different
  switch_to_door = random.randint(1, 3)
  while switch_to_door == a_bad_door or switch_to_door == picked_door:
    switch_to_door = random.randint(1, 3)
    
  if switch_to_door == good_door:
    wins_when_switched += 1
  
print("{} wins, or {:.2f} percent chance of winning when switched.".format(wins_when_switched, wins_when_switched/tries * 100))

for x in range(tries):
  #Assignments
  picked_door = random.randint(1, 3)
  good_door = random.randint(1, 3) #could be picked door
  a_bad_door = random.randint(1, 3)
  while a_bad_door == good_door or a_bad_door == picked_door:
    a_bad_door = random.randint(1, 3) #until different
  switch_to_door = random.randint(1, 3)
  if picked_door == good_door:
    wins_when_kept += 1
    
print("{} wins, or {:.2f} percent chance of winning when kept.".format(wins_when_kept, wins_when_kept/tries * 100))
