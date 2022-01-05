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
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
        
    return answer

def get_name():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value from memory where name = 'assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]

def update_name(new_name):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory SET value = '"+new_name+"' where name = 'assistant_name'"
    cur.execute(query)
    con.commit()

def update_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory SET value = '"+str(last_seen_date)+"' where name = 'last_seen_date'"
    cur.execute(query)
    con.commit()

def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'last_seen_date'"
    cur.execute(query)
    return cur.fetchall()[0][0]
