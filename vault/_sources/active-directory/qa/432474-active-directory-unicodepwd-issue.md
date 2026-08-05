---
title: "Active Directory unicodePWD issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/432474/active-directory-unicodepwd-issue
question_id: 432474
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory unicodePWD issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/432474/active-directory-unicodepwd-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

here is an issue I want to discuss with you guys kindly help me resolving this issue.    

whenever I set the value in active directory user unicodePwd this error show up:    

    

i logged in as a administrator user in the active directory

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-16*

Hello @Muhammad  Tayyab  ,    

I am so glad to receive your reply.    

I am sorry, in fact, I do not have any PHP script or any other script to change active directory user password.    

I really want to find useful code and want to test it in my AD test environment to modify the active directory user password.    

But I found out that all I can do is to Google code examples on the Internet, and there are useful codes in the two links in my first post. But I don't have tools to test those codes (the first link is Java code, and the second link is php code. In fact, I can't understand these codes because I am not an expert in this field).    

My suggestion is that you can refer to the code in the link above (or you can find more helpful code examples on the Internet, maybe C++ code), and then find the corresponding code experts on the corresponding forums, and let them test the code in their test environment and modify change active directory user password.     

IADsUser::ChangePassword method (iads.h)    

https://learn.microsoft.com/en-us/windows/win32/api/iads/nf-iads-iadsuser-changepassword    

Thank you so much for your understanding and support.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-14*

@Anonymous    Thankyou for answering i have a question i am using php here is my code for modify unicodePwd but its says "server is unwilling to perform" could you please help me out in this:    

$username = "admin username";    

$password = "admin password";    

$ldap_server = "ldaps://ip address:636";    

$ldap_conn = ldap_connect($ldap_server);    

$base_dn = "user complete dn";    

$userdata["unicodePwd"] = "TGFob3JlMSFUYXl5YWIxQCM=";   //base 64 encoded password    

$result = ldap_modify($ldap_conn, $base_dn, $userdata);    

ldap_close($ldap_conn);    

Warning: ldap_modify(): Modify: Server is unwilling to perform
