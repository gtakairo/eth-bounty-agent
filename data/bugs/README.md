# Vulnerability Knowledge Base

This directory contains the core vulnerability database used for similar bug pattern search (76.5% success rate).

## bugs_ethereum.json

The main vulnerability database with the following structure:

```json
{
  "metadata": { ... },
  "vulnerabilities": [
    {
      "id": "VULN-XXX",
      "category": "reentrancy|access_control|oracle_manipulation|...",
      "severity": "critical|high|medium|low|info",
      "pattern": { ... },
      "examples": [ ... ]
    }
  ]
}
```

## Data Sources (Phase 3)

To populate this database:

1. **Solodit** (50,000+ reports)
   - URL: https://solodit.cyfrin.io/
   - Filter by severity: High/Critical
   - Extract vulnerability patterns

2. **Code4rena Findings**
   - URL: https://code4rena.com/reports
   - Public audit reports
   - Well-documented vulnerabilities

3. **Sherlock Findings**
   - URL: https://audits.sherlock.xyz/contests
   - Contest reports
   - Multiple severity levels

4. **Immunefi Disclosed Bugs**
   - URL: https://immunefi.com/explore/
   - Real-world bug bounty findings
   - High-value vulnerabilities

5. **CVE Database**
   - Ethereum/Solidity specific CVEs
   - Historical vulnerabilities

## Categories

Current categories (expand during Phase 3):
- `reentrancy` - Recursive call vulnerabilities
- `access_control` - Authorization issues
- `oracle_manipulation` - Price oracle attacks
- `arithmetic` - Integer overflow/underflow
- `denial_of_service` - DoS attacks
- (Add more as patterns are discovered)

## Usage

The AI agent will:
1. Convert target contract code to natural language
2. Embed using LLM
3. Perform vector similarity search against this database
4. Find similar historical vulnerability patterns
5. Apply patterns to target contract (horizontal expansion)

## Maintenance

- Update frequency: Daily (automated)
- Confidence threshold: 0.7+
- Review duplicates: Weekly
- Add new patterns: As discovered in Phase 5

## Phase 3 TODO

- [ ] Scrape/API integration with Solodit
- [ ] Parse Code4rena reports
- [ ] Extract patterns from Sherlock findings
- [ ] Normalize vulnerability data format
- [ ] Build embedding index
- [ ] Set up vector database
- [ ] Create similarity search API
