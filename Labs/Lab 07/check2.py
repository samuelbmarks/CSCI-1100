def parse_line(line):
    if line.count("/") < 3:
        return None
    
    split_list = line.rsplit("/",3)
    
    if not split_list[1].isdigit():
        return None
    
    if not split_list[2].isdigit():
        return None    
    
    if not split_list[3].isdigit():
        return None
    
    return int(split_list[1]), int(split_list[2]), int(split_list[3]), split_list[0]

def get_line(fname,parno,lineno):
    file_name = open(str(fname) + ".txt")
    pcount = 0
    lcount = 0
    
    inline = True
    for line in file_name:
        
        if pcount == parno and lcount == lineno and line != '\n':
            return line
        
        if len(line) > 1:
            lcount += 1
            inline = True
            
        if len(line) == 1:
            if inline == True:
                inline = False    
                pcount += 1
            lcount = 0 

    return "not found"   
 
fn = int(input("Please enter the file number ==> "))
pn = int(input("Please enter the paragraph number ==> "))
ln = int(input("Please enter the line number ==> "))

pn = pn-1
ln = ln-1

print(get_line(fn,pn,ln))