# 🎯 バグバウンティAIエージェント開発 TODO

> 作成日: 2026年1月13日  
> 目標: Nyx Foundationの成功事例を参考に、監査コンテストで成果を出すAIエージェントを開発

---

## 📊 進捗サマリー

| フェーズ | 状態 | 完了目標 |
|---------|------|---------|
| Phase 0: 調査・計画 | ✅ 完了 | - |
| Phase 1: 基礎スキル習得 | ⬜ 未着手 | 1-2ヶ月 |
| Phase 2: 環境構築 | ⬜ 未着手 | 2週間 |
| Phase 3: データ収集 | ⬜ 未着手 | 1ヶ月 |
| Phase 4: AIエージェント開発 | ⬜ 未着手 | 2-3ヶ月 |
| Phase 5: 実戦・検証 | ⬜ 未着手 | 継続 |

---

## Phase 0: 調査・計画 ✅

- [x] プラットフォーム調査（Sherlock, Code4rena, Immunefi）
- [x] セキュリティツール調査（Slither, Echidna, Aderyn等）
- [x] 学習リソース調査
- [x] AIエージェントアーキテクチャ設計
- [x] 学術研究・既存ツール調査
- [x] gohan/Nyx Foundation実践知見調査
- [x] 全ドキュメントの最新情報検証

---

## Phase 1: 基礎スキル習得（1-2ヶ月）

### Solidityセキュリティ基礎

- [ ] **Cyfrin Security Course 完了**（50時間+）
  - URL: https://updraft.cyfrin.io/courses/security
  - 最重要の無料リソース

- [ ] **Ethernaut 全レベルクリア**
  - URL: https://ethernaut.openzeppelin.com/
  - 基本的な脆弱性パターンの理解

- [ ] **Damn Vulnerable DeFi 全チャレンジクリア**
  - URL: https://www.damnvulnerabledefi.xyz/
  - DeFi特有の攻撃パターン習得

### 監査レポート読み込み

- [ ] **Soloditで監査レポート100件読破**（第1目標）
  - URL: https://solodit.cyfrin.io/
  - 脆弱性パターンの蓄積

- [ ] **Soloditで監査レポート500件読破**（最終目標）
  - gohan推奨の学習量

### 脆弱性パターン学習

- [ ] **SWC Registry 全項目理解**
  - URL: https://swcregistry.io/
  - 標準的な脆弱性分類

- [ ] **Rekt.news 過去のハック事例50件分析**
  - URL: https://rekt.news/
  - 実際の攻撃事例

---

## Phase 2: 開発環境構築（2週間）

### 必須ツールインストール

- [ ] **Foundry インストール・設定**
  ```bash
  curl -L https://foundry.paradigm.xyz | bash
  foundryup
  ```

- [ ] **Slither インストール・動作確認**
  ```bash
  pip3 install slither-analyzer
  slither --version
  ```

- [ ] **Echidna インストール**
  ```bash
  # Docker recommended
  docker pull trailofbits/eth-security-toolbox
  ```

- [ ] **Aderyn インストール**
  ```bash
  curl -L https://raw.githubusercontent.com/Cyfrin/up/main/install | bash
  cyfrinup
  ```

### 開発環境

- [ ] **Python環境構築**（3.10+）
  - venv/conda設定
  - 必要ライブラリインストール

- [ ] **Node.js環境構築**（18+）
  - ethers.js, viem インストール

- [ ] **APIキー取得**
  - [ ] Etherscan API Key
  - [ ] Alchemy/Infura RPC URL
  - [ ] OpenAI/Anthropic API Key

### プロジェクト構造作成

- [ ] **リポジトリ初期化**
  ```
  eth-bounty-agent/
  ├── docs/           # ✅ 完了
  ├── src/
  │   ├── agents/     # AIエージェント
  │   ├── tools/      # ツール統合
  │   ├── knowledge/  # 知識ベース
  │   └── utils/      # ユーティリティ
  ├── data/
  │   ├── bugs/       # 脆弱性パターンDB
  │   └── reports/    # 監査レポート
  ├── tests/
  └── configs/
  ```

---

## Phase 3: データ収集・知識ベース構築（1ヶ月）

### 脆弱性パターンDB構築

- [ ] **bugs_ethereum.json 作成**
  - 過去の監査で発見された脆弱性パターン
  - Soloditからのデータ抽出
  - 構造化フォーマット設計

- [ ] **脆弱性分類体系の設計**
  ```json
  {
    "category": "reentrancy",
    "subcategory": "cross-function",
    "severity": "high",
    "pattern": "...",
    "examples": [...],
    "detection_rules": [...]
  }
  ```

### 類似バグ探索システム（最重要 - 76.5%の効果）

- [ ] **コード埋め込み（Embedding）システム**
  - Solidity専用の埋め込みモデル検討
  - OpenAI Embeddings / 専用モデル

- [ ] **類似度検索システム**
  - ベクトルDB選定（Pinecone, Weaviate, Chroma等）
  - 類似コードパターン検索API

- [ ] **過去の脆弱性コードのインデックス化**
  - Soloditレポートからのコード抽出
  - パターンのベクトル化

### 外部データ連携

- [ ] **Etherscan連携**
  - コントラクト情報取得
  - ソースコード取得
  - トランザクション履歴

- [ ] **Solodit API/スクレイピング**
  - 過去の監査レポート収集
  - 脆弱性パターン抽出

---

## Phase 4: AIエージェント開発（2-3ヶ月）

### 基盤構築

- [ ] **LangGraph/LangChain セットアップ**
  - エージェントフレームワーク選定
  - 基本的なReActパターン実装

- [ ] **LLMプロバイダー統合**
  - Claude 3.5 Sonnet（推奨）
  - GPT-4（バックアップ）
  - ローカルLLM検討（Llama等）

### ツール統合（MCP対応検討）

- [ ] **Slither統合**
  - CLI呼び出しラッパー
  - 結果のパース・構造化
  - 検出器選択ロジック

- [ ] **Aderyn統合（MCP対応）**
  - MCPサーバー経由での呼び出し
  - AIエージェントとの直接連携

- [ ] **Foundry統合**
  - テストコード生成
  - Fuzz実行
  - PoC自動生成

### 3つの戦略実装（Nyx方式）

#### 戦略1: 仕様ベース静的検査（17.6%）

- [ ] **コメント・NatSpec解析**
  - 仕様とコードの不整合検出

- [ ] **アクセス制御チェック**
  - 権限設定の妥当性検証

#### 戦略2: 類似バグ探索（76.5%）⭐最重要

- [ ] **コードパターンマッチング**
  - 過去の脆弱性パターンとの類似度計算

- [ ] **LLMによる類似性判断**
  - セマンティックな類似性評価

- [ ] **横展開システム**
  - 発見したパターンの他箇所への適用

#### 戦略3: 動的テスト生成（5.9%）

- [ ] **Foundry Fuzzテスト自動生成**
  - 不変条件の自動抽出
  - テストケース生成

- [ ] **Echidnaプロパティテスト**
  - プロパティの自動設計

### マルチエージェント構成

- [ ] **Orchestrator Agent**
  - タスク分解・調整
  - 最終判断

- [ ] **Recon Agent**
  - 情報収集
  - コントラクト分析

- [ ] **Vuln Agent**
  - 脆弱性検出
  - パターンマッチング

- [ ] **Exploit Agent**
  - PoC作成
  - 影響度評価

### レポート生成

- [ ] **レポートテンプレート作成**
  - プラットフォーム別フォーマット
  - 再現手順の標準化

- [ ] **自動レポート生成機能**
  - 発見→レポートの自動化

---

## Phase 5: 実戦・検証（継続）

### 監査コンテスト参加

- [ ] **Sherlock 初回コンテスト参加**
  - 手動での参加（AIなし）
  - プロセスの理解

- [ ] **Code4rena 初回コンテスト参加**
  - 異なるプラットフォームの経験

- [ ] **AIエージェント併用での参加**
  - 人間+AI協調
  - 効果測定

### 効果測定・改善

- [ ] **KPI設定**
  - 発見脆弱性数
  - 報酬額
  - False Positive率
  - 処理時間

- [ ] **継続的改善**
  - 失敗事例の分析
  - パターンDBの更新
  - モデルの調整

---

## 📚 参考リソース

### Nyx Foundation関連
- [Nyx Foundation](https://nyx.foundation/)
- [NyxFoundation GitHub](https://github.com/NyxFoundation)
- [@grandchildrice](https://x.com/grandchildrice)

### ツール公式
- [Slither](https://github.com/crytic/slither)
- [Echidna](https://github.com/crytic/echidna)
- [Aderyn](https://github.com/Cyfrin/aderyn)
- [Foundry](https://github.com/foundry-rs/foundry)

### 学習
- [Cyfrin Security Course](https://updraft.cyfrin.io/courses/security)
- [Solodit](https://solodit.cyfrin.io/)
- [SWC Registry](https://swcregistry.io/)

---

## 🎯 最優先アクション（今すぐ始めること）

1. **Cyfrin Security Course を開始する**
2. **Ethernaut の最初の5レベルをクリアする**
3. **Foundry をインストールして基本操作を覚える**
4. **Solodit で監査レポートを10件読む**

---

## 💡 成功の鍵（gohanの教訓）

> ❌ Bug Bountyから始めるのは失敗しやすい  
> ❌ LangChainゴリゴリ自動化は失敗しやすい  
> ✅ 監査コンテストから始める  
> ✅ 手動での経験を積んでからAI化  
> ✅ 類似バグ探索が最も効果的（76.5%）  
> ✅ ドメイン知識の蓄積が必須

---

*最終更新: 2026年1月13日*
