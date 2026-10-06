import math

def compress(text):
    i=0
    window=0
    tags=[]
    while i<len(text):
        length=0
        position=0
        for x in range(window):
            last=0
            while((i+last<len(text)-1)and(text[i+last]==text[x+last])):
                last+=1
            if((last>0)and(last>=length)):
                length=last
                position=window-x
        next_sombol=text[i+length]
        tags.append((position,length,next_sombol))
        window+=length+1
        i+=length+1
    return tags
                
def read_tags(data):

    tags = []
    for item in data.split():
        position, length, next_sombol = item.split(",")
        tags.append((int(position), int(length), next_sombol))
    return tags

def decompress(tags):
    text=""
    for position,length,next_sombol in tags:
        start_index=len(text)-position
        for x in range(length):
            text+=text[start_index+x]
        text+=next_sombol
    
    return text

def compression_ratio(text, tags):
    original_size = len(text) * 8

    position_bits = max(t[0] for t in tags).bit_length()
    length_bits = max(t[1] for t in tags).bit_length()
    tag_size = position_bits + length_bits + 8
    compressed_size = len(tags) * tag_size

    print("Original Size =", original_size, "bits")
    print("Compressed Size =", compressed_size, "bits")




#_____________________________________________________________________#
#inputs:
#[(0,0,"A"),(0,0,"B"),(2,1,"A"),(3,2,"B"),(5,3,"B"),(1,10,"A")]
#CABRACADABRARRARRAD
#ABAABABABABABABABABABA
#_____________________________________________________________________#
