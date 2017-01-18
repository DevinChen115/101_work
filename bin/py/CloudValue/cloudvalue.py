# coding=UTF-8
xmas={
    "NOTE"                                          :   "為了 Xams 做的雲控",
    "cmc_xmasslots_start"                           :   "聖誕屏保開始時間",
    "cmc_xmasslots_expire"                          :   "聖誕屏保失效時間",
    "cmc_xmasslots_failcount_popup"                 :   "沒中獎後展現廣告次數控制",
    "cmc_xmasslots_winrate_2"                       :   "第二次中獎機率",
    "cmc_xmasslots_winrate_3"                       :   "第三次",
    "cmc_xmasslots_winrate_4"                       :   "第四次",
    "cmc_xmasslots_winrate_5"                       :   "第五次",
    "ss_cloud_noti_style"                           :   "通知欄和全屏說明頁配圖和顏色",
    "ss_cloud_noti_string"                          :   "通知欄&全屏說明頁文案"
    }

pull={
    "NOTE"                                          :   "重新拉動屏保引導( 每+1 就重新引導 )",
    "screen_saver_noti_interval_version"            :   "插電通知欄版本識別，重洗已退訂用戶",
    "screen_saver_noti_interval_version_pull"       :   "再拉插電通知欄版本識別",
    "cmc_launch_dialog_interval_version"            :   "閃屏、結果頁彈窗引導版本識別，重洗已退訂用戶",
    "cmc_launch_dialog_interval_version_pull"       :   "閃屏、結果頁彈窗引導版本識別"
    }

plug_noti_pull={
    "NOTE"                                          :   "插電通知欄相關",
    "screen_saver_noti_switch"                      :   "插電通知欄拉動場景開關",
    "screen_saver_noti_interval_count"              :   "插電通知欄展現次數",
    "screen_saver_noti_interval_hour"               :   "插電通知欄間隔時間(小時)",
    "screen_saver_promote_case"                     :   "場景拉動A/B文案測試(過充、內容引導)"
}

result_page_pull={
    "NOTE"                                          :   "結果頁彈窗",
    "cmc_resultpage_switch"                         :   "結果頁彈窗總開關",
    "unsubscribed_users"                            :   "已開啟過的用戶不展示",
    "cmc_result_overlap"                            :   "開屏引導後幾小時不彈  N：幾小時",
    "cmc_result_interval"                           :   "相隔多少小時展示一次  N：幾小時",
    "cmc_result_total_count"                        :   "總共展示上限  N：幾次",
    "cmc_result_entry_count"                        :   "進入結果頁幾次才第一次彈    N：幾次",
    "cmc_dialog_interval_version"                   :   "結果頁彈窗版本識別(被 cmc_launch_dialog_interval_version 取代)"
}

splash_pull={
    "NOTE"                                          :   "開屏引導",
    "cmc_launch_switch"                             :   "開屏引導總開關",
    "new_open"                                      :   "新用戶第 N 次開啟PG 展現全屏彈窗 本地:6",
    "old_open"                                      :   "老用戶第 N 次開啟PG 展現全屏彈窗 本地:1",
    "screen_saver_promote_launch_dialog"            :   "開屏、結果頁彈窗拉動A/B文案測試"
}

noti_permission={
    "NOTE"                                          :   "通知欄權限",
    "cmc_card_noti_permission_string"               :   "通知欄權限引導文案",
    "cmc_dialog_permission_caution_string"          :   "權限引導彈窗提示",
    "initial_timer"                                 :   "通知欄權限引導卡片出現時間",
    "display_period"                                :   "通知欄權限引導卡片單次展現多久時間   單次展現多久(時)",
    "display_interval"                              :   "距離下次展示的間隔時間 距離下次展示的間隔時間(時)",
    "total_count"                                   :   "展現次數"
}

pic_popup={
    "NOTE"                                          :   "分辨率彈窗",
    "cmc_save_pic_popup_window"                     :   "儲存照片彈窗開關",
    "cmc_save_pic_popup_window_screensaver_item"    :   "儲存照片 開啟屏保項目 開關"
}

picOrNews={
    "NOTE"                                          :   "新聞/圖片屏保, 鎖屏切換",
    "request_content_switch"                        :   "屏保的新聞、PG社群內容拉取開關(1 新聞 2 圖片)",
    "pgcontent_rotate_interval"                     :   "卡片輪替順序控制",
    "locker_switch"                                 :   "切換成鎖屏的雲控"
}

OnOff={
    "NOTE"                                          :   "屏保總開關",
    "enable"                                        :   "功能開關",
    "cloud_screen_saver_show_on_any_app_key"        :   "亮屏已解鎖插電展示屏保",
    "cloud_screen_saver_plug_off_show_enable_key"   :   "亮屏已解鎖拔電展示屏保"
}

screensaver=[xmas,pull,plug_noti_pull,result_page_pull,splash_pull,noti_permission,pic_popup,picOrNews,OnOff]