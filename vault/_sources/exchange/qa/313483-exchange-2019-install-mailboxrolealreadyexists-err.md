---
title: "Exchange 2019 Install, MailboxRoleAlreadyExists error, what is the check?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/313483/exchange-2019-install-mailboxrolealreadyexists-err
question_id: 313483
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 Install, MailboxRoleAlreadyExists error, what is the check?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/313483/exchange-2019-install-mailboxrolealreadyexists-err (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Installing Exchange 2019 in a domain where there is an existing 2016 exchange to migrate.   

Old 2016 name is MAIL, 2019 name is MAILBOX, and is a freshly built 2019 Server that is already in the domain.   

"MAILBOX" May (emphasis on may - no one seems to know) have been the name of a prior Exchange server, if so it was likely version 2010 or before.  Before doing this we made sure the name was not in AD, was not in DNS (including CNAME) and checked the usual places in AD for references, e.g.  CN=Configuration, CN=Services, CN=Microsoft Exchange, CN=First Organization, CM=First Administrative Group (no servers), CN = Exchange Administrative Group (MAIL only as CN=Server).   

I've tried looking in all connectors, through the exchange GUI, and also simple stuff like powershell to get-exchangeserver.   Nothing shows MAILBOX.   I've reviewed articles on manually deleting old servers but all the locations I have checked had nothing already there.  So I am not (yet) cleaning up, I am trying to find any remnant and cannot.   

I've reviewed the install log but it simply says:   

[03/13/2021 23:43:36.0669] [1] Evaluated [Rule:MailboxRoleAlreadyExists] [HasException:False] [Value:"True"] [ParentValue:"<NULL>"] [Thread:53] [Duration:00:00:00.2031216]  

It does not seem to show anywhere that I can find what the rule is checking.  There's a help reference to a MS web URL that just says there is no documentation on it.   

Is there a way to dump the rule itself to see what it checks?   

Any other suggestions where to look?   

My alternative is to rename the server, which I am pretty sure will work, but I also worry if there is exchange garbage still in AD, and would like to clear it out.  Though it's been there for years clearly.  

Again -- this is a clean W2019 install, not a failed partial install that I am trying to recover from.  There is no mailbox role on this server (yet).   

Linwood

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Yes, my account is a member of both.  It's also been used for CU updates on the exchange 2016 server.   

My understanding is for adding a 2019 exchange server no AD prep is required (or more precisely that the GUI/wizard will do it for you -- it says that in the link you provided's link to prep).   

But just to be thorough I ran the command line /prepareSchema and that worked fine, so I don't think it is a permissions problem, but the readiness checks in the gui still fails with "The mainbox server is already installed on this computer".   

That's a pretty specific error, it doesn't sound like some kind of permissions issue.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-15*

Hi,    

Can you confirm that the account you're using is a member of both the Schema Admins and Enterprise Admins security group? For example, the domain administrator.    

Did you run Prepare schema and domains before running the setup?     

You can run those steps and install the server via powershell: https://learn.microsoft.com/en-us/Exchange/plan-and-deploy/deploy-new-installations/unattended-installs?view=exchserver-2019    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
