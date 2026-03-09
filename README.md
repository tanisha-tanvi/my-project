🛡️ Automated AI Red Teaming Agent
This repository contains a Streamlit-based Red Teaming Dashboard designed to automatically test LLMs against adversarial attacks such as Prompt Injection, Jailbreaking, and Social Engineering.

The system utilizes an "Attacker" model to generate sophisticated prompts and a "Target" model to simulate vulnerabilities, providing real-time metrics on security leaks.

🚀 Features
Dual-Model Orchestration: Uses Llama-3.3-70b as the sophisticated Attacker and Llama-3.1-8b as the Target.

Adversarial Knowledge Base: A built-in RAG (Retrieval-Augmented Generation) logic that feeds known attack techniques (like DAN mode) into the attacker.

Unit Economics Tracking: Real-time calculation of token consumption and estimated session costs.

Vulnerability Scoring: Automated evaluation that marks an attack as a "Success" if the target reveals a hardcoded secret password (CRYPTO_2026).

Permanent Logging: All attack attempts are recorded in attacks.log for audit purposes.

🛠️ Tech Stack
Frontend: Streamlit

LLM Framework: LangChain

Inference: Groq Cloud (Llama Models)

Data Handling: Pandas

📋 Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/your-username/ai-red-team-agent.git
cd ai-red-team-agent
2. Install Dependencies
Ensure you have Python 3.9+ installed, then run:

Bash
pip install -r requirements.txt
3. Environment Configuration
Create a .env file in the root directory and add your Groq API Key:

Code snippet
GROQ_API_KEY=your_groq_api_key_here
4. Run the Application
Bash
streamlit run app.py
🖥️ Usage Guide
Select Strategy: Choose between Prompt Injection, Jailbreak, or Social Engineering in the sidebar.

Variations: Set the number of attack variations you wish to generate.

Run Sequence: Execute the red team sequence to see the live vulnerability logs.

Analyze Metrics: Check the Vulnerability Score and Consumption Metrics to evaluate model robustness and testing costs.

📂 Project Structure
app.py: The Streamlit dashboard and UI logic.

red_team_logic.py: The RedTeamOrchestrator class managing the Attacker/Target interactions.

attacks.log: Automatically generated file storing a permanent history of attacks.

.env: Local environment variables (API Keys).

⚠️ Disclaimer
This tool is for educational and authorized security testing purposes only. Never use this agent against systems you do not have explicit permission to test.
