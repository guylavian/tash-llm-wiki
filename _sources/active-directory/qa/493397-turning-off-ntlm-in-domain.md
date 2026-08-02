---
title: "Turning off NTLM in domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/493397/turning-off-ntlm-in-domain
question_id: 493397
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Turning off NTLM in domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/493397/turning-off-ntlm-in-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I've turned on auditing for our domain, it generated man events under the NTLM audit folder but looking at the normal login Audits under the security event viewer it's showing Kerberos.   

Would turning this off mess with the logins of all domain users?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-30*

Hello anonymous user,    

Thank you for your update.    

Q: I just turned on the auditing for NTLM today I'm looking to turn off authentication and want to ensure it doesn't impact logging on to domain resources.    

A: Auditing for NTLM is different from NTLM authentication.    

1-Why do not you want to turn off auditing for NTLM, then you will not see NTLM auditing events??    

2-How did you turn on the auditing for NTLM? What setting did you configure?    

If you want to disable/turn off NTLM authentication, you must ensure NTLM authentication is not used any longer in your entire environment (event ID 4776), otherwise, there will be problems.     

As far as I know, the two commonly used authentication methods are NTLM authentication and Kerberos authentication. They are generally in use.     

From the screenshot you provided, event ID 4624 will log when one logon is successful.    

4624(S): An account was successfully logged on.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624    

And there are several logon types and each logon will be authenticated by NTLM authentication or Kerberos authentication.    

Administrative tools and logon types    

https://learn.microsoft.com/en-us/windows-server/identity/securing-privileged-access/reference-tools-logon-types    

It doesn't necessarily matter between the event ID 4624 with Kerberos and event ID 8002, because they are logged at different times.    

    

Hope the information above is helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-29*

Hello anonymous user,  

Thank you for posting here.  

Hope the information provided by DSPatrick is helpful to you.  

1-Based on the description "it generated man events under the NTLM audit folder", where did you see man events under the NTLM audit folder? Please provide the screenshot if possible.   

2-Are the event IDs 4771 or 4776?  

Note:  

When it is NTLM authentication, it will generate event ID 4776.  

When it is Kerberos authentication, it will generate event ID 4771.  

Q: Would turning this off mess with the logins of all domain users?  

A: Do you mean turn off NTLM authentication or turn off NTLM audit policy setting?  

If you want to turn off NTLM audit policy settings, there will be a little impacts, that is when NTLM authentication is successful or failed, no audit events will logged in Security log under Event Viewer on any DC.  

If you want to turn off NTLM authentication, it may generate important impacts, that is if there is any NTLM authentication, it will fail.   

Hope the information above is helpful.  

Should you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou  

============================================  

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-28*

If you want to disable NTLM I'd suggest following the detailed steps laid out in article here.  

http://woshub.com/disable-ntlm-authentication-windows  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-28*

Thank you I did look through that and then took some screenshots![118801-ntlm1.png][1]![118728-ntlm2.png][2]![118628-ntlm2cont.png][3] of my logs. The First is from the Security logs within the DC the other two are from a NTLM Event. [1]: /api/attachments/118801-ntlm1.png?platform=QnA [2]: /api/attachments/118728-ntlm2.png?platform=QnA [3]: /api/attachments/118628-ntlm2cont.png?platform=QnA Thanks for the speedy reply. ~Mitchell

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-28*

You can follow along here.  

http://woshub.com/disable-ntlm-authentication-windows/  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
