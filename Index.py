import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def menu():
    print("****************************")
    print("read data from file in different ways")
    print("1.Read complete csv file")
    print("2.Reading complete file without index")
    print("=======================")
    print("Data Visualization")
    print("3.Line Chart")
    print("4.Bar Plot")
    print("5.Pie Chart")
    print("6.Scatter Chart")
    print("=======================")
    print("Apply Data Manipulation in the records of CSV file")
    print("7.Sorting the data as per your choice")
    print("8.Read top and bottom records from file as per requirement")
    print("9.Make the copy of CSV file")
    print("10.Read the specific columns")
    print("*****************************")
menu()
option=int(input("Enter your choice:"))
while option!=0:
    if option==1:
            print("Reading Data from CSV file")
            df=pd.read_csv("C:\\states.csv")
            print(df)
            
    elif option==2:
            print("Reading Data from CSV file without index value")
            df=pd.read_csv("C:\\states.csv",index_col=0)
            print(df)
            
    elif option==3:
            df=pd.read_csv("C:\\states.csv")
            st=df['State']
            cnf=df['Confirmed']
            rc=df['Recovered']
            dth=df['Deaths']
            ac=df['Active']
            plt.xlabel("state")
            plt.xticks(rotation='vertical')
            print("Select Specific Line Chart as given below:")
            print("press 1 to print the data for State vs Confirmed Cases")
            print("press 2 to print the data for State vs Recovered Cases")
            print("press 3 to print the data for State vs Death Cases")
            print("press 4 to print the data for State vs Active Cases")
            print("press 5 to merge all the data in one Line chart")
            op=int(input("Enter your choice:"))
            if op==1:
                plt.ylabel("Confirmed Cases")
                plt.title("State wise Confirmed Cases")
                plt.plot(st,cnf)
                plt.show()
            elif op==2:
                plt.ylabel("Recovered cases")
                plt.title("State wise Recovered Cases")
                plt.plot(st,rc)
                plt.show()
            elif op==3:
                plt.ylabel("Death cases")
                plt.title("State wise Death Cases")
                plt.plot(st,dth)
                plt.show()
            elif op==4:
                plt.ylabel("Active cases")
                plt.title("State  wise Active cases")
                plt.plot(st,ac)
                plt.show()
            elif op==5:
                plt.ylabel("Number of cases")
                plt.plot(st,cnf,label="State wise Confirmed Cases")
                plt.plot(st,rc,label="State wise Recovered Cases")
                plt.plot(st,dth,label="State wise Death")
                plt.plot(st,ac,label="State wise Active Cases")
                plt.legend()
                plt.show()
            else:
                print("Enter valid input")
                
    elif option==4:
            df=pd.read_csv("C:\\states.csv")
            st=df['State']
            cnf=df['Confirmed']
            rc=df['Recovered']
            dth=df['Deaths']
            ac=df['Active']
            plt.xlabel("state")
            plt.xticks(rotation='vertical')

            print("Select Specific Bar Chart as given below:")
            print("press 1 to print the data for State vs Confirmed Cases")
            print("press 2 to print the data for State vs Recovered Cases")
            print("press 3 to print the data for State vs Death")
            print("press 4 to print the data for State vs Active Cases")
            print("press 5 to print all the data in form of stack bar chart")
            print("press 6 to print all the data in form of multi bar chart")
            op=int(input("Enter your choice:"))
            if op==1:
                plt.ylabel("Confirmed cases")
                plt.title("State wise Confirmed Cases")
                plt.bar(st,cnf)
                plt.show()
            elif op==2:
                plt.ylabel("Recovered cases")
                plt.title("State wise Recovered Cases")
                plt.bar(st,rc)
                plt.show()
            elif op==3:
                plt.ylabel("Death cases")
                plt.title("State wise Death Cases")
                plt.bar(st,dth)
                plt.show()
            elif op==4:
                plt.ylabel("Active cases")
                plt.title("State wise Active cases")
                plt.bar(st,ac)
                plt.show()
            elif op==5:
                plt.bar(st,cnf,width=0.2,label="State wise Confirmed Cases")
                plt.bar(st,cnf,width=0.2,label="State wise Recovered Cases")
                plt.bar(st,cnf,width=0.2,label="State wise Death")
                plt.bar(st,cnf,width=0.2,label="State wise Active Cases")
                plt.legend()
                plt.show()
            elif op==6:
                ind=np.arange(len(st))
                width=0.25
                plt.bar(ind,cnf,width,label="State wise Confirmed Cases")
                plt.bar(ind+0.25,rc,width,label="State wise Recovered Cases")
                plt.bar(ind+0.50,dth,width,label="State wise Death")
                plt.bar(ind+0.75,ac,width,label="State wise Active Cases")
                plt.legend()
                plt.show()
            else:
                print("Enter valid input")
                
    elif option==5:
            df=pd.read_csv("C:\\states.csv")
            st=df['State']
            cnf=df['Confirmed']
            rc=df['Recovered']
            dth=df['Deaths']
            ac=df['Active']

            print("Select Specific Pie Chart as given below:")
            print("press 1 to print the data for State vs Confirmed Cases")
            print("press 2 to print the data for State vs Recovered Cases")
            print("press 3 to print the data State vs Death")
            print("press 4 to print the data for State vs Active Cases")
            op=int(input("Enter your choice:"))
            if op==1:
                plt.title("State wise Confirmed Cases")
                plt.pie(cnf,labels=st,autopct="%3d%%")
                plt.show()
            elif op==2:
                plt.title("State wise Reovered Cases")
                plt.pie(rc,labels=st,autopct="%3d%%")
                plt.show()
            elif op==3:
                plt.title("State wise Death Cases")
                plt.pie(dth,labels=st,autopct="%3d%%")
                plt.show()
            elif op==4:
                plt.title("State wise Active Cases")
                plt.pie(ac,labels=st,autopct="%3d%%")
                plt.show()
            else:
                print("Enter valid option")

    elif option==6:
            df=pd.read_csv("C:\\states.csv")
            st=df['State']
            cnf=df['Confirmed']
            rc=df['Recovered']
            dth=df['Deaths']
            ac=df['Active']

            ax=plt.gca()
            ax.scatter(st,cnf,color='b',label="State wise Confirmed Cases")
            ax.scatter(st,rc,color='r',label="State wise Recovered Cases")
            ax.scatter(st,dth,color='g',label="State wise Death")
            ax.scatter(st,ac,color='y',label="State wise Active Cases")

            plt.xlabel("state")
            plt.xticks(rotation='vertical')
            plt.title("Complete Scatter Chart")
            plt.legend()
            plt.show()
            
    elif option==7:
            df=pd.read_csv("C:\\states.csv")
            print("press 1 to arrange the record as per the State Name")
            print("press 2 to arrange the record as per the Confirmed Cases")
            print("press 3 to arrange the record as per the Recovered Cases")
            print("press 4 to arrange the record as per the Total Deaths")
            print("press 5 to arrange the record as per the Active Cases")
            op=int(input("Enter Your Choice:"))
            if op==1:
                df.sort_values(["State"],inplace=True)
                print(df)
            elif op==2:
                df.sort_values(["Confirmed"],inplace=True)
                print(df)
            elif op==3:
                df.sort_values(["Recovered"],inplace=True)
                print(df)
            elif op==4:
                df.sort_values(["Deaths"],inplace=True)
                print(df)
            elif op==5:
                df.sort_values(["Active"],inplace=True)
                print(df)
            else:
                print("Enter valid input")
            
    elif option==8:
            df=pd.read_csv("C:\\states.csv",index_col=0)
            top=int(input("How many records to display from top:"))
            print("First",top,"records")
            print(df.head(top))
            bottom=int(input("How many records to display from bottom:"))
            print("Last",bottom,"records")
            print(df.tail(bottom))

    elif option==9:
            print("Duplicate the file with new file")
            df=pd.read_csv("C:\\states.csv")
            df.to_csv("C:\\IP Practical\\statesNew.csv")
            print("Data from the new file")
            print(df)

    elif option==10:
            print("Reading Specific Column from CSV file")
            print("******************")
            print("press 1 to see States and Confirmed column only")
            print("press 2 to see States and Recovered column only ")
            print("press 3 to see States and Deaths column only")
            print("press 4 to see States and Active column only")
            print("press 5 to see States,Confirmed and Active column only")
            print("press 6 to see States,Confirmed and Recovered column only")
            print("press 7 to see States,Recovered and Deaths column only")
            print("press 8 to see States,Deaths and Active column only")
            print("press 9 to see States,Confirmed and Deaths column only")
            opt=int(input("Enter your choice="))
            if opt==1:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Confirmed'],index_col=0)
                print(df)
            elif opt==2:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Recovered'],index_col=0)
                print(df)
            elif opt==3:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Deaths'],index_col=0)
                print(df)
            elif opt==4:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Active'],index_col=0)
                print(df)
            elif opt==5:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Confirmed','Active'],index_col=0)
                print(df)
            elif opt==6:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Confirmed','Recovered'],index_col=0)
                print(df)
            elif opt==7:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Recovered','Deaths'],index_col=0)
                print(df)
            elif opt==8:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Deaths','Active'],index_col=0)
                print(df)
            elif opt==9:
                df=pd.read_csv("C:\\states.csv",usecols=['State','Confirmed','Deaths'],index_col=0)
                print(df)
            else:
                print("Enter valid input")
    else:
        print("Invalid Option")
    menu()
    option=int(input("Enter your choice:"))        