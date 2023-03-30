import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']


months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']


days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Do you want to analyze data for Chicago, New York City or Washington? \n Enter a city: ").lower()
        print("Your choice: {}".format(city.title()))
        if city in cities:
            break
        else:
            print ('That\'s not a valid city name!')
        

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Do you want to analyze data for January, February, March, April, May or June? \n Enter a month or enter 'all': ").lower()
        print("You choice: {}".format(month.title()))
        if month in months:       
            break
        else:
            print ('That\'s not a valid month name!')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want to analyze data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday? \n Enter a weekday or enter 'all': ").lower()
        print("You choice: {}".format(day.title()))
        if day in days:       
            break
        else:
            print ('That\'s not a valid weekday name!')
           
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

  
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert column Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
      
    # extract month, day and hour from Start Time column and create columns 'month', 'day' and 'hour'
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # in case of input 'all' months   
    if month != 'all':
        # convert month names to corresponding integer month numbers 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month and create the new dataframe
        df = df[df['month'] == month]
        
    # in case of input 'all' weekdays 
    if day != 'all':
        # filter by weekday and create a new dataframe
        df = df[df['day'] == day.title()]

    return df
                 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()   
                     
    # TO DO: display the most common month
    # locate and print most common month             
    most_common_month = df['month'].value_counts().idxmax()
    print('Most common month:', most_common_month)


    # TO DO: display the most common day of the week
    # locate and print most common weekday 
    most_common_weekday = df['day'].value_counts().idxmax()
    print('Most common weekday:', most_common_weekday)


    # TO DO: display the most common start hour of the day
    # locate and print most common start hour 
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print('Most common start hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

  
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station= df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station'])['End Station'].value_counts().idxmax()
    print('The most frequent combination of start station and end station trip is: ', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time) 

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print ('The average travel time is:', average_travel_time) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts for each usertype:', user_types)


    # TO DO: Display counts of gender
    # Only access Gender, if column in available
    try:
        aux = df['Gender']
        gender = df['Gender'].value_counts()
        print('Counts for each gender:', gender)
    except KeyError:
        print('For this city there is no Gender data available.')
        


    # TO DO: Display earliest, most recent, and most common year of birth
    # Only access Bith Year, if column in available
    
    try:
        aux = df['Birth Year']
        earliest_birthyear = df['Birth Year'].min()
        print('Earliest year of birth:', earliest_birthyear)
   
        most_recent_birthyear = df['Birth Year'].max()
        print('Most recent year of birth in New York City:', most_recent_birthyear)
   
        most_common_birthyear = df['Birth Year'].value_counts().idxmax()
        print('Most common year of birth:', most_common_birthyear)
    except KeyError:
        print('For this city there is no Birth Year data available.')
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
  """We display rows of the DataFrame on users request"""
  start_loc=0
  while True:
        view_data = input('Do you want to see 5 rows of data? \n yes or no?').lower()
        if view_data == 'yes':
            print(df[start_loc : start_loc + 5]) 
            start_loc += 5
        
        if view_data != 'yes':
            break

        if start_loc >= len(df):
            print('No more data to display.')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()