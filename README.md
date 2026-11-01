# キャラ組み立てDB(CharaDB)

二次元キャラ用の **髪型・目・衣装・ポーズ** の画像素材 **1,027枚** と、そのDanbooruタグ。カードを選ぶだけでプロンプトが組み上がるアプリつき。

- アプリ(公開版): https://charadb-2fi.pages.dev/
- 画像つきの一式(zip・約220MB): このリポジトリの **Releases** からhttps://github.com/taki-ttt/charadb/releases
- 作者: たき(X: [@taki_auto](https://x.com/taki_auto))。AI画像でCG集を作って販売しているクリエイター

![キャラ組み立てDB](https://charadb-2fi.pages.dev/og.jpg)

## 何ができるか

1. 「髪型」「衣装」「ポーズ」のタブでカードを見る。カードには画像・日本語名・Danbooruタグが入っている
2. 「〜に入れる」でパーツを選ぶ(髪型は茶・黒・金・ピンク・銀の5色)
3. 「組み立てを見る」→ 表情・構図・背景を選ぶ → 「プロンプトをコピー」

品質タグは Illustrious / NoobAI 系・Anima 系・NovelAI・Pony 系から選べ、ネガティブも一緒に出ます。
ポーズは「絵」と「線画」を切り替えられ、線画は ControlNet(lineart / canny)の入力にそのまま使えます。

## 中身(公開版 1,027枚)

| タブ | 枚数 | 内訳 |
|---|---|---|
| 髪型 | 306 | 髪型 46種×5色(230)・前髪 12・髪色 20・髪飾り 16・目の色 19・瞳の形 9 |
| 衣装 | 440 | 制服・学生 40／カジュアル(春夏) 40／カジュアル(秋冬) 40／きれいめ・オフィス 25／ドレス・パーティ 30／和服 25／水着 35／スポーツ・部活 25／職業・コスプレ 45／ファンタジー 35／部屋着・パジャマ 20／イベント・季節 30／アイドル・ステージ 15／ゴスロリ・地雷系 20／ミリタリー・SF 15 |
| ポーズ | 281 | 立ち 68(横からの絵を含む)／座り 38／寝そべり 27／しゃがみ・膝立ち 23／上半身・手の仕草 45／動き 20／日常の動作 25／2人 35 |

全部の画像を同じモデル・同じ設定・同じ seed で生成しているので、カードどうしを見比べて選べます。衣装・ポーズの画像は `brown hair, medium hair, blunt bangs, brown eyes` の固定キャラに着せています(カードのタグには衣装・ポーズのタグだけが入っていて、キャラのタグは入っていません)。

生成環境: Stable Diffusion WebUI(A1111)・checkpoint JANKU v4(NoobAI-XL / Illustrious 系)・1024×1536・seed固定。

## リポジトリの構成

```
app/index.html            アプリ本体(1ファイル。data.js と img/ thumb/ line/ を同じ階層に置くと動く)
data/items_public.json    公開版 1,027 品目(id / set / cat / sub / jp / tags / parent / color)
scripts/make_data_js.py   items_public.json → data.js を作る(手元で動かすとき用)
```

画像(img/ thumb/ line/)はリポジトリに入れていません(約220MB)。**Releases の zip** に、アプリ・data.js・画像が全部入っています。zip を解凍してブラウザで `index.html` を開けば、そのまま動きます(`file://` でも動作)。

### 手元で動かす

```bash
# Releases の charadb_public.zip を解凍して
cd charadb_public
python -m http.server 8765   # http://localhost:8765/
```

### ワイルドカードとして使う

`data/items_public.json` の `tags` を 1行1品目で書き出したものを Releases に同梱しています(`wildcards/`)。Dynamic Prompts の wildcards フォルダに置いて `__charadb_outfit__` のように呼べます。

## 利用条件

- タグ・日本語名・アプリのコード: 自由に使えます(下の LICENSE を参照)
- 画像: 無償で使えます。クレジット表記は不要です
- 画像そのもの(元サイズ・加工後を含む)の再配布・転載・再販はしないでください
- 実在の人物を表す用途、未成年を表す用途には使わないでください
- タグ・プロンプト・アプリは商用利用OK。画像は参照用(見本・ControlNetの下絵)としてお使いください。画像そのものを作品に入れて販売することはできません(生成モデルの規約によります)

## 特典版(1,097枚)

ランジェリー・セクシー系の衣装、攻めたポーズ、原寸画像の一括ダウンロードは、公開版には入れていません。
作者のLINEオープンチャットで配っています → https://line.me/ti/g2/OhUywV8y_UynwVUw9p0FbYAI9zhruNMIqs4qTg

---

## English summary

**CharaDB** is a free prompt-material database for anime-style characters: **1,027 images** of hairstyles (46 styles × 5 colors, bangs, hair colors, accessories, eye colors, pupil shapes), **440 outfits** in 15 categories and **281 poses** (with line-art versions for ControlNet), each with ready-to-paste Danbooru tags. A single-file web app lets you pick a hairstyle, eyes, outfit and pose, choose expression / camera / background, and copy a complete prompt (quality tags for Illustrious / NoobAI, Anima, NovelAI or Pony are included).

All images were generated with the same model (JANKU v4, a NoobAI-XL / Illustrious-based checkpoint), same settings and a fixed seed, on a fixed base character, so cards are directly comparable.

- Live app: https://charadb-2fi.pages.dev/
- Images are distributed via **Releases** (zip, ~220 MB). The repo holds the app and the tag data (`data/items_public.json`) plus wildcard files.
- Free to use, no credit required. Please do not redistribute or resell the images themselves. Not for depicting real people or minors. Tags, prompts and the app may be used commercially. Treat the images as reference material (samples / ControlNet guides); do not include the images themselves in works you sell (per the base model's terms).
- Author: Taki ([@taki_auto](https://x.com/taki_auto)). The extended edition (1,097 images incl. lingerie / sexy outfits and bold poses, plus a bulk download) is available through the author's LINE open chat (link above).
