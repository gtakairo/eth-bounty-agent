# Audit Reports Collection

This directory stores historical audit reports from various platforms for analysis and pattern extraction.

## Purpose

- Train AI agent on real audit report formats
- Extract vulnerability patterns for bugs_ethereum.json
- Understand reporting standards across platforms
- Build corpus for RAG (Retrieval-Augmented Generation)

## Data Sources

### Code4rena
- **URL**: https://code4rena.com/reports
- **Format**: Markdown
- **Structure**: Title, Severity, Description, PoC, Recommendation
- **Storage**: `code4rena/`

### Sherlock
- **URL**: https://audits.sherlock.xyz/contests
- **Format**: GitHub Issues
- **Structure**: Issue template with Watson submissions
- **Storage**: `sherlock/`

### Trail of Bits
- **URL**: Public reports on GitHub
- **Format**: PDF/Markdown
- **Structure**: Professional audit report format
- **Storage**: `trail_of_bits/`

### OpenZeppelin
- **URL**: https://blog.openzeppelin.com/security-audits
- **Format**: PDF
- **Structure**: Executive summary, findings, recommendations
- **Storage**: `openzeppelin/`

### Consensys Diligence
- **URL**: https://consensys.io/diligence/audits/
- **Format**: Markdown/PDF
- **Storage**: `consensys/`

## Directory Structure

```
reports/
├── code4rena/
│   ├── 2024-protocol-name/
│   │   ├── findings.md
│   │   └── metadata.json
├── sherlock/
│   ├── 2024-contest-name/
│   │   ├── issues/
│   │   └── summary.md
├── trail_of_bits/
├── openzeppelin/
└── consensys/
```

## Metadata Format

Each report should include metadata:

```json
{
  "platform": "code4rena|sherlock|...",
  "protocol": "Protocol Name",
  "date": "2024-01-15",
  "auditors": ["auditor1", "auditor2"],
  "total_findings": 15,
  "severity_breakdown": {
    "critical": 2,
    "high": 5,
    "medium": 8
  },
  "prize_pool": "50000 USDC",
  "url": "https://..."
}
```

## Collection Strategy (Phase 3)

1. **Automated Scraping**
   - Code4rena API (if available)
   - Sherlock GitHub crawling
   - Scheduled daily updates

2. **Manual Collection**
   - Trail of Bits public reports
   - OpenZeppelin blog posts
   - Notable bug disclosures

3. **Processing Pipeline**
   - Parse reports → Extract vulnerabilities
   - Categorize by type
   - Add to bugs_ethereum.json
   - Update vector embeddings

## Usage by AI Agent

Reports are used for:
- **Training**: Understanding report formats
- **Pattern Recognition**: Identifying common vulnerability types
- **Report Generation**: Following platform-specific formats
- **Context**: RAG for similar historical issues

## Privacy & Ethics

- Only collect publicly disclosed reports
- Respect platform terms of service
- No scraping of private/ongoing contests
- Attribution to original authors
