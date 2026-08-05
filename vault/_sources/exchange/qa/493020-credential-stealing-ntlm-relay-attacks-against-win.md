---
title: "credential-stealing NTLM relay attacks against Windows domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/493020/credential-stealing-ntlm-relay-attacks-against-win
question_id: 493020
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# credential-stealing NTLM relay attacks against Windows domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/493020/credential-stealing-ntlm-relay-attacks-against-win (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I read the article https://www.techrepublic.com/article/microsoft-warns-of-credential-stealing-ntlm-relay-attacks-against-windows-domain-controllers/?ftag=TREee10240&bhid=28346840912463073390773750156554&mid=13452373&cid=2165475782  regarding the warning and the recommendation to set the NTLM setting to Deny all.  Unfortunately, as soon as I did this, users cannot access the Outlook client on their PCs.  Outlook webmail is working at this time.  

As recommended I set the Network Security: Restrict NTLM: Audit NTLM authentication in this domain policy setting, and then review the Operational log to understand what authentication attempts are made to the member servers.   

I also set the Network security: Restrict NTLM: Add server exceptions in this domain policy and added the domain controller and exchange server.  

However, even after I undid the setting and changed it back to the original of Not defined in the Group Policy setting staff cannot log into the Outlook client?  I see Event 4004 in the Applications and Services Log\Microsoft\Windows\NTLM event log but if I simply undid the change wouldn't it revert back to the previous working condition?  

How do I correct this?  

I need help.  

Thanks,  

Roger

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-30*

Hello @vallee2018  ,    

Thank you for your update.    

I reviewed the link you provided again, it is recommended you can disable NTLM authentication where possible.    

Meanwhile, the gpo setting is "Network security: Restrict NTLM: NTLM authentication in this domain" instead of "Restrict NTLM Audit NTLM authentication in this domain policy setting" you mentioned.    

So you should change "Restrict NTLM Audit NTLM authentication in this domain policy setting" to "Disabled" first. This is to revoke this setting and cannot be set to any other value.     

After that, you should evaluate whether you can disable NTLM authentication in your environment.     

If you can disable NTLM authentication in your environment. You can disable it as below.    

    

If you cannot disable NTLM authentication in your environment, you can also select other options.    

For more information, please refer to link below.    

KB5005413: Mitigating NTLM Relay Attacks on Active Directory Certificate Services (AD CS)    

https://support.microsoft.com/en-us/topic/kb5005413-mitigating-ntlm-relay-attacks-on-active-directory-certificate-services-ad-cs-3612b773-4043-4aa9-b23d-b87910cd3429    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-29*

Hello Daisy,    

Thank you for the reply.  Unfortunately, this doesn't help to address the main concern when following the recommendations in:    

[https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-ntlm-authentication-in-this-domain?]     

.  Selecting any of the deny options results in staff not being able to log into their desktop Outlook Client.      

The document states if choosing the  Deny all setting:    

"The domain controller will deny all NTLM pass-through authentication requests from its servers and for its accounts and return an NTLM blocked error unless the server name is on the exception list in the Network security: Restrict NTLM: Add server exceptions in this domain policy setting."  Is this saying I need to add the FQDN of the Exchange server or the domain controller in the exception list ?     

If so, I had added both servers to the exception list.  Unfortunately, soon after selecting the Deny all setting, staff could no longer access the desktop Outlook client.    What do I need to do to set the setting to Deny and enable normal access of the desktop Outlook client?    

Thanks

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-29*

Hello @vallee2018  ,    

Thank you for posting here.    

Because you configured Security Policy setting, for Security Policy setting, there is persistence of security settings policy based on the second link below.    

    

Because the default policy setting is "Not Defined". There is no any default "value" in a local database on any of your computers if nobody sets this policy setting.    

    

Based on the knowledge, when it is configured as one value via Group Policy Management on DC, the member servers or domain clients will take such settings, and even if it is configured as "Not Defined" from the previous value again, the member servers or domain clients will keep the previous value of this policy setting.    

So you need to configured it as "Disabled".    

For more information, please refer to links below.    

Network security: Restrict NTLM: Audit NTLM authentication in this domain    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-restrict-ntlm-audit-ntlm-authentication-in-this-domain    

Security policy settings    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/security-policy-settings#persistence-of-security-settings-policy    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.
