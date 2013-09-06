
def respond( message, counterWhat, counterHow, sender=""):
    
    if (message[-1]=="?"):
        message = message[0:len(message)-1] #remove the '?', if any
    youtubeMessage = message #make a copy for the youtube query
    message = message.strip()
    print "Got message",message
    words = map(str.lower, message.split()) #put message in a list, all lower case
    wordsIntact = message.split() #list with original case for some commands that need this 
    print words

    try:
        #check if my name is in the message (highest priority from what I understood in the email)
        if (("francois" in words) or ("xavier" in words) or ("lemire" in words) or ("fx" in words) or ("francois-xavier" in words) or ("fxl" in words)):
            response = "http://www.youtube.com/watch?feature=player_detailpage&v=oASZG96v0Rk#t=53s\n<3 <3"
        #what time is it
        elif ((("what" in words) and ("time" in words)) or (("what's" in words) and ("time" in words))):
            import datetime
            now = datetime.datetime.now()
            response = now.strftime("Current time: %Hh%Mm%Ss (%d-%m-%Y)")
        #what is the value of X
        elif ((("what" in words) and ("value" in words)) or (("what\'s" in words) and ("value" in words))):
            response = str(eval(words[-1]))
        #credits
        elif ("credits" in words):
            response = ("\
Francois-Xavier Lemire\n\
Student in Computer Science @ McGill university\n\
francois-xavier.lemire@mail.mcgill.ca")
        #execute ping or ls or uptime
        elif ("execute" in words):
            if ("ping" in words):
                import subprocess
                response = subprocess.Popen(["ping", "-c", "2", words[-1]], stdout=subprocess.PIPE).communicate()[0]
        #    elif ("ls" in words):
        #        import commands
        #        if (words[-1] == "ls"): #no path
        #            response = commands.getoutput("ls")
        #        else: #user gave a path
        #            response = commands.getoutput("ls " + wordsIntact[-1])
            elif ("uptime" in words):
                import commands
                response = commands.getoutput("uptime")
            else:
                response = "wrong use of command 'execute'. Type 'help' to know how to use."
        #open FILE (remove the 4 '#' below to activate command)
        #elif ("open" in words):
        #    file = open(wordsIntact[-1],"r")
        #    response = (file.read())
        #search on youtube
        elif ("youtube" in words):
            if (words[0] == "please"): #if user is polite, remove the please ahead of youtube
                query = youtubeMessage.split(' ',2)[2]
            elif (words[0] == "please,"): #same
                query = youtubeMessage.split(' ',2)[2]
            else:
                query = youtubeMessage.split(' ',1)[1] #remove 'youtube'
            query = query.replace(" ", "+")   #replace all spaces by +
            response = "www.youtube.com/results?search_query="+query+"&page=&utm_source=opensearch"
        #weather of Montreal
        elif ("weather" in words):
            import pywapi
            import string
            yahoo_result = pywapi.get_weather_from_yahoo('CAXX0301')
            response = "Yahoo says it is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in Montreal"
        #4 possible responses on general 'what' question
        elif (("what" in words) or ("what's" in words)):
            if (counterWhat[0]%4==0):
                response = "I'm sorry, my English is very limited :("
            elif (counterWhat[0]%4==1):
                response = "Je ne comprends pas. Parle-moi francais s'il te plait."
            elif (counterWhat[0]%4==2):
                response = "Sumimasenga, wakarimasen deshita. Nihongo de onegaishimasu!"
            else:
                response = "Did you know that it is physically impossible for a pig to look up at the sky?"
            counterWhat[0]+=1
        #4 possible responses on general 'how' question
        elif (("how" in words) or ("how's" in words)):
            if (counterHow[0]%4==0):
                response = "I do not have a single clue!!!!!! :D Don't worry be happy!\n\n\n\n\n(Psst! Type 'help' maybe?!?)"
            elif (counterHow[0]%4==1):
                response = "Tu crois vraiment que les machine ont reponses a tout?"
            elif (counterHow[0]%4==2):
                response = "Ano houhou ha saiaku desu. Are o tameshite mite kudasai!"
            else:
                response = "Did you know that the world's heaviest primates are \"morbidly obese\" humans? Other than that, it would be gorillas, at 485 pounds."
            counterHow[0]+=1
        #help (print all possible commands, open file and execute ls are disabled)
        elif ("help" in words):
            response = ("\n\
Here's a list of useful commands:\n"+\
#open FILE\n\
#   prints content of FILE\n\
"execute uptime\n\
   runs the uptime command and prints back result\n"+\
#execute ls PATH\n\
#   runs ls command with optional PATH and prints back result\n\
"execute ping IP\n\
   runs the ping command with IP address and returns result\n\
-----\n\
what time is it\n\
   states today's current time\n\
what is the value of X\n\
   returns the value of the mathematical expression X\n\
credits\n\
   states the name of the creator of this program\n\
youtube QUERY\n\
   provides a link of the query\n\
weather\n\
   gives the weather of Montreal\n\
what [anything]\n\
   provides a generic reply\n\
how [anything]\n\
   provides a generic reply\n\
[any string that has creator's name]\n\
   soothes you\n\
help\n\
   what you just typed\n\
please + command\n\
   always helps to be polite!\n")
        #if anything else than what is expected is sent to the bot, give general message.
        else:
            response = "Sorry. I am currently away. This is a bot. Type 'help' for more info."

        #if user is polite, reply politely
        if (('please' in words) or ('please,' in words)):
            response = "I will happily assist you! <3\n" + response
            return response
        else:
            return response
    #if anything above caused an error, means format was not respected or operation couldn't be done (like reading a folder) so refer to help.
    except:
        response = "You didn't talk to me correctly. Type 'help' for more info to learn how to talk to a bot and respect the strict format."
        return response

if __name__ == '__main__':
    respond("This is a test")
