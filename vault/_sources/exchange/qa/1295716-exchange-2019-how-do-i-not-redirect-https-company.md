---
title: "Exchange 2019: How do I NOT redirect https://company.com to https://company.com/owa"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1295716/exchange-2019-how-do-i-not-redirect-https-company
question_id: 1295716
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Exchange 2019: How do I NOT redirect https://company.com to https://company.com/owa

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1295716/exchange-2019-how-do-i-not-redirect-https-company (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I have following two server -

-  Exchange 2019 server - (IP: 1.2.3.4) - https://company.com (or https://company.com/owa)

-  Company website server - (IP: 1.2.3.5) - https://www.company.com

DNS Entry -

company.com - CNAME - 1.2.3.4

company.com - MX - 1.2.3.4

www.company.com - A - 1.2.3.5

My redirect requirement is - 

-  http://company.com  -> http://www.company.com

-  https://company.com -> http://www.company.com

I was able to solve #1 by creating an IIS entry in the exchange server for the company.com and redirecting to www.company.com.

Now, how do I achieve the #2 redirection? Exchange's default behavior is to redirect to https://company.com/owa. And I need to overwrite it.

Thanks in advance.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-06-02*

Hi @Stay,

Since it is the default setting on Exchange, disabling it would cause Exchange to malfunction.

Would it be possible to use another url, for example mail.company.com on Exchange?

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-06-01*

To achieve the redirection from `https://company.com` to `http://www.company.com`, you can follow these steps:

-  On your Exchange 2019 server, open Internet Information Services (IIS) Manager.

-  Locate the website for `https://company.com` and select it.

-  In the Features View, double-click on the "HTTP Redirect" option.

-  In the HTTP Redirect settings, check the box for "Redirect requests to this destination" and enter `http://www.company.com` in the text box.

-  Make sure to select the option "Only redirect requests to content in this directory (not subdirectories)".

-  Optionally, you can check the box for "Redirect all requests to exact destination" to ensure that any URL path within `https://company.com` is redirected to the corresponding path in `http://www.company.com`.

-  Click "Apply" to save the changes.

These settings will configure a redirect from `https://company.com` to `http://www.company.com` on the Exchange 2019 server. Any requests to `https://company.com` will be redirected to the specified destination.

Remember to test the redirection thoroughly to ensure it is working as expected.
