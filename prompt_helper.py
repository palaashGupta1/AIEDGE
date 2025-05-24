import streamlit as st
import openai

st.set_page_config(page_title="Prompt Enhancer", page_icon="✨")

st.title("🔧 AI Prompt Enhancer")
st.markdown("Create better prompts for AI apps using your role, context, and task.")

# User enters OpenAI API Key
api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# Input fields
role = st.text_input("👤 Role", placeholder="e.g., an experienced Python developer")
context = st.text_area("📄 Context", placeholder="e.g., I am learning to build AI apps using Streamlit.")
task = st.text_area("✅ Task", placeholder="e.g., Help me write a Streamlit app that enhances prompts.")

# Prompt construction
def enhance_prompt(role, context, task):
    return f"""
You are {role}.
Context: {context}
Task: {task}

Before responding:
- Ask the user at least 2–3 clarifying questions to better understand their request.
- Confirm assumptions before proceeding.

Format your final answer as:
1. **Clarified Understanding**
2. **Key Takeaways**
3. **Step-by-Step Guidance**
4. **Example (if helpful)**
"""

# Handle submission
if st.button("✨ Enhance Prompt"):
    if not api_key:
        st.error("⚠️ Please enter your OpenAI API key.")
    elif not (role and context and task):
        st.warning("📥 Please fill in all fields.")
    else:
        prompt = enhance_prompt(role, context, task)
        st.subheader("🧠 Enhanced Prompt")
        st.code(prompt, language="markdown")

        try:
            client = openai.OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.subheader("🤖 GPT's Response")
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            st.error(f"❌ Error: {e}")
