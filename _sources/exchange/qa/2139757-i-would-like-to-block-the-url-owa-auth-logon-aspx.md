---
title: "I would like to block the URL /owa/auth/logon.aspx from IIS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2139757/i-would-like-to-block-the-url-owa-auth-logon-aspx
question_id: 2139757
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# I would like to block the URL /owa/auth/logon.aspx from IIS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2139757/i-would-like-to-block-the-url-owa-auth-logon-aspx (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear All.

If any url matches hhtps://abc.com/owa/auth/logon.aspx it has to be blocked

How do I do ti I tried multiple steps on IIS but no luck

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-01-03*

Hello, @Athique Nihal,

Welcome to the Microsoft Q&A platform!

In order to block a specific URL in IIS, it is recommended for you to accomplish it by using the URL Rewrite module. 

If you haven’t already installed the URL Rewrite Module, you need to download and install it. You can find it on the Microsoft website. Then open IIS Manager, select your site, and double-click on "URL Rewrite." Add a new rule by selecting "Request Blocking," then configure the rule by setting the URL to the path you want to block (e.g., /owa/auth/logon.aspx). Choose "Abort Request" or "Custom Response" with a status code like 403 and apply the rule to save and enable it. It may be necessary to restart IIS for the changes to take effect. 

For more guidance, please refer to https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/request-blocking-rule-template.

This should block any requests to the specified URL. If you encounter any issues, make sure other rules are not conflicting with this one and check the Failed Request Tracing logs for more details.

In addition, here is a case study similar to your needs for your reference: https://learn.microsoft.com/en-us/answers/questions/870061/blocking-a-specific-url-using-iis-url-rewrite.

Should you need more help on this, you can feel free to post back. 

If the answer is helpful, please click on ACCEPT ANSWER as it could help other members of the Microsoft Q&A community who have similar questions and are looking for solutions.

Thank you for your support and understanding.

Best Wishes,

Alex Zhang

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-02*

Firstly your IIS server would never get an arbitrary request for `https://abc.com` unless your IIS server is actually hosting that domain. So the host information is a mute point here. IIS only kicks in once it matches the host information to a site you are hosting. If you aren't hosting the site then nothing happens (and DNS shouldn't let it get there anyway).

So you want to block `owa/auth/logon.aspx`? That looks like the old Outlook Web Authentication URL. To block a URL, that may or may not be valid, then you should probably use URL rewriting. This allows you to specify the path(s) that you want to treat differently. You could also use HTTP Redirection but the only responses are to redirect somewhere else. You could redirect to a non-existent URL and accomplish the same thing.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-02*

Hi,

Here are some links that might help you :

https://learn.microsoft.com/en-us/iis/manage/configuring-security/configure-request-filtering-in-iis

https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/using-the-url-rewrite-module

https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/creating-rewrite-rules-for-the-url-rewrite-module

https://www.iis.net/downloads/microsoft/url-rewrite

Sincerely,
