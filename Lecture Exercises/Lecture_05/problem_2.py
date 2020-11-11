def frame_string(string):
    '''
    Return the given string, string with a frame around it.
    '''
    frame_string = print("*"*(len(string)+6)+"\n"+"**",string,"**"+"\n"+"*"*(len(string)+6))
    return frame_string
frame_string("Spanish Inquisition")
print()
frame_string("Ni")