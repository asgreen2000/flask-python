import ldap3

from .models.LdapUser import LdapUser

# ldap login
def ldap_login(user: LdapUser) -> bool:
    username = user.get_username()
    password = user.get_password()
    lg_server = 'ldap://ldap.example.com'
    ld = ldap3.Server(lg_server, port=389, use_ssl=False)
    lg_conn = ldap3.Connection(ld, auto_bind=True, client_strategy=ldap3.STRATEGY_SYNC)
    lg_conn.search(search_base='dc=example,dc=com', search_filter='(uid=%s)' % username, attributes=['uid'])
    if lg_conn.response:
        lg_conn.bind(username, password)
        if lg_conn.bound:
            return True
        else:
            return False
    else:
        return False
        