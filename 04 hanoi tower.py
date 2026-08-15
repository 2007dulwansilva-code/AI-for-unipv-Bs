def move_tower(n,start, end, aux):
    # n is the tower size
    # start is rod where the tower is located
    # end is rod where the tower needs to be moved to
    # aux is the rod that can be use to park unused disks
    if n == 1 : 
        print("move the disk", n , "from", start , "to", end)
    else : 
        move_tower(n-1, start, aux, end)
        print("move the disk", n, "from", start, "to", end)
        move_tower(n-1, aux, end, start)
