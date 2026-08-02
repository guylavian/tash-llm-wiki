---
title: "Windows Server 2019 & Exchange 2016 mail delivery problems"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1295697/windows-server-2019-exchange-2016-mail-delivery-pr
question_id: 1295697
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Windows Server 2019 & Exchange 2016 mail delivery problems

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1295697/windows-server-2019-exchange-2016-mail-delivery-pr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day,

I am having a problem with our exchange server and was hoping to get some help here.

Some background:

We have our own domain with our website and also emails, now sending emails are not a problem but sometimes we need to send emails to alot of people. So I have setup a exchange server and on out look I have specified the outgoing server to the local mail server now it worked flawlessly but now all of a sudden email are showing as sent in outlook but they are not being delivered, I then figured it has something to do with the dns and noticed that the preferred dns was incorrect after fixing that emails still are not delivered and after an hour or so they are delivered. Still alot of warning and errors, now I am no expert and this is my first attempt to set it up.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-06-01*

ok, right now those queues look fine. 

The queue will not show after some time if there is no mail for it when running get-queue, but will re-appear when active or in retry etc...

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-15*

Hi @Eckhardt Van Der Poel

Glad to see you solved the problem, you can accept it as a solution if you like. This serves as a reference for others who encounter similar problems.

I had format the server and start from scratch, long story short it is working now.

Best Regards,

Dezhi

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2023-06-01*

It seems like you're experiencing issues with email delivery from your Exchange server. There can be several potential causes for this problem. Here are some steps you can take to troubleshoot and resolve the issue:

Check DNS Configuration: Ensure that your Exchange server has the correct DNS settings configured. Verify that the DNS server addresses are accurate, and make sure that the server can resolve external domain names properly. You can use tools like nslookup to test DNS resolution from the Exchange server.

Check SMTP Connectivity: Verify that your Exchange server can establish SMTP connections to external mail servers. Test sending emails to different external email addresses and check if there are any error messages or delays in the delivery.

Check Mail Flow Rules and Filters: Review any mail flow rules or filters you have configured in Exchange. Make sure that these rules are not inadvertently blocking or redirecting emails. Check for any specific conditions or criteria that could be affecting the delivery of certain messages.

Review Email Queues: Monitor the email queues on your Exchange server. Look for any stuck or backed-up messages. If you find any emails in the queues, investigate the reasons for the delays or failures. Check the error messages associated with those messages for further clues.

Monitor Exchange Server Logs: Check the Exchange server logs for any error messages or warnings related to email delivery. These logs can provide valuable information about the source of the problem and help you identify specific issues.

Check Firewall and Antivirus Configuration: Ensure that your firewall and antivirus software are not blocking or interfering with outgoing email traffic from the Exchange server. Verify that the necessary ports for SMTP (usually port 25) are open and not being blocked by the firewall.

-  Test with External Email Account: Send test emails from an external email account (e.g., Gmail, Yahoo) to your Exchange server. Monitor the delivery process and check if there are any delays or issues encountered.

By following these troubleshooting steps, you should be able to identify and address the issues affecting email delivery from your Exchange server.
