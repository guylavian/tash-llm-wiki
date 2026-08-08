---
title: "Exchange 2016 share calendar with external e-mail address"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/220551/exchange-2016-share-calendar-with-external-e-mail
question_id: 220551
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 share calendar with external e-mail address

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/220551/exchange-2016-share-calendar-with-external-e-mail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Client: Outlook 2016    

Exchange 2016 cu18 (We especially upgraded from CU05 to CU18)    

We like to share someone's calendar with an external e-mail address. No connection with the mailbox of the person who wants to share.    

I follow: https://learn.microsoft.com/en-us/exchange/enable-internet-calendar-publishing-exchange-2013-help    

So values for -calendarenabled is true and proxyurl is https://webmail.domain.be/owa    

Done by executing    

Set-ExchangeServer -Identity "mail server" -InternetWebProxy "https://webmail.domain.be/owa"    

Set-OwaVirtualDirectory -Identity "mail server\owa (Default Web Site)" -ExternalUrl "https://webmail.domain.be/owa" -CalendarEnabled $true    

Also, there is a sharing policy which is active. I have point some mailboxes to use this sharing policy.    

Get-SharingPolicy <policy name> | format-list gives me the info and it is enabled.    

What are the steps to solve this? And is it even possible?    

Thanks for the feedback.    

Kurt    

But it does not work.    

Every time we got:    

Calendar sharing is not available with the following entries because of permission settings on your network.    

Is this related to the exchange server? Or to the firewall? Or to permissions?    

 So I go to step 2.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

Actually the official doc is no longer existing in Exchange 2016, not sure it means "nothing changed" or "no longer works".    

In my opinion, it's much more complicated if you want to share calender with external organizaton: https://msexchangeguru.com/2016/09/30/e2013-2016-multi-org-calendar-sharing/    

If you are using O365, follow this guidance: https://robinpowered.com/blog/how-to-use-office-365-shared-calendar-outside-your-organization/    

A workround is creating an internal mailbox/mail contact for the external user and assigning calendar permission for that mailbox/mail contact, then adding this mailbox to their Outlook client.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-06*

Hi @Kurt Stichelmans   ,    

Can you try creating a new Sharing policy as below and assign that to the mailbox and test it.    

New-SharingPolicy -Name "ExternalSharing" -Domains 'Anonymous: CalendarSharingFreeBusySimple' -Enabled $true    

Set-Mailbox -Identity <user name> -SharingPolicy "ExternalSharing"    

Please try to share calendar using OWA and check if that works.     

Sometimes this error in Outlook could be Autocache. Try deleting the address in "To" field while sharing calendar and re-type the full email address of the external recipient.    

If the above suggestion helps, please click on "Accept Answer" and upvote it
