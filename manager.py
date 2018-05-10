from flasky import make_shell_context, test, app, migrate
from flask_script import Manager,Shell
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.run()
