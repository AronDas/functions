def shutdown():
    YN = input("Please decide to shutdown this computer(Y/N)")
    if YN == "Y":
        Y = input("Did you save all your work/files?(Y/N)")
        if Y == "Y":
           
            YY = input("Are you sure you want to shutdown?(Y/N)")
            
            if YY == "Y":
                print("Shutting down...")
    elif YN == "N":
        print("Aborting shutdown...")
    else:
        print("Invalid input. perhaps you forgot a uppercase?")        

shutdown()