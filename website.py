import streamlit as st


def compiledata():
    st.title("CERT AUDIT REPORT GENERATOR")
    with st.form("registration_form"):
        #creates the form
        date_of_audit = st.text_input("What day was the audit conducted? (I.e 20/05/2025)")
        time_of_audit = st.text_input("What time was the audit conducted? (I.e 2200 Hrs)")
        address = st.text_input("What is the name, address and postal code of the premise? (I.e Tampines Primary School, 250, Tampines St 12, Singapore 529426)")
        hp_num = st.text_input("Telephone no of auditor? (I.e 88881234)")
        auditor = st.text_input("Please input your rank and name. (IE SGT2 Zhou Yang): ")
        names_of_key_appointment_SMC = st.text_input("What is the name of the SMC (Site Main Controller)?")
        names_of_key_appointment_SIC = st.text_input("What is the name of the SIC (Site Incident Controller)?")
        names_of_key_appointment_FSM = st.text_input("What is the name of the FSM (Fire Safety Manager)?")
        names_of_key_appointment_ERT1 = st.text_input("What is the name of the first ERT (Emergency Rescue Team) Members?")
        names_of_key_appointment_ERT2 = st.text_input("What is the name of the second ERT (Emergency Rescue Team) Members?")
        names_of_key_appointment_ERT3 = st.text_input("What is the name of the third ERT (Emergency Rescue Team) Members?")
        names_of_key_appointment_ERT4 = st.text_input("What is the name of the forth ERT/First aider (Emergency Rescue Team) Members?")
        names_of_key_appointment_ERT5 = st.text_input("What is the name of the fifth ERT/First aider (Emergency Rescue Team) Members? (If not known, leave blank empty)")
        names_of_key_appointment_ERT6 = st.text_input("What is the name of the sixth ERT/First aider (Emergency Rescue Team) Members? (If not known, leave blank empty)" )
        names_of_key_appointment_ERT7 = st.text_input("What is the name of the seventh ERT/First aider (Emergency Rescue Team) Members? (If not known, leave blank empty)")
        section_1_sentiment = st.text_input("How many points did section 1 score? (Please enter a valid number, section 1 scores out of 30 marks.)")
        section_1_errors = st.text_input("Please elaborate on the findings (I.E Phone numbers listed in Key Appointment holders are not up to date.)")
        section_2_sentiment = st.text_input("How many points did section 2 score? (Please enter a valid number, section 2 scores out of 35 marks.)")
        section_2_errors = st.text_input("Please elaborate on the findings (I.E SMC has not attended WSQ Managing Emergency Scenarios)")
        section_3_sentiment = st.text_input("How many points did section 3 score? (Please enter a valid number, section 3 scores out of 35 marks.)")
        section_3_errors = st.text_input("Please elaborate on the findings (I.E FSM Unable to procure servicing reports of Fire Helmets)")
        overall_audit_grade = st.selectbox("Please state the final audit grade", ["Pass with commendation", "Pass", "Conditional Pass", "Fail"])


        submit = st.form_submit_button(
            label="Generate CERT Audit Report",
            
            )


    if submit:
        st.success("Generation Complete.")
        st.write("Check your file for completed report.")




    data = {
        "date_of_audit":date_of_audit,
        "address":address,
        "time_of_audit":time_of_audit,
        "hp_num":hp_num,
        "names_of_key_appointment_SMC":names_of_key_appointment_SMC,
        "names_of_key_appointment_SIC":names_of_key_appointment_SIC,
        "names_of_key_appointment_FSM":names_of_key_appointment_FSM,
        "names_of_key_appointment_ERT1": names_of_key_appointment_ERT1,
        "names_of_key_appointment_ERT2": names_of_key_appointment_ERT2,
        "names_of_key_appointment_ERT3": names_of_key_appointment_ERT3,
        "names_of_key_appointment_ERT4": names_of_key_appointment_ERT4,
        "names_of_key_appointment_ERT5": names_of_key_appointment_ERT5,
        "names_of_key_appointment_ERT6": names_of_key_appointment_ERT6,
        "names_of_key_appointment_ERT7": names_of_key_appointment_ERT7,
        "section_1_sentiment":section_1_sentiment,
        "section_2_sentiment":section_2_sentiment,
        "section_3_sentiment":section_3_sentiment,
        "section_1_errors":section_1_errors,
        "section_2_errors":section_2_errors,
        "section_3_errors":section_3_errors,
        "overall_audit_grade":overall_audit_grade,
        "auditor":auditor
    }
    return data
