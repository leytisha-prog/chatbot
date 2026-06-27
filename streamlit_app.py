import streamlit as st

st.set_page_config(
    page_title="AI Configuration Explorer",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Configuration Explorer")
st.write("Explore how AI settings affect the code, simulated output, and instructional design decisions.")

# -----------------------------
# Sidebar / Configuration Panel
# -----------------------------
st.sidebar.header("1. AI Configuration")

model = st.sidebar.selectbox(
    "Model",
    ["Gemini Flash", "Gemini Pro", "Claude Sonnet", "GPT-4o"]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.5,
    value=0.3,
    step=0.1
)

thinking_level = st.sidebar.selectbox(
    "Thinking Level",
    ["Low", "Medium", "High"],
    index=1
)

system_instruction = st.sidebar.selectbox(
    "System Instruction",
    [
        "You are an instructional designer.",
        "You are a creative storyteller.",
        "You are a college professor.",
        "You are a multimedia learning coach."
    ]
)

prompt = st.sidebar.text_area(
    "User Prompt",
    "Create a storyboard for an online cybersecurity lesson.",
    height=120
)

# -----------------------------
# Simulated logic
# -----------------------------
if "Flash" in model:
    model_effect = "fast, concise, and practical"
elif "Pro" in model:
    model_effect = "detailed, structured, and more analytical"
elif "Claude" in model:
    model_effect = "reflective, polished, and strong for writing"
else:
    model_effect = "flexible, conversational, and multimodal"

if temperature < 0.4:
    temp_effect = "structured, predictable, and consistent"
    activity = "a checklist-based activity"
elif temperature < 0.9:
    temp_effect = "balanced, clear, and moderately creative"
    activity = "a short scenario-based activity"
else:
    temp_effect = "creative, varied, and imaginative"
    activity = "a role-play or escape-room style activity"

if thinking_level == "Low":
    thinking_effect = "quick and simple, with limited explanation"
elif thinking_level == "Medium":
    thinking_effect = "moderately detailed, with some reasoning"
else:
    thinking_effect = "more detailed, reflective, and analytical"

if "instructional designer" in system_instruction.lower():
    system_effect = "learning objectives, sequencing, practice, and assessment"
elif "storyteller" in system_instruction.lower():
    system_effect = "characters, conflict, narrative flow, and emotional engagement"
elif "professor" in system_instruction.lower():
    system_effect = "formal explanation, academic language, and lecture structure"
else:
    system_effect = "visual design, media selection, and multimedia learning principles"

# -----------------------------
# Main layout
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("2. Python Configuration View")

    code = f'''model = "{model}"

temperature = {temperature}

thinking_level = "{thinking_level}"

system_instruction = """
{system_instruction}
"""

prompt = """
{prompt}
"""

response = generate_ai_output(
    model=model,
    temperature=temperature,
    thinking_level=thinking_level,
    system_instruction=system_instruction,
    prompt=prompt
)
'''
    st.code(code, language="python")

with col2:
    st.subheader("3. Simulated AI Output")

    output = f"""
The selected model would likely produce a response that is **{model_effect}**.

Because the temperature is **{temperature}**, the output would be **{temp_effect}**.

Because the thinking level is **{thinking_level}**, the response would be **{thinking_effect}**.

Because the system instruction says:

> {system_instruction}

The response would emphasize **{system_effect}**.

### Possible AI-generated storyboard

1. Opening: Introduce the cybersecurity problem.
2. Objective: Explain what learners should know or do.
3. Content: Present the key concept.
4. Activity: Include **{activity}**.
5. Assessment: Add a short knowledge check.
6. Reflection: Ask learners how they would apply this in real life.
"""
    st.markdown(output)

st.divider()

st.subheader("4. Educational Implication")

st.info(
    "For instructional designers, these settings are design decisions. "
    "The model affects depth and style. Temperature affects creativity and consistency. "
    "Thinking level affects reasoning and explanation. System instructions shape the role "
    "the AI plays in the learning experience. The user prompt defines the task the AI is expected to complete."
)

st.subheader("5. Student Reflection")

st.write("""
Ask students:

1. Which setting changed the output the most?
2. Which setting would matter most in an AI tutoring system?
3. When would a low temperature be better for learning?
4. When would a high temperature be useful?
5. How do system instructions influence the learner experience?
""")