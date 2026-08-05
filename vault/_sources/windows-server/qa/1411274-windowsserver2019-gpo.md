---
title: "WindowsServer2019のGPOにある既定のアプリの設定について"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1411274/windowsserver2019-gpo
question_id: 1411274
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# WindowsServer2019のGPOにある既定のアプリの設定について

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1411274/windowsserver2019-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

例えば、設定ファイルに以下の拡張子pdfに対して複数行追記した場合、

<Association Identifier=".pdf" ProgId="MSEdgePDF" ApplicationName="Microsoft Edge" /> 

<Association Identifier=".pdf" ProgId="AcroExch.Document.2017" ApplicationName="Adobe Acrobat Reader 2017" /> 

<Association Identifier=".pdf" ProgId="Acrobat.Document.DC" ApplicationName="Adobe Acrobat" /> 

挙動はどのような適用の流れになりますでしょうか。

上記に限らずですが、htmlの拡張子などを複数行別々のアプリに設定して

各クライアントに別々のアプリをインストールした状態でも同様化と思いますが、、、

・一番上だけを適応する挙動となり、入っていないクライアントは変更しない

・上から順番に確認していき、入っているクライアントに対して変更する

・複数行あるためエラーとなり全てのクライアントに対して変更しない

のいずれかとは思いますが、念のため、こちらでも確認の意味でお伺いします。

よろしくお願いいたします。

## Answers

_No answers on this thread._
