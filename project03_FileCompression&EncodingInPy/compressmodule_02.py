# this file can compress an inputfile in the same folder and generate outputfile
import zlib,base64
def compress(inputfile,outputfile):
    data = open(inputfile, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))  # if not perform any compression use 0,9 is the max amount of compression
    print(compressed_data)
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(outputfile, 'w')
    compressed_file.write(decoded_data)

compress('demo.txt','demo_compressed_02.txt')

def decompress(inputfile,outputfile):
    file_content = open(inputfile,'r').read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decode_data = decompressed_data.decode('utf-8')
    file = open(outputfile,'w')
    file.write(decode_data)
    file.close()

decompress('demo_compressed_02.txt','demo_decompressed_02.txt')
