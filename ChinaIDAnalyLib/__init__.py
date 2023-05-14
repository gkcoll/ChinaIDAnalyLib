try:
    from .main import *
except:
    from main import *

__all__ = ['CNID', 'GanZhi', 'IDError', 'getFull', 'id_gen', 'load', 'report', 'table', 'verify']