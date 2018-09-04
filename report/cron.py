from .models import Report
from backtest.settings import MEDIA_ROOT
from django.core.files.storage import default_storage
from utils import utils
import os
import fcntl

def Query():
    queryset = Report.objects.filter(status = 0)
    inprocess_queryset = Report.objects.filter(status = 1)
    in_length = len(inprocess_queryset)
    for report in queryset:
        if(in_length < 5):
            report.status = 0
            report.save()
            print(report.alpha_name, report.file)
            in_length += 1

            utils.unzip(report)
            print(utils.validate_files(report))
            try:
                utils.compile_alpha(report)
            except:
                pass
            #utils.clean()