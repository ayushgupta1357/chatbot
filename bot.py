import pyautogui
import time
import pyperclip
from openai import OpenAI

#This function is used to check whether the given username has texted last or not
#Note this format is used as we have logged in using chrome and based on that we have used the split function
def is_last_message_from_sender(chat_log, sender_name='userBased'):
    
    messages = chat_log.strip().split("/2026] ")[-1]
    if sender_name in messages:
        return True 
    return False

#Generating client 
client = OpenAI(
  api_key="<Your Key Here>",
)
# Step 1: Move to (1429, 1057) and click

pyautogui.moveTo(1429, 1057, duration=0.5)
pyautogui.click()
time.sleep(1)


#we will be continously check if and copy the text from the chat to reply at all the levels
while True:

    #Drag from (668, 186) to (1866, 930)
    pyautogui.moveTo(671, 190, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(1320, 930, duration=1)
    pyautogui.mouseUp()

    time.sleep(0.5)

    #Copy selected text (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')

    time.sleep(0.5)

    #Get copied text to chathistory
    chatHistory = pyperclip.paste()

    
    #now after fetching the messages we will check if the messages has been send by the sender or not
    if is_last_message_from_sender(chatHistory):
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a person named Ayush who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Ayush"},
            {"role": "user", "content": chatHistory}
        ]
        )

        reply=completion.choices[0].message.content 

        #copy the reply
        pyperclip.copy(reply)
        time.sleep(0.5)
        
        #click on the chatbox
        pyautogui.click(801,976)  # chat input box
        time.sleep(0.5)
        
        #paste the reply 
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.3)
        
        #Send using enter
        pyautogui.press('enter')

        time.sleep(5)  # wait after sending

    else:
        time.sleep(2)    