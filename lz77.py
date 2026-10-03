#ABAABABAABBBBBBBBBBBBA
def compress(text):
    Position=0
    Length=0
    i=0
    window=""
    next_symbol=text[0]
    tag=(Position, Length ,next_symbol)
    Tags=[]
    while i< len(text):
        if i==0:
            Tags.append(tag)
            window=text[i]
            i+=1    
        else:
            x=0
            max_length=0
            while x<len(window):
                curent_length=0
                last=0
                while(text[i:i+last]==window[x:x+last]):
                    curent_length=last
                    last+=1
                if(curent_length>=max_length):
                    max_length=curent_length
                    next_symbol=text[i+max_length+1]
                    Length=max_length
                    Position=x
                x+=1
        if(Length>0):
            tag=(Position, Length ,next_symbol)
            Tags.append(tag)

            window=window+text[i:i+Length+1] 
            i=i+Length+1
            Length=0
            Position=0 
            
        else:
            window=window+text[i]
        
            next_symbol=text[i]

            tag=(Position, Length ,next_symbol)
            Tags.append(tag)  

            Length=0
            Position=0                                  
            i+=1         
            
    print(Tags)
                

def decompress(data):
    # LZ77 decompression
    pass