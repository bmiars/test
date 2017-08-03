def move(player, direction):
    x, y, hp = player
    dir_horizontal, dir_vertical = direction
    if dir_horizontal < 0:
        if x == 0:
            hp-=5
        else:
            x -= 1
    if dir_horizontal > 0:
        if x == 9:
            hp-=5
        else:
            x += 1
        
    if dir_vertical < 0:
        if y == 0:
            hp-=5
        else:
            y += 1
    if dir_vertical > 0:
        if y == 9:
            hp -= 5
        else:
            y -= 1
   
    return x, y, hp

print(move((1, 1, 10), (-1, 0)))
print(move((0, 1, 10), (-1, 0)))
print(move((0, 9, 5), (0, 1)))