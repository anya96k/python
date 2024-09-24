def conversion(week,days,months,years,list_row):
  #lists have been defined to hold different inputs
  inp_day = []
  inp_mon = []
  inp_year = []
  inp_week=[]
  inp_hol=[]
  out = []
  #converts the days of a week(monday,sunday,etc.) into one hot vectors and stores them as a dictionary
  week1 = number_to_one_hot(week)
  #list_row contains primary inputs
  for row in list_row:
        #Filter out date from list_row
        d = row[0]
        #the date was split into three values date, month and year.
        d_split=d.split('/')
        if d_split[2]==str(year_all[0]):
          #prevents use of the first year data to ensure each input contains previous year data as well.
          continue
        #encode the three parameters of date into one hot vectors using date_to_enc function.
        d1,m1,y1 = date_to_enc(d,days,months,years) #days, months and years and dictionaries containing the one hot encoding of each date,month and year.
        inp_day.append(d1) #append date into date input
        inp_mon.append(m1) #append month into month input
        inp_year.append(y1) #append year into year input
        week2 = week1[row[3]] #the day column from list_is converted into its one-hot representation and saved into week2 variable
        inp_week.append(week2)# it is now appended into week input.
        inp_hol.append([row[2]])#specifies whether the day is a holiday or not
        t1 = row[1] #row[1] contains the traffic/sales value for a specific date
        out.append(t1) #append t1(traffic value) into a list out
  return inp_day,inp_mon,inp_year,inp_week,inp_hol,out #all the processed inputs are returned

inp_day,inp_mon,inp_year,inp_week,inp_hol,out = conversion(day,month,year,week,list_train)
#all of the inputs must be converted into numpy arrays to be fed into the model
inp_day = np.array(inp_day)
inp_mon = np.array(inp_mon)
inp_year = np.array(inp_year)
inp_week = np.array(inp_week)
inp_hol = np.array(inp_hol)