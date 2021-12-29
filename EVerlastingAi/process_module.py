from output_module import output
from time_module import get_time , get_date
from module_database import get_answer_from_memory, insert_question_and_answer,get_question_and_answer
from input_module import take_input
from internet_checker import check_internet_connection

def process(query):
    answer = get_answer_from_memory(query)
    
    if answer == "got time details":

        return "Time is " + get_time()

    elif answer == "Check internet connection":
        if check_internet_connection:
            return "Internet is Connected"
        else:
            return "Internet is not Connected"

    else:
        output("I dont know this one, can you please tell me what it means?")
        ans = take_input()
        if "it means" in ans:
            ans = ans.replace("it means", "")
            ans = ans.strip()   

            value = get_answer_from_memory(ans)
            if value == "":
                return "Can't help with this one"
            else:
                insert_question_and_answer(query, value)
                return "Thanks i will remember it for the next time"

        return "nothing to return"