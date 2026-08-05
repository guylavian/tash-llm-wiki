---
title: "Issue in accessing of OWA after migrating of mailbox from Exchange Server 2010 to Exchange Server 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/251542/issue-in-accessing-of-owa-after-migrating-of-mailb
question_id: 251542
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue in accessing of OWA after migrating of mailbox from Exchange Server 2010 to Exchange Server 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/251542/issue-in-accessing-of-owa-after-migrating-of-mailb (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, Good Day! May I ask your assistance please in our issue in accessing of OWA. After migrating the mailbox user from Exchange Server 2010 to Exchange Server 2013, the OWA is not accessible. Please see attached file for the reference. ![62013-issue.jpg][1] [1]: /api/attachments/62013-issue.jpg?platform=QnA Thanks, Raymond

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-16*

Hi Lou,  

Good Day!  

This is noted.  

I will run this command and provide you the result.  

Thanks,  

Raymond

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-18*

Hi Lou,  

Good Day!  

Sorry for the late response. Both Exchange Server 2010 and Exchange Server 2013 users are now able to access the OWA.  

May I ask if there is an impact if I edit the Default Frontend Mail Receive Connectors and added the Exchange Users in the Permission Groups?   

Thanks,  

Raymond

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-02-01*

Hi Zheng,  

Good Day!  

I can access the OWA using the local (Hostname or IP Address) but when I access the OWA using the FQDN (Ex. mail.contoso.com), I can't log in the users that already migrated from Exchange Server 2010 to Exchange Server 2013.  

As of the moment, we will not decommission the Exchange Server 2010 until we fully migrated the mailboxes from Exchange server 2010 to Exchange Server 2013.  

Thanks,  

Raymond

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-02-01*

Hi anonymous user ,    

Thanks for your post!    

Have you followed the Exchange Deployment Assistant to configure internal/external URLs and DNS records?    

Are you still using the coexistence environment(2010 and 2013)? If so, are you trying to login to 2010 OWA with 2013 accounts?     

In this case, there may be some problems with the redirection. Exchange Server 2013 or Exchange Server 2016 redirects to Exchange 2010 for OWA, Outlook on the web, and ECP    

Also, you can try to create a new mailbox and test if he could login to OWA.    

If you met this issue after you have uninstalled the Exchange 2010 and login to 2013 OWA with these accounts. I think you could check the URL of OWA virtual directory:    

```
Get-OWAVirtualDirectory | FL server,Name,*URL*, *auth*
```

     

Make sure the URLs are pointing to Exchange 2013. And internal auth methods are Basic and Fba by default.    

Or you can recreate it by :    

- 	Remove-OWAVirtualDirectory -Identity “owa (Default Web Site)”    

- 	New-OWAVirtualDirectory -externalurl "server.domain.com/owa" -internalurl "server.domain.com/owa" -Server EX2013    

- 	Remove-ECPVirtualDirectory -Identity “ecp (Default Web Site)”    

- 	New-ECPVirtualDirectory -externalurl "server.domain.com/ecp" -internalurl "server.domain.com/ecp" -Server EX2013    

- 	Reset IIS.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
