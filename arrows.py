
def left(chain, position):
    print(position)
    for index, n in enumerate(chain[:position]):
        if "<" not in chain[:position]:
            break
        if chain[position-index] == "<" and index!=0:
            chain[position-index] = ">"
            return position-index
        elif position+index == len(chain)-1:
            chain[position-index] = ">"
            return position-index

def right(chain, position):
    for index, n in enumerate(chain[position:]):
        if ">" not in chain[position:]:
            break
        if chain[position+index] == ">" and index!=0:
            chain[position+index] = "<"
            return position+index
        elif position+index == len(chain)-1:
            chain[position+index] = "<"
            return position+index 
        
def define_way(chain, position):
    for n in range(len(chain)):
        if chain[position] == "<":
            position = left(chain, position)
        elif chain[position] == ">":
            position = right(chain, position)
        if type(position) == list:
            return chain
    return position
    
position = int(input())
position-=1
chain = list(input())
if position < 10**5:
    define_way(chain, position)
