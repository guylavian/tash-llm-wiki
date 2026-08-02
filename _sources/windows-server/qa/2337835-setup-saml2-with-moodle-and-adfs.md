---
title: "Setup SAML2 with Moodle and ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2337835/setup-saml2-with-moodle-and-adfs
question_id: 2337835
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Setup SAML2 with Moodle and ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2337835/setup-saml2-with-moodle-and-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to configure Moodle and ADFS to use the SAML 2 login. We keep getting the following error messages

Exception - Failure Signing Data: error:25078067:DSO support routines:win32_load:could not load the shared library - SHA256

Stack trace:

·         line 197 of \auth\saml2\vendor\simplesamlphp\simplesamlphp\src\SimpleSAML\Auth\Source.php: SimpleSAML\Error\UnserializableException thrown

·         line 165 of \auth\saml2\vendor\simplesamlphp\simplesamlphp\src\SimpleSAML\Auth\Simple.php: call to SimpleSAML\Auth\Source->initLogin()

·         line 104 of \auth\saml2\vendor\simplesamlphp\simplesamlphp\src\SimpleSAML\Auth\Simple.php: call to SimpleSAML\Auth\Simple->login()

·         line 652 of \auth\saml2\classes\auth.php: call to SimpleSAML\Auth\Simple->requireAuth()

·         line 43 of \auth\saml2\login.php: call to auth_saml2\auth->saml_login()

×Dismiss this notification

Output buffer:  Warning: openssl_sign(): Supplied key param cannot be coerced into a private key in E:\Moodle\auth\saml2\vendor\robrichards\xmlseclibs\src\XMLSecurityKey.php on line 563

## Answers

_No answers on this thread._
