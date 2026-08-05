---
title: "Exchange 2016 /2010 coexistence. Users on 2010 cannot change password from OWA."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1425786/exchange-2016-2010-coexistence-users-on-2010-canno
question_id: 1425786
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 /2010 coexistence. Users on 2010 cannot change password from OWA.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1425786/exchange-2016-2010-coexistence-users-on-2010-canno (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

This is the environment that i have

2 x Exchange 2010 CAS servers. (CAS array is used also).

2 x Exchange 2010 Mailbox Servers in a DAG.

Now two new Exchange 2016 servers have been installed. (also with a DAG).

Client access is now through exchange 2016 as we have changed DNS entries for the 'mail' and 'autodiscover' to point to 2016.

Everything works fine. OWA, Outlook, Outlookanywhere all are working.

But the only issue I have is that users who are still on 2010 cannot change their passwords anymore through OWA.

When they login to OWA they get the new login page from 2016 server, but after login it redirects to 2010 OWA interface , which is fine and expected. 

At the password change page however, it seems to got 2016 page and we get the error "somethign went wrong" and the password change page does not appear.

How to solve this issue?

## Answer (community) — community member

*upvotes: 1 · updated: 2023-11-23*

Hi,

Sorry for the late reply. Actually we solved the issue so I didn't check back here.

As it happens it was the same issue as answered by Amit Singh here. 

It was the ecp virtual directory on the exchange 2010 server. It did not have windows authentication enabled on it.

Earlier we were only looking at the Owa virtual directory and that looked fine and had correct settings but later we realized the ecp virtual directory also had to be set the same way.

Adding windows authentication to the ecp virtual directory on Exchang2010 servers fixed the issue.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-11-16*

Hi @AMIM  ,

Do you mean the issue only affects users who are still on 2010? I mean, if migrating an affected user to 2016 or creating a new user on 2016, the password can be changed successfully from OWA, right?  

Aside from the change password feature, can they access and use other options in OWA as expected?  

Can the users change the password in other methods like pressing Ctrl+Alt+Delete and then change the password of the domain user account there?

Please try accessing the OWA by adding the Exchange version `?ExchClientVer=14` to the URL and see if there would be any difference.

Besides, you can also take a look at the logs via C:\Program Files\Microsoft\Exchange Server\V15\Logging\HttpProxy\Owa and C:\Program Files\Microsoft\Exchange Server\V15\Logging\HttpProxy\Ecp on Exchange 2016 to see if there are any more error messages there. You could use Excel to read the log files more easily. (Save a copy of the log file, open Excel, go to Data > From Text/CSV, select All Files so that you can see the log file, follow the wizard to import the data.) 

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in [our documentation] to enable e-mail notifications if you want to receive the related email notification for this thread.
