import requests
import json

# VLESS subscription link
url = "https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/main/category/ws.txt"

# Download subscription file (this file is plain text, not Base64)
res = requests.get(url)
data = res.text.strip()

# Extract all vless links
vless_links = [line for line in data.splitlines() if line.startswith("vless://")]

# Convert to Sing-box JSON (basic format for now)
singbox_list = []
for link in vless_links:
    singbox_list.append({"vless": link})

# Save output
with open("singbox_sub.json", "w", encoding="utf-8") as f:
    json.dump(singbox_list, f, indent=2, ensure_ascii=False)

print(f"Converted {len(vless_links)} links")
