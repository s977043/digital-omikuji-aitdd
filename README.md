# ⛩️ Digital Omikuji (AITDD)

AI支援型テスト駆動開発（AITDD）を用いて開発された、デジタルおみくじアプリです。

## ✨ 仕様
このプロジェクトの仕様は、[docs/SPEC.md](docs/SPEC.md) に記載されています。

## 🤖 開発ワークフロー
このプロジェクトは **Cipher** を記憶レイヤーとして活用し、**Gemini CLI** をメインエージェントとした自動開発フローを採用しています。

1.  **コンテキスト学習:** `Cipher` を通じてAIがプロジェクト全体の構造と仕様を解析・記憶します。
2.  **Issue起票:** 機能追加や修正は **GitHub Issue** で行います。
3.  **AIによる開発:** Issueに基づき、`Cipher`に記憶されたコンテキストを活用してAIが開発を進めます。
4.  **Pull Request:** 変更は **Pull Request** で提案され、**GitHub Actionsによる自動テスト**が実行されます。
5.  **マージ:** テスト成功後、mainブランチにマージされます。

## 状況
- **CI Status:** [![CI](https://github.com/s977043/digital-omikuji-aitdd/actions/workflows/ci.yml/badge.svg)](https://github.com/s977043/digital-omikuji-aitdd/actions/workflows/ci.yml)

---
*This README is partially maintained by AI. Project context is managed by Cipher.*
