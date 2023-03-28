# deploy-chatbot
This repository contains a simple chatbot to show its basic concepts. It uses Chatterbot library, which contains pre-trained Machine Learning algorithms. 
It uses the process of Natural Language for interaction with a user. It is based on doing the analysis of the question of the user and then returning the response of the user. 

##ChatterBot Corpu Trainer
The Chaterbot uses a corpus trainer. It is a collection of authentic text or audio organized into datasets. Authentic means that text written or audio spoken by a native of the language or dialect. A corpus can be made up of everything from newspapers, novels, recipes, radio broadcasts to television shows, movies, and tweets. 

To explore what languages and collections of corpora are available, check out the chatterbot_corpus/data directory in the separate chatterbot-corpus repository https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data. 

 ChatterBot’s training module provides methods that allow you to export the content of your chat bot’s database as a training corpus that can be used to train other chat bots. 

chatbot = ChatBot('Export Example Bot')
chatbot.trainer.export_for_training('./export.yml')

## Flask
Is useful in the tasks of web development of any program. For this project, we use it to deploy the chatbot. 

## HTML and CSS 
To deploy the chatbot as a web application, it is not possible to deploy it without the use of HTML and CSS. These two are the primary packages when it comes to the tasks of web development. So, it is recommended to learn HTML and CSS in order to work as a developer. 

##Dependencies
Flask: 
$ pip install flask
$ pip install ChatterBot 
For Mac users: 
$ pip install chatterbot==1.0.4 #This avoids issues with your compiler. 

Check chatterbot version: 
$ python3 -m chatterbot --version