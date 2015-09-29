# -*- coding: utf-8 -*-
import os

from aldryn_addons.utils import boolean_ish


INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: this is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    # </INSTALLED_ADDONS>'
]

import aldryn_addons.settings

aldryn_addons.settings.load(
    settings=locals(),
    debug=boolean_ish(os.environ.get('ALDRYN_ADDONS_DEBUG', False))
)


# all django settings can be altered here

INSTALLED_APPS.extend([
    # add you project specific apps here
])

TEMPLATE_CONTEXT_PROCESSORS.extend([
    # add your template context processors here
])

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])
