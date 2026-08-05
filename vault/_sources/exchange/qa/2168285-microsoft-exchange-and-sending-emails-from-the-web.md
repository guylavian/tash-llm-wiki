---
title: "Microsoft Exchange and sending emails from the website"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2168285/microsoft-exchange-and-sending-emails-from-the-web
question_id: 2168285
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Microsoft Exchange and sending emails from the website

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2168285/microsoft-exchange-and-sending-emails-from-the-web (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I would like to ask how we can solve the problem with sending emails from the web. The client only uses an Exchange license without Office 365 and does not have access to the Azure portal either. We need to send notification emails from the web site. I was considering SMTP sending. So I created an email in Exchange ******@domain.com. I have set up SMTP sending on the site:

server: smtp.office365.com

port: 465

I have entered the user and password for the mailbox but the sending does not work. 

How would you handle sending notifications from the web if the emails are in Microsoft Exchange ?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-02-19*

Hello, @ADM Marcinko,

Welcome to the Microsoft Q&A platform!

If your client does not use Office 365 and does not have access to Azure, then your best bet is to work with your Exchange administrator to set up an SMTP relay or receive connector on your existing Exchange server. You’d configure your web application to send mail to that connector.

Alternatively, if you do need to use SMTP authentication, confirm the right combination of host, port, and encryption based on the organization’s documentation.

In summary, rather than using smtp.office365.com (which is for Office 365 accounts) you should either configure your web application to use your organization’s own Exchange server (correct hostname, port, and encryption) or set up a dedicated SMTP relay on Exchange that allows sending from your web server. This ensures that your notification emails are properly relayed from within your Microsoft Exchange environment.

Should you need more help on this, you can feel free to post back. 

If the answer is helpful, please click on “Accept answer” as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang
