import math

def compress_lz77(text,search_window=12,lookahead=11):
    i=0
    tags=[]
    while i<len(text):
        length=0
        position=0
        start=max(0,i-search_window)
        for x in range(start,i):
            last=0
            while((last<lookahead-1)and(i+last<len(text))and(text[i+last]==text[x+last])):
                last+=1
            if((last>0)and(last>=length)):
                length=last
                position=i-x
        if i+length<len(text):
            next_sombol=text[i+length]
        else:
            next_sombol=""
        tags.append((position,length,next_sombol))

        i+=length+1
    return tags


                
def read_tags(data):
     tags = []
     for item in data.split(","):
        position, length, next_sombol = item.split()
        if next_sombol == "NULL":
            next_sombol = ""
        tags.append((int(position), int(length), next_sombol))
     return tags

def lz77_to_text(tags):
        return ", ".join(f"{p} {l} {s if s != '' else 'NULL'}" for p, l, s in tags)


def decompress_lz77(tags):
    text=""
    for position,length,next_sombol in tags:
        start_index=len(text)-position
        for x in range(length):
            text+=text[start_index+x]
        text+=next_sombol
    
    return text

def compression_ratio_lz77(text, tags):
    original_size = len(text) * 8

    position_bits = max(t[0] for t in tags).bit_length()
    length_bits = max(t[1] for t in tags).bit_length()
    tag_size = position_bits + length_bits + 8
    compressed_size = len(tags) * tag_size

    print("Original Size =", original_size, "bits")
    print("Compressed Size =", compressed_size, "bits")




#_____________________________________________________________________#
#inputs:0
#[(0,0,"A"),(0,0,"B"),(2,1,"A"),(3,2,"B"),(5,3,"B"),(1,10,"A")]
#CABRACADABRARRARRAD
#ABAABABABABABABABABABA
#0 0 C , 0 0 A , 0 0 B ,0 0 R , 3 1 C , 2 1 D , 7 4 R , 3 5 D
#_____________________________________________________________________#
