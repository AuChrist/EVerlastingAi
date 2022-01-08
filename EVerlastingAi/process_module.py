from output_module import output
from time_module import get_time , get_date
from module_database import *
from input_module import take_input
from internet_checker import check_internet_connection, check_on_wikipedia
import assistant_details

def process(query):

    answer = get_answer_from_memory(query)

    if answer == "Search on wiki":
        output("Don't know this one should i search on internet?")
        answer = take_input()
        if "yes" in answer:
            answer = answer.replace("yes", "")
            return check_on_wikipedia(query)
            if answer == "no":
                return take_input()
    
        
    if answer == "got time details":
        return "Time is " + get_time()

    if answer == "got date details":
        return "Date is " + get_date()

    if answer == "on speak":
        return turn_on_speech()
    elif answer == "off speak":
        return turn_off_speech()


    if answer == "Check internet connection":
        if check_internet_connection:
            return "Internet is Connected"
        else:
            return "Internet is not Connected"

    elif answer == 'change name':
        output("Okay! what name that suit me?")
        temp = take_input()
        if temp == assistant_details.name:
            return "Can't change. Its just my old name dear"
        else: 
            update_name(temp)
            assistant_details.name = temp
            return "Now you can call me " + temp + " dear"


    if answer == "":
        output("I dont know this one, can you please tell me what it means?")
        ans = take_input()
        if "it means" in ans:
            ans = ans.replace("it means", "")
            ans = ans.strip()   

            value = get_answer_from_memory(ans)
            if value == " ":
                return "Can't help with this one"
            else:
                insert_question_and_answer(query, ans)
                return "Thanks i will remember it for the next time"