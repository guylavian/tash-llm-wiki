---
title: "Domain Transformation - Impact on Kerberos keytab Files"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/435088/domain-transformation-impact-on-kerberos-keytab-fi
question_id: 435088
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Domain Transformation - Impact on Kerberos keytab Files

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/435088/domain-transformation-impact-on-kerberos-keytab-fi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I'm conduction a domain transformation from a Windows Server 2008R2 Domain Controller infrastructure to Windows Server 2016 Domain Controllers.  

At a very, very, high level the process will be  

-  Build new Win Svr 2016 servers, add them to the domain, and promote them to DC's  

-  Transfer the FSMO roles from the 2008R2 DC's to the 2016 DC's  

-  Demote the 2008R2 DC's  

-  Raise the Domain/Forrest Functional Level to Server 2016  

One of our stake holders has asked  

-  How this will this impact Kerberos keytab files?  

-  How will Kerberos be impacted?  

-  Will there be any impact to live services using Kerberos keytab files to authenticate?  

-  Will the Kerberos keytab files still be valid after decommissioning the 2008R2 DC's?  

I'm struggling to find any documentation, that covers my scenario, to help me answer this.  

Can anyone please advise?  

Thanks,

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-17*

Hi,  

I am glad to hear that your issue was successfully resolved. If there is anything else we can do for you, please feel free to post in the forum.  

Best Regards,  

Vicky

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-06-16*

Hi Gary,  

Thanks, I think I get it now.  

The keytab file only needs updating if the relating accounts password changes.  

The risk in my senario is if the Kerberos config files are pointing at a particular 2008R2 DC.  These config files should be pointing at the domain, so the risk should be minimal.    

Does this sound correct?  

Presumably I could get around any rouge config files pointing at my legacy 2008R2 DCs by using a CNAME record to repoint to the incoming 2016 DC's.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-06-16*

Hello Andrew,  

I don't think that re-issuing keytab files is the "safest" approach - it might actually be a "risky" approach.  

The goal of "ktpass" and keytab files is to make password/secret information present in AD available to systems that don't use AD. Ktpass can't read this information from AD but, given the plaintext password, it can generate the required hashed password values. Since the plaintext password for the account is only needed when generating a keytab file, its value is often forgotten.  

If you don't know the password for the account, then one can use the ktpass +setpass option to set a new password in AD and use the same plaintext password to generate a new keytab file. Obviously, the new keytab file would need to be distributed immediately to the affected system.  

If you do know the password and accidently specify +setpass then the key version number will be updated in AD (even if the password hash is not changed) and, again, the a new keytab file (with updated key version number) must be distributed.  

Ktpass has the "/pass +rndpass" option because these passwords are normally "set and forget" values and +rndpass spares you the effort of manually creating a strong password, so I would be surprised if you did know the passwords.  

Gary

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Hi,  

Thank you for posting in our forum.  

Create a user account in the Microsoft Active Directory for the WebSphere Application Server:  

Click Start > Programs > Administrative Tools > Active Directory Users and Computers.  

Use the name for WebSphere Application Server. For example, if the application server you are running on the WebSphere Application Server machine is called myappserver.austin.ibm.com, create a new user in an active directory called myappserver.  

Make sure that you do not have the computer name myappserver under Computers and Domain Controllers. If you already have a computer named myappserver, then you must create a different user account name.  

Click Start > Programs > Administrative Tools > Active Directory Users and Computers > Computers.  

Click Programs > Administrative Tools > Active Directory Users and Computers > Domain Controllers.  

Use the setspn command to map the Kerberos service principal name, <service name>/<fully qualified host name>, to a Microsoft user account.  

The service name for SPNEGO web authentication must be HTTP. However, the service name for Kerberos authentication can be any strings that are allowed by the KDC.  

An example of the setspn command usage for SPNEGO web authentication is as follows:  

reference：https://www.ibm.com/docs/en/was/9.0.5?topic=server-creating-kerberos-service-principal-name-keytab-file  

Tip: This answer contains the content of a third-party website. Microsoft makes no representations about the content of these websites. We provide this content only for your convenience.  

Hope this information can help you  

Best wishes  

Vicky
