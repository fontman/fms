""" Blueprints package

Provides controllers containing flask web services for Fontman GUI.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/11/2016
"""

from blueprint.auth_controller import auth_blueprint
from blueprint.collections_controller import collections_blueprint
from blueprint.fontfaces_controller import fontfaces_blueprint
from blueprint.fonts_controller import fonts_blueprint
from blueprint.settings_controller import settings_blueprint
from blueprint.typecase_controller import typecase_blueprint
