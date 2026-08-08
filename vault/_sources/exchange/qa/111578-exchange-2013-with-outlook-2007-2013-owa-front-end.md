---
title: "Exchange 2013 with Outlook 2007/2013/OWA front end yielding different/bad search results"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/111578/exchange-2013-with-outlook-2007-2013-owa-front-end
question_id: 111578
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 with Outlook 2007/2013/OWA front end yielding different/bad search results

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/111578/exchange-2013-with-outlook-2007-2013-owa-front-end (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have what seems to be a small issue that is starting to grow....quickly  

We moved from an Exchange 2007 backend to 2013 (v15.0, build 1395.4) a little over a year ago. We have about 1600 mailboxes and 3 databases. This was built by a 3rd party vendor and I am the one maintaining/administering it. It is NOT my primary focus at my job so my knowledge is a bit limited, but I have been tasked to dedicate more of my time to try and fix this issue.   

What is starting to happen is that our helpdesk is receiving more and more calls about searching not yielding good results. I spent time with them the other day and worked with a new user, only been in our system for about a month and has a pretty small mailbox, who was attempting to find an email from last week and searched a word that he knew was in the subject and it did not return the email he was looking for. This is in Outlook 2007. Yes I realize this is old and dated, but it's all I have to work with. He then tried in Outlook 2013 (which we dont widely publish, just gave him temp access to) and it returned different results but still not the original email that he was looking for. I then had him try OWA and the way it displays search results is different, basically lumps the entire conversation into one thread and he was then able to expand that thread and see the original email he was looking for.  

Another example is someone else in our IT department was looking for an email from "Sarah". She searched for an email that was in her inbox from yesterday and it didnt come up in her search. She then tried OWA and it too did not return the email she was looking for.  

Searching for most things works, but more and more calls from users are coming into the helpdesk with various searching issues and I am not sure where to start since they are so intermittent. It doesnt help the our CIO has been having searching issues for about a year now and now that there are more popping up, he wants me to look into it further. Any help would be greatly appreciated. I am willing to try anything and will take all suggestions into consideration. If any suggestion will take mail down and require downtime, obviously with proof that it will work/help, I will be able to coordinate that with our CIO and office managers.  

Things I have already done:  

Rebooted mail servers (both the database server and the OWA server).  

Check the status on all 3 databases, the "ContentIndexState" is showing healthy.  

Created new databases and migrated mailboxes to new databases.  

I have NOT blown away exchange accounts and recreated them. Most of the users in question are the ones who use email the most and arent willing to have their mail backed up to a PST, blow away their exchange accounts, then set them up as new with an imported PST. With a new user having this issue though, I could try this but I dont think it will solve the issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-30*

-  They have been around for at least a year. Our CIO has been having search issues for about a year then next heard of a director having issues around the same time. Our network engineer also let me know he was having issues as well, maybe 6 months ago. The similarities of these 3 are that they all have larger mailboxes, so at the time I just chalked it up to that. With this new user now having search issues, that kind of throws that idea out the window.    

-  This is for that new user I keep referring to. He received an email with the subject "Foundation August". When he searches this exact phrase, the results are different between Outlook 2007 and Outlook 2013 are similar, Outlook 2013 just shows a the sent as well (you can see he chose "Current Mailbox"). BOTH versions do not give the original email as a result, which is what he was looking for in this specific search. There is another coworker in IT that is in the same office as I am that has similar issues as well. She was the example I provided in my OP where she would search "Sarah" and not all emails from "Sarah" were showing up. I can get snips and examples if it will help.    

-  I will work with some users and get more examples.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-09-30*

Hi @Tom Luley  ,

Before going further, I'd like to confirm the following things with you so that we may understand better about the situation:

-   Do you have idea about when the searching issue started to occur and when it began grow rapidly? Was any change made in the environment before the issue started?

-   For the two examples you mentioned, could you please provide more details like which keyword did they use when attempting to search, and what was returned: no results, wrong results or incomplete results?  

    How about changing the search scope to “Current mailbox” or adjusting the keywords to see if there would be any difference?

-   Searching for most things works, but more and more calls from users are coming into the helpdesk with various searching issues and I am not sure where to start since they are so intermittent.    Agree with you that it could be quite hard to troubleshoot given the current situation that the reported searching issues are various and intermittent. So if possible, can you try to go through some more examples and see if there could be any findings? You can also share some more typical examples after removing any personal information involved for further investigation.

For situation similar to the first example that the message can be found in OWA, I’d like to suggest testing in Outlook client side by switching between Exchange cached mode and Online mode and see if there would be any difference.

Besides, please have a check on the Exchange server to see if there are any relevant logs in the Event Viewer.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
