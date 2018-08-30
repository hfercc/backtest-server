import xadmin
from .models import Report

class ReportAdmin(object):
    list_display=["name", "report_id", "file", "status"]
    search_fields=["name", ]

xadmin.site.register(Report, ReportAdmin)