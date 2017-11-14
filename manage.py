from flask_script import Manager
from my_resume import app

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
