#aoc_0301.py
#wip not done yet

def pathing(movement_list):
        coord = [0,0]
        
        for item in movement_list:
                
                direction = item[0]
                print(direction)
                distance = int(item[1:])
                dimX = coord[0]
                dimY = coord[1]
                
                if direction == 'R':
                    print('dir = R')
                    coord[0] += distance
                elif direction == 'L':
                    coord[0] -= distance
                elif direction == 'U':
                    coord[1] += distance
                elif direction == 'D':
                    coord[1] -= distance
                else:
                    pass
            
        print(coord)
        return coord

print(pathing(['R24', 'R14', 'R00001', 'L2']))
