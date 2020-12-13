
# import the chatterbox package
# this chat engine we wil use
from chatterbot import ChatBot

# give you chatbot a name
chatbot = ChatBot ("COVID Helper 9000")

# Packagers used to train your chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# add new trainer and personalize the chatbot
# This will be done using a python list
# format should be a question from user and response from chatbot
personality_AI= [

    "hello",
    "Hello Human.",
    "how are you?",
    "Im good, just chilling in the internet.",
    "who are you?",
    "I am an AI design by a Student from UAT.",
    "Are you an AI?",
    "Yes, Im a sofisticaded AI created by Daniel Diaz with Tony Hilton's Help",

]
personality_soccer_knowledge = [
    "How many minutes are in a soccer game?",
    "There are 90 minutes. 2 halfs of 45 minutes.",
    "How many player are in a soccer game?",
    "There are 22 players. 11 player for each team",
    "what is your favorite sport?",
    "My favorite sport is soccer.",
    "How many teams play the world cup?",
    "There are 32 teams, and the world cup is played every 4 years.",
]
personality_soccer_World_cup = [
    "Which country has won the most world cups?",
    "Brasil has won the mot world cups, with five victories.",
    "Who won the last world cup?",
    "Last world cup was in 2018 which France was the winner",
    "Where is the next world cup?",
    "The next world cup is in QATAR in 2022.",
    "How many soccer fans are there worldwide?",
    "Estimates place the number of global soccer fans at approximately 3 billion!",
    "Which cuntry is going to win the next world cup?",
    "Your guess is as good as ours, but currently Spain is the odds-on favorite to win.",
]
personality_soccer_favorites = [
    "what is your favorite soccer team?",
    "Atletico Nacional, and Colombia from a national team.",
    "Who is your favorite soccer player",
    "My favorite soccer player is Cristiano Ronaldo.",
    "Who is the best player in the world?",
    "Last player to win the ballon D'or was Lionel Messi who currently has 6",
    "Do you hate Messi?",
    "I do not hate messi, but he sucks.",
]
personality_COVID = [
    "What medications should I avoid if I have COVID-19??",
    "Currently, there is no evidence to suggest that taking any specific medications, like blood pressure medication or ibuprofen, leads to more severe illness from COVID-19.",
    "Can people recover from COVID-19?",
    "Most people who get COVID-19 recover from it. Most people who get COVID-19 have mild or moderate symptoms and can recover thanks to supportive care. If you have a cough, fever and difficulty breathing seek medical care early - call your health facility by telephone first..",
    "Is there a coronavirus data tracker??",
    "CDC COVID Data Tracker is a website that allows users to interact with a variety of data on COVID-19 that is updated daily.",
    "Are masks effective in preventing COVID-19??",
    "Wearing cloth masks can help prevent people infected with the virus that causes COVID-19 from spreading the virus. Make sure your cloth mask: fits snugly but comfortably against the side of the face, completely covers the nose and mouth, is secured with ties or ear loops, includes multiple layers of fabric, allows for breathing without restriction, and can be laundered and machine dried without damage or change to shape. Cloth masks should NOT be worn by children less than 2 years old or anyone who has trouble breathing or is unconscious, incapacitated, or otherwise unable to remove the mask without assistance.",
    "how can i prevent from Covid-19??",
    "The best way to prevent illness is to avoid being exposed to the virus. The CDC recommends everyday preventive actions to help prevent the spread of respiratory diseases. They include: Wash your hands, cover your mouth and nose wear a face mask, Social distance.",
    "is there a vaccine available already??",
    "There are currently no vaccines available for the prevention of COVID-19.",
    "What are the symptoms that COVID-19 can cause??",
    "least two of these symptoms: Fever, Chills, Repeated shaking with chills, Muscle or body aches, Headache, Sore throat, new loss of taste or smell, Congestion or runny nose, Nausea or vomiting, Diarrhea.",
    "Can I get COVID-19 from a food worker handling my food??",
    "Currently, there is no evidence of food or food packaging being associated with transmission of COVID-19.",
]


# set the trainer we want to train
trainer_personality_AI = ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer_personality_soccer_knowledge = ListTrainer(chatbot)
trainer_personality_soccer_World_cup = ListTrainer(chatbot)
trainer_personality_soccer_favorites = ListTrainer(chatbot)
trainer_personality_COVID = ListTrainer(chatbot)

# Now her are actually train our chatbot on the corpus
# this is what gives ou'chatbot its persnality
# override the personality
trainer_personality_AI.train(personality_AI)
trainer_personality_soccer_World_cup.train(personality_soccer_World_cup)
trainer_personality_soccer_favorites.train(personality_soccer_favorites)
trainer_personality_soccer_knowledge.train(personality_soccer_knowledge)
trainer_personality_COVID.train(personality_COVID)
# this is the standard personality training
trainer.train('chatterbot.corpus.english')

# type something better
# print("welcome to talk with hall-9000 type something to begin....")

# main loop for our chatbot to keep talking
# where the chatbot interact with the user
# flip this flag if user wants to leave chat
# otherwise keep looping

''' ******************* GUI Below Engine Above **************** '''
# Import for the GUI 
from chatbot_gui import ChatbotGUI

# create the chatbot app
"""
    Options
    - title: App window title.
    - gif_path: File Path to the ChatBot gif.
    - show_timestamps: If the chat has time-stamps.
    - default_voice_options: The voice options provided to the text-to-speech engine by default if not specified
                             when calling the send_ai_message() function.
"""
app = ChatbotGUI(
    title="COVID-19 HELPER",
    gif_path="123.gif",
    show_timestamps=True,
    default_voice_options={
        "rate": 100,
        "volume": 0.8,
        "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    }
)


# define the function that handles incoming user messages
@app.event
def on_message(chat: ChatbotGUI, text: str):
    """
    This is where you can add chat bot functionality!

    You can use chat.send_ai_message(text, callback, voice_options) to send a message as the AI.
        params:
            - text: the text you want the bot to say
            - callback: a function which will be executed when the AI is done talking
            - voice_options: a dictionary where you can provide options for the AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }

    You can use chat.start_gif() and chat.stop_gif() to start and stop the gif.
    You can use chat.clear() to clear the user and AI chat boxes.

    You can use chat.process_and_send_ai_message to offload chatbot processing to a thread to prevent the GUI from
    freezing up.
        params:
            - ai_response_generator: A function which takes a string as it's input (user message) and responds with
                                     a string (AI's response).
            - text: The text that the ai is responding to.
            - callback: a function which will be executed when the AI is done talking
            - voice_options: a dictionary where you can provide options for the AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }

    :param chat: The chat box object.
    :param text: Text the user has entered.
    :return:
    """
    # this is where you can add chat bot functionality!
    # text is the text the user has entered into the chat
    # you can use chat.send_ai_message("some text") to send a message as the AI, this will do background
    # you can use chat.start_gif() and chat.stop_gif() to start and stop the gif
    # you can use chat.clear() to clear the user and AI chat boxes

    # print the text the user entered to console
    print("User Entered Message: " + text)             
    
    ''' Here you can intercept the user input and override the bot
    output with your own responses and commands.'''
    # if the user send the "clear" message clear the chats
    if text.lower().find("erase chat") != -1:
        chat.clear()
    # user can say any form of bye to close the chat.
    elif text.lower().find("bye") != -1:
        # define a callback which will close the application
        def close():
            chat.exit()

        # send the goodbye message and provide the close function as a callback
        chat.send_ai_message("It has been good talking with you. Have a great day! Later!", callback=close)
    else:
        # offload chat bot processing to a worker thread and also send the result as an ai message
        chat.process_and_send_ai_message(chatbot.get_response, text)


# run the chat bot application
app.run()
