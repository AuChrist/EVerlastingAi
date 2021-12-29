import mysql.connector 
from mysql.connector import Error

def create_connection():
    connection = mysql.connector.connect(host ='localhost',
                                         database ='everlastingai',
                                         user='root',
                                         password='')
    
    return connection 

def get_question_and_answer():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM questionsandanswers")
    return cur.fetchall()

def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()
    query = ("INSERT INTO questionsandanswers values('"+question+"', '"+answer+"')")
    cur.execute(query)
    con.commit()

def get_answer_from_memory(question):
    rows = get_question_and_answer()
    answer = " "
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
        
    return answer