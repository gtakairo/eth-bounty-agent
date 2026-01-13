# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research and development project for building an AI agent to autonomously discover vulnerabilities in Ethereum smart contracts, targeting bug bounty platforms (Immunefi, Code4rena, Sherlock) and audit contests.

**Current Status**: Documentation and research phase. No implementation code exists yet - the repository contains comprehensive research documentation in Japanese.

**Inspiration**: Based on Nyx Foundation's success (led by gohan/@grandchildrice), whose AI agent achieved **1st place** in the Ethereum "Fusaka" audit contest (December 2025), discovering 17 vulnerabilities.

## Repository Structure

```
eth-bounty-agent/
└── docs/               # All current content is here (Japanese)
    ├── 00-overview.md                    # Project summary and highlights
    ├── 01-bug-bounty-platforms.md        # Platform comparison (Immunefi, Code4rena, Sherlock)
    ├── 02-security-tools.md              # Security tools (Slither, Foundry, Echidna, Aderyn)
    ├── 03-learning-resources.md          # Learning resources (CTFs, courses)
    ├── 04-project-proposal.md            # AI agent architecture proposal
    ├── 05-ai-agent-research.md           # Academic research on AI security
    ├── 06-gohan-insights-research.md     # ⭐ Most important: Real-world insights
    ├── 07-TODO.md                        # Development roadmap
    └── 07-development-todo.md            # Detailed TODO list
```

## Core Architecture (Proposed)

### Three-Strategy Approach (From Nyx Foundation)

Based on real-world success, the agent should implement three parallel strategies:

1. **Specification-Based Static Analysis** (17.6% success rate)
   - Verify implementation against specifications (EIP documents)
   - Use Slither, Aderyn for pattern matching

2. **Similar Bug Pattern Search** (76.5% success rate) ⭐ **Most Effective**
   - Semantic search using known vulnerability patterns
   - Convert code to natural language → vector similarity search
   - Database: bugs_ethereum.json with CVE patterns, past audit findings

3. **Dynamic Test Generation** (5.9% success rate)
   - Auto-generate Foundry tests and fuzzing scenarios
   - Proof-of-Concept creation

### Multi-Agent Architecture (Proposed)

```
Orchestrator Agent (task decomposition & coordination)
├── Recon Agent (information gathering)
├── Vuln Agent (vulnerability discovery - 3 strategies)
└── Exploit Agent (PoC creation with Foundry)
```

## Technology Stack (Planned)

- **Language**: Python 3.11+
- **Agent Framework**: LangGraph (preferred over LangChain for fine-grained control)
- **LLM**: Claude 3.5 Sonnet (Anthropic API)
- **Static Analysis**: Slither, Aderyn (with MCP support)
- **Testing**: Foundry (forge, cast, anvil)
- **Fuzzing**: Echidna
- **Blockchain**: ethers.py / web3.py
- **Storage**: PostgreSQL + pgvector (for RAG/semantic search)
- **Vulnerability DB**: Solodit (50,000+ reports)

## Key Tools for Smart Contract Security

### Installation Commands (When Implementation Starts)

```bash
# Foundry (required)
curl -L https://foundry.paradigm.xyz | bash
foundryup

# Slither (required)
pip3 install slither-analyzer

# Aderyn (recommended - MCP compatible)
curl -L https://raw.githubusercontent.com/Cyfrin/up/main/install | bash
cyfrinup

# Echidna (optional - fuzzing)
brew install echidna  # macOS
```

### Running Security Tools

```bash
# Slither analysis
slither path/to/contract.sol

# Foundry tests
forge test
forge test --match-test testVulnerability -vvvv

# Echidna fuzzing
echidna-test contract.sol --test-mode assertion
```

## Critical Lessons from gohan's Experience

### What Failed ❌

1. **Starting with Bug Bounties**: Too difficult for beginners (production code already heavily audited)
2. **LangChain "Full Automation" Early On**: Failed without domain knowledge

### What Succeeded ✅

1. **Start with Audit Contests** (Code4rena, Sherlock): Better learning curve, feedback available
2. **Manual Experience First**: Gained domain knowledge through 31 audits in first 2 months
3. **Then AI Automation**: After mastering manual auditing, AI automation achieved world #1 ranking

### Success Formula

```
Phase 1: Manual Mastery (2-3 months)
├── Read 500+ audit reports on Solodit
├── Participate in audit contests
└── Build domain knowledge

Phase 2: Tool-Assisted (1-2 months)
├── Integrate static analysis tools
├── Semantic search for similar vulnerabilities
└── Semi-automated PoC generation

Phase 3: AI Agent Automation
├── Multi-agent architecture
├── Three-strategy parallel execution
└── Autonomous vulnerability discovery
```

## Development Priorities

### Phase 0: Research ✅ COMPLETED
- Platform research (Immunefi, Code4rena, Sherlock)
- Security tools research (Slither, Echidna, Foundry, Aderyn)
- Academic research and existing tools
- gohan/Nyx Foundation case study analysis
- All documentation verified with latest data

### Phase 1: Foundation Skills (1-2 months) - **START HERE**

#### Solidity Security Fundamentals
- [ ] **Cyfrin Security Course** (50+ hours) - Priority: HIGHEST
  - URL: https://updraft.cyfrin.io/courses/security
  - Free, comprehensive security course

- [ ] **Ethernaut** - All 32 levels
  - URL: https://ethernaut.openzeppelin.com/
  - Master fundamental vulnerability patterns

- [ ] **Damn Vulnerable DeFi** - All challenges
  - URL: https://www.damnvulnerabledefi.xyz/
  - DeFi-specific attack patterns

#### Audit Report Analysis
- [ ] **Solodit: 100 reports** (First milestone)
  - URL: https://solodit.cyfrin.io/
  - Build vulnerability pattern recognition

- [ ] **Solodit: 500 reports** (Final goal)
  - gohan's recommended learning volume

- [ ] **SWC Registry** - All patterns
  - URL: https://swcregistry.io/
  - Standard vulnerability taxonomy

- [ ] **Rekt News** - 30+ major hack analyses
  - URL: https://rekt.news/
  - Real-world attack case studies

#### DeFi Protocol Understanding
- [ ] Study major DeFi protocols:
  - Uniswap V2/V3 (AMM patterns)
  - Aave V3 (Lending)
  - Compound V3 (Lending)
  - MakerDAO (Stablecoin)

### Phase 2: Environment Setup (1-2 weeks)

#### Essential Tools
```bash
# Foundry (REQUIRED)
curl -L https://foundry.paradigm.xyz | bash
foundryup
forge --version

# Slither (REQUIRED)
pip3 install slither-analyzer
slither --version

# Aderyn (RECOMMENDED - MCP support)
curl -L https://raw.githubusercontent.com/Cyfrin/up/main/install | bash
cyfrinup

# Echidna (OPTIONAL - fuzzing)
docker pull trailofbits/eth-security-toolbox
```

#### Development Environment
- Python 3.11+ (venv/conda recommended)
- Node.js 18+ (for ethers.js, viem)
- Required packages:
  ```bash
  pip install langchain langgraph anthropic openai web3 eth-abi
  ```

#### API Keys Required
- [ ] Etherscan API Key
- [ ] Alchemy/Infura RPC URL
- [ ] Anthropic API (Claude)
- [ ] OpenAI API (GPT-4, optional)

#### Project Structure Setup
```bash
mkdir -p src/{agents,tools,knowledge,utils}
mkdir -p data/{bugs,reports,contracts}
mkdir -p tests configs
```

### Phase 3: Knowledge Base Construction (1 month)

#### bugs_ethereum.json - Core Vulnerability Database
**Priority: HIGHEST** (Source of 76.5% successful detections)

Structure:
```json
{
  "id": "VULN-001",
  "category": "reentrancy",
  "subcategory": "cross-function",
  "severity": "critical",
  "pattern": "...",
  "detection_query": "...",
  "examples": [
    {
      "code": "...",
      "explanation": "...",
      "source": "Solodit/Code4rena/CVE-xxx"
    }
  ]
}
```

Data sources:
- Solodit (50,000+ reports)
- Code4rena findings
- Sherlock findings
- Immunefi disclosed bugs
- CVE database

#### Semantic Search System
- [ ] Choose vector DB (ChromaDB/Pinecone/Weaviate)
- [ ] Implement code embedding (OpenAI/Solidity-specific model)
- [ ] Index historical vulnerability patterns
- [ ] Build similarity search API

#### External Data Integration
- [ ] Etherscan API wrapper (contract info, source code)
- [ ] Solodit scraper/API (audit reports)
- [ ] Historical audit report collection

### Phase 4: AI Agent Implementation (2-3 months)

#### Foundation (Week 1-2)
- [ ] LangGraph setup and ReAct pattern implementation
- [ ] Claude 3.5 Sonnet integration
- [ ] Basic agent loop with memory/context management

#### Tool Integration (Week 2-3)
- [ ] Slither wrapper with result parsing
- [ ] Foundry wrapper (test execution, PoC generation)
- [ ] Aderyn integration via MCP
- [ ] Etherscan API tool

#### Three-Strategy Implementation (Week 4-8)

**Strategy 1: Specification-Based Static Analysis (17.6%)**
- [ ] NatSpec/comment analysis
- [ ] Spec-to-code mapping
- [ ] Access control verification

**Strategy 2: Similar Bug Pattern Search (76.5%) ⭐ MOST CRITICAL**
- [ ] Code → Natural Language converter
- [ ] Vector similarity search implementation
- [ ] Pattern matching with context awareness
- [ ] Horizontal expansion (apply found patterns across codebase)

**Strategy 3: Dynamic Test Generation (5.9%)**
- [ ] Foundry fuzz test auto-generation
- [ ] Echidna property test generation
- [ ] Invariant auto-extraction

#### Multi-Agent Architecture (Week 9-12)
- [ ] Orchestrator Agent (task decomposition, coordination)
- [ ] Recon Agent (information gathering, dependency analysis)
- [ ] Vuln Agent (3-strategy execution, prioritization)
- [ ] Exploit Agent (PoC creation with Foundry)

#### Report Generation
- [ ] Platform-specific templates (Immunefi, Code4rena, Sherlock)
- [ ] Automated report generation with:
  - Severity assessment
  - Root cause analysis
  - Impact analysis
  - PoC code
  - Remediation recommendations

### Phase 5: Real-World Testing (Ongoing)

#### Contest Participation
- [ ] **Sherlock** - First manual participation (no AI)
- [ ] **Code4rena** - Second manual participation
- [ ] AI-assisted participation (human + AI collaboration)
- [ ] Autonomous AI agent participation

#### Performance Metrics
Track:
- Number of valid findings
- False positive rate (audit contests penalize invalid submissions)
- Duplicate rate
- Reward amount
- Processing time per contract

#### Continuous Improvement
- Analyze failures and false positives
- Update bugs_ethereum.json with new patterns
- Refine prompts and detection logic
- Adjust LLM parameters

## Important Platforms

- **Sherlock**: https://audits.sherlock.xyz/ - Weekly contests, beginner-friendly
- **Code4rena**: https://code4rena.com/ - Largest platform, highest rewards
- **Immunefi**: https://immunefi.com/ - Live bug bounties (advanced)
- **Solodit**: https://solodit.cyfrin.io/ - 50,000+ vulnerability reports database

## Common Vulnerability Patterns to Implement

Based on Cyfrin course and real audits:
- Reentrancy (including cross-function)
- Weak randomness
- Oracle manipulation
- Access control issues
- Unchecked return values
- Dangerous delegatecall
- Storage collision (proxy patterns)
- Flash loan attacks
- MEV vulnerabilities
- Signature replay attacks

## Notes for AI Development

### Semantic Search Approach (Most Promising)

gohan's insight: Converting code to natural language and performing semantic search was the most successful approach:

1. Parse Solidity code → AST
2. Convert to natural language descriptions
3. Embed using LLM
4. Vector similarity search against known vulnerability patterns
5. Analyze matches in context

### Avoid Common Pitfalls

- Don't try full end-to-end automation without domain knowledge
- Don't rely solely on LLM reasoning (combine with static analysis)
- Don't skip manual learning phase
- Don't ignore false positive rates - audit contests penalize invalid reports

## Language Note

All documentation is currently in Japanese. When implementing, code comments and documentation should follow standard English conventions for open source projects, but refer to Japanese docs for detailed research insights.

## Future File Structure (Proposed)

```
eth-bounty-agent/
├── agent/
│   ├── core/              # Orchestrator, planner, executor
│   ├── agents/            # Recon, vuln, exploit agents
│   ├── tools/             # Etherscan, Slither, Foundry wrappers
│   ├── prompts/           # System prompts, vulnerability patterns
│   └── utils/             # Parsers, reporters
├── knowledge/
│   ├── vulnerabilities/   # bugs_ethereum.json
│   ├── audit_reports/     # Historical reports from Solodit
│   └── defi_protocols/    # DeFi-specific knowledge
├── tests/
├── docs/                  # Current research documentation
└── scripts/              # Setup and execution scripts
```

## Success Metrics

The agent should aim for:
- **Short-term**: Solve Ethernaut and Damn Vulnerable DeFi autonomously
- **Medium-term**: Achieve 30%+ valid finding rate in audit contests (matching Nyx's 31.5%)
- **Long-term**: Discover vulnerabilities that win bounties in real contests

## Quick Start Guide

For someone starting TODAY, here's the immediate action plan:

### Day 1
1. [ ] Register for Cyfrin Security Course and watch first 2 hours
2. [ ] Install Foundry and complete basic "Hello World" contract
3. [ ] Solve Ethernaut levels 0-3
4. [ ] Read 3 audit reports on Solodit

### Week 1
1. [ ] Complete Ethernaut levels 1-10
2. [ ] Read 10 more Solodit reports (focus on high/critical findings)
3. [ ] Set up Python environment and install Slither
4. [ ] Start Damn Vulnerable DeFi (complete 2-3 challenges)

### Month 1
1. [ ] Complete Cyfrin Security Course to 50%
2. [ ] Ethernaut fully completed (32 levels)
3. [ ] Read 50 Solodit reports total
4. [ ] Observe one Sherlock contest (don't submit, just learn)
5. [ ] Complete 5-7 Damn Vulnerable DeFi challenges

### Month 2-3
1. [ ] Cyfrin Security Course 100% complete
2. [ ] Read 100-200 Solodit reports
3. [ ] Participate in first Sherlock contest manually (expect to find nothing - that's OK!)
4. [ ] Start building bugs_ethereum.json database
5. [ ] Begin LangGraph tutorials and experimentation

**Key Reminder**: gohan failed when trying "LangChain full automation" first. Success came from domain knowledge → manual auditing → AI automation. Don't skip the learning phase!

## Research References

### Documentation
Key insight sources in [docs/06-gohan-insights-research.md](docs/06-gohan-insights-research.md):
- Nyx Foundation's world #1 achievement (December 2025)
- Three-strategy architecture details
- Semantic search implementation approach
- "Democratization of auditing" - non-engineers found most bugs using AI agent

Complete TODO roadmap: [docs/07-TODO.md](docs/07-TODO.md)

### External Resources
- [Nyx Foundation](https://nyx.foundation/) - gohan's research organization
- [NyxFoundation GitHub](https://github.com/NyxFoundation) - AI agent repositories
- [Cyfrin Security Course](https://updraft.cyfrin.io/courses/security) - 50+ hours free course
- [Solodit](https://solodit.cyfrin.io/) - 50,000+ vulnerability reports
- [Ethernaut](https://ethernaut.openzeppelin.com/) - CTF challenges
- [Damn Vulnerable DeFi](https://www.damnvulnerabledefi.xyz/) - DeFi CTF
