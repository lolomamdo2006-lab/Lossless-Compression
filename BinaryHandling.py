#From Tags To Binary
def from_lz78(tags):
    maxindex=0
    for tag in tags:
      index,symbol=tag
      ind=int(index)
      if ind>maxindex:
         maxindex=ind
    num_bits = maxindex.bit_length()
    bit_string=""
    for tag in tags:
       index,symbol=tag
       ind=int(index)
       index_bits = format(index, f"0{num_bits}b")
       symbol_bits = format(ord(symbol), "08b")
       bit_string+=(index_bits) 
       bit_string+=(symbol_bits)
    return bit_string

def from_lz77(tags):
    maxindex=0
    for tag in tags:
      position,length,symbol=tag
      ind=(max(int(position),int(length)))
      if ind>maxindex:
         maxindex=ind
    num_bits = maxindex.bit_length()
    bit_string=""
    for tag in tags:
       position,length,symbol=tag
       p=int(position)
       l=int(length)
       position_bits = format(p, f"0{num_bits}b")
       length_bits = format(p, f"0{num_bits}b")
       symbol_bits = format(ord(symbol), "08b")
       bit_string+=(position_bits) 
       bit_string+=(length_bits)
       bit_string+=(symbol_bits)
    return bit_string
 
def from_lzw(tags):
    max_code = max(int(tag) for tag in tags)  
    num_bits = max_code.bit_length()
    bit_string=""
    for code in tags:
       c=int(code)
       code_bits = format(c, f"0{num_bits}b")
       bit_string+=(code_bits)
    return bit_string

def from_tag__to_Binary(tags,selected,file_path):
    bit_string=""
    if selected=="Lz78":
        bit_string=from_lz78(tags)
    elif selected=="Lz77":
        bit_string=from_lz77(tags)
    elif selected== "Lzw":
        bit_string=from_lzw(tags)
    byte_data = bytearray()
    for i in range(0, len(bit_string), 8):
        byte_value = int(bit_string[i : i + 8], 2)  
        byte_data.append(byte_value)
    with open(file_path, "wb") as file:
     file.write(byte_data)
    print("done")
#From Binary To Tags