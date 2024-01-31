# this file can compress a 'demo.txt' file in the same folder and form 'compressed.txt'
import zlib,base64

data = open('demo.txt','r').read()
data_bytes = bytes(data,'utf-8')
compressed_data = base64.b64encode(zlib.compress(data_bytes,9))#if not perform any compression use 0,9 is the max amount of compression
print(compressed_data)
decoded_data = compressed_data.decode('utf-8')
compressed_file = open('compressed_01.txt','w')
compressed_file.write(decoded_data)

decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data)
