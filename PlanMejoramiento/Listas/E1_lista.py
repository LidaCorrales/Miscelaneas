"""Gaddis, T. (2015). Starting out with Python. 
Pearson Educación. https://www-ebooks7-24-com.bdigital.sena.edu.co/?il=7498
Pagina digital: 322 - 323"""

# This program demonstrates the in operator used with a lisst
prod_nums = ['V475', 'F987', 'Q143', 'R688']
search = input('Enter a product number: ')             
if search in prod_nums:
    print(search, 'was found in the list.')    
else:      
    print(search, 'was not found in the list.')