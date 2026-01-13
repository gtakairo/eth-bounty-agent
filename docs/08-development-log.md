# 開発ログ・知見集

> このファイルは開発中の試行錯誤、学び、重要な決定事項を記録します。
> **原則**: 作業で得た知見は必ずここにドキュメント化すること。

---

## 📅 2026年1月13日 - Phase 0 & Phase 2準備

### 作業内容

#### 1. プロジェクト初期化とCLAUDE.md作成
**目的**: 将来のClaude Codeインスタンスが効率的に作業できるようガイドを作成

**実施内容**:
- リポジトリ全体を分析（日本語ドキュメントのみ、コードなし）
- CLAUDE.mdに以下を統合:
  - プロジェクト概要
  - 3戦略アプローチ（76.5%が類似バグ探索由来）
  - Phase 0-5の詳細ロードマップ
  - 具体的なインストールコマンド
  - Quick Start Guide（Day 1 / Week 1 / Month 1-3）
  - gohanの失敗と成功の教訓

**知見**:
- ✅ TODOファイルが2つ存在（07-TODO.md, 07-development-todo.md）→ ほぼ同内容
- ✅ CLAUDE.mdには**実装開始時の具体的な初期ステップ**が必要
- ✅ チェックリスト形式で具体的なタスクを列挙すると後で使いやすい

**決定事項**:
- CLAUDE.mdを「メインガイド」として位置づけ
- 既存のTODOファイルの重要情報を全てCLAUDE.mdに統合
- コマンド例は必ずコピペ可能な形式で記載

---

#### 2. Git初期化とリポジトリ作成

**試行錯誤**:
1. `git init` 実行
2. `.gitignore`を作成（Python, Node.js, Foundry, 環境変数等を除外）
3. README.mdを作成（英語、GitHubで読みやすい形式）
4. `git add .` → `git commit`
5. GitHub CLI (`gh`) が利用可能か確認 → ✅ 認証済み
6. `gh repo create` でリポジトリ作成 + 自動プッシュ

**知見**:
- ✅ GitHub CLIが使える場合、`gh repo create --public --source=. --push`で一発作成
- ✅ コミットメッセージにCo-Authored-Byを追加すると協調作業が明確化
- ✅ 初回コミットには「Phase 0完了」と明記し、次の作業を示唆

**決定事項**:
- リポジトリURL: https://github.com/gtakairo/eth-bounty-agent
- ブランチ: main
- 可視性: Public（オープンソース化を想定）

---

#### 3. Phase 2準備: プロジェクト構造とテンプレート作成

**実施内容**:

##### 3.1 ディレクトリ構造
```bash
mkdir -p src/{agents,tools,knowledge,utils}
mkdir -p data/{bugs,reports,contracts}
mkdir -p tests configs
```

**知見**:
- ✅ 早期に構造を固定することで、後のファイル配置が明確になる
- ✅ data/の下に3つのサブディレクトリ（bugs, reports, contracts）を明確に分離

##### 3.2 requirements.txt作成
**包含ライブラリ**:
- AI Framework: langchain, langgraph, anthropic, openai
- Ethereum: web3, eth-abi, eth-utils, py-solc-x
- 静的解析: slither-analyzer
- ベクトルDB: chromadb, sentence-transformers
- 開発ツール: pytest, black, ruff

**知見**:
- ✅ slither-analyzerは0.10.0以上を指定（最新機能対応）
- ✅ chromadbを選択（ローカル実行可能、Pineconeより軽量）
- ⚠️ 将来的にバージョン固定が必要（pip freeze相当）

##### 3.3 pyproject.toml
**決定事項**:
- Python 3.11以上を必須とする（型ヒント、パフォーマンス）
- black（line-length=100）、ruff（py311）を標準化
- 開発依存関係を`[project.optional-dependencies]`に分離

**知見**:
- ✅ `pip install -e ".[dev]"`で開発環境を一括セットアップ可能
- ✅ pyproject.tomlに全設定を集約（setup.py不要）

##### 3.4 設定ファイル
**configs/.env.example**:
- Anthropic, OpenAI, Etherscan, Alchemy/Infuraのキー
- LLMプロバイダ、モデル、温度、最大トークン数

**configs/agent_config.yaml**:
- 3戦略の重み（0.176 / 0.765 / 0.059）
- 各エージェント（Orchestrator, Recon, Vuln, Exploit）の設定
- ベクトルDB、ナレッジベースパス、レポートフォーマット

**知見**:
- ✅ .envは環境変数、YAMLは構造化設定という役割分担
- ✅ 3戦略の重みをハードコードせず、設定ファイルで調整可能に
- ✅ 将来的にA/Bテストで重みを最適化可能

##### 3.5 bugs_ethereum.json スキーマ
**構造**:
```json
{
  "metadata": { version, last_updated, sources },
  "vulnerabilities": [
    {
      "id": "VULN-XXX",
      "category": "reentrancy|access_control|...",
      "severity": "critical|high|medium|low|info",
      "pattern": { code_structure, attack_vector, detection_query },
      "examples": [ { source, code, explanation, fix, url } ]
    }
  ],
  "categories": { ... },
  "severity_levels": { ... }
}
```

**サンプルパターン**:
1. Reentrancy（クロス関数型）
2. Access Control（modifier欠如）

**知見**:
- ✅ パターンに`detection_query`を含めることで、セマンティック検索のクエリ生成に利用
- ✅ 各exampleに`url`を含め、元ソースにトレーサブル
- ✅ confidence_scoreフィールドで信頼度を管理
- ⚠️ Phase 3でSoloditから最低100パターンを収集する必要あり

##### 3.6 テスト構造
**conftest.py**:
- `project_root` fixture
- `bugs_db_path` fixture
- `sample_contract` fixture（脆弱なReentrancy例）
- `mock_llm_response` fixture

**test_placeholder.py**:
- 基本的な構造テスト（ディレクトリ存在確認）
- Phase 4用のskipマーカー付きプレースホルダー

**知見**:
- ✅ fixtureを早期に定義すると、実装時のテストコードが書きやすい
- ✅ `@pytest.mark.skip`で未実装テストを明示
- ✅ sample_contractは実際の脆弱性を含む（Reentrancy after external call）

##### 3.7 ドキュメント作成
**SETUP.md**:
- Phase 2の詳細セットアップ手順
- ツールインストールコマンド（Foundry, Slither, Aderyn, Echidna）
- トラブルシューティング

**data/bugs/README.md**:
- bugs_ethereum.jsonの説明
- データソース（Solodit, Code4rena等）
- Phase 3のTODO

**data/reports/README.md**:
- 監査レポート収集戦略
- プラットフォーム別の構造
- メタデータフォーマット

**data/contracts/README.md**:
- サンプルコントラクトの分類（CTF, 既知脆弱性, 合成テスト）
- ベンチマーク用途
- 安全性警告

**知見**:
- ✅ 各dataサブディレクトリにREADMEを置くと、用途が明確になる
- ✅ SETUP.mdにトラブルシューティングセクションを含める
- ✅ 「Phase 3で何をするか」を各READMEに明記

---

### 重要な決定と根拠

#### 決定1: ChromaDBをベクトルDBとして採用
**理由**:
- ローカル実行可能（外部サービス不要）
- Pineconeより軽量で開発初期に適している
- LangChainとの統合が容易

**今後の考慮点**:
- Phase 5でスケール課題が出たらPinecone/Weaviateを検討

#### 決定2: Python 3.11以上を必須とする
**理由**:
- 型ヒント機能が充実（PEP 673等）
- パフォーマンス改善（CPython最適化）
- LangGraph等のライブラリが3.11+を推奨

#### 決定3: 3戦略の重みを設定ファイルで管理
**理由**:
- Nyx Foundationの実績（17.6% / 76.5% / 5.9%）を初期値とする
- Phase 5で実際のデータに基づいてチューニング可能
- A/Bテストでの比較実験が容易

#### 決定4: bugs_ethereum.jsonにconfidence_scoreを含める
**理由**:
- Phase 3で自動収集したパターンの信頼性を定量化
- 閾値（例: 0.7以上）でフィルタリング可能
- 継続的な品質管理に必要

---

### 発見した問題と解決

#### 問題1: TODOファイルが重複
**状況**: 07-TODO.mdと07-development-todo.mdがほぼ同内容

**解決**:
- CLAUDE.mdに統合し、重複を解消
- 既存TODOファイルは参照用として残す

#### 問題2: 初期のCLAUDE.mdがQuick Startを欠いていた
**状況**: 「今日から何をすべきか」が不明確

**解決**:
- Day 1 / Week 1 / Month 1-3の具体的なマイルストーンを追加
- 各Phaseを週次タスクまでブレイクダウン

---

### 次回以降への引き継ぎ事項

#### Phase 2 (Environment Setup) で実施すること
1. Foundry, Slither, Aderyn, Echidnaのインストール
2. Python仮想環境の作成とrequirements.txtインストール
3. .envファイルの設定（APIキー取得）
4. `pytest`実行で構造テストが通ることを確認

#### Phase 3 (Knowledge Base Construction) で実施すること
1. **最優先**: Soloditから脆弱性レポート100件以上を収集
2. bugs_ethereum.jsonに最低100パターンを追加
3. ChromaDBのセットアップとembedding生成
4. 類似度検索APIの実装
5. Etherscan API wrapperの実装

#### Phase 4 (AI Agent Implementation) で実施すること
1. LangGraphでReActパターンを実装
2. Slither/Foundry toolラッパーを実装
3. 3戦略を並行実行するVuln Agentを実装
4. Orchestrator Agentでタスク分配
5. レポート生成機能

---

### 技術的メモ

#### LangGraph vs LangChain Agents
**選択**: LangGraph
**理由**:
- グラフベースで複雑なフローを表現可能
- マルチエージェント構成に適している
- 細かい制御が可能（LangChain Agentsはシンプルすぎる）

#### セマンティック検索の実装方針
**アプローチ**:
1. Solidityコード → 自然言語（Claude/GPT）
2. 自然言語 → Embedding（OpenAI text-embedding-3-small）
3. Embedding → ベクトルDB（ChromaDB）
4. コサイン類似度で上位K件取得
5. LLMで最終判定（適用可能性の評価）

**注意点**:
- Solidityコードを直接embeddingするのではなく、まず自然言語化
- gohanの知見「コードを自然言語に起こして意味論的にバグ探索」

---

### 参考資料・リンク

- [Nyx Foundation](https://nyx.foundation/)
- [Solodit](https://solodit.cyfrin.io/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Slither GitHub](https://github.com/crytic/slither)
- [Foundry Book](https://book.getfoundry.sh/)

---

### このログの使い方

1. **作業前**: 前回のログを読み、引き継ぎ事項を確認
2. **作業中**: 試行錯誤した内容、失敗した理由、成功した理由をリアルタイム記録
3. **作業後**: 決定事項、知見、次回へのTODOを必ず追記
4. **定期的**: 週次でログを見返し、パターンや改善点を抽出

---

**最終更新**: 2026年1月13日
**次回作業**: Phase 2 (Environment Setup) の実施、またはPhase 1 (学習) の開始
