def compress(text):
    i=0
    window=""
    tags=[]
    while i<len(text):
        length=0
        position=0
        for x in range(len(window)):
            last=0
            while((i+last<len(text)-1)and(x+last<len(window))and(text[i+last]==window[x+last])):
                last+=1
            if((last>0)and(last>=length)):
                length=last
                position=len(window)-x
        next_sombol=text[i+length]
        tags.append((position,length,next_sombol))
        window+=text[i:i+length+1]
        i+=length+1
    print(tags)
                

def decompress(data):
    # LZ77 decompression
    pass
#ABAABABAABBBBBBBBBBBBA
