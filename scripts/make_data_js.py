# -*- coding: utf-8 -*-
"""data/items_public.json から、アプリが読む data.js を作る。
python scripts/make_data_js.py <画像フォルダ(img/ thumb/ line/ がある場所)> [出力先 data.js]
公開版の配布 zip には data.js が入っているので、普段は要らない。タグを直してアプリに反映したいとき用。"""
import json, sys, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
LINE_URL = 'https://line.me/ti/g2/OhUywV8y_UynwVUw9p0FbYAI9zhruNMIqs4qTg'   # 特典版の案内先(LINEオープンチャット)

site = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE
out = Path(sys.argv[2]) if len(sys.argv) > 2 else site / 'data.js'
items = json.loads((HERE / 'data' / 'items_public.json').read_text(encoding='utf-8'))
keep = []
for it in items:
    rec = {k: it[k] for k in ('id', 'set', 'cat', 'jp', 'tags', 'sub') if k in it}
    if it.get('parent') and it['set'] != 'pose':   # 髪の色違いだけ親カードに畳む。ポーズの「横から」は独立カード
        rec['parent'] = it['parent']
    if it['set'] == 'pose' and (site / 'line' / f"{it['id']}.png").exists():
        rec['line'] = True
    rec['tier'] = 'public'
    keep.append(rec)
counts = {s: sum(1 for r in keep if r['set'] == s and not r.get('parent')) for s in ('hair', 'outfit', 'pose')}
db = {'tier': 'public', 'items': keep, 'counts': counts, 'total_full': 1097, 'built': datetime.date.today().isoformat(), 'line_url': LINE_URL, 'zip_url': ''}
out.write_text('window.DB=' + json.dumps(db, ensure_ascii=False) + ';', encoding='utf-8')
print(out, len(keep), counts)
