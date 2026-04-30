from docxtpl import DocxTemplate
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
import requests
import sys
import json
import streamlit as st
from website import compiledata

def main():
    data = compiledata()
    parsed_data = parsedata(data)
    create_doc(parsed_data)




def parsedata(data):
    system_prompt = """You are an SCDF officer writing a formal report detailing the results of a CERT (Company Emergency Rescue Team) audit.

General Instructions:
- Use precise and formal language.
- Use plain text only (no bold, no formatting).
- The report must contain exactly three paragraphs.
- Each paragraph corresponds to one section of the audit.
- Do not reveal the score aquired for each section, only use the value to gauge the tone that should be used

---

Section 1: ERP (Emergency Response Plan) Audit

The ERP is graded out of 30 points based on completeness and accuracy. It contains the following sections:
1. AIM
2. SITUATION (Introduction, Area of Operations, Location, Surroundings, Layout, Hazard Risk Assessment)
3. EXECUTION (Concept of Operations, Emergency Actions including notification, evacuation, containment, shutdown, firefighting, IPP, cleanup)
4. SERVICE SUPPORT (Fire/Hazmat systems, safety equipment)
5. COMMAND AND SIGNAL (Structure, organisation chart, command centre)
6. PLAN REVIEW MAINTENANCE (Communication, exercises, drills, review)
7. ANNEXES (Site plans, layout, inventory, emergency data, SOPs, roles, CERT structure)

Write a paragraph assessing:
- Whether the ERP is up to date
- Whether all sections are complete and accurate
- Any discrepancies or incorrect information
- Recommendations for improvement

Example style:
- “During inspection, it was found that…”
- “However, it was noted that…”
- “As such, the FSM was advised to…”

---

Section 2: Training Records and Certifications

The section is graded out of 35 points. Audit whether CERT members have completed required training and whether documentation is available.

Required training:
- SMC: WSQ Implement Incident Management Processes (or equivalent)
- SIC: WSQ Implement Incident Management Processes + WSQ Respond to Fire and Hazmat Emergency (3-day)
- Response Team: WSQ Respond to Fire and Hazmat Emergency (3-day)
- First Aiders: CERT First Aid Course (1-Day)

Write a paragraph assessing:
- Availability of training records
- Whether key personnel meet training requirements
- Any missing certifications or ongoing training
- Recommendations for compliance

Example style:
- “Upon inspection of training records…”
- “It was observed that…”
- “SCDF officers recommended that…”

---

Section 3: PPE and Equipment Check

The section is graded out of 35 points. Audit the condition, availability, and serviceability of equipment.

Equipment categories:
- PPE: fire retardant coveralls, helmets, goggles/face shields, gloves, boots
- Mitigation: fire extinguishers, hose reels
- First Aid/Rescue: first aid kit, stretcher, blanket, AED
- Communication: loud hailer, walkie talkie

Write a paragraph assessing:
- Whether equipment is present and properly stored
- Whether equipment is serviceable
- Whether service records are available
- Any deficiencies or missing items
- Recommendations for rectification

Example style:
- “The equipment was inspected and found to…”
- “However, it was noted that…”
- “The premise was advised to…”

---

Output Requirements:
- Exactly 3 paragraphs
- Paragraph 1 → ERP
- Paragraph 2 → Training
- Paragraph 3 → PPE
- No bullet points
- No headings
"""

    user_prompt = f"""
    Generate the three paragraphs using the scores and findings for each section of the audit.
    Use score: {data["section_1_sentiment"]} and {data["section_1_errors"]} for section 1, ERP,
    Use score: {data["section_2_sentiment"]} and {data["section_2_errors"]} for section 2, Certification,
    Use score: {data["section_3_sentiment"]} and {data["section_3_errors"]} for section 3, PPE.

"""

    response = requests.post(
                    url = "https://openrouter.ai/api/v1/chat/completions",
                    headers = {"Authorization": "Bearer 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"},
                    json = {"model": "openai/gpt-5.2",
                            "messages": [
                                {"role": "system", "content": system_prompt},

                                {"role": "user", "content": user_prompt}
                                ]
                            }
                        )
    try:
        chatbot_response = response.json()["choices"][0]["message"]["content"].split("\n\n")
        if len(chatbot_response) == 3:
            data["para_1"] = chatbot_response[0]
            data["para_2"] = chatbot_response[1]
            data["para_3"] = chatbot_response[2]
    except KeyError:
        st.write("Chatbot response failed")
        
    data.pop("section_1_sentiment")
    data.pop("section_2_sentiment")
    data.pop("section_3_sentiment")
    data.pop("section_1_errors")
    data.pop("section_2_errors")
    data.pop("section_3_errors")

    return data



# only section 1 will generate a response, can improve

def create_doc(data):
    document = DocxTemplate("CERT Audit Report Template.docx")
    replace_text(data, document)


    document.save(f"CERT Audit Report {data['address']}.docx")

def replace_text(data, document):

    context = {
        "date": data["date_of_audit"],
        "address": data["address"],
        "time": data["time_of_audit"],
        "erp": data["para_1"],
        "training": data["para_2"],
        "ppe": data["para_3"],
        "audit_grade": data["overall_audit_grade"],
        "auditor": data["auditor"],
        "telephone": data["hp_num"],
        "smc": data["names_of_key_appointment_SMC"],
        "sic": data["names_of_key_appointment_SIC"],
        "fsm": data["names_of_key_appointment_FSM"],
        "ert1": data["names_of_key_appointment_ERT1"],
        "ert2": data["names_of_key_appointment_ERT2"],
        "ert3": data["names_of_key_appointment_ERT3"],
        "ert4": data["names_of_key_appointment_ERT4"],
        "ert5": data["names_of_key_appointment_ERT5"],
        "ert6": data["names_of_key_appointment_ERT6"],
        "ert7": data["names_of_key_appointment_ERT7"]
    }
    document.render(context)






if __name__ == "__main__":
    main()

