# Create your views here.
from django.shortcuts import render
from read_log_file import readfile
import datetime
from django.http import HttpResponse
import json


def convert_string_to_date(date_data):
    return datetime.datetime(int(date_data[0:4]), int(date_data[5:7]), int(date_data[8:10]))


def index(request):
    return render(request, 'd3js/index.html', dict())


def nova_log_view(request):
    p_start_date = request.GET.get('start_date')
    p_end_date = request.GET.get('end_date')
    start_date = None
    end_date = None
    if p_start_date != "unspecified":
        try:
            start_date = datetime.datetime.strptime(p_start_date, "%Y:%m:%d-%H:%M:%S")
        except TypeError:
            return HttpResponse(json.dumps({"result": "invalid value"}), status=404)
        except ValueError:
            return HttpResponse(json.dumps({"result": "invalid value"}), status=404)
    if p_end_date != "unspecified":
        try:
            end_date = datetime.datetime.strptime(p_end_date, "%Y:%m:%d-%H:%M:%S")
        except TypeError:
            return HttpResponse(json.dumps({"result": "invalid value"}), status=404)
        except ValueError:
            return HttpResponse(json.dumps({"result": "invalid value"}), status=404)
    # t = datetime.datetime.now()
    # check_time = datetime.datetime(t.year,t.month,t.day,00,00,00)+datetime.timedelta(days=1,hours=1)
    # if (start_date and end_date and start_date>end_date)or (end_date and end_date>check_time):
    if (start_date and end_date and start_date > end_date):
        return HttpResponse(json.dumps({"result": "invalid value"}), status=404)
    log_reader = readfile.ReadLog("/home/cong/n-api.log")
    log_summary_result = log_reader.summary_log_by_day(start_date, end_date)
    return HttpResponse(json.dumps(log_summary_result.__dict__, ), status=200)
