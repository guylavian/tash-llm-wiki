---
title: "Active Directory failed login attemps"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1166682/active-directory-failed-login-attemps
question_id: 1166682
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Active Directory failed login attemps

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1166682/active-directory-failed-login-attemps (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a program that sends me an email with all of the login attempts be it a successful attempt or a failed login.  I am seeing where after a user is able to authenticate against one of the domain controllers and logs into their workstation.  I am seeing a failed login from a former employee's admin account.  I am having a hard time tracking down what is causing this to happen.  

Please help I am pulling my hair out.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-03*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query.

To track down the cause of the failed login attempts from a former employee's admin account, you can try the following steps:

-  Check Event Viewer on the domain controller and workstation where the login attempts are recorded to see if there are any specific error messages or codes related to the failed login attempts.

-  Monitor the security logs of the domain controllers and workstations for any suspicious activity.

-  Check if there are any scheduled tasks or scripts that are running under the former employee's admin account.

-  Verify if there are any devices or systems that may be authenticating with the former employee's admin account credentials, such as automated backup systems or network printers.

-  If the issue persists, you can use network monitoring tools to track the source of the failed login attempts.

-  If you are still unable to find the cause of the failed login attempts, you may need to change the password for the former employee's admin account to prevent further unauthorized access.

It's important to take the necessary steps to secure your network and prevent unauthorized access. It is recommended to engage the services of an experienced IT security professional if you are unable to resolve the issue.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-02-02*

Hi @BBennett  

In the event check the IP of source machine. If you are able to identify this machine , check if there is mapped drive, scheduled task, windows service, script still using the admin account.

Please don't forget to mark helpful answer as accepted

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-02-02*

Hello,

this is probably a service or scheduled task configured to run under that user credentials.
