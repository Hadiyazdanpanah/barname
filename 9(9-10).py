def hadi(d):
    a={"mamad":85,"reza":17}
    if (d in a):
        del a[d]
        print("hazf")
    else:
        print("nabud")
        hadi(input("benvis"))