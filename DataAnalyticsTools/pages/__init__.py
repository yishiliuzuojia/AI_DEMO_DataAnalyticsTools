# -*- coding: utf-8 -*-
"""页面模块"""

from .home import render_home_page
from .upload import render_upload_page
from .results import render_results_page
from .advice import render_advice_page
from .help import render_help_page

__all__ = [
    'render_home_page',
    'render_upload_page', 
    'render_results_page',
    'render_advice_page',
    'render_help_page'
]
