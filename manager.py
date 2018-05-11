#encoding='utf-8'
import os
'''
if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]
            '''

from flasky import make_shell_context, test, app, migrate
from flask_script import Manager,Shell
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
