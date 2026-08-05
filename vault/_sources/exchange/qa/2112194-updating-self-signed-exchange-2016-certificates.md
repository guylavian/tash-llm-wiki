---
title: "Updating Self-signed Exchange 2016 certificates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2112194/updating-self-signed-exchange-2016-certificates
question_id: 2112194
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
---
# Updating Self-signed Exchange 2016 certificates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2112194/updating-self-signed-exchange-2016-certificates (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Доброго дня! 

Подскажите правильный алгоритм продления самоподписанных сертификатов почтовой системы. По интернету много противоречивых сведений, зачастую предлагается противоположные решения. Тестового полигона у меня нет и проверить мне негде. 

У меня два сервера и на каждом есть такие сертификатов (которые скоро заканчиваются): сервер RN14: 

1 Microsoft Exchange Server Auth Certificate, Самозаверяющий сертификат, Срок действия истекает: 09.11.2024 Назначено службам SMTP 

2 Microsoft Exchange, Самозаверяющий сертификат, Издатель: CN=RN14, Срок действия истекает: 06.12.2024 Назначено службам IMAP, POP, IIS, SMTP 

3 Exchange Delegation Federation, Самозаверяющий сертификат, Издатель: CN=Federation, Срок действия истекает: 26.08.2025 Назначено службам SMTP, Federation 

4 Microsoft Exchange, Самозаверяющий сертификат, Издатель: CN=RN14, Срок действия истекает: 29.01.2029 Назначено службам IMAP, POP, SMTP 

5 WMSVC-SHA2, Самозаверяющий сертификат Издатель: CN=WMSvc-SHA2-RN4 Назначено службам НЕТ 

сервер RN15 

1 Microsoft Exchange Server Auth Certificate, Срок действия истекает: 09.11.2024 Назначено службам SMTP 

2 Microsoft Exchange Самозаверяющий сертификат Издатель: CN=RN15 Назначено службам IMAP, POP, IIS, SMTP 

3 Exchange Delegation Federation Срок действия истекает: 26.08.2025 Назначено службам SMTP, Federation 

4 WMSVC-SHA2 Срок действия истекает: 03.12.2029 Назначено службам НЕТ 

Насколько я понимаю продлить истекающие сертификаты можно через ECP, нажать "продлить" и затем перезапустить IIS ну или на крайний случай сервер презапустить. Проделать такую же манипуляцию и на втором сервере. 

Правильно я мыслю? интересует еще момент - что после нажатия "продлить" - будут ли еще какие-то манипуляции?

## Answers

_No answers on this thread._
