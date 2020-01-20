import ldap


class LdapService():

    ldap_server = "ldap://192.168.56.3:389"  # host address
    ldap_ou = "security"  # organization unit
    ldap_group = "security-group"  # organization sub-group

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):

        # the following is the user_dn format provided by the ldap server

        # admin domain
        # user_dn = "cn=admin,dc=insat,dc=tn"

        # organization user's domain
        user_dn = "cn=" + self.username + ",cn=" + self.ldap_group + ",ou=" + \
            self.ldap_ou + ",dc=insat,dc=tn"

        print(user_dn)

        # base domain
        base_dn = "cn=" + self.ldap_group + ",ou=" + self.ldap_ou + ",dc=insat,dc=tn"

        # start connection
        ldap_client = ldap.initialize(self.ldap_server)
        # search for specific user
        search_filter = "cn=" + self.username

        try:
            # if authentication successful, get the full user data
            ldap_client.bind_s(user_dn, self.password)
            result = ldap_client.search_s(
                base_dn, ldap.SCOPE_SUBTREE, search_filter)

            # return all user data results
            ldap_client.unbind_s()
            print(result)
            return None
        except ldap.INVALID_CREDENTIALS:
            ldap_client.unbind()
            print("Wrong username or password..")
            return "Wrong username or password.."
        except ldap.SERVER_DOWN:
            print("Server is down at the moment, please try again later!")
            return "Server is down at the moment, please try again later!"
        except ldap.LDAPError:
            ldap_client.unbind_s()
            print("Authentication error!")
            return "Authentication error!"

    def register(self):

        # custom user domain
        m_user_dn = "cn=" + self.username + ",dc=insat,dc=tn"


# TESTING CONNECTION, also IGNORE the ERRORS since there's NO ERROR,
# dunno why they are being thrown,
# the attributes DO EXIST in ldap module and I VERIFIED it!
# CONNECTION WILL ONLY WORK WHEN MY SERVER IS UP


# # test case
# s = LdapService(username="guest", password="0000")
# s.login()
# s.register()
