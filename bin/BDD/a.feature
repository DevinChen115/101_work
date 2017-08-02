Feature: 第一個在手機上的 bdd

  Scenario: 點擊 ＋ 號
    Given PG 開啟
    # When 點擊 ＋ 號
    When click "apps"
    Then 我應該可以看到工具列
