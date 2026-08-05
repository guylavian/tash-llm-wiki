---
title: "active directoryについて"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2190968/active-directory
question_id: 2190968
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# active directoryについて

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2190968/active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

クライアントPCで外字エディターを起動すると、「外字エディターを使うには、Fonts フォルダーへの書き込みアクセス権が必要 です。 管理者に問い合わせ、 このアクセス権を取得してください。」とエラーが出て使用できません。active directoryで制限されていると思うのですが、解除方法を教えていただけますでしょうか。 よろしくお願いいたします。

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-12*

デイジー・チョウ様

「フォントフォルダ」はクライアントPCに保存されており、共有されていません。

クライアント PC のローカル管理者アカウントでログオンして、「フォント フォルダー」のアクセス許可を変更しようとすると、下記のメッセージが出て変更できません。

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-11*

Hello 寺田_220,  

Thank you for your reply.  

1.The "Fonts folder" is stored on client PC and not shared, am I right?  

If your current account is a normal domain account in the domain or a normal local account in this PC.  

You can contact your local Administrator in this client PC and log on this client PC to change permissions (make your current account have read and write permissions) on "Fonts folder".  

You can add your current account into Local Administrators group in this client PC and try to change permissions  (make your current account have read and write permissions) on "Fonts folder".  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-11*

デイジー・チョウ様

ご回答いただきありがとうございます。

1.クライアントPCがドメイン内にあります。

2.「外字エディタ」はこのクライアント PC にもともとインストールされていたものです。

3.「フォントフォルダー」はクライアント PC 上に保存されています。

Fontsのプロパティ→「セキュリティ」タブ→Usersにフルコントロールのアクセス許可を与えようとすると「コンテナー内のオブジェクトを列挙できませんでした。アクセスが拒否されています。」とエラーが出ます。

ドメインユーザーに管理者権限を与えると「外字エディター」を利用できるようになりますが、管理者権限は与えずに、「外字エディター」の使用権限だけ与えたいと考えています。

よろしくお願いいたします。

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-10*

Hello 寺田_220,  

Thank you for posting in Microsoft Community forum.  

1.Please check if your client PC in the domain or not?  

-  Whether "Gaiji Editor" is installed manually on this client PC or installed via domain GPO software installation?  

3.Where is "Fonts folder" stored? On Domain Controller or on your client PC?  

If "Fonts folder" is stored on Domain Controller or other domain member server, please contact your domain Administrator and log on Domain Controller or other domain member server to give your account access permission on "Fonts folder".  

I hope the information above is helpful.  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou
