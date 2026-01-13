"""
Pytest configuration and fixtures for eth-bounty-agent tests.
"""
import pytest
from pathlib import Path


@pytest.fixture
def project_root():
    """Return the project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def bugs_db_path(project_root):
    """Return the path to bugs_ethereum.json."""
    return project_root / "data" / "bugs" / "bugs_ethereum.json"


@pytest.fixture
def sample_contract():
    """Return a sample vulnerable Solidity contract for testing."""
    return """
    // SPDX-License-Identifier: MIT
    pragma solidity ^0.8.0;

    contract VulnerableContract {
        mapping(address => uint256) public balances;

        // Vulnerable to reentrancy
        function withdraw() external {
            uint256 amount = balances[msg.sender];
            (bool success, ) = msg.sender.call{value: amount}("");
            require(success, "Transfer failed");
            balances[msg.sender] = 0;  // State update after external call
        }

        function deposit() external payable {
            balances[msg.sender] += msg.value;
        }
    }
    """


@pytest.fixture
def mock_llm_response():
    """Return a mock LLM response for testing."""
    return {
        "vulnerability_found": True,
        "category": "reentrancy",
        "severity": "critical",
        "description": "Reentrancy vulnerability in withdraw function",
        "recommendation": "Apply CEI pattern: update state before external call"
    }
