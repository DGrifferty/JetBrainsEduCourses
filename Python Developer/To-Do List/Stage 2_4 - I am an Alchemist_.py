from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///todo.db?check_same_thread=False')


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Empty')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return str(self.task)#+ ' ' + str(self.deadline)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#####################################


def add_task():
    new_task = input('Enter task:')
    new_row = Table(task= new_task, deadline = datetime.today())
    session.add(new_row)
    session.commit()

def show_tasks():
    rows = session.query(Table).all()
    print(rows)
    if rows == []:
        print('Nothing to do!')
    pass

while True:

    user_choice = int(input('''1) Today's tasks
2) Add task
0) Exit
'''))

    if user_choice == 1:
        show_tasks()
    elif user_choice == 2:
        add_task()
    elif user_choice == 0:
        quit()
