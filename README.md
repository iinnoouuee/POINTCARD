# プロジェクト README

## 概要

このプロジェクトは、個人店舗向けのポイント管理アプリのMVP開発を目的としています。アプリは Flask（Python）をバックエンドに使用し、フロントエンドはシンプルなHTMLテンプレート（Jinja2）で構築されています。将来的にはStripe等の決済連携やPOS連携も視野に入れています。

## 開発方針

本プロジェクトでは、\*\*テスト駆動開発（TDD）\*\*を導入します。以下の方針で開発を進めます。

* `pytest` を使用してユニットテスト・統合テストを実施
* テストを先に書き、期待される挙動を明確化したうえで実装を行う
* 開発対象は最小限のMVPに絞り、最短1か月で実用できる形を目指す
* 進捗管理はスプリント（週単位）でタスクボードを使って進める

## プロジェクト構成（予定）

```
/app
    /static
    /templates
    app.py
/tests
    test_index.py
    test_register_owner.py
    test_subscribe.py
    test_login_staff.py
    test_qr_scan.py
/conftest.py
requirements.txt
README.md
```

## 使用技術

* Python 3.x
* Flask
* pytest
* Jinja2

## セットアップ手順

1. 必要なパッケージをインストール

   ```bash
   pip install -r requirements.txt
   ```

2. テストを実行

   ```bash
   pytest
   ```

3. アプリを起動

   ```bash
   python app.py
   ```

## 注意事項

* テスト駆動開発のため、必ず **テストを書く→実装を書く→テストが通るか確認** の順で進めます。
* データは本番環境ではなく、テスト用のインメモリデータを使用します（将来的にはSQLiteやPostgreSQL導入予定）。
* コードの大幅な変更を行う場合は、必ずマネジメント担当と相談してください。

## 今後の計画

* Week1：モード選択、オーナー登録、スタッフログイン、QRスキャン
* Week2：購入金額入力、ポイント付与、店舗情報編集
* Week3以降：メニュー編集、お知らせ、顧客体験部分の拡張

## コンタクト

このリポジトリに関する質問は、マネジメント担当まで連絡してください。
