---
title: "ADFS 4.0 - WAP - IIS - Apple iOS / iPadOS - PHP post  - Error 500"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/40669/adfs-4-0-wap-iis-apple-ios-ipados-php-post-error-5
question_id: 40669
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# ADFS 4.0 - WAP - IIS - Apple iOS / iPadOS - PHP post  - Error 500

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/40669/adfs-4-0-wap-iis-apple-ios-ipados-php-post-error-5 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear forum,    

have ADFS 4.0 with WAP, non-claims-aware party trust to an IIS application running a PHP website. The PHP site contains a simple form with POST. Authentication is working, form is working (Internet Explorer, Chrome, Edge Chromium), however not on Safari (Apple iOS (iPhone) and iPadOS). There I get an Error 500 as soon I press the POST button (loading the form is not a problem). Even on a MacBook with Safari everything is working fine.     

Cannot find any error in the Eventlogs (WAP / ADFS / IIS) nor in the PHP log. I guess it's not a server error (500 = internal server error) as don't see any log entries.    

The site appears blank, had to connect the iPhone to a MacBook to get the error.     

    

I checked the user agent configuration, I added Mozilla 5/0 to the ADFS properties, no success. Even when I overwrite the user agent with the iPhone's value on the MacBook with Safari it works. So I guess the user agent is not causing the issue.    

If I am in the internal network via WiFi, I can access the site with the iPhone and post the form without an issue -> something is wrong with WAP / ADFS (maybe IIS). When I pass-through, the form is working too from external. Seems iOS / iPadOS does not like something with the authentication. I've installed Chrome / Edge on iPhone and iPad -> same issue    

Any ideas?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-09-11*

Ensure that your SSL/TLS configuration is correct. Some iOS versions may be more strict about SSL/TLS certificate validation. Make sure that your SSL certificate is valid, properly installed, and does not have any issues.
