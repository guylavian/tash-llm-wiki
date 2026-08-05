---
title: "DCDIAG error message meaning and way to correct them"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/421712/dcdiag-error-message-meaning-and-way-to-correct-th
question_id: 421712
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# DCDIAG error message meaning and way to correct them

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/421712/dcdiag-error-message-meaning-and-way-to-correct-th (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,  

 I have a Win SBS 2011 server and I am trying to migrate to a Win 2019 Std. server. trying to run dcdiag I get error referencing  these errors  

Starting test: SysVolCheck  

```
* You must make sure there are no existing net use connections,

      you can use "net use /d \\QI-FS-02\ipc$" or "net use /d

      \\\"

    ......................... QI-FS-02 failed test SysVolCheck
```

and  

Starting test: MachineAccount  

```
Could not open pipe with [QI-FS-02]:failed with 1219:

    Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.

    Could not get NetBIOSDomainName

    Failed can not test for HOST SPN

    Failed can not test for HOST SPN
```

and  

Starting test: SystemLog  

```
A warning event occurred. EventID: 0x00009016

        Time Generated: 06/03/2021 19:45:23

        Event String:

        No suitable default server credential exists on this system. This will prevent server applications that expect to make use of the system default credentials from accepting SSL connections. An example of such an application is the directory server. Applications that manage their own credentials, such as the internet information server, are not affected by this.

    A warning event occurred. EventID: 0x00009016
```

I am wondering what it means and how to correct it.  

Any help is appreciated.  

AJINC

## Answer (community) — community member [Mvp]

*upvotes: 2 · updated: 2021-06-07*

Sounds good then.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 2 · updated: 2021-06-04*

All looks Ok. Some minor warnings but I don't see any show stoppers. You'll need to migrate FRS to DFSR before hand.  

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 2 · updated: 2021-06-04*

Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed

Might try `net use * /delete`

Please run;

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`  

`repadmin /showrepl >C:\repl.txt`  

`ipconfig /all > C:\dc1.txt`

then put `unzipped` text files up on OneDrive and share a link.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-04*

DSPatrick  

Here is the link  

https://1drv.ms/u/s!Aho0v9TZR8WEgna15BqEU84wfiFR?e=kINkOp  

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-04*

DSPatrick  

Here is the link  

https://1drv.ms/u/s!Aho0v9TZR8WEgna15BqEU84wfiFR?e=kINkOp
