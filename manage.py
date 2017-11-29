
from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    panzera = Professor(name='Mauro Panzera', department='Business Administration')
    ying = Professor(name='Ying Li', department='Business Administration')
    thompson = Professor(name='Hubert Thompson', department='Business Administration')
    wang = Professor(name='Jiannan Wang', department='Accounting & MIS')
    course1 = Course(course_number= 'BUAD 475', title='Internatinal Marketing', description='Learning how to apply marketing strategies to different countries.')
    course2 = Course(course_number='MISY 302', title='Market Research', description='Learning how to apply data analytics to marketing.')
    course3 = Course(course_number='BUAD 309', title='Introduction to Organization Behavior', description='Management of the marketing functions in different business aspects.')
    course4 = Course(course_number='MISY 350', title='Web Application Development', description='Fundamentals of web development, including Python and Flask.')
    db.session.add(panzera)
    db.session.add(ying)
    db.session.add(thompson)
    db.session.add(wang)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
