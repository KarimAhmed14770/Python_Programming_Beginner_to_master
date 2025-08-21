#url means universal resource locator
#ex: https://www.kaggle.com/datasets this is a url
#https is the protocol, whatever is between www. and .com is the domain name
#after the dommain name there is a / whatever is after the slash is the page or query string
#url parsing is u have to take the url and extract theses information
#the url will be given in this format https://www.domain_name.com/page
url=input('Enter the url: ')
protocol=url[:5]
first_dot_index=url.index('.')
second_dot_index=url.rindex('.')
domain=url[first_dot_index+1 : second_dot_index]
com_index=url.index('com')
page=url[com_index+3:]

protocol_string='protocol:'
Domain_string='Domain:'
page_string='page:'

protocol_string=protocol_string.ljust(20)
Domain_string=Domain_string.ljust(20)
page_string=page_string.ljust(20)

print(protocol_string,protocol)
print(Domain_string,domain)
print(page_string,page)
