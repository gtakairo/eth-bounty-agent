# Setup Guide

This guide covers the setup process for Phase 2 (Environment Setup) and beyond.

## Prerequisites

- Python 3.11 or higher
- Node.js 18+ (for ethers.js, viem)
- Git
- (Optional) Docker for Echidna

## Phase 2: Environment Setup

### 1. Install Foundry (REQUIRED)

```bash
curl -L https://foundry.paradigm.xyz | bash
foundryup
forge --version
```

### 2. Install Slither (REQUIRED)

```bash
pip3 install slither-analyzer
slither --version
```

### 3. Install Aderyn (RECOMMENDED - MCP support)

```bash
curl -L https://raw.githubusercontent.com/Cyfrin/up/main/install | bash
cyfrinup
aderyn --version
```

### 4. Install Echidna (OPTIONAL - fuzzing)

**Option 1: Docker (Recommended)**
```bash
docker pull trailofbits/eth-security-toolbox
```

**Option 2: Homebrew (macOS)**
```bash
brew install echidna
```

### 5. Python Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Or install with development dependencies
pip install -e ".[dev]"
```

### 6. Configuration

```bash
# Copy environment template
cp configs/.env.example .env

# Edit .env and add your API keys
# - ANTHROPIC_API_KEY
# - OPENAI_API_KEY (optional)
# - ETHERSCAN_API_KEY
# - ALCHEMY_API_KEY or INFURA_API_KEY
```

### 7. Verify Installation

```bash
# Run tests
pytest

# Check code formatting
black --check src/
ruff check src/
```

## Project Structure

```
eth-bounty-agent/
├── src/
│   ├── agents/           # AI agents (Orchestrator, Recon, Vuln, Exploit)
│   ├── tools/            # Tool wrappers (Slither, Foundry, Etherscan)
│   ├── knowledge/        # Vulnerability knowledge base
│   └── utils/            # Utilities (parsers, reporters)
├── data/
│   ├── bugs/             # bugs_ethereum.json
│   ├── reports/          # Audit reports
│   └── contracts/        # Sample contracts
├── tests/                # Test suite
├── configs/              # Configuration files
│   ├── .env.example      # Environment variables template
│   └── agent_config.yaml # Agent configuration
├── docs/                 # Research documentation (Japanese)
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project metadata
├── CLAUDE.md             # Guide for Claude Code
└── README.md             # Project overview
```

## API Keys Required

### Essential
- **Anthropic API** (Claude): Get from https://console.anthropic.com/
- **Etherscan API**: Get from https://etherscan.io/apis
- **Alchemy or Infura**: Get from https://www.alchemy.com/ or https://infura.io/

### Optional
- **OpenAI API** (GPT-4): Get from https://platform.openai.com/
- **Pinecone** (if using cloud vector DB): Get from https://www.pinecone.io/

## Development Workflow

### Code Style

```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_placeholder.py

# Run with verbose output
pytest -v
```

### Running the Agent (Phase 4+)

```bash
# TODO: Add agent execution commands during Phase 4 implementation
# Example (future):
# python -m src.agents.orchestrator --contract <address>
```

## Troubleshooting

### Slither Installation Issues

If Slither installation fails:
```bash
# Install solc first
pip install py-solc-x
python -c "import solcx; solcx.install_solc('0.8.20')"

# Then install Slither
pip install slither-analyzer
```

### Foundry Not Found

Make sure to restart your terminal after installing Foundry:
```bash
# Re-run foundryup
foundryup

# Verify installation
which forge
```

### Permission Issues (Linux/Mac)

If you encounter permission errors:
```bash
# Use --user flag
pip install --user -r requirements.txt
```

## Next Steps

After completing Phase 2 setup:

1. **Phase 3**: Knowledge Base Construction
   - Populate bugs_ethereum.json from Solodit
   - Set up vector database for semantic search
   - Collect audit reports

2. **Phase 4**: AI Agent Implementation
   - Implement tool wrappers
   - Build multi-agent architecture
   - Integrate three strategies

3. **Phase 5**: Real-World Testing
   - Participate in audit contests
   - Measure performance metrics
   - Continuous improvement

## Resources

- [Foundry Book](https://book.getfoundry.sh/)
- [Slither Documentation](https://github.com/crytic/slither)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Cyfrin Security Course](https://updraft.cyfrin.io/courses/security)
