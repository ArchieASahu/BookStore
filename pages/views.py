from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'pages/index.html')

def aboutus(request):
    # return HttpResponse("<h2>About Us</h2>")
    # name = "John"
    student ={1:"john",2: "jane",3: "blake",4: "kriti"}
    results={
        1:{"name" : "john","cgpa":[9.2, 9.8, 8.9, 9.7]},
        2:{"name" : "jane","cgpa":[8.2, 7.8, 6.9, 5.7]},
        3:{"name" : "sam","cgpa":[6.2, 9.5, 84., 9.5]},
        4:{"name" : "sara","cgpa":[4.2, 7.8, 7.9, 9.7]},
        5:{"name" : "will","cgpa":[9.2, 9.8, 7.9, 9.7]},

    }
    context ={
        "name" : "Sam",
        "age" : 20,
        "num1" :12,
        "num2" : 10,
        "nums" :[1,2,3,4,5,10,20,30],
        "students" :student,
        "result" :results

    }
    return  render(request, "pages/about.html", context)
