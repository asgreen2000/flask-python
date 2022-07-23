from http import server
from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError
from numpy import true_divide
from .models import *

# ldap login
def ldap_login(user: LdapUser) -> bool:

    username = user.get_username()
    password = user.get_password()
    try:
        server = Server('ipa.demo1.freeipa.org',  get_info=ALL)
        conn = Connection(server, 'uid=%s,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org' % username, password=password, auto_bind=True)
        result = conn.search('dc=demo1,dc=freeipa,dc=org', '(&(objectclass=person)(uid=%s))' % username, attributes=['sn', 'krbLastPwdChange', 'objectclass'])
        if conn.result['description'] == 'success':
            return True
        else:
            return False
    except LDAPException as e:
        return False

   
    