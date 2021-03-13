from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()
engine = create_engine('sqlite:///todo.db?check_same_thread=False')


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='Empty')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return str(self.task)  # + ' ' + str(self.deadline)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


#####################################


def add_task():
    new_task = input('Enter task:')
    task_deadline = input('Enter deadline:')
    task_deadline = datetime.strptime(task_deadline, '%Y-%m-%d')
    new_row = Table(task=new_task, deadline=task_deadline)
    session.add(new_row)
    session.commit()


def show_tasks(filter):
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    format_month_name = '%b'
    today = datetime.today().date()
    if filter == 1:
        print(f'Today {today.day} {today.strftime(format_month_name)}:')
        rows = session.query(Table).filter(Table.deadline == today).all()
        print_rows(rows)
    elif filter == 2:
        for i in range(8):
            if i == 0:
                day_name = day_names[today.weekday()]
                # print(f'Today {today.day} {today.strftime(format_month_name)}:')
                print(f'{day_name} {today.day} {today.strftime(format_month_name)}:')
                rows = session.query(Table).filter(Table.deadline == today).all()
            else:
                next_day = today + timedelta(days=i)
                day_name = day_names[next_day.weekday()]
                print(f'{day_name} {next_day.day} {today.strftime(format_month_name)}:')
                rows = session.query(Table).filter(Table.deadline == next_day).all()
            print_rows(rows)

    elif filter == 3:
        rows = session.query(Table).all()
        print_rows(rows)


def print_rows(r):
    if r:
        print(r)
    else:
        print('Nothing to do!')
    print('')


while True:
    session.query(Table).order_by(Table.deadline).all()

    user_choice = int(input('''1) Today's tasks
2) Week's Tasks
3) All Tasks
4) Add task
0) Exit
'''))

    if user_choice == 1:
        show_tasks(1)
    elif user_choice == 2:
        show_tasks(2)
    elif user_choice == 3:
        show_tasks(3)
    elif user_choice == 4:
        add_task()
    elif user_choice == 0:
        quit()

