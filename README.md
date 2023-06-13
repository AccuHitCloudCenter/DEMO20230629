# Cloud Open AI Project

這是為學校做的機器人，主要用於回答已知道的校務問題

## 情境需求

希望基於校方會提供的FAQ（https://statics.teams.cdn.office.net/evergreen-assets/safelinks/1/atp-safelinks.html），對應的問答，如下例：

Q. 如何申號帳號 ? 帳號的使用期限 ? 帳號終止前會通知 ?

```
Ans:
1. 專任教職員

採申請制，依帳號申請單辦理，使用期限為到職日起至離職日後14日止。退休同仁欲保留電子郵件帳號，應於退休前填具申請單辦理。
於離職前一個月暨前三日、帳號終止前三日，發帳號終止使用通知email。

2. 兼任教師

採申請制，依帳號申請單辦理，使用期限為起聘日至連續二學期未開課確定日止。
於帳號終止日前一個月(4/1、11/1)，發帳號終止使用通知email。

3. 計畫人員、專案人員

採申請制，依編制外帳號申請單辦理，使用期限為申請單上之帳號起迄日期。

於帳號終止前30日、15日、3日，發帳號終止使用通知email。

4. 學生

採入學即自動建立制，使用期限至教務處畢業生轉檔日止；或退學生轉檔日後10日止，屆時自動註銷不另行通知。
```

因此，當使用者輸入`要怎麼申號帳號 ?`或是`帳號申請方式？期限？`，就會回答上述的答案。只有當問題超出事前提供的FAQ，則會轉詢問ChatGPT。