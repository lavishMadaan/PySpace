
def display_main_menu(title, options):
    ascii_art='''
 _____        _____                      
|  __ \      / ____|                     
| |__) |   _| (___  _ __   __ _  ___ ___ 
|  ___/ | | |\___ \| '_ \ / _` |/ __/ _ \ 
| |   | |_| |____) | |_) | (_| | (_|  __/
|_|    \__, |_____/| .__/ \__,_|\___\___|
        __/ |      | |                   
       |___/       |_|                   
    '''
    
    print(ascii_art)
    
    # Using the display menu method
    return display_menu(title, options)  
    
def display_menu(title, options):
    ''' The choices should be comma separated string'''
    
    banner(title)
    options = options.split(',')
    
    count = 1
    for option in options:
        print(str(count)+'.'+option)
        count += 1
    choice = input('\nPlease enter your choice: ')
    return choice
        

def banner(title):
    print('--------------------')
    print(title.center(20))
    print('--------------------')
    
