from flask.ext import script

import commands

if __name__ == "__main__":
   from main import app_factory

   import config
   default_config = config.Dev

   manager = script.Manager(app_factory)
   manager.add_option("-c", "--config", dest="config", required=False, default=default_config)
   manager.add_command("test", commands.Test())
   manager.add_command("create_db", commands.CreateDB())
   manager.add_command("drop_db", commands.DropDB())
   manager.add_command("runserver", script.Server(host=default_config.DEV_SERVER_HOST, port=default_config.DEV_SERVER_PORT))
   manager.run()