---
title: "Sending email problem with exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1241089/sending-email-problem-with-exchange
question_id: 1241089
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "windows-business-windows-server-user-experience-user-experience-other"]
---
# Sending email problem with exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1241089/sending-email-problem-with-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi , i have problem to sending mail from PHP (codeigniter4) to external mail , this is my config :

```
/**

     * The "user agent"

     */

    public string $userAgent = 'CodeIgniter';

    /**

     * The mail sending protocol: mail, sendmail, smtp

     */

    public string $protocol = 'smtp';

    /**

     * SMTP Server Address

     */

	public $SMTPHost = 'exchange.*********.com';

   	/**

     * SMTP Username

     */

    public $SMTPUser='*****************';

    /**

     * SMTP Password

     */

    public $SMTPPass='***********';

    /**

     * SMTP Port

     */

    public int $SMTPPort = 587;

    /**

     * SMTP Timeout (in seconds)

     */

    public int $SMTPTimeout = 5;

    /**

     * Enable persistent SMTP connections

     */

    public bool $SMTPKeepAlive = false;

    /**

     * SMTP Encryption. Either tls or ssl

     */

    public string $SMTPCrypto = 'tls';

    /**

     * Enable word-wrap

     */

    public bool $wordWrap = true;

    /**

     * Character count to wrap at

     */

    public int $wrapChars = 76;

    /**

     * Type of mail, either 'text' or 'html'

     */

    public string $mailType = 'html';

    /**

     * Character set (utf-8, iso-8859-1, etc.)

     */

    public string $charset = 'UTF-8';

    /**

     * Whether to validate the email address

     */

    public bool $validate = false;

    /**

     * Email Priority. 1 = highest. 5 = lowest. 3 = normal

     */

    public int $priority = 3;

    /**

     * Newline character. (Use “\r\n” to comply with RFC 822)

     */

    public string $CRLF = "\r\n";

    /**

     * Newline character. (Use “\r\n” to comply with RFC 822)

     */

    public string $newline = "\r\n";
```

This is the error:

```
220 srv-exchange3.******.local Microsoft ESMTP MAIL Service ready at Fri, 14 Apr 2023 15:40:42 +0200
```

```
hello: 250-srv-exchange3.*.local Hello []
250-SIZE 37748736
250-PIPELINING
250-DSN
250-ENHANCEDSTATUSCODES
250-STARTTLS
250-AUTH GSSAPI NTLM
250-8BITMIME
250-BINARYMIME
250 CHUNKING
starttls: 220 2.0.0 SMTP server ready
Unable to send email using SMTP. Your server might not be configured to send mail using this method.
Date: Fri, 14 Apr 2023 13:40:43 +0000
From: 
Return-Path: 
To: ***************
Subject: =?UTF-8?Q?Test?=
Reply-To: 
User-Agent: CodeIgniter
X-Sender: @.it
X-Mailer: CodeIgniter
X-Priority: 3 (Normal)
Message-ID: 
Mime-Version: 1.0
Content-Type: multipart/alternative; boundary="B_ALT_643957db4699c7.51227430"
This is a multi-part message in MIME format.
Your email application may not support this format.
--B_ALT_643957db4699c7.51227430
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-17*

Hello there,
This issue occurs if a third-party certificate that is installed on the server that is running Exchange Server is not bound to the SMTP service.
Please try the troubleshooting steps described in the below article.
https://learn.microsoft.com/en-us/exchange/troubleshoot/mailflow/outbound-email-messages-are-not-sent
Hope this resolves your Query !!
--If the reply is helpful, please Upvote and Accept it as an answer--
