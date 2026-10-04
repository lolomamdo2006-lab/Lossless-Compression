import math


def compress_to_lz78(data):
    dictionary={}
    tags=[]
    lastindex=0
    i=0
    max_index=0
    while i < len(data):
        longest=""
        current=""
        while i < len(data):
            current+=data[i]
            if current in dictionary:
                longest+=data[i]
                
                if i+1>=len(data):
                    #current symbol is the last
                    tags.append((dictionary.get(longest,0),"Null"))
                    if(dictionary.get(longest,0)==0):
                        lastindex+=1
                        dictionary[longest]=lastindex
                i+=1

            else:
                if (dictionary.get(longest,0)>max_index):
                    max_index=dictionary.get(longest,0)
                next_symbol=data[i]
                tags.append((dictionary.get(longest,0),next_symbol))
                lastindex+=1
                dictionary[longest+data[i]]=lastindex
                i+=1
                break
    print("Tags: ")
    for tag in tags:
        print(tag)
    print("\nDictionary: ")
    for symbol,index in dictionary.items():
        print(index,":",symbol)
    compression_ratio(data,len(tags),max_index)
    decompress_lz78(tags)

#ABAABABAABABBBBBBBBBBA
def compression_ratio(data,tags,max_index):
    print(f"Original Size: {len(data)*8} bits")

    print(f"Compressed Size: {tags*(8+ max_index.bit_length())} bits")

def decompress_lz78(tags):
    dic = [""]
    data = ""
    for tag in tags:
        index, symbol = tag
        if symbol=="Null":
            data += dic[index]
        else:
            data += dic[index] + symbol
            dic.append(dic[index] + symbol)

    print(data)
#ABAABABAABABBBBBBBBBBA