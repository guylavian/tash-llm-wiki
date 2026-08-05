---
title: "Python x Exchange 2013"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1419963/python-x-exchange-2013
question_id: 1419963
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Python x Exchange 2013

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1419963/python-x-exchange-2013 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello.

I work in the IT sector of a company in Brazil. I am supporting the Systems team in creating a Python script that performs the following functions:

1- Connection to an Exchange email account.

2- Read the messages in your inbox.

3- Analyze the collected data.

My part in this task is related to items 1 and 2.

This is the case:

a) An email account has been created for this project.

b) Connection to this email account using IMAP4 and POP3 works normally (without Outlook). But when performing an inbox search, it returns an error.

c) This error appears to be related to Exchange Server, which does not allow passwords to be sent unencrypted over the network. Source: chilkatforum.com/questions/2949/pop3-command-is-not-valid-in-this-state.

d) As we are deploying a Wildcard SSL certificate on the Exchange Server Standard 2013 server (latest build available), a script was run to connect to the email account using IMAPS and POP3S, but it did not work (protocol error).

e) As a last alternative, a script that uses the Exchange connection instead of IMAP4/IMAPS or POP3/POP3S was executed:

-  A script was attempted with AUTODISCOVER enabled (error in the validation process).

-  Then another with Exchange server information enabled (the connection was refused).

f) All the tests mentioned were carried out on the computer of the programmer responsible for the project, who is authenticated in the domain. This machine is also with a fixed IP and running Windows 11 Pro 22H2 (latest build available).

Finally, it was agreed that the programmer would seek help on the Python forums, while I would seek help here.

Has anyone here participated in a similar project (creating a Python script that connects to an Exchange email account, to read emails from the inbox and then process the data obtained) and had a similar problem? If so, how was it possible to resolve it?

I appreciate everyone's patience in reading my case.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-09*

Hi, @Yuki Sun-MSFT  ,

It's done.
