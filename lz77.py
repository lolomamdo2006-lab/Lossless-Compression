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
    print(tags)
                

def decompress(data):
    # LZ77 decompression
    pass
#CABRACADABRARRARRAD
#ABAABABABABABABABABABA