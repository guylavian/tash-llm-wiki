---
title: "Exchange 2013 mailbox sizing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/415819/exchange-2013-mailbox-sizing
question_id: 415819
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 mailbox sizing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/415819/exchange-2013-mailbox-sizing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey all,

I have a quick question...

Right now our users use a lot of PST data files with their mailboxes. It was a solution that was made a long time ago to encounter with specific users considered to be VIPs, but by the time a lot of users found that bypass to "increase their mailbox" without any limit.

Then, what to do next?

We do want all the data in the PST files will be transferred back to the users mailboxes. However, we do have a few requirements -

-    We want to create sort of user "quota profiles" the majority of our users need in about 1G of mailbox, and the rest is sliced between 5G and 10G. How can we create sort of 'tears' of mailbox capacities?

-    We do want to give the users the option to search in their old mails, but they do so in a low frequency. How can we achieve that with the maximum of data reduction and compression?

-    We do have users that come once in a few months. Those users continue to get unnecessary mails and to fill up our databases.... we thought to put them in seperate unmounted database, but than when these users do come, we don't want them to wait for us to mount their mailbox back.... what can be the right solution for this?    Oh and I didn't mentioned....we do have Exchagne 2013.....😢😢    Thanks    Tankwell

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-22*

Hi,

I could not reply to you since I was working on another project....Hope you would understand 😊

It doesn't matter. I'm always glad to help :)

I guess this error will show up also if I manage the move request through the Exchange Administration Web Interface?

Yes. If you use Exchange Administration Web Interface ( Exchange Admin Center) to move the mailbox, you will also get the same error.

How can I calculate / approximate the daily message rate? I think this is an important detail for the calculations here "Ask the Perf Guy: Sizing Exchange 2013 Deployments"

You may need some scripts to count the messages.  

Here is a link for your reference: How to check total mails(IN and OUT) of one month in exchange server 2016  

Please refer to Kyle's answer.

On the Other hand, we use by now the same tactics / retentions on PST files, so our users PST files keep growing...Do you know to approximate the growth rate of PST vs Mailbox Databae?

Since the structure is different (Exchange database stores items in edb file), to my knowledge it should consume less disk space then storing in pst files.  

While I suppose the main point here is whether you would like to save server disk space or user disk space :)  

To me I would recommend enabling archive mailboxes for them.

Can I set these quotas after I have set the mailbox to unlimited?

Did you mean the quota of the database hosting the archive mailboxes is unlimited?  

If so, the quota of the archive mailboxes won't inherit from the quota of the database which is hosting the archive mailboxes. (By default it should be 100GB)

These mailboxes reciving emails on a daily basis....we do want to recognize them and to put on them sort of reject any message rule (move to deleted items or such thing)

I think using mail flow rule to reject the emails should work for you in this scenario.  

Please see my first reply. It would reject all emails sending to these mailboxes.  

When the users come to support, you may need to disable the mail flow rule to enable emails to be sent to these mailboxes.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-20*

Quota management

Did you mean you have multiple Exchange servers coexisting cross

sites?

All the Exchange serers are running in the same version

If the mailbox quota is inherited from database (Use the default quota settings from the mailbox database), it will be changed to 1G (the quota of the target database).

And if the current mailbox size is over 1G (larger than the quota of the target database), you may get the following error message when moving the mailbox:  

In this case, I think you may need to customize the quota before moving the mailbox.

That's what I wanted to hear, thanks 😊  

I guess this error will show up also if I manage the move request through the Exchange Administration Web Interface?

It also depends on the amount of messages.

This topic is introduced in this link: Ask the Perf Guy: Sizing Exchange 2013 Deployments  

You may also use the Exchange server role calculator to calculate the size: Released: Exchange 2013 Server Role Requirements Calculator  

Archive

How can I calculate / approximate the daily message rate? I think this is an important detail for the calculations here "Ask the Perf Guy: Sizing Exchange 2013 Deployments"

Since the in-place archive mailboxes are hosted on the Exchange server, if the size of the archive mailboxes is set to unlimited and there are no retention policies to periodically remove the items which reach a certain age(for example three years), the size would for sure grow larger and larger since there are new items keep being moved to the archive mailboxes and the old ones are also kept.

And it will consume the disk space.

On the Other hand, we use by now the same tactics / retentions on PST files, so our users PST files keep growing...

Do you know to approximate the growth rate of PST vs Mailbox Databae?

I suppose you may either set a quota for the archive mailboxes instead of setting it to unlimited, or you may have to remove some old items in the archive mailboxes using retention policy like mentioned in my former reply.

Can I set these quotas after I have set the mailbox to unlimited?

Scenario

May I ask what is your concern in this scenario?

Are there new messages sending to these mailboxes when they are not in use?  

If the mailboxes are not used for sending or receiving any new messages, their sizes will not grow and will not consume more disk space.

These mailboxes reciving emails on a daily basis....we do want to recognize them and to put on them sort of reject any message rule (move to deleted items or such thing)

Or did you mean you would like to totally empty the mailboxes when they are not in use to release disk space?

No, we want to save these mails

And have the users using the mailboxes with the same email addresses

when they come to do the support work?

True - they use their 'old' mailboxes

Thank you very much for these answers - I could not reply to you since I was working on another project....

Hope you would understand 😊

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-07*

Hi,

Thanks for the update!

-    Quota management

I think the right solution for us is to create some seperate databases with different quotas

Yes. You may also move the mailboxes to separate databases with different quotas :)

we might move these users to database in another site

Did you mean you have multiple Exchange servers coexisting cross sites?

If I move existing mailbox with 5G quota to Database with 1G quota, will the quota change?

If the mailbox quota is inherited from database (Use the default quota settings from the mailbox database), it will be changed to 1G (the quota of the target database).  

And if the current mailbox size is over 1G (larger than the quota of the target database), you may get the following error message when moving the mailbox:  

  

In this case, I think you may need to customize the quota before moving the mailbox.

If the mailbox quota is customized, it will not be changed.

Is there a limit or official recommendation about the amaount of mailboxes per one database? In order to reduce I/O,latency,..etc?

It also depends on the amount of messages.  

This topic is introduced in this link: Ask the Perf Guy: Sizing Exchange 2013 Deployments  

You may also use the Exchange server role calculator to calculate the size: Released: Exchange 2013 Server Role Requirements Calculator

-    Archive

Do you relly think It would not save space?

Since the in-place archive mailboxes are hosted on the Exchange server, if the size of the archive mailboxes is set to unlimited and there are no retention policies to periodically remove the items which reach a certain age(for example three years), the size would for sure grow larger and larger since there are new items keep being moved to the archive mailboxes and the old ones are also kept.  

And it will consume the disk space.

I also heard that enabling unlimited archiving will deny the option to restrict the archive mailbox again. If that so, we do fear it would blow up owr disk space....is there a way to elude such senerio?

I suppose you may either set a quota for the archive mailboxes instead of setting it to unlimited, or you may have to remove some old items in the archive mailboxes using retention policy like mentioned in my former reply.  

Configure archive quotas for an In-Place Archive in Exchange 2013

-    Scenario

Thanks for the clarification.  

However, I still have some questions.

May I ask what is your concern in this scenario?  

Are there new messages sending to these mailboxes when they are not in use?  

If the mailboxes are not used for sending or receiving any new messages, their sizes will not grow and will not consume more disk space.

Or did you mean you would like to totally empty the mailboxes when they are not in use to release disk space?  

And have the users using the mailboxes with the same email addresses when they come to do the support work?

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-06*

Hey,  

First - thank you very much about this informative answer!  

Let me response about each subject seperately -

Quota management

We looked up for a nice "quota profiles" to assign mailboxes in order to bypass the need to do some move requests and manage some seperate mailboxes.

We do confiugre by now on each database the quota to 2Gb. I think the right solution for us is to create some seperate databases with different quotas -

DB amaount
Quota
Perpose

5
1GB
Regular user

1
5GB
Important users

1
10GB
VIP users

◼  

Having that said - we might move these users to database in another site. Do we must move the mailbox to database with the same default quota? Or (Let me be clear) - If I move existing mailbox with 5G quota to Database with 1G quota, will the quota change?

-  Is there a limit or official recommendation about the amaount of mailboxes per one database? In order to reduce I/O,latency,..etc?

Archive

We do want the users to use archive mailbox, In an attempt to create "unlimited" mailbox capacity without having to deal with on a daily basis quota management.

We considered to enable the "unlimited archiving" feature to the mailboxes of Important users.

While, if you would like to keep all the mails instead of removing old mails periodically, I suppose that it may not be possible to reduce the disk usage on Exchange server.

Do you relly think It would not save space?

I also heard that enabling unlimited archiving will deny the option to restrict the archive mailbox again. If that so, we do fear it would blow up owr disk space....is there a way to elude such senerio?

Sorry I was a little confused with the scenario.

Did you mean:  

There are some users who have mailboxes in your organization and they will use these mailboxes to send and receive mails from time to time.  

After they left, they will use other mailboxes hosted by other email service providers (for example, gmail, yahoo, etc.)  

But some senders don't know about it and will keep sending mails to the mailboxes hosted by your Exchange server.

If I misunderstood anything,please feel free to correct me.

This is partly true - These users do leave the organization offially, but they do come from time to time to support. When they do, they have to send & recive emails. The question is what to do with their mailboxes -  

-  We can't delete them, since they would need this mailbox when they come  

-  We thought to put their mailbox in unmounted database, but the process of enabling the mailbox again when it's needed is uncomfortable

The optimal solution is a feature that "freezes" the user mailbox until the next user login. I know there is no such thing, so I do search for another ideas using the availbale tools

Thank you very much, and sorry about the slow reply - I was not at the office 😊  

Tankwell

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-06-01*

Hi Tankwell.    

We want to create sort of user "quota profiles" the majority of our users need in about 1G of mailbox, and the rest is sliced between 5G and 10G. How can we create sort of 'tears' of mailbox capacities?    

By default the storage quota of the mailboxes is inherited from settings of the database which hosts the mailboxes.    

While you may also customize the mailbox storage quotas for specific mailboxes.    

In your case, you may first set the default storage quota of the database to 1G.     

It will set the default storage quota for user mailboxes in this database to 1G.    

Here are the steps:    

-  access EAC and locate servers>databases    

-  double click to edit the database which host the mailboxes    

-  under limits,set the quotas for the database,which also sets the quotas for the most mailboxes    

    

And then manually set custom settings for the rest user mailboxes whose quota should be between 5G and 10G:    

-  in EAC, locate recipients>mailboxes    

-  double click to edit the mailboxes    

-  under mailbox usage, click More options...    

    

-  select Customize the quota settings for this mailbox and set the custom quota (5G to 10G)    

    

-  repeat the above  steps on other mailboxes    

Here are also some documents on this topic:    

Configure storage quotas for a mailbox    

Manage mailbox databases in Exchange Server    

We do want to give the users the option to search in their old mails, but they do so in a low frequency. How can we achieve that with the maximum of data reduction and compression?    

I think you may enable archive mailboxes for users and create and apply a retention policy to user mailboxes.    

You may create two default policy tag (DPT), one to periodically move old mails from primary mailbox to archive mailbox and the other one to delete old mails which reach a specific age.    

Here are some documents for your reference:    

Archive:    

In-Place Archiving in Exchange 2013    

Retention Policy:    

Create a Retention Policy in Exchange 2013    

Add retention tags to or remove retention tags from a retention policy in Exchange 2013    

Apply a retention policy to mailboxes in Exchange 2013    

While, if you would like to keep all the mails instead of removing old mails periodically, I suppose that it may not be possible to reduce the disk usage on Exchange server.    

We do have users that come once in a few months. Those users continue to get unnecessary mails and to fill up our databases.... we thought to put them in seperate unmounted database, but than when these users do come, we don't want them to wait for us to mount their mailbox back.... what can be the right solution for this?    

Sorry I was a little confused with the scenario.    

Did you mean:    

There are some users who have mailboxes in your organization and they will use these mailboxes to send and receive mails from time to time.    

After they left, they will use other mailboxes hosted by other email service providers (for example, gmail, yahoo, etc.)    

But some senders don't know about it and will keep sending mails to the mailboxes hosted by your Exchange server.     

If I misunderstood anything,please feel free to correct me.    

In this case, I suppose the best solution is to inform the senders that they should send to the correct mailboxes.     

You may achieve it by configuring Automatic Replies(also known as Out Of Office message and OOF) for the mailboxes.    

Here is a link about how it can be done on the admin side for your reference:    

Configure Automatic Replies for a user in Exchange 2010    

It is for Exchange 2010 but works the same way in Exchange 2013.    

If the senders still keep sending mails, you can also create a mail flow rule to reject the mails which are sent to the specific recipients with an explanation.    

It would be like:    

    

When the users come to use the mailboxes, you may need to remove the Automatic Replies and disable the mail flow rule.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
