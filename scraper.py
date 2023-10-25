from datetime import date, timedelta

# https://www.gocomics.com/calvinandhobbes/1985/11/18
# <img class="img-fluid lazyloaded" srcset="https://assets.amuniversal.com/cc713730deb701317193005056a9545d 900w" data-srcset="https://assets.amuniversal.com/cc713730deb701317193005056a9545d 900w" sizes="
#                        (min-width: 992px) 900px,
#                        (min-width: 768px) 600px,
#                        (min-width: 576px) 300px,
#                        900px" width="100%" alt="Calvin and Hobbes Comic Strip for November 18, 1985 " src="https://assets.amuniversal.com/cc713730deb701317193005056a9545d">
# https://assets.amuniversal.com/cc713730deb701317193005056a9545d

base_url = 'https://www.gocomics.com/calvinandhobbes/'

def createDateList():
    # Define the start date (November 18, 1985)
    start_date = date(1985, 11, 18)

    # Get the current date
    end_date = date.today()

    # Create an empty list to store the dates
    date_list = []

    # Generate the dates and add them to the list
    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y/%m/%d'))
        current_date += timedelta(days=1)

    # Print the list of dates or save it to a file
    for date_string in date_list:
        print(date_string)
    return date_list



def createUrlList():
    url_list = []
    date_list = createDateList()
    for date_string in date_list:
        url_list.append(f'{base_url}{date_string}')
    # write url_list to file
    with open('url_list.txt', 'w') as file:
        for url_string in url_list:
            file.write(url_string + '\n')
createUrlList()


