---
title: "TLS Cert Fail on Exchange server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2711045/tls-cert-fail-on-exchange-server
question_id: 2711045
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 5
qa_tags: []
---
# TLS Cert Fail on Exchange server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2711045/tls-cert-fail-on-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are enable the TLS on exchange server and when we checked on this link(http://www.checktls.com/perl/TestReceiver.pl?FULL) its showing TLSCert fail.

We have local exchange server 2010 and use the third party service for email filtering. Please find the snapshot

TestReceiver

CheckTLS Confidence Factor for "******@rolfebenson.com[rolfebenson.com.pri-mx.na0107.smtproutes.com:25]": 90

MX Server
Pref
Con-  <br><br>nect
All-  <br><br>owed
Can  <br><br>Use
TLS  <br><br>Adv
Cert  <br><br>OK
TLS  <br><br>Neg
Sndr  <br><br>OK
Rcvr  <br><br>OK

rolfebenson.com.pri-mx.na0107.smtproutes.com:25   <br><br>[192.69.16.71]
0
OK   <br><br>(5,094ms)
OK   <br><br>(3,391ms)
OK   <br><br>(302ms)
OK   <br><br>(302ms)
FAIL
OK   <br><br>(10,191ms)
OK   <br><br>(2,304ms)
OK   <br><br>(507ms)

Average

100%
100%
100%
100%
0%
100%
100%
100%

(double click matrix to select all for copy and paste)

Note:
 Cert failures do not affect TLS encryption, but may mean the site isn't who they say they are.

Run same test with:

Instructions About Tests

Note: you can run many tests at once and/or schedule tests with BatchTest.

Note: use the FULL version to test servers with custom IP addresses, ports, authentications, and/or timeouts.

See email policy. We will not use addresses. Use of any test is explicit agreement to Acceptable
 Use Policy.

(double click in detail below to select all for copy and paste)

Checking ******@rolfebenson.com[rolfebenson.com.pri-mx.na0107.smtproutes.com:25]

using supplied MX: "rolfebenson.com.pri-mx.na0107.smtproutes.com"

Trying TLS on rolfebenson.com.pri-mx.na0107.smtproutes.com[192.69.16.71]:25 (0):

seconds

test stage and result

[005.094]

Connected to server

[008.485]
<--
220 ams1-mh928.smtproutes.com kath-5.0.3 ESMTP Ready

[008.485]

We are allowed to connect

[008.485]
-->
EHLO checktls.com

[008.787]
<--
250-ams1-mh928.smtproutes.com says Hello [216.68.85.112]  <br><br>250-STARTTLS  <br><br>250-ENHANCEDSTATUSCODES  <br><br>250-8BITMIME  <br><br>250 OK

[008.787]

We can use this server

[008.787]

TLS is an option on this server

[008.788]
-->
STARTTLS

[009.088]
<--
220 Ready to start TLS

[009.089]

STARTTLS command works on this server

[009.786]

SSLVersion in use: TLSv1.2

[009.786]

Cipher in use: AES128-SHA

[009.787]

Connection converted to SSL

[009.809]

Certificate 1 of 4 in chain:<br>    subject= /serialNumber=LilimpZol/LrBVIEgBjG/5kZBwHnRQQ-/OU=GT83257704/OU=See www.rapidssl.com/resources/cps (c)14/OU=Domain Control Validated - RapidSSL(R)/CN=*.smtproutes.com<br>    issuer= /C=US/O=GeoTrust, Inc./CN=RapidSSL CA

[009.830]

Certificate 2 of 4 in chain:<br>    subject= /C=US/O=GeoTrust, Inc./CN=RapidSSL CA<br>    issuer= /C=US/O=GeoTrust Inc./CN=GeoTrust Global CA

[009.852]

Certificate 3 of 4 in chain:<br>    subject= /C=US/O=GeoTrust Inc./CN=GeoTrust Global CA<br>    issuer= /C=US/O=Equifax/OU=Equifax Secure Certificate Authority

[009.874]

Certificate 4 of 4 in chain:<br>    subject= /C=US/O=Equifax/OU=Equifax Secure Certificate Authority<br>    issuer= /C=US/O=Equifax/OU=Equifax Secure Certificate Authority

[009.875]

Cert VALIDATED: ok

[009.875]

Cert Hostname DOES NOT VERIFY (rolfebenson.com.pri-mx.na0107.smtproutes.com != *.smtproutes.com)

[009.875]

(see RFC-2818 section 3.1 paragraph 4 for info on wildcard<br> ("*") matching)

[009.875]

So email is encrypted but the host is not verified

[009.875]
~~>
EHLO checktls.com

[010.191]
<~~
250-ams1-mh928.smtproutes.com says Hello [216.68.85.112]  <br><br>250-STARTTLS  <br><br>250-ENHANCEDSTATUSCODES  <br><br>250-8BITMIME  <br><br>250 OK

[010.191]

TLS successfully started on this server

[010.191]

warning: STARTTLS after second EHLO (see RFC3207 #4.2)

[010.192]
~~>
MAIL FROM:<******@checktls.com>

[012.494]
<~~
250 2.1.0 Sender Accepted: ******@checktls.com

[012.495]

Sender is OK

[012.495]
~~>
RCPT TO:<******@rolfebenson.com>

[013.002]
<~~
250 2.1.5 Recipient Accepted:

[013.002]

Recipient OK, E-mail address proofed

[013.002]
~~>
QUIT

[013.286]
<~~
221 2.0.0 ams1-mh928.smtproutes.com Service closing transmission channe

## Answers

_No answers on this thread._
