---
title: "Having a weird behavior on outlook with Exchange server 2016 when receiving mails with french characters é,è,ä,è"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1444646/having-a-weird-behavior-on-outlook-with-exchange-s
question_id: 1444646
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Having a weird behavior on outlook with Exchange server 2016 when receiving mails with french characters é,è,ä,è

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1444646/having-a-weird-behavior-on-outlook-with-exchange-s (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello All,

For some reasons and not all the time, when receiving external mails with french characters inside, these characters are getting replaced by Ã§u, or Ã©, or Ãªt ......

In some cases the message description is the following:

 x-ms-exchange-antispam-messagedata-chunkcount: 1 

x-ms-exchange-antispam-messagedata-0: =?iso-8859-1?Q?y0yDAp7J8clpDrIlBrx2683ZK5v2NCGUn7B2QGpPWktk/szaqYXfPgWzCX?= 

=?iso-8859-1?Q?XM4IXfv1gWhVUe0AWp0dRtrjIVyfcvgcbCACf0HYK0kP/0mg15I35iEWE2?= 

=?iso-8859-1?Q?RbSCpA6ggwDhuBS+lBBU5Z5WLuBAdSEdcq+gBn/hESksLglLdLz54Uk9GG?= 

=?iso-8859-1?Q?qlOtaDsc/vO66UAMPuzrCl7MPL4ZIsVXdnWgbJpTz699fb4QTLeKvxlqy3?=

and some other times it's 

x-ms-exchange-antispam-messagedata-chunkcount: 1 

x-ms-exchange-antispam-messagedata-0: =?utf-8?B?MHZxN2JPcmw3ZDVmNVZMaWxUcWt0NEtFdStBbnVDYTFxeEcrZERnSkR3UlBa?= 

=?utf-8?B?WU1CYVRJMk1lUjhMZ0dDcHRWWU5HT0I1TmhaZjJBaWZkVVVleHBhS2wrWjFK?= 

=?utf-8?B?dFhickw1ZFM5ajhscU9ycjhGRUhMQXQvWVdpU1dNSnVaZVZyT3JpTjhGUm1q?=

I found in the below article a kind of similar case but I don't know if it's applicable to my issue since we have a Disclaimer message added to the mail when receiving from an external sources

https://learn.microsoft.com/en-us/answers/questions/394418/exchange-messages-encoding-error

Does anyone having or faced the same issue ? Please if you can help me on this it would be great

Thank you!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-30*

To resolve this issue, you can try the following solutions:

-  Configure your Exchange server to expect iso-8859-1 and utf-8 encoding: You can adjust your Exchange server's character set settings to support iso-8859-1 and utf-8. This ensures that your server can adequately interpret messages encoded using these schemes.

-  Request the sender to encode messages using utf-8: If you can access the sender's email system, you can request that the encoding be changed to utf-8. This method is preferred since it assures uniform encoding throughout all email messages.

-  Convert the encoded text: If you only need to examine the message content and don't care about preserving the original encoding, you can use a tool or script to convert the encoded text from iso-8859-1 or utf-8 to the encoding scheme supported by your Exchange server.

-  Disable anti-spam filtering: In some circumstances, your Exchange server's anti-spam filtering may interfere with character encoding. If you can disable anti-spam filtering momentarily for testing purposes, determine if the character corruption problem persists. If not, you may need to change the anti-spam filtering settings to allow for proper character encoding.

Let me know if the above solutions work for you or not.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-11-30*

Hi @Touma Rami  ，

According to the situation you described, different error information may be due to the character encoding in the META tag of this type of mail is different from the character encoding in the MIME part. In order to quickly narrow down the issue, confirm whether it is indeed related to disclaimer, it is recommended that you try to disable the mail flow rule related to disclaimer or add an Except for a specific user to  test it.

If the test results show that there will be no garbled problems without disclaimer, then you could refer to the method of modifying EdgeTransport.exe.config mentioned in the similar case.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
