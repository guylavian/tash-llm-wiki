---
title: "Change primary SMTP and recipient name in Exchange hybrid"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/293798/change-primary-smtp-and-recipient-name-in-exchange
question_id: 293798
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Q&A User"]
---
# Change primary SMTP and recipient name in Exchange hybrid

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/293798/change-primary-smtp-and-recipient-name-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Forgive me, I'm sure this has been asked and answered in this forum, but I have no idea how to search within just this forum. Searches seem to be only across every forum and yield thousands of results. We have less than a quarter of our recipient mailboxes on O365 so far, and this hasn't come up until now. I assumed it would be straightforward, but it doesn't appear so. I have a user who has a primary SMTP that differs from her display name (it matches her AD account). It was set up that way before her mailbox was migrated to O365. She has requested that her primary SMTP address be changed to match her display name. Her AD account is MJones. Instead of Display Name: Mary Smith; SMTP: ******@mycorp.com; smtp: ******@mycorp.com she now wants Display Name: Mary Smith; SMTP: ******@mycorp.com; smtp: ******@mycorp.com She also currently has smtp: @mycorptenant.mail.onmicrosoft.com and smtp:@mycorptenant.onmicrosoft.com In the Office 365 Admin Center, I have the check box available for setting a secondary email address as primary, but since this is a hybrid environment, I know I have to make such settings on prem and let them replicate. When I look at the O365 mailbox object in the on prem EAC, I do not see any way of setting any of the addresses as primary. How do I properly make this change? Am I overlooking something in on-prem EAC, do I use Set-RemoteMailbox, or do I edit AD? The other question I have is regarding the tenant SMTP addresses. Do I need to create additional secondary tenant SMTP addresses (mycorptenant.mail.onmicrosoft.com and mycorptenant.onmicrosoft.com in my example) to match the new primary SMTP address? Looking ahead, what is the proper way to change someone's name when for example a woman gets married (or divorced)? Thank you very much for your help with this.

## Answer (community) — Q&A User

*upvotes: 8 · updated: 2021-03-01*

First thing is we need to make sure we understand that the primary SMTP address and username, first name, last name are user attributes in AD. If you are running a hybrid environment with Azure AD Connect then all changes need to be made on-premise and then synced to Office 365/Azure AD.   

To change the primary SMTP you can either use the EAC, and go to the mail addresses dialog box, or go to the Attribute editor in Active Directory Users and Computers, once you've enabled advanced view, under the view menu, and change the proxyAddress attribute to match what you need.  

Please note that the caps SMTP is the primary or reply-as SMTP address and the lowercase smtp are additional aliases. The username, first name, last name etc can be changed from the regular Account Tab and User Info tab.   

Hope this helps and let me know if you have any trouble with that.

## Answer (community) — community member

*upvotes: 2 · updated: 2021-03-02*

Hi @Logan Burt   ,

Agree with above.

1.You could directly change the display name and primary emaild address of user mailbox in EAC in on-premises Exchange server.  

2.You do not need to create a second tenant. According to the information you provide, you only need to modify the Display name and primary SMTP address for the user. After the change, the smtp address related to onmicrosoft.com of the mailbox will remain unchanged.

Below screenshots is a test in my lab environment, I changed display name from user3 to user3-1, and changed the primary email address from ******@mydomain.com to ******@mydomain.com. After AAD connect is synchronized, I can see that the primary SMTP address of the mailbox also has changed in Exchange online. After that, I can successfully send emails to this address, and the emails sent from the user's mailbox can also be successfully received by the recipient, and the displayed name and email address that I see are updated.  

  

  

In addition, please note the following points:  

1.As mentioned above, please uncheck the “Automatically update email address…” before you change the primary SMTP address.  

2.When the user logs in to the mailbox, the UPN address is used. It’s may be different from the primary SMTP address.  

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-02*

Thank you very much sabny21 and especially michaelbartak for your clarification.  As soon as I saw it I was kicking myself.  I should have noticed that and remembered it myself.    

Thank you LucasLiu for your clarification about the tenant address.  May I ask some general clarification about these tenant addresses using my example?  I understand that the tenant addresses route mail between the on premise Exchange and the O365 tenant, but I'm unclear on the relationship between the real address and the tenant address.  Can I take from that that the tenant address needs to correspond with one of the smtp addresses of the mailbox, but not necessarily the primary SMTP address?  So in my illustration, I will wind up with   

Display Name: Mary Smith; SMTP: ******@mycorp.com; smtp: ******@mycorp.com; smtp: @mycorptenant.mail.onmicrosoft.com;  smtp:@mycorptenant.onmicrosoft.com  

In this illustration, is smtp:******@mycorptenant.onmicrosoft.com valid because of the existence of smtp: ******@mycorp.com?  If so, if the address ******@mycorp.com were to ever be removed, would I then need to create smtp: @mycorptenant.mail.onmicrosoft.com and  smtp:@mycorptenant.onmicrosoft.com?  

For that matter, do you know why there are two tenant domains, mycorptenant.mail.onmicrosoft.com and mycorptenant.onmicrosoft.com?  

Thank you all again for your help.
