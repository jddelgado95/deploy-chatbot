#import the Flask class
#request: handles different HTTP methods
#render_template: Templates can be used to generate any type of text file. 
#For web applications, you’ll primarily be generating HTML pages, but you can also generate markdown, plain text for emails...
#To render a template you can use the render_template() method. 
#All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.
from flask import Flask, render_template, request
from chatterbot import ChatBot #import ChatterBot 
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


#Create an instance of this class. 
#argument "name" of the application’s module or package. 
# __name__ is a convenient shortcut for this that is appropriate for most cases. 
# This is needed so that Flask knows where to look for resources such as templates and static files
app = Flask(__name__)
#create chatbot
#This line of code has created a new chat bot named Chatterbot
#storage_adapter: allows to connect to different types of databases. 
#Using the SQLStorageAdapter allows the chat bot to connect to SQL databases.
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter") #instance of the ChatBot class
trainer = ListTrainer(englishBot)
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english

#define app routes
#route() decorator to bind a function to a URL
@app.route("/")
def index():
    return render_template("index.html")

#a route only answers to GET requests
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))
    print("HEY")

#Allows to execute code when the file runs as a script, but not when it’s imported as a module
if __name__ == "__main__":
    app.run()