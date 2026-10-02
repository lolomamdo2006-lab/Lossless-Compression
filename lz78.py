def compress_to_lz78(data):
    dictionary={}
    tags=[]
    lastindex=0
    i=0
    while i < len(data):
        longest=""
        current=""
        while i < len(data):
            current+=data[i]
            if current in dictionary:
                longest+=data[i]
                i+=1
            else:
                next_symbol=data[i]
                if longest in dictionary:
                    tags.append((dictionary[longest],next_symbol))
                    #print(f"({dictionary[longest]}, {next_symbol})")
                else:
                    tags.append((lastindex,next_symbol))
                    #print(f"({lastindex}, {next_symbol})")

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

#ABAABABAABABBBBBBBBBBA