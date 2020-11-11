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

print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Here is some spaces 12/32/4"))
print(parse_line(" Again some spaces\n/12/12/12"))
