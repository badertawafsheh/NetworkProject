import socket
import null as null

HOST, PORT = '0.0.0.0', 7000

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((HOST, PORT))
my_socket.listen(1)
print(f"\033[91m--------------------------------------------------------------------\033[0m")
print('                    Serving on port ', PORT)
print(f"\033[91m--------------------------------------------------------------------\033[0m")

i=0
while 1:
    connection, address = my_socket.accept()
    request = connection.recv(1024).decode('utf-8')
    string_list = request.split(' ')  # Split request from spaces #['GET', '/', 'HTTP/1.1\r\nHost:', '127.0.0.1:7001\r\nConnection:', 'keep-alive\r\nUpgrade-Insecure-Requests:', '1\r\nUser-Agent:', 'Mozilla/5.0', '(Windows', 'NT', '10.0;', 'Win64;', 'x64)', 'AppleWebKit/537.36', '(KHTML,', 'like', 'Gecko)', 'Chrome/80.0.3987.149', 'Safari/537.36\r\nSec-Fetch-Dest:', 'document\r\nAccept:', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nPurpose:', 'prefetch\r\nSec-Fetch-Site:', 'none\r\nSec-Fetch-Mode:', 'navigate\r\nSec-Fetch-User:', '?1\r\nAccept-Encoding:', 'gzip,', 'deflate,', 'br\r\nAccept-Language:', 'ar,en-US;q=0.9,en;q=0.8\r\n\r\n']
    if(len(string_list)<=1):
        continue
    method = string_list[0]
    requesting_file = string_list[1]
    (ip,port)=str(address).split(',')
    ip=str(ip).replace("(","")
    ip = str(ip).replace("'", "")
    port = str(port).replace(")", "")



    if (string_list[len(string_list)-1]!=null):
        for i in range(0,(len(string_list)-1)):
            string_list[i]=null

    print('Client request ', requesting_file)

    myfile = requesting_file.split('?')[0]  # After the "?" symbol not relevent here


    if (myfile =='/1'):
        response = f"<html lang='en'><head> <meta charset='UTF-8'> <title>ENCS436 Webserver</title></head><body style='border: green solid 2px ;margin: 120px;background-color: #fff4f4' > <p style='text-align: center;font-size: 30px;margin-top: 90px'> Welcome to our course <strong style='color: green'> Computer Networks</strong></p> <p style='text-align: center'><b>Bader Tawafsheh 1171214</b></p> <p style='text-align: center'><b>Amro Rommaneh 1170129</b>  <p style='text-align: center'><b>IP = {ip}</b></p> <p style='text-align: center'><b>PORT = {port}</b></p> <p style='text-align: center; color: #bda5a5'>Instructor : Dr.Abdalkarim Awad</p></body></html>".encode(
            'utf-8')
    elif (myfile == '/2'):
         myfile = 'templates/text.html'
         mimetype = 'text/html'
    elif (myfile == '/3'):
        myfile = 'templates/bader1.jpg'
        mimetype = 'image/jpg'

    try:
        if (myfile != '/1'):

            file = open(myfile, 'rb')  # open file , r => read , b => byte format
            response = file.read()
            file.close()

        header = 'HTTP/1.1 200 OK\n'
        header += 'Content-Type: ' + str(mimetype) + '\n\n'
        print(header)
        print(f"\033[91m--------------------------------------------------------------------\033[0m")


    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode(
            'utf-8')
        print(header)
        i+=1

    final_response = header.encode('utf-8')
    final_response += response
    connection.send(final_response)
    connection.close()