import ldap


class LdapLogin():
    def __init__(self, username="joe", password="joe"):
        self.username = username
        self.password = password

    def login(self):
        ldap_server = "ldap://192.168.2.115:389"

        # the following is the user_dn format provided by the ldap server
        user_dn = "cn="+self.username+",cn=users,dc=chatroom,dc=local"

        base_dn = "cn=users,dc=chatroom,dc=local"

        ldap_client = ldap.initialize(ldap_server)
        search_filter = "cn="+self.username
        try:
            # if authentication successful, get the full user data
            ldap_client.bind_s(user_dn, self.password)
            result = ldap_client.search_s(
                base_dn, ldap.SCOPE_SUBTREE, search_filter)

            # return all user data results
            ldap_client.unbind_s()
            print(result)
        except ldap.INVALID_CREDENTIALS:
            ldap_client.unbind()
            print("Wrong username or password..")
        except ldap.SERVER_DOWN:
            print("Server is down at the moment, please try again later!")
        except ldap.LDAPError:
            ldap_client.unbind_s()
            print("authentication error!")

# TESTING CONNECTION, also IGNORE the ERRORS since there's NO ERROR, dunno why they are being thrown, the attributes DO EXIST in ldap module and I VERIFIED it!
# CONNECTION WILL ONLY WORK WHEN MY SERVER IS UP


log = LdapLogin()
log.login()
