import urllib2  
import urllib  
import time

class Loginer():  
    def __init__(self, username, password):  
        self.loginUrl = 'http://202.118.1.87/srun_portal_pc.php?ac_id=1&'  
        self.username = username  
        self.password = password  
        self.openner = urllib2.build_opener()  

    def login(self):  
        postdata = {  
            'username': self.username,  
            'password': self.password,  
            'action': 'login',  
            'ac_id': '1',
            'user_ip':'',
            'nas_ip':'',
            'user_mac':'',
            'url':''  
        }  
        postdata = urllib.urlencode(postdata)  
        myRequest = urllib2.Request(url=self.loginUrl, data=postdata)  
        logw = open("/home/user/login_logfile.txt", "w")
        result = self.openner.open(myRequest).read()
        resStr=str(result)
        ind=resStr.find('font-weight:bold;color:orange') 
        if(ind!=-1):
            print 'connected successfully'
	    logw.write("connected successfully\n")
	    logw.write(time.ctime())
	    logw.write("\n") 
        else:
            print 'connected faild!! Maybe your username or password is wrong!'
            logw.write("connected faild!\n")
def check():
	print "test"

def main():  
   # username=raw_input('Enter your username:')
   # password=raw_input('Enter your password:')
    while True:
        username=''
        password=''
	print time.ctime()
	print username,password
	check()
	#time.sleep(60*60)
        file=open('temp_username.dat','w')
        file.write(username)
        file.close()
        l = Loginer(username,password)
        l.login() 
	time.sleep(10) 

if __name__ == '__main__':  
    main()  
    print 'done'
