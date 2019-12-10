def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

def get_values_not_in_set(the_set):
        #the list is like "C1","I4",etc
        #the set is like 6789
        missing_ones = []
        for xxx in range(1,10):
                if str(xxx) in the_set:
                        a = 5
                else:
                        missing_ones.append(str(xxx))
        return missing_ones
def apply_F8(values):
#F8 + C1 + F6 + D3 + B6 = 25
        rule = "F8 + C1 + F6 + D3 + B6"
        total = 25
        value_list = []        
        set_map = {}
        string_list = rule.split(" + ")
#        print(string_list)
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
#        print(value_list)
        result = [
                a + b + c + d + e
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3] 
                for e in value_list[4]
                if int(a) + int(b) + int(c) + int(d) + int(e)  == total and a != c and c != e 
        ]        
        for candidate in result:
                set_map["F8"].add(candidate[0])
                set_map["C1"].add(candidate[1])
                set_map["F6"].add(candidate[2])
                set_map["D3"].add(candidate[3])
                set_map["B6"].add(candidate[4])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                
                for xy in get_values_not_in_set(set_map[grid_string]):
#                        print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values
def apply_A2(values):
#A2 + A8 + D7 + E4 = 21
        rule = "A2 + A8 + D7 + E4"
        total = 21
        value_list = []        
        set_map = {}
        string_list = rule.split(" + ")
#        print(string_list)
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
#        print(value_list)
        result = [
                a + b + c + d 
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3] 
                if int(a) + int(b) + int(c) + int(d)  == total and a!= b 
        ]        
        for candidate in result:
                set_map["A2"].add(candidate[0])
                set_map["A8"].add(candidate[1])
                set_map["D7"].add(candidate[2])
                set_map["E4"].add(candidate[3])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                
                for xy in get_values_not_in_set(set_map[grid_string]):
#                        print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values
def apply_D3(values):
#D3 + I8 + A4 + I6 = 27
        rule = "D3 + I8 + A4 + I6"
        total = 27
        value_list = []        
        set_map = {}
        string_list = rule.split(" + ")
#        print(string_list)
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
#        print(value_list)
        result = [
                a + b + c + d 
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3] 
                if int(a) + int(b) + int(c) + int(d)  == total and b!= d 
        ]        
        for candidate in result:
                set_map["D3"].add(candidate[0])
                set_map["I8"].add(candidate[1])
                set_map["A4"].add(candidate[2])
                set_map["I6"].add(candidate[3])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                
                for xy in get_values_not_in_set(set_map[grid_string]):
#                        print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values

def apply_I6(values):
#I6 + A5 + I3 + B8 + C3 = 20
        rule = "I6 + A5 + I3 + B8 + C3"
        total = 20
        value_list = []        
        set_map = {}
        string_list = rule.split(" + ")
        #print(string_list)
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
        #print(value_list)
        result = [
                a + b + c + d + e
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3]
                for e in value_list[4]
                if int(a) + int(b) + int(c) + int(d) + int(e)  == total and a != c and c != e 
        ]        
        #print(result)
        for candidate in result:
                set_map["I6"].add(candidate[0])
                set_map["A5"].add(candidate[1])
                set_map["I3"].add(candidate[2])
                set_map["B8"].add(candidate[3])
                set_map["C3"].add(candidate[4])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                
                for xy in get_values_not_in_set(set_map[grid_string]):
#                        print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values



def apply_I2(values):
#I2 + I3 + F2 + E9 = 15
        rule = "I2 + I3 + F2 + E9"
        total = 15
        value_list = []        
        set_map = {}
        string_list = rule.split(" + ")
#        print(string_list)
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
#        print(value_list)
        result = [
                a + b + c + d 
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3] 
                if int(a) + int(b) + int(c) + int(d)  == total and a!= b and a != c 
        ]        
        for candidate in result:
                set_map["I2"].add(candidate[0])
                set_map["I3"].add(candidate[1])
                set_map["F2"].add(candidate[2])
                set_map["E9"].add(candidate[3])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                
                for xy in get_values_not_in_set(set_map[grid_string]):
#                        print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values


def apply_A5(values):
        #A5 + D7 + I5 + G8 + B3 + A5 = 19
        rule = "D7 + I5 + B3 + A5 + A5"
        # G8 = 2        
        total = 17
        value_list = []        
        set_map = {}
        string_list = rule.split(" + ")
#        print(string_list)
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
#        print(value_list)
        result = [
                a + b + c + d 
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3] 
                if int(a) + int(b) + int(c) + int(d) + int(d) == total and b!= d 
        ]        
        for candidate in result:
                set_map["D7"].add(candidate[0])
                set_map["I5"].add(candidate[1])
                set_map["B3"].add(candidate[2])
                set_map["A5"].add(candidate[3])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                
                for xy in get_values_not_in_set(set_map[grid_string]):
 #                       print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values


def apply_B9(values):
        #B9 + B8 + C1 + H4 + H4 = 23
        rule = "B9 + B8 + C1 + H4 + H4"
        total = 23
        value_list = []        
        set_map = {}
        string_list = rule.split(" + ")
 #       print(string_list)
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
 #       print(value_list)
        result = [
                a + b + c + d 
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3] 
                if int(a) + int(b) + int(c) + int(d) + int(d) == total and a!=b 
        ]        
        for candidate in result:
                set_map["B9"].add(candidate[0])
                set_map["B8"].add(candidate[1])
                set_map["C1"].add(candidate[2])
                set_map["H4"].add(candidate[3])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                
                for xy in get_values_not_in_set(set_map[grid_string]):
 #                       print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values

def apply_F5(values):
        # F5 + B8 + F8 + I7 + F1 = 33
        rule = "F5 + B8 + F8 + I7 + F1"
        total = 33
        value_list = []        
        set_map = {}
        string_list = rule.split(" + ")
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
        result = [
                a + b + c + d + e
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3]
                for e in value_list[4]
                if int(a) + int(b) + int(c) + int(d) + int(e) == total and a!=d and a!=c and c !=d and b != c
        ]        
        for candidate in result:
                set_map["F5"].add(candidate[0])
                set_map["B8"].add(candidate[1])
                set_map["F8"].add(candidate[2])
                set_map["I7"].add(candidate[3])
                set_map["F1"].add(candidate[4])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                
                for xy in get_values_not_in_set(set_map[grid_string]):
        #                print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values
        
def apply_B6(values):
        rule = "B6 + A8 + A3 + C4"
        total = 18
        value_list = []
        
        set_map = {}
        string_list = rule.split(" + ")
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
        result = [
                a + b + c + d 
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3] 
                if int(a) + int(b) + int(c) + int(d) == total and a!=d and b!=c
        ]        
        for candidate in result:
                set_map["B6"].add(candidate[0])
                set_map["A8"].add(candidate[1])
                set_map["A3"].add(candidate[2])
                set_map["C4"].add(candidate[3])
        #        result_count = result_count+ 1
        for grid_string in string_list:
                for xy in get_values_not_in_set(set_map[grid_string]):
#                        print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        return values
        
def apply_C7(values):
        rule = "H9 + I7 + H8 + G3"
        total = 28
        value_list = []
        set_map = {}
        string_list = rule.split(" + ")
        for x in string_list:
                value_list.append(values[x])
                set_map[x] = set()
        # value list = ["5678","6789","23456789",etc...]        
        
        #H9 + I7 + H8
        result = [
                a + b + c + d 
                for a in value_list[0] 
                for b in value_list[1] 
                for c in value_list[2] 
                for d in value_list[3] 
                if int(a) + int(b) + int(c) + int(d) == total and a!=b and b!=c and a!=c
        ]
        result_count = 0
        for candidate in result:
                set_map["H9"].add(candidate[0])
                set_map["I7"].add(candidate[1])
                set_map["H8"].add(candidate[2])
                set_map["G3"].add(candidate[3])
                result_count = result_count+ 1

        
        for grid_string in string_list:
                for xy in get_values_not_in_set(set_map[grid_string]):
#                        print("eliminate {} from {}".format(xy,grid_string))
                        eliminate(values,grid_string,str(xy))
        
        return values
    
#def general_rule(values, v_list, total):
        
def apply_C1(values):
    # C1 + I4 + C2 + I1 + A4 = 20
    # C1 + C2 + A4 = 17
    
    C1 = values["C1"]
    C2 = values["C2"]
    A4 = values["A4"]
    c1_set = set()
    c2_set = set()
    a4_set = set()
    #[int(x) + int(p) + int(z) for x in v for p in k for z in b]
    
    for a in C1:
        for b in C2:
                for c in A4:
                        if int(a) + int(b) + int(c) == 17:
                               # print("{} : {} : {}".format(a,b,c))
                                c1_set.add(a)
                                c2_set.add(b)
                                a4_set.add(c)
    for d in get_values_not_in_set(c1_set):
#        print("eliminating {} from C1".format(d))
        eliminate(values,"C1",str(d))
    for e in get_values_not_in_set(c2_set):
#        print("eliminating {} from C2".format(e))
        eliminate(values,"C2",str(e))
    
    for f in get_values_not_in_set(a4_set):
#        print("eliminating {} from A4".format(f))
        eliminate(values,"A4",str(f))
    return values
    
def apply_I7(values):
    # I7 + H8 + C2 + D9 = 26   (8 possible solutions!)
    # I7 + H8 + C2 = 24
    I7 = values["I7"]
    H8 = values["H8"]
    C2 = values["C2"]  #6 or 8
    #print("here is I7: {}".format(I7))
    #print("here is H8: {}".format(H8))    
    the_set = set()
    for d in I7:
        for e in H8:
                for f in C2:
                        #print("Check: {}:{}:{}".format(d,e,f))
                         
                        if int(d) + int(e) + int(f) == 24:
                                #print("Poss: {}:{}:{}".format(d,e,f))
                                the_set.add(d)
                                the_set.add(e)
                                the_set.add(f)
     

    # get values not in set:
    for xxx in range(1,10):
        if str(xxx) in the_set:
                #print(xxx)
                a=3
        else:
                eliminate(values,"I7",str(xxx))
                eliminate(values,"H8",str(xxx))
                eliminate(values,"C2",str(xxx))
    return values    

def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    
    values = apply_B6(values)
    values = apply_I7(values)
    values = apply_C1(values)
    values = apply_C7(values)
    values = apply_F5(values)
    values = apply_B9(values)
    values = apply_A5(values)
    values = apply_I2(values)
    values = apply_I6(values)
    values = apply_D3(values)
    values = apply_A2(values)
    values = apply_F8(values)

    return values

def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))
    


def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values
    


def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print (''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print
    
def solve(grid): return search(parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares): 
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    print("n: {}".format(n))
    print("s: {}".format(s))
    return some(search(assign(values.copy(), s, d)) 
                for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False
    
def check_rules(values):
    rule_b9 = values["B9"] + values["B8"] + values["C1"] + values["H4"] + values["H4"] == 23
    rule_a5 = values["A5"] + values["A5"] + values["D7"] + values["I5"] + values["G8"] + values["B3"] == 19
    rule_i2 = values["I2"] + values["I3"] + values["F2"] + values["E9"] == 15
    rule_i7 = values["I7"] + values["H8"] + values["C2"] + values["D9"] == 26
    rule_i6 = values["I6"] + values["A5"] + values["I3"] + values["B8"] + values["C3"] == 20
    rule_i7d9 = values["I7"] + ["D9"] + values["B6"] + values["A8"] +  values["A3"] + values["C4"] == 27
    rule_c7 = values["C7"] + ["H9"] + values["I7"] + values["B2"] + values["H8"] + values["G3"] == 31
    rule_d3 = values["D3"] + values["I8"] + values["A4"] + values["I6"] == 27
    rule_f5 = values["F5"] + ["B8"] + values["F8"] + values["I7"] + values["F1"]  == 33
    rule_a2 = values["A2"] + ["A8"] + values["D7"] + values["E4"] == 21
    rule_c1 = values["C1"] + values["I4"] + ["C2"] + values["I1"] + values["A4"] == 20
    rule_f8 = values["F8"] + values["C1"] + values["F6"] + values["D3"] + values["B6"] == 25
    if rule_b9 and rule_a5 and rule_i2 and rule_a7 and rule_i6 and rule_i7d9 and rule_c7 and rule_d3 and rule_f5 and rule_a2 and rule_c1 and rule_f8:
        return True
    else: 
        return False
    

    #    A        B        C        D        E        F        G        H        I                '
grid88= '000020001012000000000000200000000002020000005000000000000000120100002000200170000'
grid3 = '00000001012000000060000200000000002020000000000000000000000120100002060200100900'
grid19= '000000001012000000000000200000000002020000000000000000000000120100002000200100000'
grid18= '000000001012000000000000200000000002020000000000000000000000120100002000000100000'
grid18m1 = '00000001012000000000000200000000002020000000000000000000000120100002000000100000'
grid_special = ""
for x in range(1,10):
    xchar = str(x)
    grid_special = xchar + grid18m1
    solved = solve(grid_special)
    if check_rules(solved):
        print("FALSE")
    else:
        print("TRUE")
        display(solved)

#display(solve(grid18))

