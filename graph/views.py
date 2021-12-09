from django.shortcuts import render
from graph.models import Stock
import pandas as pd 
import numpy as np 
import json

json_data= open("data.json")
json2dic = json.load(json_data)

def topstocks(request):
    sectors=["all"] 
    weeks=["all"]
    periods=["1","2","4","8","12","24"]

    sectors_all=[]
    start_dates_all=[]
    end_dates_all=[]
    codes_all=[]

    
    Week1PandL_list=[]
    Week2PandL_list=[]
    Week4PandL_list=[]
    Week8PandL_list=[]
    Week12PandL_list=[]
    Week24PandL_list=[]

    close_list_all=[]

    Week1PandL_percent_list= []
    Week2PandL_percent_list= []
    Week4PandL_percent_list= []
    Week8PandL_percent_list= []
    Week12PandL_percent_list= []
    Week24PandL_percent_list= []    
    
  

    for stock in json2dic:

        start_dates_all.append(stock["Date_StartDate"])
        end_dates_all.append(stock["End_date"])
        sectors_all.append(stock["scoring_category"]) 
        codes_all.append(stock["Code"])   
        close_list_all.append(stock["close"])

        if "Week1PandL" in stock["ROI"]:
            Week1PandL_list.append(stock["ROI"]["Week1PandL"]) 
            Week1PandL_percent_list.append(stock["ROI"]["Week1PandL"]/stock["close"])
        else:
            Week1PandL_list.append(0) 
            Week1PandL_percent_list.append(0)

        if "Week2PandL" in stock["ROI"]:
            Week2PandL_list.append(stock["ROI"]["Week2PandL"])
            Week2PandL_percent_list.append(stock["ROI"]["Week2PandL"]/stock["close"])
        else:
            Week2PandL_list.append(0) 
            Week2PandL_percent_list.append(0)

        if "Week4PandL" in stock["ROI"]:
            Week4PandL_list.append(stock["ROI"]["Week4PandL"]) 
            Week4PandL_percent_list.append(stock["ROI"]["Week4PandL"]/stock["close"])
        else:
            Week4PandL_list.append(0) 
            Week4PandL_percent_list.append(0)

        if "Week8PandL" in stock["ROI"]:
            Week8PandL_list.append(stock["ROI"]["Week8PandL"]) 
            Week8PandL_percent_list.append(stock["ROI"]["Week8PandL"]/stock["close"])
        else:
            Week8PandL_list.append(0) 
            Week8PandL_percent_list.append(0)

        if "Week12PandL" in stock["ROI"]:
            Week12PandL_list.append(stock["ROI"]["Week12PandL"]) 
            Week12PandL_percent_list.append(stock["ROI"]["Week12PandL"]/stock["close"])  
        else:
            Week12PandL_list.append(0) 
            Week12PandL_percent_list.append(0)

        if "Week24PandL" in stock["ROI"]:
            Week24PandL_list.append(stock["ROI"]["Week24PandL"])
            Week24PandL_percent_list.append(stock["ROI"]["Week24PandL"]/stock["close"])
        else:
            Week24PandL_list.append(0)     
            Week24PandL_percent_list.append(0)        

        #create unique sectors list
        if stock["scoring_category"] not in sectors:
            sectors.append(stock["scoring_category"])

        #create unique weeks list
        if stock["start_date"]+" to " + stock["End_date"] not in weeks:
            weeks.append(stock["start_date"]+" to " + stock["End_date"])
         

    print(len(Week1PandL_list),len(Week2PandL_list),len(Week4PandL_list),len(Week8PandL_list))
    print(len(Week2PandL_percent_list),Week2PandL_percent_list)

    return render(request, "graph/topstocks.htm",{"sectors":sectors,"weeks":weeks,"periods":periods,"sectors_all":sectors_all,"codes_all":codes_all,"start_dates_all":start_dates_all,"end_dates_all":end_dates_all,"Week1PandL_list":Week1PandL_list,"Week2PandL_list":Week2PandL_list,"Week4PandL_list":Week4PandL_list,"Week8PandL_list":Week8PandL_list,"Week12PandL_list":Week12PandL_list,"Week24PandL_list":Week24PandL_list,"close_list_all":close_list_all,  "Week1PandL_percent_list":Week1PandL_percent_list,   "Week2PandL_percent_list":Week2PandL_percent_list,  "Week4PandL_percent_list": Week4PandL_percent_list, "Week8PandL_percent_list": Week8PandL_percent_list,  "Week12PandL_percent_list":Week12PandL_percent_list, "Week24PandL_percent_list":Week24PandL_percent_list })

def trial(request):
    sectors=["all"] 
    weeks=["all"]
    codes=["all"]



    sectors_all=[]
    start_dates_all=[]
    end_dates_all=[]
    codes_all=[]
    weeks_all=[]



    close_list_all=[]



    Week1PandL_list=[]
    Week2PandL_list=[]
    Week4PandL_list=[]
    Week8PandL_list=[]
    Week12PandL_list=[]
    Week24PandL_list=[]

    TwoHundMovingAverage=[]
    TwentyMovingAverage= []
    ThreeMonthPercentGain= []
    StandardDeviationWithMarket= []
    StandardDeviation= []
    PercentageLag= []
    OneMonthPercentGain= []
    Multiple= []
    InvestmentRank= []
    IndPrice= []
    IndGrowth2= []
    IndGrowth12= []
    IndGrowth1= []
    FourWeekLow= []
    FourWeekHigh= []
    FiftyMovingAverage= []
    Fifty2WeekLow= []
    Fifty2WeekHigh= []
    Fifty2WeekChange= []
    AvgVol3Months= []
    AvgVol1Month= []
    AvgVol10Days= []



    length= len(codes_all)
    range_array= range(0,length)

    for stock in json2dic:
        start_dates_all.append(stock["Date_StartDate"])
        end_dates_all.append(stock["End_date"])
        sectors_all.append(stock["scoring_category"]) 
        codes_all.append(stock["Code"])      

        close_list_all.append(stock["close"]) 

        TwoHundMovingAverage.append(stock["SP"]["TwoHundMovingAverage "])
        TwentyMovingAverage.append(stock["SP"]["TwentyMovingAverage"])
        ThreeMonthPercentGain.append(stock["SP"]["ThreeMonthPercentGain"])
        StandardDeviationWithMarket.append(stock["SP"]["StandardDeviationWithMarket"])
        StandardDeviation.append(stock["SP"]["StandardDeviation"])
        PercentageLag.append(stock["SP"]["PercentageLag"])
        OneMonthPercentGain.append(stock["SP"]["OneMonthPercentGain"])
        Multiple.append(stock["SP"]["Multiple"])
        InvestmentRank.append(stock["SP"]["InvestmentRank"])
        IndPrice.append(stock["SP"]["IndPrice"])
        IndGrowth2.append(stock["SP"]["IndGrowth2"])
        IndGrowth12.append(stock["SP"]["IndGrowth12"])
        IndGrowth1.append(stock["SP"]["IndGrowth1"])
        FourWeekLow.append(stock["SP"]["FourWeekLow"])
        FourWeekHigh.append(stock["SP"]["FourWeekHigh"])
        FiftyMovingAverage.append(stock["SP"]["FiftyMovingAverage"])
        Fifty2WeekLow.append(stock["SP"]["Fifty2WeekLow"])
        Fifty2WeekHigh.append(stock["SP"]["Fifty2WeekHigh"])
        Fifty2WeekChange.append(stock["SP"]["Fifty2WeekChange"])
        AvgVol3Months.append(stock["SP"]["AvgVol3Months"])
        AvgVol1Month.append(stock["SP"]["AvgVol1Month"])
        AvgVol10Days.append(stock["SP"]["AvgVol10Days"])
        
        #create unique sectors list
        if stock["scoring_category"] not in sectors:
            sectors.append(stock["scoring_category"])

        #create unique weeks list
        if stock["start_date"]+" to " + stock["End_date"] not in weeks:
            weeks.append(stock["start_date"]+" to " + stock["End_date"])

        #create unique sectors list
        if stock["Code"] not in codes:
            codes.append(stock["Code"])    

        if "Week1_ROI" in stock["ROI"]:
            Week1PandL_list.append(stock["ROI"]["Week1PandL"])
            
        else:
            Week1PandL_list.append(0)  

        if "Week2_ROI" in stock["ROI"]:
            Week2PandL_list.append(stock["ROI"]["Week2PandL"])
        else:
            Week2PandL_list.append(0)  

        if "Week4_ROI" in stock["ROI"]:
            Week4PandL_list.append(stock["ROI"]["Week4PandL"])
        else:
            Week4PandL_list.append(0)  

        if "Week8_ROI" in stock["ROI"]:
            Week8PandL_list.append(stock["ROI"]["Week8PandL"])
        else:
            Week8PandL_list.append(0)  
   
        if "Week12_ROI" in stock["ROI"]:
     
            Week12PandL_list.append(stock["ROI"]["Week12PandL"])
        else:
            Week12PandL_list.append(0)  

        if "Week24_ROI" in stock["ROI"]:
            Week24PandL_list.append(stock["ROI"]["Week24PandL"])
        else:
            Week24PandL_list.append(0)  
        
  

    
    #create weeks alll list
    for i in range(0,len(start_dates_all)):
        weeks_all.append(start_dates_all[i]+" to "+ end_dates_all[i])

    print(sum(TwoHundMovingAverage))

   

 
    
    
    return render(request, "graph/trial.html",{"sectors":sectors,"weeks":weeks,"codes":codes,"sectors_all":sectors_all,"length":length,"range_array": range_array,"start_dates_all":start_dates_all,"end_dates_all":end_dates_all,"codes_all":codes_all,"weeks_all":weeks_all, "Week1PandL_list":Week1PandL_list,"Week2PandL_list":Week2PandL_list,"Week4PandL_list":Week4PandL_list,"Week8PandL_list":Week8PandL_list,"Week12PandL_list":Week12PandL_list,"Week24PandL_list":Week24PandL_list,"close_list_all":close_list_all, "TwoHundMovingAverage": TwoHundMovingAverage, "TwentyMovingAverage":TwentyMovingAverage, "ThreeMonthPercentGain" : ThreeMonthPercentGain, "StandardDeviationWithMarket":StandardDeviationWithMarket,     "StandardDeviation":StandardDeviation, "PercentageLag":PercentageLag,"OneMonthPercentGain":OneMonthPercentGain,"Multiple":Multiple, "InvestmentRank":InvestmentRank, "IndPrice":IndPrice,"IndGrowth2":IndGrowth2,"IndGrowth12":IndGrowth12,"IndGrowth1":IndGrowth1,"FourWeekLow":FourWeekLow, "FourWeekHigh":FourWeekHigh,"FiftyMovingAverage":FiftyMovingAverage,"Fifty2WeekLow":Fifty2WeekLow,"Fifty2WeekHigh":Fifty2WeekHigh,"Fifty2WeekChange":Fifty2WeekHigh,"AvgVol3Months":AvgVol3Months,"AvgVol1Month":AvgVol1Month,"AvgVol10Days":AvgVol10Days})


