Last login: Fri Feb 20 19:11:40 on ttys000
Kevins-MacBook-Pro:REST kevin_murphy4$ ssh -i kmurphy-key-pair-NVirginia.pem ubuntu@54.172.230.50
Warning: Identity file kmurphy-key-pair-NVirginia.pem not accessible: No such file or directory.
Permission denied (publickey).
Kevins-MacBook-Pro:REST kevin_murphy4$ cd 
Kevins-MacBook-Pro:~ kevin_murphy4$ ls
Applications	Downloads	Justinmind	Music		VirtualBox VMs
Desktop		Dropbox		Library		Pictures	results.js
Documents	Google Drive	Movies		Public
Kevins-MacBook-Pro:~ kevin_murphy4$ cd Documents/
Kevins-MacBook-Pro:Documents kevin_murphy4$ ls
Age of Empires III		Networks HW1.docx
Astronomy			OCI Form 382.docm
BUAD				Random
CPSC				Soccer
Caci Letter.pdf			Spanish
ComputerNetworks.pdf		Tutorial
GitHub.app			Vuze Downloads
Job Application Stuff		Wireshark HTTP Lab.docx
Lab2 Wireshark Lab.docx		caci work forms
Microsoft User Data		cs350VM
Murphy_Lab1.doc			dashboard_project
Murphy_Lab2.docx		kmurphy-key-pair-NVirginia.pem
Murphy_Lab3.docx		ruby-getting-started
Kevins-MacBook-Pro:Documents kevin_murphy4$ clear

Kevins-MacBook-Pro:Documents kevin_murphy4$ ssh -i kmurphy-key-pair-NVirginia.pem ubuntu@54.172.230.50
Welcome to Ubuntu 14.04.1 LTS (GNU/Linux 3.13.0-36-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Sat Feb 21 00:13:19 UTC 2015

  System load:  0.0               Processes:           75
  Usage of /:   19.0% of 7.75GB   Users logged in:     0
  Memory usage: 28%               IP address for eth0: 172.31.61.15
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

121 packages can be updated.
74 updates are security updates.


*** System restart required ***
Last login: Sat Feb 21 00:13:21 2015 from ip72-209-205-174.dc.dc.cox.net
ubuntu@ip-172-31-61-15:~$ clear

ubuntu@ip-172-31-61-15:~$ ls
hello-world  patchwork  redditBot  restLab  tmp  venv
ubuntu@ip-172-31-61-15:~$ cd restLab/
ubuntu@ip-172-31-61-15:~/restLab$ ls
restAPI.php  rest.py
ubuntu@ip-172-31-61-15:~/restLab$ vim rest.py




from flask import Flask, url_for,json
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid



@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
"rest.py" 71L, 1499C                                          1,1           Top
