import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_city_input():
    while True:
        city = input("Which city's bikeshare data would you like to explore? (Chicago, New York, Washington) ").lower()
        if city in CITY_DATA:
            return city
        else:
            print("Invalid input. ")
            print("Make sure you select from Chicago, New York, or Washington.")

def get_month_input():
    # to get month from input
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'All']
    while True:
        month = input("Please select a month (Jan, Feb, Mar, Apr, May, Jun) or 'all' for all months: ").title()
        if month in months:
            return month
        else:
            print("Invalid input. Please choose a valid month or 'all'.")

def get_day_input():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']
    while True:
        day = input("Please enter a day of the week or 'all' for no specific day: ").title()
        if day in days:
            return day
        else:
            print("Invalid input. Please choose a valid day Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'all'.")

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = get_city_input()
    month = get_month_input()
    day = get_day_input()
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    file_path = CITY_DATA[city]
    df = pd.read_csv(file_path)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'All':
        month_index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'].index(month) + 1
        df = df[df['month'] == month_index]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    Start_Station = df['Start Station'].mode()[0]
    print('Most Commonly used start station:', Start_Station)

    End_Station = df['End Station'].mode()[0]
    print('\nMost Commonly used end station:', End_Station)

    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]

    df['Start to End Station'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Start to End Station'].mode()[0]
    print('\nMost Commonly used combination of start station and end station trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('We Have User Types:\n', user_types)

    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types we have in our data:\n', gender_types)
    except KeyError:
        print("\nGender Types:\nThere is No data for gender types available for this month.")

    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
        print("\nEarliest Year:\nThere is No data for Earliest Year available for this month.")

    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
        print("\nMost Recent Year:\nThere is No data for Most Recent Year available for this month.")

    try:
        Most_Common_Year = df['Birth Year'].mode()[0]
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("\nMost Common Year:\nThere is No data for Most Common Year available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+10])

        to_continue = input("Do you wish to continue?: Enter yes or no.\n ").lower()
        print("*"*80)
        if to_continue.lower() != 'yes':
            break
        start_loc += 10

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