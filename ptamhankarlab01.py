import datetime
#variable declaration and initialization
now=datetime.datetime.now()
cost_kw=0.0;
total_cost=0.0;
sum_of_total=0;
average=0.0;
var=0.0;
app_cost=0.0;

#For accepting inputs from user
app_name1=input("please enter the appliance name:")
app_cost1=float(input("please enter the cost per KW - hr of the appliance (in cents):"))
app_usage1=float(input("please enter the annual usage (in KW - hr):"))
indi_cost1=app_cost1*app_usage1;
total_cost=total_cost+indi_cost1;
app_cost=app_cost+app_cost1;

app_name2=input("please enter the appliance name:")
app_cost2=float(input("please enter the cost per KW - hr of the appliance (in cents):"))
app_usage2=float(input("please enter the annual usage (in KW - hr):"))
indi_cost2=app_cost2*app_usage2;
total_cost=total_cost+indi_cost2;
app_cost=app_cost+app_cost2;


app_name3=input("please enter the appliance name:")
app_cost3=float(input("please enter the cost per KW - hr of the appliance (in cents):"))
app_usage3=float(input("please enter the annual usage (in KW - hr):"))
indi_cost3=app_cost3*app_usage3;
total_cost=total_cost+indi_cost3;
app_cost=app_cost+app_cost3;

app_name4=input("please enter the appliance name:")
app_cost4=float(input("please enter the cost per KW - hr of the appliance (in cents):"))
app_usage4=float(input("please enter the annual usage (in KW - hr):"))
indi_cost4=app_cost4*app_usage4;
total_cost=total_cost+indi_cost4;
app_cost=app_cost+app_cost4;

app_name5=input("please enter the appliance name:")
app_cost5=float(input("please enter the cost per KW - hr of the appliance (in cents):"))
app_usage5=float(input("please enter the annual usage (in KW - hr):"))
indi_cost5=app_cost5*app_usage5;
total_cost=total_cost+indi_cost5;
app_cost=app_cost+app_cost5;

app_name6=input("please enter the appliance name:")
app_cost6=float(input("please enter the cost per KW - hr of the appliance (in cents):"))
app_usage6=float(input("please enter the annual usage (in KW - hr):"))
indi_cost6=app_cost6*app_usage6;
total_cost=total_cost+indi_cost6;
app_cost=app_cost+app_cost6;

#computation
average=total_cost/6;
avg_app_cost=(app_cost/6);
var1=(((avg_app_cost-app_cost1)**2)+((avg_app_cost-app_cost2)**2)+((avg_app_cost-app_cost3)**2)+
      ((avg_app_cost-app_cost4)**2)+((avg_app_cost-app_cost5)**2)+((avg_app_cost-app_cost6)**2))/6;
#output display
std=var1**0.5;

#displaying outputs
print("Total application cost: "+str(round(app_cost,4)));
print("\nAverage of application cost total: "+str(round(avg_app_cost,4)));
print("\nTotal cost of annual usage is: "+str(round(total_cost,4)));
print("\naverage: "+str(round(average,4)))
print("\nvariance: "+str(round(var1,4)))
print("\nSTD: "+str(round(std,4)))
print("Output as of:")
print(now.strftime("%Y-%m-%d %H:%M"))