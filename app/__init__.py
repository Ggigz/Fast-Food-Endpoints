# app/__init__.py
import os
from flask import Flask
from instance.config import app_configuration

# Initialing our application
app=Flask(__name__, instance_relative_config=True)

from app.api.v1 import views
from app.api.v2.database import create_table, destory
create_table()
#destory()

#Loading our configuration package
app.config.from_object(app_configuration['development'])