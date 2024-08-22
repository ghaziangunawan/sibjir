from django.shortcuts import render,redirect
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def show_html(request):
    cursor = connection.cursor()
    sql = f"""
            SELECT *
            FROM person
            WHERE id = 1 
            """
    cursor.execute(sql)
    fetch = cursor.fetchall()[0][1]
    response = {'fetch': fetch}

    return render(request, "home.html",response)
