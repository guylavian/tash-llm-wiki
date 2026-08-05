---
title: "How can I get LDAP to work on Windows Server 2019 with internal CA certificate or with comodo certificate"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/384168/how-can-i-get-ldap-to-work-on-windows-server-2019
question_id: 384168
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How can I get LDAP to work on Windows Server 2019 with internal CA certificate or with comodo certificate

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/384168/how-can-i-get-ldap-to-work-on-windows-server-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have spent many months on this issue, but recently on a new Windows Server 2019, I have the same issue:  

I would think that the internal Windows 2019 certificates would be fine for LDAPS, not sure if it is a matter of trust, or a configuration issue. I have looked at many documents on the internet, but none seem to help me get beyon this LDAPS issue. My goal is to use a Windows 2019 ldaps certificate so other applications can authenticate and retrieve ldap data.  

I have installed Windows Server 2019 and I installed the Certification Authority and I see port 389 and 636 in a listen mode, but when I attempt to use port 636 I have errors. Port 389 is fine. When I use the openssl connect command on port 443 I have no errors.  

What I have tried.  

I have spent hours searching for solution that work in www.google.com. This has not worked.  

I have used a JXplorer ldap browser i can login to port 389 and see active directory objects fine, but when I use port 636 it fails immediately with the error "Error opening connection: LDAP connection has been closed". The details on the error are: javax.naming.NamingException: LDAP connect has been closed".  

When I do this command, I get a response as shown below that :  

openssl s_client -connect FicticiousServerName.com:636 -showcerts  

CONNECTED(00000003) depth=0 CN = LAB.FicticiousServerName.com verify error:num=20:unable to get local issuer certificate verify return:1 depth=0 CN = LAB.FicticiousServerName.com verify error:num=21:unable to verify the first certificate verify return:1  

Certificate chain 0 s:/CN=LAB.FicticiousServerName.com i:/DC=com/DC=FicticiousServerName/CN=FicticiousServerName.com  

Use Windows 2019 ldp.exe to test ldap and port 636, IT LOOKS FINE.... :  

How can I use the existing ldap certificate in Windows 2019 and not get errors when  

doing :  

openssl s_client -connect FicticiousServerName.com:636 -showcerts

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-11*

Hello @Robert Perez  ,

Thank you for your reply.

As I understand, now you can only connect using Windows built-in LDP.exe tool, but can not bind and search information.

How many DCs are there in your domain?

You can check one DC that you want to connect, if you have requested a computer certificate using certificate template named ”Domain Controller or Domain Controller Authentication or Kerberos Authentication“ on this DC.

Logon this DC using domain Administrator account.  

Open certlm.msc and click Enter.  

Open Certificates- Local Computer\Personal\Certificates container and check as below.

For example:  

If there is such certificate, you should enroll such a certificate.  

1.Duplicate a Kerberos Authentication certificate template.  

2.Give "Authenticated Users" read permission and give "Domain Controllers" read and enroll permissions.  

3.Issue this certificate template we just duplicated.  

4.Logon this DC using domain Administrator account.

5.Open certlm.msc and click Enter.

6.Right click Certificates- Local Computer\Personal\Certificates container \All Tasks\Request new certificate\Next\Next\select the "Kerberos Authentication" certificate template you just duplicated\click Enroll button.  

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-10*

Hello @Robert Perez  ,    

Thank you for your update.    

I can see the result you provided is OK.    

    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-07*

Daisy,

When I do your step # 6, I see:

Expanding base 'DC=gwlinux,DC=com'...  

ldap_get_next_page_s failed: 1  

Server error: 000004DC: LdapErr: DSID-0C090A5C, comment: In order to perform this operation a successful bind must be completed on the connection., data 0, v4563  

Error 0x4DC The operation being requested was not performed because the user has not been authenticated.  

Result <1>: 000004DC: LdapErr: DSID-0C090A5C, comment: In order to perform this operation a successful bind must be completed on the connection., data 0, v4563  

Getting 0 entries:

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-07*

Daisy,

When I do step # 5 above, the bind, I see :

53 = ldap_set_option(ld, LDAP_OPT_ENCRYPT, 1)  

res = ldap_bind_s(ld, NULL, &NtAuthIdentity, NEGOTIATE (1158)); // v.3  

{NtAuthIdentity: User='NULL'; Pwd=<unavailable>; domain = 'NULL'}  

Error <81>: ldap_bind_s() failed: Server Down.  

Server error: <empty>

Even though when I go to a CMD dos window, and do "whoami"  

I see : gwlinux\administrator

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-06*

Hello @Robert Perez  ,

Thank you for posting here.

In my test lab, I have installed internal CA server.

On one machine, I can connect DC with 636 port and SSL.

For example:

1.On one machine, open ldp.exe and click Enter.

2.Connect PDC.  

3.Connect successfully.  

4.Bind with credential.  

5.Bind successfully.  

6.View information on PDC.  

7.I can see data on PDC successfully.

Tip: I am sorry, we do not know much about openssl command.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
