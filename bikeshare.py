import time
import pandas as pd
import numpy as np
from numpy import mean

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input("Please enter the City of service :").lower()
    while (city != 'chicago') and (city != 'new york city') and (city != 'washington'):
        print("The city you have input is out of our service")
        city = input("Please enter the City of service :")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_ls = ['all', 'january', 'february', 'march', 'april', 'june']
    month = input("Please enter the month of service from january to june (type 'all' to view all of the month): ").lower()
    while month not in month_ls:
        print("The month you have input does not exist")
        month = input("Please enter the month of service :")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_ls = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input("Please enter the day of service (type 'all' to view all of the day): ").lower()
    while day not in day_ls:
        print("The day you have input does not exist")
        day = input("Please enter the day of service :")



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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most Frequent Month of Usage :')
    most_common_month = df['month'].value_counts().idxmax()
    print(most_common_month)
    print('\n')

    # TO DO: display the most common day of week
    print('Most Frequent Day of Usage : ')
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print(most_common_day)
    print('\n')

    # TO DO: display the most common start hour
    print('Most Frequent Start Hour of Usage : ')
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print(most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Commonly Used Start Station :')
    most_common_start_st = df['Start Station'].value_counts().idxmax()
    print(most_common_start_st)
    print('\n')

    # TO DO: display most commonly used end station
    print('Most Commonly Used End Station :')
    most_common_end_st = df['End Station'].value_counts().idxmax()
    print(most_common_end_st)
    print('\n')

    # TO DO: display most frequent combination of start station and end station trip
    print('Most Frequent Combination of Start and End Station trip :')
    most_common_comb_st = df.groupby(['Start Station','End Station']).size().idxmax()
    print(most_common_comb_st)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['time_traveled'] = df['End Time'] - df['Start Time']
    total_time_traveled = df['time_traveled'].sum()
    print('\n')

    #print(df['time_traveled'])
    print('Total Duration of Travel Time :')
    print(total_time_traveled)
    print('\n')

    # TO DO: display mean travel time
    print('Average Duration of Rental Travel Time :')
    mean_time = mean(df['time_traveled'])
    print(mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Frequency of Usage Based on User Types :")
    Typecount = df['User Type'].value_counts()
    print(Typecount)
    print('\n')

    # TO DO: Display counts of gender
    print("Frequency of Usage Based on Users' Gender Types :")
    Gendercount = df['Gender'].value_counts()
    print(Gendercount)
    print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    Youngest = df['Birth Year'].max()
    Oldest = df['Birth Year'].min()
    Common_Date_of_Birth = df['Birth Year'].value_counts().idxmax()
    print('Most Recent Year of Birth (Youngest):')
    print(Youngest)
    print('Earliest Year of Birth (Oldest):')
    print(Oldest)
    print('Most Common Year of Birth :')
    print(Common_Date_of_Birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        start_loc = 0
        while (view_data != 'no'):
            if (view_data == 'yes'):
                print(df.iloc[start_loc:start_loc+5])
                print('-'*40)
                start_loc += 5
                view_data = input("Do you wish to continue?: ").lower()
            else :
                view_data = input("please type 'yes' or 'no' :").lower()

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
