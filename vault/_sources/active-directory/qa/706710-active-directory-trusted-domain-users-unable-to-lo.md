---
title: "Active Directory Trusted domain users Unable to Login SLES(Linux) server using Winbind"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/706710/active-directory-trusted-domain-users-unable-to-lo
question_id: 706710
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["msc-operations-manager", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory Trusted domain users Unable to Login SLES(Linux) server using Winbind

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/706710/active-directory-trusted-domain-users-unable-to-lo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

There are two domains (Different Active directory-2019 forest), abc.com (Default domain) and xyzde5.com (trusted domain), One way incoming trust to xyzde5.com and outgoing trust from abc.com  

we can login default domain users (abc.com) in the SLES 15 SP2 Clint server(abc.com). , but unable to access trusted domain users (xyzde5.com) from same SLES client server. however we could   

able to login trusted users in the windows client system. only issue in the SLES clients.  

Note: Also we need to user the UUID and GID reflect from active directory only. (With in default domain everything working fine, similar kind of solution looking for trusted domain users)  

Do we need to open any port number from Default domain member SLES to trusted domain xyzde5.com ?  

and any additional configuration need for trusted user login working? please advice on this!  

Thanks in advance!  

We could find the following error message in the winbindd.log  

error message:  

Could not convert sid S-1-5-21-1090010102-1892896508-1865459154-1106: NT_STATUS_NO_SUCH_USER  

above SID matching with trusted domain user.  

Please find the Windind configuration as follows:  

smb.conf`  

```
[global]
workgroup = abc
realm = ABC.COM
usershare allow guests = YES
idmap config * : backend = tdb
idmap config * : range = 5000000-5999999
idmap config  ABC : backend = ad
idmap config  ABC : range = 10-9999
idmap config  ABC : schema_mode = rfc2307
idmap config  ABC : unix_nss_info = yes

idmap config  XYZDE5 : backend = ad
idmap config  XYZDE5 : range = 10000-19999
idmap config  XYZDE5 : schema_mode = rfc2307
idmap config  XYZDE5 : unix_nss_info = yes
kerberos method = secrets and keytab
security = ADS
template homedir = /home/%U
template shell = /bin/bash
winbind offline logon = yes
log file = /var/log/samba/%m.log
log level = 5
vfs objects = acl_xattr
map acl inherit = yes
store dos attributes = yes

winbind use default domain = yes

winbind enum groups = yes
winbind nested groups = no
winbind expand groups = 2
winbind enum users = yes
winbind refresh tickets = yes
winbind separator = +
client use spnego = yes
```

krb5.conf  

```
includedir  /etc/krb5.conf.d
[libdefaults]
default_realm = abc.com
clockskew = 300
[realms]
abc.com = {
    kdc = adserver001.abc.com
    default_domain = abc.com
    admin_server = adserver001.abc.com
}
xyzde5.com = {
    kdc = trustad001.xyzde5.com
    admin_server = trustad001.xyzde5.com
}
[domain_realm]
abc.com = abc.com
.abc.com = abc.com
xyzde5.com = xyzde5.com
.xyzde5.com = xyzde5.com
[appdefaults]
pam = {
    ticket_lifetime = 1d
    renew_lifetime = 1d
    forwardable = true
    proxiable = false
    minimum_uid = 1
}
```

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-28*

Hi there,    

The Below article discusses the required network ports, protocols, and services that are used by Microsoft client and server operating systems, server-based programs, and their subcomponents in the Microsoft Windows Server system. Administrators and support professionals may use this article as a roadmap to determine which ports and protocols Microsoft operating systems and programs require for network connectivity in a segmented network.    

Service overview and network port requirements for Windows    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements    

How to configure a firewall for Active Directory domains and trusts    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/config-firewall-for-ad-domains-and-trusts    

--------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
