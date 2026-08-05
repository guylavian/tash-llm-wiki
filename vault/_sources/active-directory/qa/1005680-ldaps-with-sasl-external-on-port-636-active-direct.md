---
title: "LDAPS with SASL External on port 636: Active Directory errors out with LdapErr: DSID-0C0905F0"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1005680/ldaps-with-sasl-external-on-port-636-active-direct
question_id: 1005680
fetched: 2026-07-25
answer_count: 8
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# LDAPS with SASL External on port 636: Active Directory errors out with LdapErr: DSID-0C0905F0

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1005680/ldaps-with-sasl-external-on-port-636-active-direct (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have been trying to configure SASL External over LDAPS (Port 636). Below things are already in place.  

-  Have enforced the LDAP (aka AD server 2019) for LDAP signing and Binding via Domain Controllers Group Policy.  

-  Have a User Certificate issued by its Enterprise CA configured with User DN (cn=testuser,cn=users,dc=dummydomain,dc=test) in Subject and SAN (cn=testuser,cn=users,dc=dummydomain,dc=test), SAN also includes the UPN (******@dummydomain.test) and the certificates are uploaded to active directory. The certificate extension uses Client Authentication  

-  Client and the server are trusting the CA which have issued the cert for the LDAPS server certificate and the User certificate  

-  Have a linux server in place with OpenLDAP client installed.

The .ldaprc has the below settings:  

TLS_REQCERT hard  

TLS_CACERT /etc/openldap/cacerts/caroot.pem  

TLS_CERT /etc/openldap/certs/usercert.pem  

TLS_KEY /etc/openldap/certs/private.key  

SASL_MECH external  

TLS_PROTOCOL_MIN 1.2

Below works successfully on port 389 with LDAP (START-TLS):  

Command:  

ldapwhoami -Y EXTERNAL -H ldap://server.dummydomain.test -Z  

Results of above command:  

SASL/EXTERNAL authentication started  

SASL username: cn=testuser,cn=users,dc=dummydomain,dc=test  

SASL SSF: 0  

u:DUMMYDOMAIN\testuser

Using the same with LDAPS on port 636 doesn't work at all and gives the below error.  

Command:  

ldapwhoami -Y EXTERNAL -H ldaps://server.dummydomain.test  

Results of above command:  

SASL/EXTERNAL authentication started  

ldap_sasl_interactive_bind_s: Authentication method not supported (7)  

additional info: 00002027: LdapErr: DSID-0C0905F0, comment: Invalid Authentication method, data 0, v4563

Have searched with DSID for any references on error and I was not able to find any resolution or references on the same.  

I wonder what is the difference and why SASL-EXTERNAL works fine on port 389 with START-TLS and refuses to work on port 636 with the error stated above.

The debug logs also don't provide much information:  

*host: server.dummydomain.test port: 636 (default)  

refcnt: 2 status: Connected  

last used: Tue Sep 13 11:14:09 2022  

ld 0x55c987e4e3c0 Outstanding Requests:  

msgid 1, origid 1, status InProgress  

outstanding referrals 0, parent count 0  

ld 0x55c987e4e3c0 request count 1 (abandoned 0)  

** ld 0x55c987e4e3c0 Response Queue:  

Empty  

ld 0x55c987e4e3c0 response count 0  

ldap_chkResponseList ld 0x55c987e4e3c0 msgid 1 all 1  

ldap_chkResponseList returns ld 0x55c987e4e3c0 NULL  

ldap_int_select  

read1msg: ld 0x55c987e4e3c0 msgid 1 all 1  

ber_get_next  

ber_get_next: tag 0x30 len 104 contents:  

read1msg: ld 0x55c987e4e3c0 msgid 1 message type bind  

ber_scanf fmt ({eAA) ber:  

read1msg: ld 0x55c987e4e3c0 0 new referrals  

read1msg: mark request completed, ld 0x55c987e4e3c0 msgid 1  

request done: ld 0x55c987e4e3c0 msgid 1  

res_errno: 7, res_error: <00002027: LdapErr: DSID-0C0905F0, comment: Invalid Authentication method, data 0, v4563>, res_matched: <>  

ldap_free_request (origid 1, msgid 1)  

ldap_int_sasl_bind: EXTERNAL  

ldap_parse_sasl_bind_result  

ber_scanf fmt ({eAA) ber:  

ldap_parse_result  

ber_scanf fmt ({iAA) ber:  

ber_scanf fmt (}) ber:  

ldap_msgfree  

ldap_err2string  

ldap_sasl_interactive_bind_s: Authentication method not supported (7)  

additional info: 00002027: LdapErr: DSID-0C0905F0, comment: Invalid Authentication method, data 0, v4563  

ldap_free_connection 1 1  

ldap_send_unbind  

ber_flush2: 7 bytes to sd 3  

TLS trace: SSL3 alert write:warning:close notify  

ldap_free_connection: actually freed*

Any help on getting this worked is much appreciated. Thanks in anticipation.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-14*

Hello David,    

Would you be prepared to share trace data from the AD server? If the "test" like names in the information you have post are accurate, then this should not be a problem.    

I still need to work out what tracing would be most helpful for this scenario (I have never used SASL EXTERNAL authentication), so that might take a while...    

Interesting to see that @Gary Reynolds   has posted a correction to his first post - we two Garys seem to share several troubleshooting characteristics: I wanted to post a correction to my first post too. Gary was correct with the error code: CRYPT_E_NO_VERIFY_USAGE_DLL is the symbolic name for the error code decimal 2027; because it seemed vaguely relevant to the problem (and perhaps because there was no leading "0x"), I did not notice the number base error :-(    

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-14*

@Gary Reynolds    @Gary Nebbett       

The TLS handshake is done and the server cert and client cert is also verified.     

I had not posted the above verbose lines as it would be a lot of information to look at. Have attached the working START-TLS (Port-389 LDAP - 240873-ldaps-start-tls-389-debug-working.txt) debug logs and aswell as the non-working one for comparison (Port-636 LDAPS - 240829-ldaps-tls-636-debug-failure.txt).     

The certificate seems to be fine as I'm using the same certificate with START-TLS on port 389 and it works 100% fine without any errors and also LDAP bind is successful with the user certificate.     

The only issue is with using port 636 (This is TLS/SSL).     

The main purpose here is to test Certificate based authentication with Mutual Auth which works as expected with LDAP START-TLS. So, having to set TLS_REQCERT never is not an option.     

However as per you suggestion I have given a try with the configs but the result is the same.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-13*

Hi,    

The 00002027 is the hex Windows Error code, which doesn't provide any additional information    

```
Hex: 0x00002027 	Int: 8231  
Severity Code: 00,	Source Facility: NULL,	Error Code: Hex: 0x2027 Int: 8231  
  
(8231) The requested authentication method is not supported by the server.
```

I would also try changing the TLS_REQCERT option to never, and also reduce TLS_PROTOCOL_MIN 1.2 to 1.0.  While the LDAP connection and Start_TLS option worked, I can't find any details on the behavior when TLS encryption is started and if the server certificate is verified.  So you might have a certificate configuration issues.    

I'm not familiar with the OpenLDAP client but is there an option to do an ldap_bind as a separate operation which might help identify the authentication issue.    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-13*

Hello David,    

The DSID information encodes the directory, file and line number of the source code file where the problem was reported (the vNNNN number encodes the build of the software). This information will vary with different builds of the server, so it is not a good "identifier" when used to search for similar problems.    

The error code 00002027 has the symbolic name CRYPT_E_NO_VERIFY_USAGE_DLL.    

Does adding a "-v" option to ldapwhoami reveal any more information?    

Would you be prepared to share trace data created on the LDAP/AD server?    

Gary
