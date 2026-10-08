
def lzw_compress_fuc(text):
   
    dictionary = {}
     
    mylist = []
  
    current = ""
    code = 65
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
         dictionary[char] = code
         code += 1
    code =128
    
    for x in text:
         new = current + x
         if new in dictionary:
               current = new
         else:
              
              mylist.append(dictionary[current])
              dictionary[new] = code
              code += 1
              current = x

    
    mylist.append(dictionary[current])
    print("Compressed List:", mylist)

    def lzw_compression_ratio(text):
     original_size = len(text) * 8
     max_code = max(int(code) for code in mylist)
     compressed_size = len(mylist) * (max_code.bit_length())
     ratio = original_size / compressed_size
     print("Original Size:", original_size, "bits")
     print("Compressed Size:", compressed_size, "bits")
     print("Compression Ratio:", ratio)
     return ratio
    lzw_compression_ratio(text)
   
    return mylist

    
 #lzw_compress_fuc()




def lzw_decompress_fuc(compressed_data):
  
     decomdictionary = {}
     afterdecompress = ""
    
     code = 65
     for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
         decomdictionary[code] = char
         code += 1
     code =128
     
     current_code= int(compressed_data.split()[0])
     current_char = decomdictionary[current_code]
     afterdecompress=current_char

        

     for x in compressed_data.split()[1:]:
         x= int(x)
         if x in decomdictionary:
              new = decomdictionary[x]
         else:
             new = current_char + current_char[0]
         afterdecompress+=new
             
         decomdictionary[code] = current_char + new[0]
         code += 1
         current_char = new
     print("Decompressed Text:", afterdecompress)
     return afterdecompress 

def lzw_decompress_fuc(data):
   clean_data = data.replace("[", "").replace("]", "").replace(",", "")
     
#lzw_decompress_fuc()

   


