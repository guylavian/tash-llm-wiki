---
title: "How to Configure Account Policies Using GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5696544/how-to-configure-account-policies-using-gpo
question_id: 5696544
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# How to Configure Account Policies Using GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5696544/how-to-configure-account-policies-using-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

GPOの優先順位にて、以下のようにアカウントポリシーを使い分けたいが、

GPOのセキュリティフィルタにて実現可能でしょうか？

例）

　コンピュータ１(ユーザA)：既存GPO(Default Domain Policy)

　コンピュータ２(ユーザB)：新規GPO

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-01-07*

こんにちは itec奥野 陽介。

グループ ポリシー オブジェクト（GPO）は、リンク順序、継承、およびセキュリティ フィルタリングの組み合わせによって適用されます。 セキュリティ フィルタリングを使用すると、GPO を適用するユーザーやコンピューターを制限することはできますが、GPO の基本的な処理順序自体を上書きすることはできません。

ご提示の例では、セキュリティ フィルタリングを適用することで、 コンピューター 1（ユーザー A）には引き続き既存の GPO（Default Domain Policy）を適用し、 コンピューター 2（ユーザー B）には新しい GPO を適用する、といった使い分けが可能です。

具体的には、それぞれの GPO のセキュリティ フィルタリングを設定し、適用対象としたい特定のユーザーまたはコンピューターのみを含めるように構成します。 なお、複数の GPO が同一のオブジェクトに適用される場合、競合時の優先順位は OU 構造やリンク順序によって決まり、最後に適用された GPO が優先されます。

そのため、希望どおりの動作を実現するには、セキュリティ フィルタリングに加えて、OU 設計や GPO のリンク順序を調整する必要がある場合があります。

結論として、セキュリティ フィルタリングを用いてポリシーの適用を切り分けることは可能ですが、一貫した結果を得るために GPO の優先順位ルールも併せて考慮することが重要です。

本説明がお役に立ちましたら、「Accept Answer」をクリックしていただけますと幸いです。

Jason.

## Answer (community) — community member

*upvotes: 0 · updated: 2026-01-07*

To configure account policies using Group Policy Objects (GPO) and manage their application based on user or computer criteria, you can indeed utilize security filtering. Security filtering allows you to specify which users or computers can apply a particular GPO based on their permissions in Active Directory.

In your example, you want to apply the existing GPO (Default Domain Policy) to Computer 1 (User A) and a new GPO to Computer 2 (User B). You can achieve this by setting up the security filtering for each GPO:

-  For the existing GPO (Default Domain Policy): Ensure that the security filtering includes only the users or computers that should apply this policy. You can remove other users or groups that should not receive this policy.

-  For the new GPO: Create the new GPO and set its security filtering to include only User B or Computer 2. This way, only the specified user or computer will apply this new GPO, while others will not.

By carefully configuring the security filtering for each GPO, you can effectively manage which policies apply to which users or computers in your environment.
