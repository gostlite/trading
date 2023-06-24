from django.shortcuts import render,redirect
from . import client
import json

# Create your views here.


#testing the connection
# try:
#     client.admin.command('ping')
#     print("Connection established")
# except Exception as e:
#     print(e)


data_base = client["traderstock"]
collection = data_base["traders"]

curr_user =""

def get_time_profit_loss():
    user = collection.find_one({"name":curr_user})
    p_l_list =[]
    time_int_list =[]
    for data in user["profit_loss/time"]:
        profit_loss, time = data
        p_l_list.append(profit_loss)
        time_int_list.append(time)
    return (p_l_list, time_int_list)


def home_page(request):
    global curr_user 
    curr_user = ""
    if request.method=="POST":
        curr_user= request.POST.get("username").strip().lower()
        return redirect(chart_view)
    return render(request, "cial.html")

def chart_view(request):
    global curr_user
    try:
         p_l_list, time_int_list=get_time_profit_loss()# get the details of the users for graph
        
    except Exception:
        return redirect(home_page)
    data_list_json, time_list_json = json.dumps(p_l_list), json.dumps(time_int_list)
    return render(request, 'user_dash.html', {"profit_loss":data_list_json, "time": time_list_json, "name":curr_user})

