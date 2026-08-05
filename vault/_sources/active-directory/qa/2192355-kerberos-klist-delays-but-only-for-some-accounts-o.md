---
title: "Kerberos klist delays but only for some accounts (on Cisco AnyConnect VPN)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2192355/kerberos-klist-delays-but-only-for-some-accounts-o
question_id: 2192355
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Kerberos klist delays but only for some accounts (on Cisco AnyConnect VPN)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2192355/kerberos-klist-delays-but-only-for-some-accounts-o (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

While connected to a Cisco AnyConnect VPN session on my laptop from home to the workplace, I note the following behaviour for some accounts.

ADDS related TCP/UDP ports are open/listening 135 RPC, 389 LDAP, 88 Kerberos, 123 NTP, LDAPS 636, GC 3268,3269, SMB 445 etc  

Firewall is on no dropped packets.  

Example 1:

If an active directory account has a DitinguishedName attribute like: 

CN=TestAccount   

klist immediately shows me tickets 

I can browse / access windows server shares   

setspn -L TestAccount 

Registered ServicePrincipalNames for CN=TestAccount ,CN=Users,DC=domain,DC=com:

Example 2: 

However, If another active directory account has a DistinguishedName attribute like: 

CN=Smith, John

klist hangs   

I cannot perform net view \dc etc  

System Event log reports:  

KDC_ERR_S_PRINCIPAL_UNKNOWN   

setspn -L jsmith 

Ldap Error(0x22 -- Invalid DN Syntax): ldap_search_s  

Has anyone come across this behaviour and how to remediate?   

Thank you!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-14*

Thanks Neuvi for the reply.  

The behaviour only seems to occur on some accounts, not all.  

Tuesday 15/10/24 Update:  

I deleted my user profile on the laptop, and Windows 10 re-created the profile when I logged back in.   

That seems to have helped, there is now a klist delay of 5 - 10 minutes before I have session tickets and can perform net view \dc1 etc  

I have also updated the Cisco AnyConnect Client to 5.1.4.74  

Currently working with our ISP to resolve the 0x7  KDC_ERR_S_PRINCIPAL_UNKNOWN as its the Server/Target names point the them.  

A Kerberos error message was received:

 on logon session 

 Client Time: 

 Server Time: 9:24:14.0000 10/14/2024 Z

 Error Code: 0x7  KDC_ERR_S_PRINCIPAL_UNKNOWN

 Extended Error: 

 Client Realm: 

 Client Name: 

 Server Realm: f.q.d.n  

 Server Name: DNS/ns1.f.q.d

 Target Name: DNS/ns1.f.q.d@f.q.d.n

 Error Text: 

 File: onecore\ds\security\protocols\kerberos\client2\kerbtick.cxx

 Line: 12fa

 Error Data is in record data.  

Monday 15/10/24  

As a test, I created 2 new accounts in ADDS ADUC:  

DistinguishedName CN=Paul, Steven,OU=ICT,OU=Users and Computers, DC=work,C=place,DC=au  

user login name: stevenp  

user login name (pre- windows 2000), stevenp  

Display Name: Paul, Steven  

DistinguishedName CN=sphar,OU=ICT,OU=Users and Computers, DC=work,C=place,DC=au  

user login name: sphar  

user login name (pre- windows 2000), sphar  

Display Name:  sphar

My existing account (where I note klist, net view \dc1 hanging):  

CN=Harris,Steven,OU=ICT,OU=Users and Computers, DC=work,C=place,DC=au  

DistinguishedName user login name: steve.harris  

user login name (pre- windows 2000), stevenh  

Display Name:  Harris, Steven

I logged into the laptop with each of the accounts while on the domain/wired network to cache the credentials.  

I then disconnected and performed a klist purge for each account.  

At home on the laptop, I login as stevenp, connected to the wireless network, the Cisco AnyConnect client connected me to the corporate network.  

tnc tcp 135, 389, 636, 3268, 3269, 139, 88, 445, 464 all return tcp success  

portqry 123, 464 all listening  

klist grants tickets and I can perform net view \dc1   

Same result for sphar  

Yet when I login using on my own domain account with cached credentials (my account was created over 5 years ago), I note hanging behaviour for:  

klist   

 net view \dc1  

I have compared the AD attribute properties but cant note anything that would cause the hanging with my account  

Get-ADUser <username> -properties * | select * | Export-Csv -Path "C:\admin&lt;user>.csv" -NoTypeInformation   

Any suggestions most welcome.  

Steve

## Answer (community) — community member

*upvotes: 0 · updated: 2024-10-14*

Hi sphar,

Thank you for posting in the Microsoft Community Forums.

The DistinguishedName attribute is authenticated with Kerberos:

Each user object in Active Directory has a unique DistinguishedName (DN), which defines the object's location in the directory structure.

Kerberos authentication relies on ServicePrincipalNames (SPNs) to identify service instances.SPNs are typically associated with the DN of an account.

If the DN contains special characters (e.g., commas, spaces, etc.), this may interfere with the Kerberos authentication process because the registration and parsing of the SPNs may not be able to handle these characters correctly.

Question about CN=Smith, John:

In LDAP and Kerberos, commas (,) in DNs are typically used to separate different components (e.g., organizational units, containers, etc.). If the DN contains a comma, and that comma is not used to separate components, it may need to be escaped (e.g., by using ,).

In your example, the comma in CN=Smith, John is escaped. However, this may cause problems when parsing DNs in some cases (e.g., Kerberos authentication).

The KDC_ERR_S_PRINCIPAL_UNKNOWN error indicates that the Kerberos Key Distribution Center (KDC) was unable to find the account associated with the requested Service Principal Name (SPN). This could be because the SPN is not properly registered, or the DN is not properly resolved.

Solution:

Check and correct the DN: Ensure that all Active Directory accounts have the correct DN and do not contain any special characters that could cause parsing issues. If special characters are used, make sure they are properly escaped.

Re-register SPNs: For accounts that are experiencing problems, try manually deleting and re-registering the SPNs. this can be accomplished by deleting the existing SPNs using the setspn -D command and then re-registering them using the setspn -A command.

Check firewall and network settings: Ensure that all necessary ports (e.g. 88 for Kerberos, 445 for SMB) are correctly open on the VPN connection and that there are no firewall rules blocking communication on these ports.

Best regards

Neuvi
