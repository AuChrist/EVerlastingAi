import assistant_details
from speak_module import speak
from module_database import speak_is_on
#command input line
def output(o):
    
    if speak_is_on():
        speak(o)

    print(assistant_details.name+": " + str(o))
    print(" ")
