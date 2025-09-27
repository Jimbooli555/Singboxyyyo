import base64
import requests
import json

# لینک ساب VLESS
url = "https://raw...لینک_ساب_تو_اینجا_بزار"

# دانلود ساب
res = requests.get(url)
data = base64.b64decode(res.text).decode("utf-8")

# استخراج تمام لینک‌های vless
vless_links = [line for line in data.splitlines() if line.startswith("vless://")]

# تبدیل به JSON Sing-box
singbox_list = []
for link in vless_links:
    # فعلا فقط نام و لینک رو ذخیره میکنیم
    singbox_list.append({"vless": link})

# ذخیره خروجی
with open("singbox_sub.json", "w") as f:
    json.dump(singbox_list, f, indent=2)

print(f"تبدیل شد {len(vless_links)} لینک")
