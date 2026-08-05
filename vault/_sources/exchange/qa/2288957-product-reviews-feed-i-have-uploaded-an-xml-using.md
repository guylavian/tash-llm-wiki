---
title: "Product reviews feed - I have uploaded an XML using the FTP method, but the feed is not appearing in the Bing Merchant Center"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2288957/product-reviews-feed-i-have-uploaded-an-xml-using
question_id: 2288957
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Product reviews feed - I have uploaded an XML using the FTP method, but the feed is not appearing in the Bing Merchant Center

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2288957/product-reviews-feed-i-have-uploaded-an-xml-using (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm trying to upload a product reviews feed to my merchant center using the FTP method. I followed all the requested steps, but I can't find the feed in my account.

This is actually the second time I'm doing it, the last time I talked to the support they said it could take a couple of days, but it has been two weeks now, and of course, our shopping ads are still without the reviews.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-22*

Hello Dori1,

Thank you for using our Microsoft Advertising Community Forum! 

I understand that you've been struggling to upload your XML file via the FTP method. Since you had contacted our support teams before, I've sent you a private message to get some additional details from your side before delving into the matter at length. For the time being, I hope the response and resources here could be of some help to you.

You can upload via FTP/SFTP if the feed file is smaller than 1GB. We recommend this option if the feed file is larger than 4MB.

If uploading via FTP/SFTP, the file name of TXT or XML files must match the file name specified for a feed’s settings. For compressed text format, the compressed TXT file inside the archive and the archive file (ZIP, GZ, GZIP) must have the matching file name. Any feed file that is archived needs to have a single compressed file inside. The max file size should be no more than 3GB (after the file is uncompressed, if the file is compressed).

-  From the navigation menu on the left, select Tools > Merchant Center > Feeds.

-  Select Create feed.

-  At the bottom of the setup wizard, select Upload via FTP/SFTP.

-  Enter Update feed. Do not include the file extension (for example, "merchant").

-  Select Create feed.

-  Enter File name. Do not include the file extension. For example, “merchant”.

-  If necessary, you can always select Change the FTP/SFTP account settings and update your FTP user name and password. To do this, you must follow the Update a feed file instructions.

You can now upload the file via the FTP/SFTP tool of your choice using the file name you specified.

FTP/SFTP server requirements:

 The recommended FTP/SFTP upload mechanism is via an FTP/SFTP program. It is, however, possible to do so via the command line or custom scripts (such as Python's ftplib.FTP module). The FileZilla FTP client is recommended for all platforms. Use the following settings for file transfer with your FTP/SFTP client:

-  Host: ftps://feeds.adcenter.microsoft.com

-  User name: Your store's FTP/SFTP user name. Your user name must be 6 - 64 characters and cannot include any special characters. Use only a - z, A- Z, and 0 - 9.

-  Password: Your store's FTP/SFTP password

-  Transfer Mode: Passive

You can learn more about FTP/SFTP upload. The following help pages may also be of use:

About Microsoft Shopping campaigns feed files

Microsoft Merchant Center

Our support teams are happy to discuss your account in more detail via phone, chat or email to provide review assistance, please see our support page to reach out! 

I hope the information provided here will at least partly answer your question.  If you have any additional questions please do not hesitate to reach out to our support. I have also sent you a private message asking for further details. You are more than welcome to respond to me so I can begin the investigation on my end.

Kind regards, 

Vahid | Microsoft Advertising Support Specialist | 800-518-5689
