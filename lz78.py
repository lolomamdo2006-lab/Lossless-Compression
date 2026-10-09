#For Testing
#xyxyxyxyxyxyzzzzzzzz data
#ABAABABAABABBBBBBBBBBA data
#0A0B1A2A4A4B2B7B8B0A  compressed data
#=====================================
#string to list
def parse_tags(tags_string):
    tags = []
    for item in tags_string.split(","):
        ind, next_sombol = item.split()
        tags.append((int(ind), next_sombol))
    return tags
#=========================================list to string
def parse_string(tags):
    tags_as_string=""
    for tag in tags:
        index,symbol=tag
        ind=str(index)
        tags_as_string+=ind
        tags_as_string+=" "
        tags_as_string+=symbol
        tags_as_string+=","
    tags_as_string = tags_as_string[:-1]

    return tags_as_string
#==============================
def compression_ratio(data,tags):
    max_index=0
    for tag in tags:
      index,symbol=tag
      ind=int(index)
      if ind>max_index:
         max_index=ind
    print(f"Original Size: {len(data)*8} bits, {len(data)} bytes")
    inbits=len(tags)*(8+ max_index.bit_length())
    print(f"Compressed Size: {inbits} bits, {inbits/8} bytes")
#==========================================================
def decompress_lz78(str_tags):
    tags=parse_tags(str_tags)
    dic = [""]
    data = ""
    for tag in tags:
        index, symbol = tag
        data += dic[index] + symbol
        dic.append(dic[index] + symbol)
    
    print(data)
    return data
#======================================
def compress_to_lz78(data):
    dictionary={}
    tags=[]
    lastindex=0
    i=0
    max_index=0


    while i<len(data):
        longest=""
        current=""
        while i<len(data) and current+data[i] in dictionary :
            current+=data[i]
            i+=1
        longest=current
        
        if (dictionary.get(longest,0)>max_index):
                max_index=dictionary.get(longest,0)
        if (i<len(data)):
            next_symbol=data[i]
            tags.append((dictionary.get(longest,0),next_symbol))
            lastindex+=1
            dictionary[longest+data[i]]=lastindex
            i+=1
        else:
            if longest:
                prefix = longest[:-1]
                last_char = longest[-1]
                tags.append((dictionary.get(prefix, 0), last_char))
    tags_as_string=""
    for tag in tags:
        index,symbol=tag
        ind=str(index)
        tags_as_string+=ind
        tags_as_string+=symbol
    print("Tags: ")
    for tag in tags:
        print(tag)
    print("\nDictionary: ")
    for symbol,index in dictionary.items():
        print(index,":",symbol)
    compression_ratio(data,tags)
    print(tags_as_string)
    return tags



