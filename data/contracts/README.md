# Sample Contracts

This directory contains sample smart contracts for testing and development.

## Purpose

- Test agent capabilities on known vulnerable contracts
- Benchmark detection rates
- Develop and refine detection strategies
- Training material for manual auditing practice

## Categories

### 1. CTF Challenges
Sample contracts from security CTFs:
- Ethernaut solutions
- Damn Vulnerable DeFi challenges
- Capture The Ether

### 2. Known Vulnerabilities
Historical vulnerabilities (public):
- DAO hack (reentrancy)
- Parity wallet bugs
- Integer overflow examples

### 3. Synthetic Test Cases
Custom-built contracts for testing:
- Reentrancy variants
- Access control issues
- Oracle manipulation
- Flash loan attack scenarios

### 4. DeFi Protocol Snippets
Simplified versions of real protocols:
- AMM (Uniswap-like)
- Lending (Aave-like)
- Staking mechanisms

## Directory Structure

```
contracts/
├── ethernaut/
│   ├── Fallback.sol
│   ├── Reentrancy.sol
│   └── ...
├── damn-vulnerable-defi/
│   ├── unstoppable/
│   ├── naive-receiver/
│   └── ...
├── historical/
│   ├── dao-reentrancy.sol
│   ├── parity-wallet.sol
│   └── ...
├── synthetic/
│   ├── reentrancy-variants/
│   ├── access-control/
│   └── ...
└── real-world-samples/
    ├── uniswap-v2-simplified.sol
    ├── aave-simplified.sol
    └── ...
```

## Usage

### Testing Agent Detection

```bash
# Run agent on a sample contract
python -m src.agents.orchestrator --contract data/contracts/ethernaut/Reentrancy.sol

# Batch test on all Ethernaut challenges
python scripts/batch_test.py --dir data/contracts/ethernaut/
```

### Benchmarking

Track detection rates:
- True Positives: Correctly identified vulnerabilities
- False Positives: Incorrectly flagged issues
- False Negatives: Missed vulnerabilities
- Processing time per contract

### Manual Practice

Use these contracts for Phase 1 learning:
1. Read contract code
2. Identify vulnerabilities manually
3. Write PoC tests
4. Compare with agent's findings

## Expected Results

Each contract should have:
- `contract.sol` - The vulnerable contract
- `exploit.sol` - PoC exploit (Foundry test)
- `analysis.md` - Expected findings and severity
- `metadata.json` - Contract metadata

Example `metadata.json`:
```json
{
  "name": "Reentrancy Example",
  "source": "Ethernaut Level 10",
  "vulnerabilities": [
    {
      "type": "reentrancy",
      "severity": "critical",
      "function": "withdraw",
      "line": 15
    }
  ],
  "difficulty": "medium"
}
```

## Adding New Contracts

When adding new samples:
1. Ensure license allows redistribution
2. Add clear comments explaining vulnerability
3. Include PoC if possible
4. Update metadata.json
5. Add to appropriate category

## Safety Notice

⚠️ **DO NOT deploy these contracts to mainnet!**
These are intentionally vulnerable for educational purposes only.
