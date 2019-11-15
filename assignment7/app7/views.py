from django.shortcuts import render

# Create your views here.
def loginPage(request):
    return render(request,"login.html")


def validateDetails(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    type = request.POST.get("type")

    if type == "admin":
        if username == "sathya" and password == "tech":
            res = "Welcome Admin"
            return render(request,"account.html",{"response":res,"username":username})
        else:
            res = "Admin Username or Password is     invalid"
            return render(request,"login.html",{"response":res})
    elif type == "employee":
        if (username == "vara" and password == "prasad") or (username == "krishna" and password == "mohan"):
            res = "Welcome Employee"
            return render(request,"account.html",{"response":res,"username":username})
        else:
            res = "Employee Username or Password is invalid"
            return render(request,"login.html",{"response":res})
    elif type == "faculty":
        if (username == "naveen" and password == "kumar") or (username == "kanna" and password == "banna"):
            res = "Welcome Faculty"
            return render(request, "account.html", {"response": res, "username": username})
        else:
            res = "Faculty Username or Password is invalid"
            return render(request, "login.html", {"response": res})
    elif type == "student":
        if (username == "ravi" and password == "123@R") or (username == "mohan" and password == "mo@123"):
            res = "Welcome Employee"
            return render(request,"account.html",{"response":res,"username":username})
        else:
            res = "Student Username or Password is invalid"
            return render(request,"login.html",{"response":res})
    else:
        res = "Please select type of log in (Admin/Employee/Faculty/Student)"
        return render(request, "login.html", {"response": res})