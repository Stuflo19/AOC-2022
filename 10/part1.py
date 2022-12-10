with open("10/input.txt", "r") as f:
    lines = f.readlines()
    cycles = 0
    total = 0
    x_reg = 1
    desired_cycles = 20
    adding = False
    
    for line in lines:
        line = line.strip().split(' ')
        if(line[0] == 'addx'):
            cycles += 2
            if cycles >= desired_cycles: adding = True
            else: x_reg += int(line[1])
            # if desired_cycles == 60: print('adding: ', int(line[1]),' new: ', x_reg)
        elif(line[0] == 'noop'):
            cycles += 1
        
        # print('cycles: ', cycles)
        # if cycles == 21: print(x_reg)
        if(cycles >= desired_cycles):
            print('x_reg: ', x_reg)
            total += x_reg * desired_cycles
            print(line)
            print('cycles ', cycles, ': ' , total)
            desired_cycles += 40
            if adding: x_reg += int(line[1])
            adding = False
    print(total)