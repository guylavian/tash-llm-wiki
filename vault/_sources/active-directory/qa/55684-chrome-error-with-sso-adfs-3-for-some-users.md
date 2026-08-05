---
title: "chrome error with sso adfs 3 for some users"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/55684/chrome-error-with-sso-adfs-3-for-some-users
question_id: 55684
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
---
# chrome error with sso adfs 3 for some users

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/55684/chrome-error-with-sso-adfs-3-for-some-users (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I had posted here     

https://learn.microsoft.com/en-us/answers/questions/53776/chrome-sharepoint-adfs-the-same-client-browser-ses.html     

After some input from the end users posting the new thread.     

Some of our users started reported errors when trying to login to sharepoint portal through adfs sso using chrome about a couple of weeks ago.     

For some clearing cache works temporarily. If they login to a different relying party, close the browser. Then log in through the sharepoint portal later it errors. Clearing the browser helps sometimes.     

In the past they used to be prompted for login after signing out or closing the browser. Now some of them go straight to the portal if they try after a few minutes of closing browser.     

Any one has any insight? It is not the number of groups the user belongs to since user with very less groups have had this issue. Seems to be chrome specific. Would this have to do anything with Chrome's samesite=lax? If it had I would have expected this issue to pop up earlier in the year rather than like two / three weeks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-31*

Whether the issue occurs on other browser?    

Please check whether you installed CU update referred in this article, if not, install it and compare the result.    

More information:    

http://thewindowsupdate.com/2020/03/25/effect-on-sharepoint-sites-that-use-adfs-saml-authentication-in-chrome-version-80-or-later/
