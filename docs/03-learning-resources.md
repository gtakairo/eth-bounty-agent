# スマートコントラクト セキュリティ 学習リソース

> バグバウンティハンター・セキュリティ監査人になるための学習パス

---

## 📚 学習ロードマップ

```
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: 基礎                                                  │
│  ├── ブロックチェーン基礎                                        │
│  ├── Solidity基礎                                               │
│  └── 開発環境セットアップ                                        │
├─────────────────────────────────────────────────────────────────┤
│  Phase 2: セキュリティ入門                                       │
│  ├── 一般的な脆弱性パターン                                      │
│  ├── CTFチャレンジ（初級）                                       │
│  └── 静的解析ツール                                              │
├─────────────────────────────────────────────────────────────────┤
│  Phase 3: DeFi深掘り                                            │
│  ├── DeFiプロトコル理解                                          │
│  ├── DeFi特有の攻撃パターン                                      │
│  └── CTFチャレンジ（中級）                                       │
├─────────────────────────────────────────────────────────────────┤
│  Phase 4: 実践                                                  │
│  ├── 監査レポート読解                                            │
│  ├── Fuzzingツール                                              │
│  └── バグバウンティ参加                                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📖 Phase 1: 基礎

### ブロックチェーン & Ethereum

| リソース | 種類 | 難易度 |
|---------|------|-------|
| [Mastering Ethereum](https://github.com/ethereumbook/ethereumbook) | 書籍 | ⭐⭐ |
| [Ethereum.org Documentation](https://ethereum.org/en/developers/) | ドキュメント | ⭐ |
| [Blockchain Technology Explained](https://www.youtube.com/watch?v=qOVAbKKSH10) | 動画 | ⭐ |

#### 必読チャプター（Mastering Ethereum）
- Chapter 1: What is Ethereum?
- Chapter 4: Cryptography
- Chapter 5: Wallets
- Chapter 6: Transactions
- Chapter 7: Smart Contracts
- Chapter 9: Smart Contract Security
- Chapter 13-14: EVM

---

### Solidity 基礎

| リソース | 種類 | 難易度 | URL |
|---------|------|-------|-----|
| Solidity Documentation | 公式ドキュメント | ⭐⭐ | [docs.soliditylang.org](https://docs.soliditylang.org/) |
| CryptoZombies | インタラクティブ | ⭐ | [cryptozombies.io](https://cryptozombies.io/) |
| Solidity by Example | コード例 | ⭐⭐ | [solidity-by-example.org](https://solidity-by-example.org/) |
| Smart Contract Engineer | コース | ⭐⭐ | [smartcontract.engineer](https://www.smartcontract.engineer/) |

#### Secureum シリーズ
- [Solidity 101](https://secureum.substack.com/p/solidity-101) - 基礎文法
- [Solidity 201](https://secureum.substack.com/p/solidity-201) - 高度なトピック

---

### 開発環境

| ツール | 用途 | 推奨度 |
|-------|------|-------|
| **Foundry** | メイン開発環境 | ⭐⭐⭐ |
| Hardhat | JavaScript/TypeScript | ⭐⭐ |
| Remix | ブラウザIDE（学習用） | ⭐ |

---

## 🛡️ Phase 2: セキュリティ入門

### 脆弱性データベース

| リソース | 説明 | URL |
|---------|------|-----|
| **SWC Registry** | 37種類の標準脆弱性分類 | [swcregistry.io](https://swcregistry.io/) |
| Smart Contract Attack Vectors | 攻撃パターン集 | [GitHub](https://github.com/KadenZipfel/smart-contract-attack-vectors) |
| Not So Smart Contracts | 脆弱性例とサンプル | [GitHub](https://github.com/crytic/building-secure-contracts/tree/master/not-so-smart-contracts) |

### 主要な脆弱性パターン

| 脆弱性 | SWC ID | 説明 |
|-------|--------|------|
| Reentrancy | SWC-107 | 再入攻撃 |
| Integer Overflow | SWC-101 | 整数オーバーフロー |
| Unchecked Return | SWC-104 | 戻り値未チェック |
| tx.origin | SWC-115 | tx.originの誤用 |
| Unprotected Selfdestruct | SWC-106 | 保護なしのselfdestruct |
| Weak Randomness | SWC-120 | 弱い乱数生成 |

### Secureum セキュリティシリーズ
- [Security Pitfalls 101](https://secureum.substack.com/p/security-pitfalls-and-best-practices-101)
- [Security Pitfalls 201](https://secureum.substack.com/p/security-pitfalls-and-best-practices-201)

---

### 🎮 CTFチャレンジ（初級〜中級）

| CTF | 難易度 | 説明 | URL |
|-----|-------|------|-----|
| **Ethernaut** | ⭐〜⭐⭐ | OpenZeppelin製、最も有名 | [ethernaut.openzeppelin.com](https://ethernaut.openzeppelin.com/) |
| Capture The Ether | ⭐〜⭐⭐ | 古典的CTF | [capturetheether.com](https://capturetheether.com/) |
| **Damn Vulnerable DeFi** | ⭐⭐〜⭐⭐⭐ | DeFi特化 | [damnvulnerabledefi.xyz](https://www.damnvulnerabledefi.xyz/) |
| QuillCTF | ⭐⭐ | QuillAudits製 | [quillaudits.com/academy/ctf](https://www.quillaudits.com/academy/ctf) |
| CipherShastra | ⭐⭐ | インド発 | [ciphershastra.com](https://ciphershastra.com/) |
| Curta CTF | ⭐⭐⭐ | 上級者向け | [curta.wtf](https://www.curta.wtf/) |
| Paradigm CTF | ⭐⭐⭐ | 難問揃い | [ctf.paradigm.xyz](https://ctf.paradigm.xyz/) |

#### 100+ CTFまとめ
- [minaminao/ctf-blockchain](https://github.com/minaminao/ctf-blockchain) - 100以上のCTF問題集

---

## 💰 Phase 3: DeFi 深掘り

### DeFi 基礎

| リソース | 種類 | URL |
|---------|------|-----|
| Finematics - DeFi | 動画シリーズ | [YouTube](https://www.youtube.com/playlist?list=PLjrTIwaNiTwn39tg3sR_bPBWGHoznv47D) |
| DeFi MOOC | 大学講義 | [YouTube](https://www.youtube.com/playlist?list=PLS01nW3RtgopJOtsMVOK3N7n7qyNMPbJ_) |
| Teach Yourself Crypto | 総合コース | [teachyourselfcrypto.com](https://teachyourselfcrypto.com/) |

### 主要プロトコル

| プロトコル | カテゴリ | 学習リソース |
|-----------|---------|------------|
| **Uniswap** | DEX | [Uniswap V3 Explained](https://mvpworkshop.co/blog/uniswap-v3-explained-all-you-need-to-know/) |
| **Aave** | Lending | [Aave Explained](https://www.youtube.com/watch?v=WwE3lUq51gQ) |
| **Compound** | Lending | [Compound Protocol](https://compound.finance/docs) |
| **Curve** | DEX (Stableswap) | [Curve Docs](https://curve.readthedocs.io/) |
| **Balancer** | DEX | [Balancer ELI5](https://medium.com/token-terminal/eli5-what-is-balancer-labs-16c8cfe092d9) |

### DeFi攻撃パターン

| 攻撃 | 説明 |
|------|------|
| **Flash Loan Attack** | 無担保ローンを使った価格操作 |
| **Price Oracle Manipulation** | 価格オラクルの操作 |
| **Front-Running / MEV** | トランザクション順序操作 |
| **Sandwich Attack** | 前後を挟む攻撃 |
| **Rug Pull** | 流動性引き抜き |

---

## 🔬 Phase 4: 実践

### 監査レポート読解

| リソース | 説明 | URL |
|---------|------|-----|
| **Solodit** | 監査レポート検索DB | [solodit.cyfrin.io](https://solodit.cyfrin.io/) |
| Code4rena Reports | C4監査レポート | [code4rena.com/reports](https://code4rena.com/reports) |
| Trail of Bits | ToB公開レポート | [GitHub](https://github.com/trailofbits/publications) |
| OpenZeppelin | OZ監査レポート | [blog.openzeppelin.com](https://blog.openzeppelin.com/security-audits/) |
| ConsenSys Diligence | Consensys監査 | [consensys.io/diligence/audits](https://consensys.io/diligence/audits/) |
| Sherlock | Sherlock監査 | [audits.sherlock.xyz](https://audits.sherlock.xyz/) |

### Secureum 監査シリーズ
- [Audit Findings 101](https://secureum.substack.com/p/audit-findings-101)
- [Audit Findings 201](https://secureum.substack.com/p/audit-findings-201)

### ハッキング事後分析

| リソース | 説明 |
|---------|------|
| **Rekt News** | 有名ハッキング事後分析 |
| Immunefi Medium | バグバウンティ事例 |
| BlockSec | 攻撃分析 |
| SlowMist | セキュリティインシデント |
| PeckShield | リアルタイム警告 |

---

## 📚 体系的コース

### 無料コース

| コース | 提供元 | URL |
|-------|-------|-----|
| **Security and Auditing Course** | Cyfrin Updraft | [updraft.cyfrin.io](https://updraft.cyfrin.io/courses/security) |
| Building Secure Contracts | Trail of Bits | [secure-contracts.com](https://secure-contracts.com/) |

### 有料コース

| コース | 価格帯 |
|-------|-------|
| Smart Contract Hacking | $$ |

---

## 🗺️ ロードマップ参考

| リソース | 説明 | URL |
|---------|------|-----|
| QuillAudit Auditor Roadmap | 詳細なマインドマップ | [GitHub](https://github.com/Quillhash/QuillAudit_Auditor_Roadmap) |
| Razzorsec Auditors Roadmap | ステップバイステップ | [GitHub](https://github.com/razzorsec/AuditorsRoadmap) |
| Awesome Web3 Security | リソース集 | [GitHub](https://github.com/Anugrahsr/Awesome-web3-Security) |

---

## 📢 コミュニティ & 情報源

### Discord
| コミュニティ | 用途 |
|------------|------|
| Immunefi | バグバウンティ |
| Secureum | セキュリティ学習 |
| Ethereum R&D | 技術議論 |
| Blockchain Pentesting | ペンテスト |

### Twitter（X）
| アカウント | 専門 |
|-----------|------|
| @samczsun | セキュリティリサーチ |
| @Mudit__Gupta | セキュリティ |
| @PeckShieldAlert | リアルタイム警告 |
| @CertiKAlert | セキュリティ警告 |
| @BlockSecTeam | 攻撃分析 |

### ニュースレター
| 名前 | 頻度 |
|-----|------|
| Blockthreat | 週刊 |
| Hashingbits | 週刊 |

---

## 📋 学習チェックリスト

### 初級（1-2ヶ月）
- [ ] Ethereumの仕組みを理解
- [ ] Solidity基礎文法をマスター
- [ ] Foundryでプロジェクト作成
- [ ] Ethernaut 10問クリア
- [ ] SWC上位10個を理解

### 中級（2-4ヶ月）
- [ ] Ethernaut全問クリア
- [ ] Damn Vulnerable DeFi 10問クリア
- [ ] Slitherで自作コントラクト解析
- [ ] 監査レポート10本読破
- [ ] Uniswap/Aaveのコード理解

### 上級（4-6ヶ月+）
- [ ] Echidnaでプロパティテスト作成
- [ ] 実際のバグバウンティに参加
- [ ] 脆弱性を1つ以上発見
- [ ] カスタムSlither検出器作成
