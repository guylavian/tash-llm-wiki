---
title: "Active Directory with various objects accidentally locked with userAccountControl=514 - how to recover?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/390829/active-directory-with-various-objects-accidentally
question_id: 390829
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory with various objects accidentally locked with userAccountControl=514 - how to recover?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/390829/active-directory-with-various-objects-accidentally (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This happened as an accident in our sandbox environment so no harm was done. I can also always just delete everything and install anew. But I take it as a learning opportunity, so I wonder if anyone knows a way out of this...  

I am up for any kind of witchery. :)  

We have two DCs in our AD domain `domain.tld` and we use LDAP interface to manage accounts in the directory tree. By accident, we ran a batch job from external application that took every object in the AD resembling an user and set its `userAccountControl` to `514` (locked).  

The LDAP base for operation was `dc=domain,dc=tld` with subtree scope -> effectively: every object in the AD.  

I suspect (do not know for sure) the filter for recognizing objects was `objectclass=person`.  

The operation was run under `Administrator` user.  

First problem we discovered was that logging to `Administrator` no longer worked. No wonder here, the account was blocked.  

I booted into safe mode, ran `net user Administrator /active:yes` to unlock the account and rebooted.  

(On the second try, I also added `net user Administrator *` and set a new password. This did not make a difference in what happened next.)  

On the login screen, when I tried to log under `Administrator`, I logged in with his correct password. The system asked for new password and it seems it successfully changed it.  

Upon next login attempt (with freshly-set password), this message pops out:  

`The security database on the server does not have a computer account for this workstation trust.`  

However, when the password is incorrect, the system rightly complains that `Username or password is invalid.` (or whatever the message is). When I provide correct password, I face the `The security database on the server does not have a computer account for this workstation trust.`.  

I also found some other admin account that was in the AD and results are the same, so this does not affect only the `Administrator`.  

I suspect this has something to do with `computer` entry of the DC inside the directory tree. If this entry is also locked with `userAccountControl=514`... is that possible?  

Or could it be something else?  

How to diagnose and recover?  

Win 2k12 R2, Active Directory with Certificate Services. Clean install with defaults, no GPOs or whatnot.  

(Also, no backups available because sandbox. Only thing I have is a virtual machine snapshot of the broken domain, working safe mode, and installation DVD of Windows.)  

Thanks for the ideas. :))

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-17*

Hello @Petr Fiser  ,    

Thank you for your update.    

Is this AD environment a production environment？    

"userAccountControl=514" means the account is disabled.    

Use the UserAccountControl flags to manipulate user account properties    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/useraccountcontrol-manipulate-account-properties    

If it is a production environment and you do not have any backup. I suggest you submit a service request to MS Professional tech support service so that a dedicated support professional can further assist you with this request.     

The following web site for more detail of Professional Support Options.    

https://support.microsoft.com/en-in/gp/contactus81?forceorigin=esmc&Audience=Commercial    

https://support.microsoft.com/en-us/help/4051701/global-customer-service-phone-numbers    

Thanks for your understanding and support.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-12*

Hello @Petr Fiser  ,

Thank you for posting here.

Do you have the same issue (tried to log DC with domain Administrator credential and receive the error message above) on both DCs?

We can check on the problematic DC:  

1.Run command to check the secure channel: NETDOM VERIFY computer_name  

2.Run command to RESET the secure channel:

Netdom resetpwd /s:<target_server> /ud:mydomain\domain_admin /pd:*

/s:<server> is the name of the domain controller to use for setting the machine account password. It's the server where the KDC is running.

/ud:<domain\User> is the user account that makes the connection with the domain you specified in the /s parameter. It must be in domain\User format. If this parameter is omitted, the current user account is used.

/pd:* specifies the password of the user account that is specified in the /ud parameter. Use an asterisk (*) to be prompted for the password. For example, the local domain controller computer is Server1 and the peer Windows domain controller is Server2. If you run Netdom.exe on Server1 with the following parameters, the password is changed locally and is simultaneously written on Server2.  

And replication propagates the change to other domain controllers:

netdom resetpwd /s:server2 /ud:mydomain\administrator /pd:*

In your case, you have two DCs, I assume one is DC1(if it is also PDC) and the other is DC2.

If you run command on DC1, you can run:  

Netdom resetpwd /s:DC2 /ud:mydomain\domain_admin /pd:*

If you run command on DC2, you can run:  

NETDOM VERIFY DC2  

Netdom resetpwd /s:DC1 /ud:mydomain\domain_admin /pd:*

After that, check if it helps.

Reference  

https://learn.microsoft.com/en-us/troubleshoot/windows-server/windows-security/use-netdom-reset-domain-controller-password

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc785478(v=ws.11)

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
