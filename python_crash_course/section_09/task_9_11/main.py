'''
Module import.
'''

from accounts import Admin

if __name__ == '__main__':
    admin: Admin = Admin('Koby', 'Fisher')
    admin.privileges.show_privileges()
    admin.privileges.change_privileges(('remove user', 'display daily report'))
    admin.privileges.show_privileges()
