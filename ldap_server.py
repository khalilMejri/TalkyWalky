import ldap
import hashlib
import sys
from base64 import b64encode


class LdapService():

    ldap_server = "ldap://192.168.56.3:389"  # host address
    ldap_ou = "security"  # organization unit
    ldap_group = "security-group"  # organization sub-group

    # admin domain
    LDAP_ADMIN_DN = "cn=admin,dc=insat,dc=tn"
    LDAP_ADMIN_PWD = ""

    def __init__(self, admin_pwd):
        self.LDAP_ADMIN_PWD = admin_pwd

    def login(self, username, password):
        self.username = username
        self.password = password

        # the following is the user_dn format provided by the ldap server

        # organization user's domain
        user_dn = "cn=" + self.username + ",cn=" + self.ldap_group + ",ou=" + \
            self.ldap_ou + ",dc=insat,dc=tn"

        print(user_dn)

        # base domain
        LDAP_BASE_DN = "cn=" + self.ldap_group + \
            ",ou=" + self.ldap_ou + ",dc=insat,dc=tn"

        # start connection
        ldap_client = ldap.initialize(self.ldap_server)
        # search for specific user
        search_filter = "cn=" + self.username

        try:
            # if authentication successful, get the full user data
            ldap_client.bind_s(user_dn, self.password)
            result = ldap_client.search_s(
                LDAP_BASE_DN, ldap.SCOPE_SUBTREE, search_filter)

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

    def register(self, user):

        # base domain
        LDAP_BASE_DN = "cn=" + self.ldap_group + \
            ",ou=" + self.ldap_ou + ",dc=insat,dc=tn"
        # home base
        HOME_BASE = "/home/users"

        # new user domain
        dn = 'cn=' + user['username'] + ',' + LDAP_BASE_DN
        home_dir = HOME_BASE + '/' + user['username']
        gid = user['group_id']

        # encoding password using md5 hash function
        hashed_pwd = hashlib.md5(user['password'].encode("UTF-8"))

        # printing the equivalent byte value.
        # print("The byte equivalent of hash is : ", end="")
        # print(result.hexdigest())

        entry = []
        entry.extend([
            ('objectClass', [b'inetOrgPerson',
                             b'posixAccount', b'top']),
            ('uid', user['username'].encode("UTF-8")),
            ('givenname', user['username'].encode("UTF-8")),
            ('sn', user['username'].encode("UTF-8")),
            ('mail', user['email'].encode("UTF-8")),
            ('uidNumber', user['uid'].encode("UTF-8")),
            ('gidNumber', str(gid).encode("UTF-8")),
            ('loginShell', [b'/bin/sh']),
            ('homeDirectory', home_dir.encode("UTF-8")),
            ('userPassword', [b'{md5}' +
                              b64encode(hashed_pwd.digest())])

        ])

        # connect to host with admin
        ldap_conn = ldap.initialize(self.ldap_server)
        ldap_conn.simple_bind_s(self.LDAP_ADMIN_DN, self.LDAP_ADMIN_PWD)

        try:
            # add entry in the directory
            ldap_conn.add_s(dn, entry)
            print("success")
            return None
        except Exception:
            return sys.exc_info()[0]

        finally:
            # disconnect and free memory
            ldap_conn.unbind_s()

# TESTING CONNECTION, also IGNORE the ERRORS since there's NO ERROR,
# dunno why they are being thrown,
# the attributes DO EXIST in ldap module and I VERIFIED it!
# CONNECTION WILL ONLY WORK WHEN MY SERVER IS UP


# # test case
# TODO change admin password
s = LdapService(admin_pwd="<ur_admin_pwd>")

# test login
# s.login(username="hamma", password="0000")

# test registration
user_obj = {
    'username': 'guest',
    'password': '0000',
    'email': 'u@gmail.com',
    'gender': 'male',
    'group_id': 500,  # default gid
    'uid': '1600222'  # student card
}
# s.register(user_obj)
