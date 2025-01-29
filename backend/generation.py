from groq import Groq
import os

groq_key= os.getenv("Groq_API_key") #need up to date api key for groq
assert(groq_key != None, "Groq Key not found")

groq_client= Groq(groq_key)

multiple_choice= (
    'You will create questions in the following format: Multiple Choice'
    'When prompted you will make the question a specific difficulty as requested: (Easy, Medium, Hard).'
    'You will also be given a amount of options that you must make for the problem, do not make more than 6 even if requested'
    'Your response will be formated as: (Question:"The question"\nCorrect:"Correct_Answer"\nIncorrect1:"Incorrect_Answer1"\nIncorrect1:"Incorrect_Answer2"...)'
)
fill_in_the_blank= (
    'You will create questions in the following format: Fill in the Blank'
    'When prompted you will make the question a specific difficulty as requested: (Easy, Medium, Hard).'
    'Your response will be formated as: (Question:"fill in the blank question")'
    #this is for single question generation, if we want a word bank we will generate that first and then have this generate the question
)
free_response= (
    'You will create questions in the following format: Free Response'
    'When prompted you will make the question a specific difficulty as requested: (Easy, Medium, Hard).'
    'Your response will be formated as: (Question:"The question"\nAnswer:"A sample answer for the question.".)'
)
free_response_checker= (
    'You will be given questions in the following format: Free Response'
    'When prompted you will use both the sample answer and the user answer to determine if the user is correct.'
    'Your response will be formated as for a correct verdict: (Correct! "A few sentences of anything that was missed or additional information.")'
    'Your response will be formated as for a incorrect verdict: (Incorrect! "A few sentences regarding the reason for the verdict.")'
)

#TODO: Format input prompt for each question type
def format_prompt(info):
    if info['type'] == 'MultipleChoice':
        pass
    elif info['type'] == 'FillBlank':
        pass
    elif info['type'] == 'FreeResponse':
        pass
    elif info['type'] == 'FreeResponseChecker':
        pass

def generate_content(sys_msg, info): #temp function
    #append info to sys_msg
    
    sys_msg+= f"\n{format_prompt(info)}"
    
    convo= [{'role':'system', 'content': sys_msg}]
    generator= groq_client.chat.completions.create(messages=convo, model='deepseek-r1-distill-llama-70b') # deepseek-r1-distill-llama-70b (DeepSeek): Context Window: 128,000 tokens
    
    response= generator.choices[0].message
    
    return response.content