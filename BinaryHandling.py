#From Tags To Binary
def from_tag__to_Binary(tags):
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
    byte_data = bytearray()
    for i in range(0, len(bit_string), 8):
        byte_chunk = bit_string[i : i + 8]  
        byte_value = int(byte_chunk, 2)  
        byte_data.append(byte_value)
    with open("tests/compressed.bin", "wb") as file:
     file.write(byte_data)
    print("done")
#From Binary To Tags