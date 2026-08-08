---
title: "Cannot send email with Exchange account in Mac Mail. Error says \"From address is not one of your addresses\" - but it is one of my addresses."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2286768/cannot-send-email-with-exchange-account-in-mac-mai
question_id: 2286768
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Cannot send email with Exchange account in Mac Mail. Error says "From address is not one of your addresses" - but it is one of my addresses.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2286768/cannot-send-email-with-exchange-account-in-mac-mai (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

It's been days since I posted a query, and there is NO WAY TO GET TECH HELP on the phone, so this is my only option with MS. 

I set up my hotmail as an Exchange account on the MacBook Pro. It's enabled and green, and can receive emails, but cannot send. Error says "From address is not one of your addresses". And in Edit SMTP list there is no Exchange server listed. So when configuring the Exchange account it does not automatically add the SMTP server.   

Have deleted and readded account, configured manually using both outlook.com and office365.com servers, cleared cache and deleted plist. 

Everything works fine on my other Mac, with the exact same settings.  And the Hotmail sends and receives fine in the Outlook app. 

Would be grateful for expert advice, as I cannot be the only person with this issue. If there is no fix I will switch to my GMail going forward.

## Answer (community) — Microsoft Moderator [MicrosoftVendor]

*upvotes: 0 · updated: 2025-06-25*

Dear @Jason Kaufman,

Thank you so much for contacting Microsoft Q&A Support. 

Based on your descriptions, I find that it is a known issue with macOS Mail when configuring Hotmail accounts as Exchange rather than Outlook.com accounts. The Exchange setup sometimes fails to properly link the SMTP server, which is required for sending mail. Also, the error message "From address is not one of your addresses" typically means: 

-  The Mail app is trying to send from an address that isn’t associated with the configured SMTP server. 

-  The SMTP server is either missing or misconfigured. 

Microsoft does not currently have a specific support article that directly addresses the "From address is not one of your addresses" error in macOS Mail when configuring Hotmail accounts as Exchange. However, I find this article that may help you: I can't send or receive messages with Outlook for Mac - Microsoft Support 

I really appreciate all the effort you’ve put into trying those fixes and I would like to know that have you try to send email in Outlook web? Please kindly do it to see if it can work.

If it still does not work, I find a few more things during my research that you could try: 

1. Use Outlook.com Setup Instead of Exchange: 

Instead of setting it up as an Exchange account, try this: 

-  Select Tools > Accounts. Then select the plus (+) sign > New Account. 

-  Sign in with the Hotmail credentials. 

This method ensures macOS uses the correct SMTP and IMAP settings for Outlook.com accounts. 

Reference: Add an Outlook.com or Microsoft 365 account in Outlook for Mac - Microsoft Support 

2. Manually Add SMTP Server, please consult in these articles: 

-  Server settings you'll need from your email provider - Microsoft Support 

-  POP, IMAP, and SMTP settings for Outlook.com - Microsoft Support 

Additionally, you can check "Email Address" field to make sure the Email Address field in the account settings matches the actual Hotmail address exactly. Even a small mismatch can cause the "From address" error.

I hope this information can help you to solve this issue.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
