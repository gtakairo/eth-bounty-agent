# Ethereum Bug Bounty AI Agent

An AI agent for autonomous discovery of vulnerabilities in Ethereum smart contracts, targeting bug bounty platforms and audit contests.

## 🏆 Project Status

**Phase 0: Research** ✅ COMPLETED

This repository currently contains comprehensive research documentation on building an AI security agent, inspired by Nyx Foundation's world #1 achievement in the Ethereum "Fusaka" audit contest (December 2025).

## 📚 Documentation

All research and planning documentation is located in the [`docs/`](docs/) directory (in Japanese):

- [`00-overview.md`](docs/00-overview.md) - Project overview and key insights
- [`01-bug-bounty-platforms.md`](docs/01-bug-bounty-platforms.md) - Platform comparison (Immunefi, Code4rena, Sherlock)
- [`02-security-tools.md`](docs/02-security-tools.md) - Security tools analysis (Slither, Foundry, Echidna, Aderyn)
- [`03-learning-resources.md`](docs/03-learning-resources.md) - Learning resources and CTF challenges
- [`04-project-proposal.md`](docs/04-project-proposal.md) - AI agent architecture proposal
- [`05-ai-agent-research.md`](docs/05-ai-agent-research.md) - Academic research on AI security
- [`06-gohan-insights-research.md`](docs/06-gohan-insights-research.md) - ⭐ Real-world insights from Nyx Foundation
- [`07-TODO.md`](docs/07-TODO.md) - Development roadmap

## 🤖 For Claude Code

If you're Claude Code working in this repository, please read [`CLAUDE.md`](CLAUDE.md) for:
- Project architecture and three-strategy approach (76.5% success from similar bug pattern search)
- Technology stack and tool setup commands
- Development priorities and phased roadmap
- Quick start guide for immediate actions
- Critical lessons from gohan's experience

## 🎯 Core Approach

Based on Nyx Foundation's proven success, the agent will implement three parallel strategies:

1. **Specification-Based Static Analysis** (17.6% success rate)
2. **Similar Bug Pattern Search** (76.5% success rate) ⭐ Most effective
3. **Dynamic Test Generation** (5.9% success rate)

## 🛠️ Technology Stack (Planned)

- **Language**: Python 3.11+
- **Agent Framework**: LangGraph
- **LLM**: Claude 3.5 Sonnet (Anthropic API)
- **Static Analysis**: Slither, Aderyn (with MCP support)
- **Testing/Fuzzing**: Foundry, Echidna
- **Blockchain**: ethers.py / web3.py
- **Storage**: PostgreSQL + pgvector (for semantic search)

## 🚀 Quick Start

### For Learning (Phase 1)
1. Complete [Cyfrin Security Course](https://updraft.cyfrin.io/courses/security) (50+ hours)
2. Solve all [Ethernaut](https://ethernaut.openzeppelin.com/) challenges (32 levels)
3. Complete [Damn Vulnerable DeFi](https://www.damnvulnerabledefi.xyz/)
4. Read 100+ audit reports on [Solodit](https://solodit.cyfrin.io/)

### For Development (Phase 2+)
```bash
# Install Foundry
curl -L https://foundry.paradigm.xyz | bash
foundryup

# Install Slither
pip3 install slither-analyzer

# Install Aderyn (MCP compatible)
curl -L https://raw.githubusercontent.com/Cyfrin/up/main/install | bash
cyfrinup

# Setup Python environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install langchain langgraph anthropic web3 eth-abi
```

## 📖 Key Lessons from gohan's Experience

❌ **What Failed:**
- Starting with bug bounties (too difficult for beginners)
- "LangChain full automation" without domain knowledge

✅ **What Succeeded:**
- Starting with audit contests (Sherlock, Code4rena)
- Manual auditing experience first (31 audits in 2 months)
- Building domain knowledge, then automating with AI → World #1 ranking

## 🎓 Learning Resources

- [Sherlock](https://audits.sherlock.xyz/) - Weekly audit contests, beginner-friendly
- [Code4rena](https://code4rena.com/) - Largest audit platform
- [Solodit](https://solodit.cyfrin.io/) - 50,000+ vulnerability reports database
- [Cyfrin Security Course](https://updraft.cyfrin.io/courses/security) - Free comprehensive course

## 🔗 Inspiration

- [Nyx Foundation](https://nyx.foundation/) - gohan's research organization
- [NyxFoundation GitHub](https://github.com/NyxFoundation) - AI agent repositories
- [@grandchildrice](https://x.com/grandchildrice) - gohan's X/Twitter

## 📄 License

[To be determined]

## 🤝 Contributing

This project is currently in the research and planning phase. Implementation will begin after completing Phase 1 (Foundation Skills).

---

**Note**: All detailed research documentation is in Japanese. The implementation code will follow standard English conventions for open source projects.
