CHATBOT
=======
Here's a list of required packages with their versions.
You can find each of those on Google

(Talkbot2013)➜  Talkbot2013  yolk -l
Python          - 2.7.3        - active development (/usr/lib64/python2.7/lib-dynload)
dnspython       - 1.10.0       - active 
pip             - 1.1          - active 
pyasn1-modules  - 0.0.4        - active 
pyasn1          - 0.1.6        - active 
pywapi          - 0.3          - active 
setuptools      - 0.6c11       - active 
sleekxmpp       - 1.1.11       - active 
wsgiref         - 0.1.2        - active development (/usr/lib64/python2.7)

********************************************

- HOW TO INSTALL SLEEKMPP


Install method 2 (if you have hg installed):
hg clone git://github.com/fritzy/SleekXMPP.git

Install method 1 (if you have unzip installed):
wget https://github.com/fritzy/SleekXMPP/archive/develop.zip
   Saving to: develop.zip
unzip develop.zip (or whatever the expanded file is, maybe just "develop")


cd SleekXMPP-develop
python setup.py build
cd ..

ln -s SleekXMPP-develop/sleekxmpp sleekxmpp
python -c "import sleekxmpp;print 'ok'"
    YOU SHOULD NOT SEE ANY ERROR MESSAGE OR ANYTHING BUT ok

python talk206.py -j YOURLOGIN@gmail.com -p YOURPASSWORD

*********************************************

- DESCRIPTION

This chatbot will reply to a bunch of different pre-defined questions, which can be seen by typing help when talking to him. If the bot does not recognize a question, he will give some general replies (3 variations before repeating himself).
He can also be polite if he wishes!
His talking capability can be found in chatter.py.
