---
title: "Exchange 2010 проблема с Autodiscover у некоторых пользователей"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1367777/exchange-2010-autodiscover
question_id: 1367777
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2010 проблема с Autodiscover у некоторых пользователей

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1367777/exchange-2010-autodiscover (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Есть контроллер домена и exchange 2010 sp3. Сейчас работает почта и внутри офиса и через интернет, без VPN.

На телефонах почта настраивается и работает без проблем, при выборе метода "exchange" на всех учётках.

На компьютерах почта настраивается по "exchange" только на некоторых старых учётках, работает и через интернет и внутри офиса. 

Остальные учётки просто перестали перенастраиваться по "exchange", как внутри офиса, так и через интернет, но продолжают работать, если их не перенастраивать. При подключении через Outlook постоянно висит окошко запроса учётных данных, как-будто пароль не правильный вводишь, не принимает, поэтому новые учетки настраиваю по протоколу IMAP/SMTP, хотя эти же учётки подключаются через интернет с телефона по "exchange". Наследование прав включал в AD, не помогает.

В IIS на сайте "Autodiscover" включена и обычная аутентификация и NTLM с галочкой "проверка подлинности в режиме ядра", так как если я её убираю, то и мои старые учётки перестают работать :) 

Анализатор майкрософта  ругается на большинство учёток, что ошибка 401, они не видят autodiscover.xml, хотя некоторые мои старые учётки без проблем проходят тест и обнаруживают autodiscover.xml, такое ощущение, что в старые учётки имеют больше прав либо содержат какие-то иные настройки.

Подскажите пожалуйста, куда копать?)

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-28*

проблему решил. на основном контроллере домена, где был установлен exchange 2010 перестала работать репликация, репликацию восстановил, проверка подлинности сразу же заработала на всех учётках!

тему можно закрывать, всем спасибо за участие.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-10*

Спасибо тебе за твой комент, мучался 4 месяца с поиском проблемы, а потом благодаря твоему - копнул в репликацию и понял, что дело в ней было.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-14*

I have already written that only some of the accounts are not working, others are working fine, you are inattentive. I don't have a problem with logins and passwords or ssl.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-14*

Hi @Андрей `,

Thanks for posting in our Q&A forum, must tell you that currently our Q&A forum only support English, please post or reply with your questions in English next time.

Through the translation, it seems that you are having trouble connecting to your Exchange account via Outlook. The issue could be due to incorrect account credentials, network connectivity issues, or a problem with the Exchange server connection.

Regarding the error 401, it indicates that the client is not authorized to access the requested resource. The analyzer may not be able to detect autodiscover.xml if there is an issue with the server connection or if there are authentication issues.

Reference: https://support.microsoft.com/en-us/office/i-can-t-connect-to-my-exchange-account-372b793f-e8d3-4aed-a3a9-dbfbfad97c6d

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
