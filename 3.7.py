def hadii(a,b):#درست تابع 
    if(a==0):#درست شرط
        print("stop")#نمایش استاپ

    else:#اگر انجام نشد شرط
        print(a-b)#چاپ aمنهای b
        hadii(a-b,b)#aمنهای bمیکند و تابع باز میگردد
hadii(20,5)#نشان تابع 



