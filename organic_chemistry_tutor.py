import streamlit as st
import random
import openai
from PIL import Image

# Set up Streamlit app configuration
st.set_page_config(page_title="Organic Chemistry Tutor", page_icon="🧪", layout="centered")
st.title("🌿 Organic Chemistry Tutor")

# Sidebar menu selection
menu = st.sidebar.selectbox("Choose a topic", [
    "🏠 Home",
    "🧬 Functional Groups",
    "🔤 IUPAC Naming",
    "📈 Homologous Series",
    "🧠 Quick Quiz",
    "🤖 AI Compound Naming"
])

# ------------------------ Home Page ------------------------
if menu == "🏠 Home":
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Organic_chemistry_structure.svg/800px-Organic_chemistry_structure.svg.png", width=500)
    st.header("Welcome to the Organic Chemistry Tutor")
    st.markdown("""
    This interactive app helps you:
    - Understand **functional groups**
    - Master **IUPAC naming**
    - Explore **homologous series**
    - Test your knowledge with quizzes
    - Use **AI** to name any organic compound 🔬

    Navigate using the sidebar on the left. 👈
    """)
    st.success("Built with ❤️ using Streamlit + OpenAI")

# ------------------------ Functional Groups ------------------------
elif menu == "🧬 Functional Groups":
    st.header("🧬 Common Functional Groups")
    
    groups = {
        "Alkane": {"Group": "C-C (single bond)", "Example": "Ethane (C2H6)", "Desc": "Saturated hydrocarbon with only single bonds."},
        "Alkene": {"Group": "C=C (double bond)", "Example": "Ethene (C2H4)", "Desc": "Unsaturated hydrocarbon with one or more double bonds."},
        "Alkyne": {"Group": "C≡C (triple bond)", "Example": "Ethyne (C2H2)", "Desc": "Unsaturated hydrocarbon with one or more triple bonds."},
        "Alcohol": {"Group": "-OH", "Example": "Ethanol (C2H5OH)", "Desc": "Contains a hydroxyl group."},
        "Carboxylic Acid": {"Group": "-COOH", "Example": "Ethanoic acid (CH3COOH)", "Desc": "Contains a carboxyl group; acidic."},
        "Ketone": {"Group": "C=O (within chain)", "Example": "Propanone (CH3COCH3)", "Desc": "Contains a carbonyl group bonded to two carbon atoms."},
        "Aldehyde": {"Group": "-CHO", "Example": "Ethanal (CH3CHO)", "Desc": "Carbonyl group at end of chain."},
        "Ester": {"Group": "-COO-", "Example": "Ethyl ethanoate (CH3COOC2H5)", "Desc": "Formed from acid + alcohol."},
        "Amine": {"Group": "-NH2", "Example": "Methylamine (CH3NH2)", "Desc": "Contains an amino group."}
    }

    for name, info in groups.items():
        with st.expander(name):
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Organic_functional_groups.svg/640px-Organic_functional_groups.svg.png", width=300)
            st.write(f"**Functional Group:** {info['Group']}")
            st.write(f"**Example:** {info['Example']}")
            st.write(f"**Description:** {info['Desc']}")

# ------------------------ IUPAC Naming ------------------------
elif menu == "🔤 IUPAC Naming":
    st.header("🔤 IUPAC Naming of Organic Compounds")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/IUPAC-2.svg/640px-IUPAC-2.svg.png", width=500)
    
    formula = st.text_input("Enter a compound formula (e.g., CH3COOH, C2H5OH):")
    if formula:
        sample_responses = {
            "CH3COOH": "**Ethanoic Acid** – A carboxylic acid with two carbon atoms.",
            "C2H5OH": "**Ethanol** – A two-carbon alcohol with a hydroxyl group.",
            "CH3CH2CH3": "**Propane** – A three-carbon alkane.",
            "CH3CH=CH2": "**Propene** – A three-carbon alkene with a double bond."
        }
        result = sample_responses.get(formula.strip(), "Compound not in database. Try a common organic molecule.")
        st.markdown(result)

# ------------------------ Homologous Series ------------------------
elif menu == "📈 Homologous Series":
    st.header("📈 Homologous Series and General Formulas")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Alkanes.svg/640px-Alkanes.svg.png", width=500)

    n = st.slider("Value of n (1–10)", min_value=1, max_value=10, value=1)

    st.subheader("Alkanes (CₙH₂ₙ₊₂)")
    st.write(f"Formula: C{n}H{2*n + 2}")

    st.subheader("Alkenes (CₙH₂ₙ)")
    st.write(f"Formula: C{n}H{2*n}")

    st.subheader("Alkynes (CₙH₂ₙ₋₂)")
    st.write(f"Formula: C{n}H{2*n - 2}" if n >= 2 else "Formula not valid for n < 2")

    st.subheader("Alcohols (CₙH₂ₙ₊₁OH)")
    st.write(f"Formula: C{n}H{2*n + 1}OH")

# ------------------------ Quick Quiz ------------------------
elif menu == "🧠 Quick Quiz":
    st.header("🧠 Quick Quiz: Functional Groups & Naming")
    
    quiz_questions = [
        {"question": "Which functional group does ethanol contain?", "options": ["Ketone", "Alcohol", "Alkene"], "answer": "Alcohol"},
        {"question": "What is the general formula for alkenes?", "options": ["CₙH₂ₙ", "CₙH₂ₙ₊₂", "CₙH₂ₙ₋₂"], "answer": "CₙH₂ₙ"},
        {"question": "Which group is represented by -COOH?", "options": ["Alcohol", "Ester", "Carboxylic Acid"], "answer": "Carboxylic Acid"},
        {"question": "Which hydrocarbon has a triple bond?", "options": ["Alkene", "Alkyne", "Alkane"], "answer": "Alkyne"},
        {"question": "Which functional group is present in esters?", "options": ["-OH", "-COOH", "-COO-"], "answer": "-COO-"}
    ]

    score = 0
    for q in quiz_questions:
        st.subheader(q["question"])
        user_answer = st.radio("Select one:", q["options"], key=q["question"])
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is: {q['answer']}")

    st.markdown(f"### 🏁 Final Score: **{score} / {len(quiz_questions)}**")

# ------------------------ AI Naming Assistant ------------------------
elif menu == "🤖 AI Compound Naming":
    st.header("🤖 AI Compound Naming Assistant")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chemical_structure_example.svg/640px-Chemical_structure_example.svg.png", width=400)

    openai.api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else "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"

    user_input = st.text_input("Enter a compound formula or description (e.g., CH3CH2OH, a 3-carbon alcohol):")

    if user_input and openai.api_key != "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":
        with st.spinner("Contacting AI..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a chemistry expert. Respond with the IUPAC name and a short explanation."},
                        {"role": "user", "content": f"Name this compound: {user_input}"}
                    ],
                    max_tokens=100
                )
                result = response.choices[0].message['content'].strip()
                st.success("✅ AI Response:")
                st.markdown(result)
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
elif user_input:
    st.warning("⚠️ Please add your OpenAI API key in Streamlit secrets to use the AI assistant.")