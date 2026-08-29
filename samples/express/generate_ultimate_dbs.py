import random
import os

last_names = ["陳", "林", "黃", "張", "李", "王", "吳", "劉", "蔡", "楊", "許", "鄭", "謝", "洪", "郭", "邱", "曾", "廖", "賴", "徐", "周", "葉", "蘇", "莊"]
first_names = ["俊傑", "宗翰", "冠宇", "家豪", "柏翰", "承恩", "宇軒", "雅婷", "怡君", "心如", "欣穎", "子瑜", "品妍", "詩涵", "建國", "志明", "春嬌", "淑芬", "嘉誠", "偉翔", "建宏", "佳穎", "宜蓁", "家維", "冠廷"]

banks = ["中國信託(822)", "國泰世華(013)", "台新銀行(812)", "富邦銀行(012)", "玉山銀行(808)", "中華郵政(700)", "第一銀行(007)", "華南銀行(008)", "兆豐銀行(017)"]

# --- 1. 電商詐騙 逼真資料 ---
ecom_platforms = ["蝦皮購物", "7-11 賣貨便", "全家好賣+", "Momo購物網", "PChome24h", "博客來", "誠品線上", "旋轉拍賣"]
ecom_items = [
    "Apple iPhone 15 Pro 256G 原色鈦金屬", "AirPods Pro 第2代", "Switch 薩爾達傳說特仕機", 
    "Jo Malone 英國梨與小蒼蘭 100ml", "理膚寶水 B5 全面修復霜", "SK-II 青春露 230ml", 
    "大研生醫 德國頂級魚油 3盒", "Nike Air Force 1 白", "無印良品 懶骨頭沙發", "《原子習慣》精裝版"
]
ecom_errors = ["升級成批發商會員，年費12000元", "結帳誤勾分期，連續12個月扣款", "條碼刷錯成代理商，每月扣款5000元"]
locations = ["7-11 大安門市", "全家 信義松仁店", "萊爾富 逢甲店", "OK 超商 師大店", "7-11 站前門市", "黑貓宅急便"]

def gen_ecom():
    content = "=== 台灣電商詐騙：外洩訂單資料庫 (500筆) ===\n姓名,電話,平台,商品,取貨地點,綁定銀行,錯誤類型\n"
    for _ in range(500):
        name = random.choice(last_names) + random.choice(first_names)
        phone = f"09{random.randint(10,99)}-{random.randint(100,999)}-{random.randint(100,999)}"
        content += f"{name},{phone},{random.choice(ecom_platforms)},{random.choice(ecom_items)},{random.choice(locations)},{random.choice(banks)},{random.choice(ecom_errors)}\n"
    return content

# --- 2. 投資詐騙 逼真資料 ---
inv_groups = ["【老王】飆股私董會", "元大投顧內部群", "柴鼠兄弟財富自由班", "【蔡明彰】主力籌碼分析", "外資券商黑馬俱樂部"]
inv_stocks = ["2330 台積電", "2382 廣達", "00940 台灣價值高息", "0050 台灣50", "2317 鴻海", "NVDA 輝達", "比特幣 USDT 合約"]
inv_hooks = ["免費領取飆股代碼", "主力即將拉抬，現在進場賺30%", "AI 選股軟體免費體驗一個月", "跟著老師做當沖，一個月買車"]

def gen_inv():
    content = "=== 台灣投資詐騙：外洩名單與洗腦話術庫 (500筆) ===\n姓名,電話,加入群組名,誘導投資標的,鉤子話術,受害者痛點\n"
    pain_points = ["房貸壓力大", "剛生小孩缺奶粉錢", "當沖賠掉半個月薪水", "定存被通膨吃掉", "對現狀不滿想財富自由"]
    for _ in range(500):
        name = random.choice(last_names) + random.choice(first_names)
        phone = f"09{random.randint(10,99)}-{random.randint(100,999)}-{random.randint(100,999)}"
        content += f"{name},{phone},{random.choice(inv_groups)},{random.choice(inv_stocks)},{random.choice(inv_hooks)},{random.choice(pain_points)}\n"
    return content

# --- 3. 路邊推銷 逼真資料 ---
street_locations = ["台北車站 M8 出口", "中山捷運站 4 號出口", "西門町 6 號出口", "台中一中街", "高雄新堀江", "信義威秀影城旁"]
street_hooks = ["同學幫忙填個時尚問卷", "我們是台灣文創系的學生", "你在找人嗎？要不要體驗深層淨膚", "差最後一個業績就能下班"]
street_products = ["愛心精油筆", "手工環保零錢包", "死海泥去角質洗面乳", "法國進口抗痘凝膠", "手工皂禮盒"]

def gen_street():
    content = "=== 台灣路邊強迫推銷：目標特徵與話術庫 (500筆) ===\n攔截地點,目標特徵,搭訕開場白,強迫推廣商品,拒絕時的勒索話術\n"
    targets = ["落單男學生", "看起來趕時間的上班族", "逛街落單女子", "牽手的情侶檔"]
    guilt_trips = ["你連一百塊都不肯支持學生嗎？", "我今天站了八小時都沒業績你忍心嗎？", "都幫你試用在手上了你說不要？", "這可以刷卡或Line Pay不用現金啦"]
    for _ in range(500):
        content += f"{random.choice(street_locations)},{random.choice(targets)},{random.choice(street_hooks)},{random.choice(street_products)},{random.choice(guilt_trips)}\n"
    return content

# --- 4. 熟人直銷 逼真資料 ---
mlm_relationships = ["高中沒聯絡的綠洲熱音社學弟", "大學迎新宿營同組同學", "前公司的隔壁部門老同事", "當兵同梯只借過一次肥皂的朋友"]
mlm_products = ["微分子量子太赫茲活化水", "元宇宙區塊鏈被動合約", "頂級抗老除皺微商代理", "生機飲食大健康排毒餐", "虛擬貨幣自動搬磚機器人"]
mlm_buzzwords = ["選擇大於努力", "被動收入", "財富自由", "大健康產業", "你不理財財不理你"]

def gen_mlm():
    content = "=== 台灣熟人直銷/老鼠會：洗腦與關係對應庫 (500筆) ===\n朋友姓名,關係,直銷話術精華金句,推銷毒藥產品,洗腦與打擊自尊策略\n"
    attacks = ["貶低對方月薪才三萬", "攻擊對方買不起房", "質疑對方沒企圖心", "情勒對方不為父母著想"]
    for _ in range(500):
        name = random.choice(last_names) + random.choice(first_names)
        content += f"{name},{random.choice(mlm_relationships)},{random.choice(mlm_buzzwords)},{random.choice(mlm_products)},{random.choice(attacks)}\n"
    return content

# --- 寫入檔案 ---
base_dir = r"e:\專案\perxona\perxona-connect-kit\samples\express"
files = {
    "db_ecommerce_massive.txt": gen_ecom(),
    "db_investment_massive.txt": gen_inv(),
    "db_street_massive.txt": gen_street(),
    "db_mlm_massive.txt": gen_mlm()
}

for filename, content in files.items():
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)
