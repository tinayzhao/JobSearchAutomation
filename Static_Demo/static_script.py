from remotework import *

#Test Requests and Beautiful Soup

webpage = get_webpage("https://weworkremotely.com/categories/remote-programming-jobs")

#Prints Request object
#print(webpage)

#prints content of the Request object (HTML code of the website requested)
#print(webpage.content)

data = get_data(webpage, 'company', 'title')

#prints data in final format
#print(data)
