import streamlit as st
import random

st.set_page_config(page_title="Sherlock AI | Mystery Detective", page_icon="🕵️", layout="wide")

# Fictional cases for a self-contained, no-API prototype.
CASES = {
    "The Missing Diamond": {
        "intro": "At 9:00 PM, the Blue Star diamond vanished from a locked display room during a private museum event.",
        "victim": "Museum curator: Dr. Evelyn Hart",
        "culprit": "Maya",
        "suspects": {
            "Alex": {
                "role": "Security guard",
                "alibi": "I was checking the east entrance at 8:50 PM.",
                "statement": "I never entered the display room tonight.",
                "answers": {
                    "Where were you?": "I was near the east entrance. The security log should show my patrol.",
                    "Did you see anything unusual?": "I saw Maya leave the gallery carrying a folded scarf.",
                    "Do you have access?": "I can access the gallery, but the display case needs a separate key."
                }
            },
            "Maya": {
                "role": "Museum assistant",
                "alibi": "I was organizing catalog cards in the archive from 8:40 to 9:00 PM.",
                "statement": "I did not go near the display case.",
                "answers": {
                    "Where were you?": "In the archive, sorting catalog cards. Nobody saw me there, though.",
                    "Did you see anything unusual?": "I heard a brief alarm beep, but I ignored it.",
                    "Do you have access?": "I sometimes handle display keys when the curator asks me."
                }
            },
            "Ryan": {
                "role": "Photographer",
                "alibi": "I was taking photos in the west hall at 8:55 PM.",
                "statement": "I stayed in the west hall all evening.",
                "answers": {
                    "Where were you?": "In the west hall. Several guests were there.",
                    "Did you see anything unusual?": "I photographed the display at 8:45 PM; the diamond was still there.",
                    "Do you have access?": "No, I was only allowed in public areas."
                }
            }
        },
        "evidence": [
            {
                "name": "E1 — Security Log",
                "description": "The east entrance log records Alex's patrol from 8:48 to 8:57 PM.",
                "points_to": "Alex",
                "hint": "This supports Alex's patrol alibi, though it does not prove every second of his location."
            },
            {
                "name": "E2 — Photograph Timestamp",
                "description": "Ryan's photo from 8:45 PM shows the diamond still inside the display case.",
                "points_to": "Ryan",
                "hint": "The theft happened after 8:45 PM, narrowing the timeline."
            },
            {
                "name": "E3 — Archive Dust",
                "description": "A thin line of archive dust on Maya's sleeve matches dust near the display-room service passage.",
                "points_to": "Maya",
                "hint": "This suggests Maya may have used the service passage, but it is not proof by itself."
            },
            {
                "name": "E4 — Key Register",
                "description": "The key register shows the spare display key was signed out under Maya's initials at 8:42 PM and never signed back in.",
                "points_to": "Maya",
                "hint": "This links Maya to access to the display case."
            },
            {
                "name": "E5 — Contradictory Statement",
                "description": "Maya said she never went near the display case, but the service passage sensor recorded a badge assigned to her at 8:51 PM.",
                "points_to": "Maya",
                "hint": "A statement conflicts with the access record. Consider this alongside the other evidence."
            }
        ],
        "secret": {
            "question": "Decode this clue: 20-8-5 / 11-5-25 / 23-1-19 / 9-14 / 20-8-5 / 1-18-3-8-9-22-5",
            "answer": "THE KEY WAS IN THE ARCHIVE",
            "explanation": "Using A=1, B=2, ... Z=26 gives: THE KEY WAS IN THE ARCHIVE."
        },
        "solution": "Maya is the most strongly supported suspect in this fictional case. The key register, service-passage sensor, and contradictory statement jointly support the accusation. In a real investigation, these clues would need independent verification."
    },
    "The Vanishing Prototype": {
        "intro": "A prototype robot chip disappeared from a university lab shortly before a technology showcase.",
        "victim": "Lab director: Professor Sen",
        "culprit": "Noah",
        "suspects": {
            "Isha": {
                "role": "Research student",
                "alibi": "I was presenting slides in the seminar room.",
                "statement": "I did not enter the lab after 4 PM.",
                "answers": {
                    "Where were you?": "In the seminar room preparing my presentation.",
                    "Did you see anything unusual?": "I saw Noah return toward the lab carrying a small toolbox.",
                    "Do you have access?": "My student card opens the main lab door."
                }
            },
            "Noah": {
                "role": "Lab technician",
                "alibi": "I was repairing a printer in the corridor.",
                "statement": "I never opened the prototype cabinet.",
                "answers": {
                    "Where were you?": "In the corridor fixing the printer. It took longer than expected.",
                    "Did you see anything unusual?": "I heard a cabinet alarm, but I thought it was a false alert.",
                    "Do you have access?": "I maintain the lab and have a cabinet override key."
                }
            },
            "Leah": {
                "role": "Visiting researcher",
                "alibi": "I was on a video call in the library.",
                "statement": "I was not in the engineering building.",
                "answers": {
                    "Where were you?": "In the library on a video call.",
                    "Did you see anything unusual?": "I noticed the lab door was propped open around 4:20 PM.",
                    "Do you have access?": "I only have a visitor badge."
                }
            }
        },
        "evidence": [
            {"name": "E1 — Seminar Attendance", "description": "A signed attendance sheet places Isha in the seminar room during the key time window.", "points_to": "Isha", "hint": "This supports Isha's stated location."},
            {"name": "E2 — Visitor Badge", "description": "Leah's visitor badge only opens the building lobby, not the prototype cabinet.", "points_to": "Leah", "hint": "Access restrictions make direct access less likely."},
            {"name": "E3 — Cabinet Override", "description": "The cabinet audit records an override key used at 4:24 PM. Only the lab technician's key is registered for that override.", "points_to": "Noah", "hint": "The audit links the cabinet opening to a specific access method."},
            {"name": "E4 — Printer Repair Ticket", "description": "The printer repair ticket was created at 4:42 PM, after the cabinet opened.", "points_to": "Noah", "hint": "The timestamp weakens Noah's claim that the printer repair occupied the whole time."},
            {"name": "E5 — Toolbox Mark", "description": "A fresh rectangular grease mark on the cabinet matches the base of Noah's maintenance toolbox.", "points_to": "Noah", "hint": "This is another clue to weigh with the access audit."}
        ],
        "secret": {
            "question": "Decode this clue: 3-8-5-3-11 / 20-8-5 / 12-15-7 / 2-5-6-15-18-5 / 25-15-21 / 20-18-21-19-20",
            "answer": "CHECK THE LOG BEFORE YOU TRUST",
            "explanation": "Using A=1, B=2, ... Z=26 gives: CHECK THE LOG BEFORE YOU TRUST."
        },
        "solution": "Noah is the most strongly supported suspect in this fictional case. The cabinet override audit, the timing of the repair ticket, and the toolbox mark point toward Noah. These clues are part of a fictional game, not real-world evidence."
    }
}

def init_state():
    defaults = {
        "case_name": "The Missing Diamond",
        "found_evidence": [],
        "interrogations": [],
        "solved_secret": False,
        "accusation": None,
        "show_solution": False,
        "score_awarded": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def reset_case(case_name):
    st.session_state.case_name = case_name
    st.session_state.found_evidence = []
    st.session_state.interrogations = []
    st.session_state.solved_secret = False
    st.session_state.accusation = None
    st.session_state.show_solution = False
    st.session_state.score_awarded = False

init_state()
case = CASES[st.session_state.case_name]

st.title("🕵️ Sherlock AI")
st.caption("A fictional mystery investigation game — follow the clues, question suspects, and make your accusation.")

with st.sidebar:
    st.header("🗂️ Case Files")
    selected_case = st.selectbox("Choose a case", list(CASES.keys()), index=list(CASES.keys()).index(st.session_state.case_name))
    if selected_case != st.session_state.case_name:
        reset_case(selected_case)
        st.rerun()

    st.divider()
    st.subheader("📈 Investigation progress")
    total = len(case["evidence"])
    found = len(st.session_state.found_evidence)
    st.progress(found / total)
    st.write(f"Evidence collected: **{found}/{total}**")
    st.write(f"Suspects questioned: **{len(set(x['suspect'] for x in st.session_state.interrogations))}/{len(case['suspects'])}**")
    if st.button("🔄 Restart this case", use_container_width=True):
        reset_case(st.session_state.case_name)
        st.rerun()

st.subheader("📁 Case briefing")
st.info(case["intro"])
st.write(f"**Case contact:** {case['victim']}")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🔎 Evidence Room", "💬 Interrogate", "🧩 Secret Code", "🧠 Detective Board", "🏆 Final Accusation"])

with tab1:
    st.markdown("### Investigate the evidence")
    st.write("Choose a clue to inspect. Keep track of what it proves—and what it does not prove.")
    cols = st.columns(2)
    for i, clue in enumerate(case["evidence"]):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{clue['name']}**")
                if clue["name"] in st.session_state.found_evidence:
                    st.success("Evidence collected")
                    st.write(clue["description"])
                    with st.expander("Detective note"):
                        st.write(clue["hint"])
                else:
                    st.write("This clue has not been examined yet.")
                    if st.button(f"Examine {clue['name']}", key=f"evidence_{st.session_state.case_name}_{i}"):
                        st.session_state.found_evidence.append(clue["name"])
                        st.rerun()

with tab2:
    st.markdown("### Question the suspects")
    suspect_name = st.selectbox("Select a suspect", list(case["suspects"].keys()))
    suspect = case["suspects"][suspect_name]
    st.write(f"**Role:** {suspect['role']}")
    st.write(f"**Initial statement:** “{suspect['statement']}”")
    question = st.radio("Choose a question", list(suspect["answers"].keys()), key=f"q_{st.session_state.case_name}_{suspect_name}")
    if st.button("Ask question", type="primary"):
        response = suspect["answers"][question]
        record = {"suspect": suspect_name, "question": question, "response": response}
        if record not in st.session_state.interrogations:
            st.session_state.interrogations.append(record)
        st.session_state.last_response = (suspect_name, question, response)
    if "last_response" in st.session_state:
        who, asked, response = st.session_state.last_response
        st.markdown("#### Suspect's response")
        st.success(f"**{who}:** {response}")
    if st.session_state.interrogations:
        with st.expander("Interrogation notes"):
            for item in st.session_state.interrogations:
                st.write(f"- **{item['suspect']}** — Asked: {item['question']} Answer: {item['response']}")

with tab3:
    st.markdown("### Decode the secret message")
    st.write("Hint: A=1, B=2, C=3 ... Z=26.")
    st.code(case["secret"]["question"])
    answer = st.text_input("Enter the decoded message", key=f"secret_{st.session_state.case_name}", placeholder="Type the decoded words...")
    if st.button("Check code"):
        normalized = " ".join(answer.upper().replace("/", " ").split())
        if normalized == case["secret"]["answer"]:
            st.session_state.solved_secret = True
            st.success("🔓 Correct! You cracked the code.")
            st.write(case["secret"]["explanation"])
        else:
            st.error("Not quite. Try converting each number to its matching letter (A=1, B=2...).")
    if st.session_state.solved_secret:
        st.success("Secret code solved!")

with tab4:
    st.markdown("### Detective reasoning board")
    st.write("Review what you've discovered and decide which clues support each suspect.")
    if not st.session_state.found_evidence:
        st.warning("You have not collected any evidence yet. Visit the Evidence Room first.")
    else:
        for name in st.session_state.found_evidence:
            clue = next(x for x in case["evidence"] if x["name"] == name)
            st.markdown(f"- **{name}** → {clue['description']}")
    st.divider()
    st.write("**Your current theory:**")
    theory = st.selectbox("Who seems most suspicious right now?", ["Undecided"] + list(case["suspects"].keys()), key=f"theory_{st.session_state.case_name}")
    if theory != "Undecided":
        related = [x for x in case["evidence"] if x["name"] in st.session_state.found_evidence and x["points_to"] == theory]
        st.write(f"You have collected **{len(related)}** clue(s) directly associated with {theory} in this game's evidence notes.")
        st.caption("This is a simple game mechanic, not a real forensic conclusion.")

with tab5:
    st.markdown("### Make your final accusation")
    st.write("Choose the suspect you believe is responsible. You can inspect more evidence before submitting.")
    accusation = st.radio("I accuse:", list(case["suspects"].keys()), horizontal=True, key=f"accuse_{st.session_state.case_name}")
    if st.button("Submit accusation", type="primary"):
        st.session_state.accusation = accusation
        st.session_state.show_solution = True
        st.session_state.score_awarded = True
    if st.session_state.show_solution:
        if st.session_state.accusation == case["culprit"]:
            st.success(f"🎉 Correct, detective! You identified {case['culprit']}.")
            points = len(st.session_state.found_evidence) * 10 + len(set(x["suspect"] for x in st.session_state.interrogations)) * 5
            if st.session_state.solved_secret:
                points += 15
            st.metric("Detective score", points + 50)
        else:
            st.error(f"Not this time. Your accusation was **{st.session_state.accusation}**.")
            st.write("Review the evidence and try the case again.")
        with st.expander("Reveal the case explanation"):
            st.write(case["solution"])
            st.caption("This is a fictional mystery game. Its solution is predetermined by the story, not generated by an AI model.")

st.divider()
st.caption("Prototype note: This first version uses scripted fictional cases and rule-based responses. It does not connect to a real AI model or investigate real people.")
