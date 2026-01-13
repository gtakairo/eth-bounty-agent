# スマートコントラクト セキュリティツール一覧

> バグバウンティハンター・セキュリティ監査人が使用するツール  
> 最終検証日: 2026年1月13日

---

## 📊 ツールカテゴリ概要

| カテゴリ | 目的 | 主要ツール |
|---------|------|----------|
| 静的解析 | コードの脆弱性パターン検出 | Slither, Mythril |
| 動的解析/Fuzzing | ランダム入力でのテスト | Echidna, Foundry Fuzz |
| シンボリック実行 | 全実行パスの検証 | hevm, Manticore |
| デコンパイラ | バイトコード→Solidity変換 | Heimdall, Panoramix |
| 開発環境 | ビルド、テスト、デプロイ | Foundry, Hardhat |
| 監視・防御 | リアルタイム脅威検出 | Forta, Tenderly |

---

## 🔍 静的解析ツール

### Slither

| 項目 | 内容 |
|------|------|
| **開発元** | Trail of Bits |
| **言語** | Python |
| **GitHub** | [crytic/slither](https://github.com/crytic/slither) |
| **⭐ Stars** | 6.1k |
| **最新バージョン** | v0.11.3 (2025年4月リリース) |

#### 機能
- **99+種類の脆弱性検出器** - Reentrancy, Unchecked Transfer 等
- **Vyperスマートコントラクトのサポート**（新機能）
- Hardhat/Foundry/Brownie との統合
- カスタム検出器をPythonで作成可能
- SlithIR中間表現
- 継承グラフ、コールグラフの可視化

#### 主な検出器（抜粋）
| ID | 脆弱性 | 深刻度 |
|----|-------|-------|
| reentrancy-eth | Reentrancy（ETH盗難） | High |
| arbitrary-send-eth | 任意アドレスへのETH送信 | High |
| unprotected-upgrade | 保護されていないアップグレード | High |
| unchecked-transfer | 未チェックのトークン転送 | High |
| tx-origin | tx.originの危険な使用 | Medium |

#### インストール
```bash
pip3 install slither-analyzer
```

#### 使用例
```bash
slither .  # プロジェクトルートで実行
slither contract.sol --print human-summary
```

---

### Mythril

| 項目 | 内容 |
|------|------|
| **開発元** | ConsenSys Diligence |
| **言語** | Python |
| **GitHub** | [ConsenSys/mythril](https://github.com/ConsenSysDiligence/mythril) |
| **⭐ Stars** | 4.2k |

#### 機能
- **シンボリック実行**ベースの解析
- EVMバイトコードを直接解析可能
- トランザクションシーケンスの生成

#### インストール
```bash
pip3 install mythril
```

#### 使用例
```bash
myth analyze contract.sol
myth analyze -a 0x... # オンチェーンコントラクト
```

---

### Aderyn

| 項目 | 内容 |
|------|------|
| **開発元** | Cyfrin |
| **言語** | Rust |
| **GitHub** | [Cyfrin/aderyn](https://github.com/Cyfrin/aderyn) |
| **⭐ Stars** | 699 |
| **最新バージョン** | v0.6.7 (2026年1月リリース) |

#### 機能
- 高速な静的解析（Rust製）
- **MCPサーバー対応**（AIエージェント統合に有利）
- **VSCode拡張機能**（1800+ダウンロード）
- Foundry/Hardhat統合
- Markdown/JSON/Sarifレポート出力
- 45,000+ダウンロード実績

#### インストール
```bash
# Cyfrinup (推奨)
curl -L https://raw.githubusercontent.com/Cyfrin/up/main/install | bash
cyfrinup

# npm
npm install @cyfrin/aderyn -g

# Homebrew
brew install cyfrin/tap/aderyn
```

#### 使用例
```bash
cd path/to/solidity/project
aderyn  # report.md が生成される
```

#### AIエージェントとの統合
AderynはMCP（Model Context Protocol）サーバーをサポートしており、
AIエージェントから直接呼び出して静的解析を実行可能。


---

### Surya

| 項目 | 内容 |
|------|------|
| **開発元** | ConsenSys |
| **言語** | JavaScript |
| **GitHub** | [ConsenSys/surya](https://github.com/ConsenSys/surya) |

#### 機能
- 関数呼び出しグラフ生成
- 継承関係の可視化
- Markdownレポート生成

---

## 🧪 動的解析 / Fuzzing

### Echidna

| 項目 | 内容 |
|------|------|
| **開発元** | Trail of Bits |
| **言語** | Haskell |
| **GitHub** | [crytic/echidna](https://github.com/crytic/echidna) |
| **⭐ Stars** | 3.1k |
| **最新バージョン** | v2.3.0 (2024年12月リリース) |

#### 機能
- **プロパティベースFuzzing**
- ABIに基づくインテリジェントな入力生成
- カバレッジガイド付きFuzzing
- テストケースの自動最小化
- Foundry/Hardhat統合

#### 使用例
```solidity
// 不変条件を定義
function echidna_balance_check() public returns (bool) {
    return balance >= 20;
}
```

```bash
echidna contract.sol --contract TestContract
```

#### 主なユーザー
- Uniswap
- Balancer
- MakerDAO
- Compound
- Aave

---

### Foundry Fuzz

| 項目 | 内容 |
|------|------|
| **含まれるツール** | Foundry (forge) |
| **GitHub** | [foundry-rs/foundry](https://github.com/foundry-rs/foundry) |
| **⭐ Stars** | 10k |

#### 機能
- Forgeに組み込まれたFuzzer
- 高速実行
- Invariant Testing対応

#### 使用例
```solidity
function testFuzz_transfer(uint256 amount) public {
    // amountは自動的にランダム値でテスト
    token.transfer(address(1), amount);
}
```

---

### Medusa

| 項目 | 内容 |
|------|------|
| **開発元** | Trail of Bits |
| **言語** | Go |
| **GitHub** | [crytic/medusa](https://github.com/crytic/medusa) |

#### 機能
- Echidnaの次世代版
- より高速な実行
- 改善されたUI

---

## 🔮 シンボリック実行

### hevm

| 項目 | 内容 |
|------|------|
| **開発元** | Ethereum Foundation → Argot Collective |
| **言語** | Haskell |
| **GitHub** | [argotorg/hevm](https://github.com/argotorg/hevm) |
| **⭐ Stars** | 324 |

#### 機能
- EVMのシンボリック/具体的実行
- Forgeテストのシンボリック実行
- 等価性チェック

#### 使用例
```bash
forge build --ast
hevm test --prefix test  # シンボリック実行
```

---

### Manticore

| 項目 | 内容 |
|------|------|
| **開発元** | Trail of Bits |
| **言語** | Python |
| **GitHub** | [trailofbits/manticore](https://github.com/trailofbits/manticore) |

#### 機能
- シンボリック実行エンジン
- カスタム探索戦略
- 複数プラットフォーム対応

---

## 🔧 デコンパイラ / 逆アセンブラ

### Heimdall-rs

| 項目 | 内容 |
|------|------|
| **開発元** | Jonathan Becker |
| **言語** | Rust |
| **GitHub** | [Jon-Becker/heimdall-rs](https://github.com/Jon-Becker/heimdall-rs) |
| **⭐ Stars** | 1.5k |

#### 機能
- EVMバイトコードの逆アセンブル
- デコンパイル（バイトコード→疑似Solidity）
- CFG（制御フローグラフ）生成
- ストレージダンプ
- Calldataデコード
- トランザクショントレースのデコード

#### インストール
```bash
curl -L http://get.heimdall.rs | bash
bifrost
```

#### 使用例
```bash
heimdall decompile 0x... --rpc-url https://eth.merkle.io
heimdall disassemble <bytecode>
heimdall cfg 0x...
```

---

### Panoramix

| 項目 | 内容 |
|------|------|
| **開発元** | eveem.org |
| **言語** | Python |
| **GitHub** | [eveem-org/panoramix](https://github.com/eveem-org/panoramix) |
| **⭐ Stars** | 995 |

#### 機能
- EVMデコンパイラ
- パターンマッチングによる高精度変換

---

### Dedaub

| 項目 | 内容 |
|------|------|
| **種類** | 商用サービス（Web） |
| **URL** | [app.dedaub.com](https://app.dedaub.com/) |

#### 機能
- 高品質デコンパイル
- コントラクトライブラリ
- セキュリティスキャン

---

## 🛠️ 開発環境

### Foundry

| 項目 | 内容 |
|------|------|
| **開発元** | Paradigm |
| **言語** | Rust |
| **GitHub** | [foundry-rs/foundry](https://github.com/foundry-rs/foundry) |
| **⭐ Stars** | 10k |

#### 含まれるツール
| ツール | 用途 |
|-------|------|
| **Forge** | ビルド、テスト、デプロイ |
| **Cast** | コントラクト操作、チェーン情報取得 |
| **Anvil** | ローカル開発ノード |
| **Chisel** | Solidity REPL |

#### インストール
```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
```

---

### Hardhat

| 項目 | 内容 |
|------|------|
| **言語** | TypeScript/JavaScript |
| **URL** | [hardhat.org](https://hardhat.org/) |

#### 機能
- プラグインエコシステム
- デバッグ機能
- Ethers.js統合

---

## 🔭 監視・防御ツール

### Tenderly

| 項目 | 内容 |
|------|------|
| **種類** | 商用サービス |
| **URL** | [tenderly.co](https://tenderly.co/) |

#### 機能
- **Virtual TestNets** - メインネットフォーク環境
- **Transaction Simulator** - TX実行前シミュレーション
- **Debugger** - 詳細なトレース・デバッグ
- **Gas Profiler** - ガス使用量分析
- **Monitoring** - リアルタイムアラート

#### 主要ユーザー
- Uniswap
- Aave
- MakerDAO
- Safe

---

### Forta

| 項目 | 内容 |
|------|------|
| **種類** | 分散型監視ネットワーク |
| **URL** | [forta.org](https://forta.org/) |

#### 機能
- リアルタイム脅威検出
- **Firewall** - 悪意あるTXをブロック
- AI搭載の検出エンジン
- 99%+のリコール率、0.0002%未満の偽陽性

---

## 📎 VS Code拡張機能

| 拡張機能 | 用途 |
|---------|------|
| **Solidity Visual Developer** | コード可視化、監査支援 |
| **Solidity Metrics** | コードメトリクス |
| **Slither VSC** | Slither統合 |
| **EthOver** | アドレス情報ホバー表示 |

---

## 📋 ツール選択ガイド

### ユースケース別推奨

| ユースケース | 推奨ツール |
|-------------|----------|
| 開発中のクイックチェック | Slither |
| 深い脆弱性探索 | Echidna + Mythril |
| 未検証コントラクト解析 | Heimdall |
| トランザクションデバッグ | Tenderly |
| 本番環境監視 | Forta |

### スキルレベル別

| レベル | 推奨ツール |
|-------|----------|
| 初心者 | Foundry, Slither |
| 中級 | + Echidna, Tenderly |
| 上級 | + hevm, Manticore, カスタム検出器 |
