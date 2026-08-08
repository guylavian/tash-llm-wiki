---
title: "CU 19 for Exchange 2016 servers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/234489/cu-19-for-exchange-2016-servers
question_id: 234489
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# CU 19 for Exchange 2016 servers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/234489/cu-19-for-exchange-2016-servers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi  

We are planning to install CU19 with Exchange 2016 servers which are running on CU17. In 2-3 days (before installing CU19) we will integrate with OOS to preview Word / Excel docs. We saw the comments from many saying "after installing CU19, pdf docs could not be viewed from OWA" (as of now we can able to preview pdf with Edge Chromium). Looking for suggestions on CU19 installation, also is there any security updates related for CU19?  

Thanks in advance

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-26*

Hi @LMS   ,    

Thank you for your understanding. As I mentioned above, you could use OOS to open and edit(not preview) these docs on your browser.    

The introduce of Office Online Server: Office Online Server overview.    

And about how to install OOS: Install Office Online Server in an Exchange organization.    

Hope these would help you.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-21*

Thank You  

We postponed the activity till MS release a fix for it...

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-19*

Hi @LMS   ,    

We saw the comments from many saying "after installing CU19, pdf docs could not be viewed from OWA"    

The CU19 update soloved this problem in CU18:     

     

But it also brings a new issue:    

     

I did a test in my lab(CU19), and the result is like the official doc said, if you click Preview, it will start downloading and keep loading.    

    

     

Then Microsoft gives a work around in KB 4583558: To work around this problem, use the Outlook client to preview .pdf documents. It is also possible to open the .pdf document, which was downloaded automatically using Outlook on the Web, with a PDF reader of your choice.    

Since you are going to install OOS, I think you don’t have to worry about it, the OOS will help you open these docs on your browsers:    

     

Looking for suggestions on CU19 installation, also is there any security updates related for CU19?    

According to my research, since the CU17 and CU19 have same prerequisites, no preparation will be needed to update Exchange 2016 CU17 to CU19, you can directly update it to CU19. Upgrade Exchange to the latest Cumulative Update    

And I didn’t find security updates for CU19, as It is the latest version of Exchange 2016.    

You can find the known issues and fixed issues in Cumulative Update 19 for Exchange Server 2016.     

And this article shows the latest CU,RU for Exchange: Exchange Server build numbers and release dates.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
