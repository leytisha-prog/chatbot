import streamlit as st

st.set_page_config(
    page_title="AI Configuration Explorer",
    page_icon="🧠",
    layout="wide"
)

# -----------------------------
# Page Header
# -----------------------------
st.title("🧠 AI Configuration Explorer")
st.write(
    "A no-code simulation for exploring how AI settings shape the user interface, "
    "Python configuration, and educational AI outputs."
)

st.info(
    "This is a simulation. It does not call Gemini, Claude, or OpenAI. "
    "The goal is to help students read and interpret AI configuration, not write production code."
)

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.title("🎛️ AI Settings")

model = st.sidebar.selectbox(
    "Model / AI Engine",
    ["Gemini Flash", "Gemini Pro", "Claude Sonnet", "GPT-4o"]
)

temperature = st.sidebar.slider(
    "Temperature / Creativity Control",
    min_value=0.0,
    max_value=1.5,
    value=0.3,
    step=0.1
)

thinking_level = st.sidebar.selectbox(
    "Thinking Level / Reasoning Depth",
    ["Low", "Medium", "High"],
    index=1
)

system_instruction = st.sidebar.selectbox(
    "System Instruction / AI Teaching Role",
    [
        "You are an instructional designer.",
        "You are a creative storyteller.",
        "You are a college professor.",
        "You are a multimedia learning coach.",
        "You are a Socratic tutor who asks guiding questions."
    ]
)

prompt = st.sidebar.text_area(
    "User Prompt / Learning Task",
    "Create a storyboard for an online cybersecurity lesson.",
    height=120
)

compare_mode = st.sidebar.checkbox("Show comparison version", value=False)

# -----------------------------
# Helper Functions
# -----------------------------
def get_model_effect(model):
    if "Flash" in model:
        return "fast, concise, and practical"
    if "Pro" in model:
        return "detailed, structured, and more analytical"
    if "Claude" in model:
        return "reflective, polished, and strong for writing"
    return "flexible, conversational, and multimodal"

def get_temperature_effect(temp):
    if temp < 0.4:
        return "structured, predictable, and consistent", "a checklist-based activity"
    elif temp < 0.9:
        return "balanced, clear, and moderately creative", "a short scenario-based activity"
    else:
        return "creative, varied, and imaginative", "a role-play or escape-room style activity"

def get_thinking_effect(level):
    if level == "Low":
        return "quick and simple, with limited explanation"
    if level == "Medium":
        return "moderately detailed, with some reasoning"
    return "more detailed, reflective, and analytical"

def get_system_effect(system):
    s = system.lower()
    if "instructional designer" in s:
        return "learning objectives, sequencing, practice, and assessment"
    if "storyteller" in s:
        return "characters, conflict, narrative flow, and emotional engagement"
    if "professor" in s:
        return "formal explanation, academic language, and lecture structure"
    if "socratic" in s:
        return "guiding questions, learner reflection, and metacognitive thinking"
    return "visual design, media selection, and multimedia learning principles"

def make_code(model, temperature, thinking_level, system_instruction, prompt):
    return f'''# AI Application Configuration

model = "{model}"

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

def make_output(model, temperature, thinking_level, system_instruction, prompt):
    model_effect = get_model_effect(model)
    temp_effect, activity = get_temperature_effect(temperature)
    thinking_effect = get_thinking_effect(thinking_level)
    system_effect = get_system_effect(system_instruction)

    return f"""
### Simulated AI Response

The selected model would likely produce a response that is **{model_effect}**.

Because the temperature is **{temperature}**, the output would be **{temp_effect}**.

Because the thinking level is **{thinking_level}**, the response would be **{thinking_effect}**.

Because the system instruction says:

> {system_instruction}

The response would emphasize **{system_effect}**.

### Possible AI-Generated Storyboard

1. **Opening:** Introduce the learning problem.
2. **Objective:** Explain what learners should know or do.
3. **Content:** Present the key concept.
4. **Activity:** Include **{activity}**.
5. **Assessment:** Add a short knowledge check.
6. **Reflection:** Ask learners how they would apply this in real life.

### Original User Prompt

> {prompt}
"""

# -----------------------------
# Main Layout
# -----------------------------
tab1, tab2, tab3 = st.tabs([
    "Explorer",
    "Compare Configurations",
    "Student Activity"
])

with tab1:
    st.header("AI Configuration Explorer")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("1. Interface Settings")
        st.markdown(f"""
        🟦 **Model / AI Engine**  
        `{model}`

        🟧 **Temperature / Creativity Control**  
        `{temperature}`

        🟨 **Thinking Level / Reasoning Depth**  
        `{thinking_level}`

        🟩 **System Instruction / AI Teaching Role**  
        `{system_instruction}`

        🟪 **Prompt / Learning Task**  
        `{prompt}`
        """)

    with col2:
        st.subheader("2. Python Configuration")
        st.code(
            make_code(model, temperature, thinking_level, system_instruction, prompt),
            language="python"
        )

    with col3:
        st.subheader("3. Simulated AI Output")
        st.markdown(
            make_output(model, temperature, thinking_level, system_instruction, prompt)
        )

    st.divider()

    st.subheader("Instructional Design Interpretation")
    st.success(
        "These settings are design decisions. The model affects depth and style. "
        "Temperature affects creativity and consistency. Thinking level affects reasoning. "
        "System instructions shape the AI's teaching role. The prompt defines the learning task."
    )

with tab2:
    st.header("Compare Two AI Configurations")

    st.write(
        "Use this section to compare a more consistent configuration with a more creative one."
    )

    left, right = st.columns(2)

    with left:
        st.subheader("Configuration A: Consistent Tutor")
        a_model = "Gemini Flash"
        a_temp = 0.2
        a_thinking = "Medium"
        a_system = "You are an instructional designer."
        a_prompt = prompt

        st.code(make_code(a_model, a_temp, a_thinking, a_system, a_prompt), language="python")
        st.markdown(make_output(a_model, a_temp, a_thinking, a_system, a_prompt))

    with right:
        st.subheader("Configuration B: Creative Designer")
        b_model = "Gemini Pro"
        b_temp = 1.2
        b_thinking = "High"
        b_system = "You are a creative storyteller."
        b_prompt = prompt

        st.code(make_code(b_model, b_temp, b_thinking, b_system, b_prompt), language="python")
        st.markdown(make_output(b_model, b_temp, b_thinking, b_system, b_prompt))

with tab3:
    st.header("Student Activity: Read the AI Configuration")

    st.markdown("""
    ### Part 1: Identify the Configuration

    Students should locate the following in the Python configuration:

    - 🟦 Model
    - 🟧 Temperature
    - 🟨 Thinking Level
    - 🟩 System Instruction
    - 🟪 Prompt

    ### Part 2: Predict

    Before changing a setting, students answer:

    1. What do you think will change in the output?
    2. Will the output become more creative, more formal, or more structured?
    3. Would this change help or hurt learners?

    ### Part 3: Modify One Setting

    Students change only one setting at a time.

    Recommended experiments:

    - Change temperature from `0.2` to `1.2`
    - Change the system instruction from instructional designer to storyteller
    - Change thinking level from Low to High
    - Rewrite the prompt to be more specific

    ### Part 4: Reflect

    Students respond:

    > Which AI setting seems most important for instructional design, and why?
    """)

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption(
    "AI Configuration Explorer v2.0 | Designed for AI in Multimedia for Instructional Design"
)