import streamlit as st
import pandas as pd
import logging
from red_team_logic import RedTeamOrchestrator

# 1. Permanent Logging Setup
logging.basicConfig(
    filename="attacks.log", 
    level=logging.INFO, 
    format='%(asctime)s - STRATEGY: %(message)s'
)

st.set_page_config(page_title="AI Red Team Dashboard", layout="wide")
st.title("🛡️ Automated AI Red Teaming Agent")

# Cache the orchestrator to prevent re-initialization lag
@st.cache_resource
def get_orchestrator():
    return RedTeamOrchestrator()

orchestrator = get_orchestrator()

# Initialize session state
if 'results' not in st.session_state:
    st.session_state.results = []
if 'total_tokens' not in st.session_state:
    st.session_state.total_tokens = 0

# Sidebar - Settings & Unit Economics
st.sidebar.header("Attack Configuration")
attack_strategy = st.sidebar.selectbox("Select Strategy", ["Prompt Injection", "Jailbreak", "Social Engineering"])
num_attacks = st.sidebar.slider("Number of Variations", 1, 10, 2)

if st.sidebar.button("Run Red Team Sequence"):
    for _ in range(num_attacks):
        # Execute Attack
        attack_prompt, attacker_usage = orchestrator.generate_attack(attack_strategy)
        target_output, target_usage = orchestrator.simulate_target(attack_prompt)
        status = orchestrator.evaluate_success(target_output)
        
        # Calculate Costs (The 'Royalty' side of things)
        session_tokens = attacker_usage.get('total_tokens', 0) + target_usage.get('total_tokens', 0)
        st.session_state.total_tokens += session_tokens
        
        # Log to file permanently
        logging.info(f"{attack_strategy} | STATUS: {status} | TOKENS: {session_tokens}")
        
        # Store for UI display
        res = {
            "Strategy": attack_strategy, 
            "Prompt": attack_prompt, 
            "Response": target_output, 
            "Status": status,
            "Tokens": session_tokens
        }
        st.session_state.results.append(res)

# Sidebar Unit Economics Display
st.sidebar.divider()
st.sidebar.subheader("Consumption Metrics")
st.sidebar.metric("Total Tokens Used", f"{st.session_state.total_tokens:,}")
# Hypothetical cost of $0.002 per 1k tokens
est_cost = (st.session_state.total_tokens / 1000) * 0.002
st.sidebar.caption(f"Estimated Session Cost: ${est_cost:.4f}")

# Main UI Dashboard
if st.session_state.results:
    df = pd.DataFrame(st.session_state.results)
    
    # KPIs
    m1, m2 = st.columns(2)
    with m1:
        success_rate = (df['Status'] == 'Success').mean() * 100
        st.metric("Vulnerability Score", f"{success_rate}%")
    with m2:
        st.metric("Avg Tokens / Run", int(df['Tokens'].mean()))

    st.subheader("Live Vulnerability Logs")
    # Styling 'Success' as red to highlight security leaks
    st.dataframe(
        df.style.applymap(lambda x: 'background-color: #9e1a1a' if x == 'Success' else '', subset=['Status']),
        use_container_width=True
    )

    if st.button("Clear Dashboard"):
        st.session_state.results = []
        st.session_state.total_tokens = 0
        st.rerun()