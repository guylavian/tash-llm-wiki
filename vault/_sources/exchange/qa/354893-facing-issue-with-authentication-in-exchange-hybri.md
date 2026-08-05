---
title: "Facing issue with authentication in Exchange Hybrid Wizard sign in page not loading"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/354893/facing-issue-with-authentication-in-exchange-hybri
question_id: 354893
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Facing issue with authentication in Exchange Hybrid Wizard sign in page not loading

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/354893/facing-issue-with-authentication-in-exchange-hybri (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are facing an issue with a new Exchange hybrid deployment. The wizard unfortunately fails to open the Exchange Online sign-in page. I tried and I was able to sign in from a browser but getting a warning then a blank page when using the Hybrid Wizard.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-14*

Hi @Sultan Sheikh   ,  

Since you can log in normally in the browser, this means that your account is no problem. And based on my research on the error report, this seems to be a related error about browser settings.  

If you click "Yes", what error will be displayed afterwards?

1.Please make sure that your browser is upgrade to the lastest version.

2.Please make sure that the firewall or antivirus software in your computer will not block the communication.

3.Please try to the following the steps, then run the HCW again:  

1)On the Tools menu, click Internet Options.  

2)On the Advanced tab, click to clear the "Display a notification about every script error" box, and then click OK.  

For more information: How to troubleshoot script errors in Internet Explorer

In addition, are there any related error logs in the Event Viewer? If so, please sharing with us, but pay attention to covering personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
