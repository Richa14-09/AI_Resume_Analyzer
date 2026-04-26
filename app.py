import streamlit as st
import pandas as pd
import base64
import time
import datetime
import os
import random
from PIL import Image
import plotly.express as px

from utils.resume_parser import extract_resume_data, pdf_reader
from utils.resume_analyzer import ResumeAnalyzer
from utils.coursers import (ds_course, web_course, android_course, ios_course, 
                            uiux_course, resume_videos, interview_videos)

# Page config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Create upload directory
if not os.path.exists('./uploaded_resumes'):
    os.makedirs('./uploaded_resumes')

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def course_recommender(course_list):
    st.subheader("**Courses & Certificates Recommendations 🎓**")
    rec_course = []
    no_of_reco = st.slider('Choose Number of Course Recommendations:', 1, 10, 5)
    random.shuffle(course_list)
    for c, (c_name, c_link) in enumerate(course_list, start=1):
        st.markdown(f"({c}) [{c_name}]({c_link})")
        rec_course.append(c_name)
        if c == no_of_reco:
            break
    return rec_course

def main():
    st.title("AI Resume Analyzer 📄")
    st.sidebar.markdown("# Choose User")
    activities = ["Normal User", "Admin"]
    choice = st.sidebar.selectbox("Choose among the given options:", activities)
    
    st.sidebar.markdown(
        """
        - 🚀 **Built by CSE Final Year Student**
        - 📧 your.email@example.com
        - 🔗 [GitHub](https://github.com/yourusername)
        """
    )

    if choice == 'Normal User':
        st.markdown("### Upload your resume to get smart recommendations")
        pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
        
        if pdf_file is not None:
            with st.spinner('Uploading your Resume...'):
                time.sleep(2)
            
            save_image_path = './uploaded_resumes/' + pdf_file.name
            with open(save_image_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            
            show_pdf(save_image_path)
            
            # Parse resume
            resume_data = extract_resume_data(save_image_path)
            
            if resume_data:
                resume_text = pdf_reader(save_image_path)
                analyzer = ResumeAnalyzer()
                
                st.header("**Resume Analysis** 🔍")
                st.success(f"Hello {resume_data.get('name', 'User')}")
                
                st.subheader("**Your Basic Info**")
                try:
                    st.text(f"Name: {resume_data.get('name', 'N/A')}")
                    st.text(f"Email: {resume_data.get('email', 'N/A')}")
                    st.text(f"Contact: {resume_data.get('mobile_number', 'N/A')}")
                    st.text(f"Resume pages: {resume_data.get('no_of_pages', 'N/A')}")
                except:
                    pass
                
                # Candidate level
                cand_level = analyzer.get_candidate_level(resume_data.get('no_of_pages', 1))
                st.subheader(f"**You are at {cand_level} level!**")
                
                # Skills analysis
                st.subheader("**Skills Recommendation 💡**")
                skills = resume_data.get('skills', [])
                st.write(f"**Your Current Skills:** {', '.join(skills) if skills else 'None detected'}")
                
                # Predict field
                field, recommended_skills = analyzer.predict_field(skills)
                st.success(f"**Our analysis says you are looking for {field} Jobs**")
                
                if recommended_skills:
                    st.write(f"**Recommended Skills:** {', '.join(recommended_skills)}")
                    st.markdown('''<h5 style='color:#1ed760;'>Adding these skills will boost your chances of getting a job!</h5>''', 
                              unsafe_allow_html=True)
                
                # Course recommendations
                if field == 'Data Science':
                    rec_course = course_recommender(ds_course)
                elif field == 'Web Development':
                    rec_course = course_recommender(web_course)
                elif field == 'Android Development':
                    rec_course = course_recommender(android_course)
                elif field == 'IOS Development':
                    rec_course = course_recommender(ios_course)
                elif field == 'UI-UX Development':
                    rec_course = course_recommender(uiux_course)
                else:
                    rec_course = []
                    st.warning("Add more skills to get specific recommendations.")
                
                # Resume Score
                st.subheader("**Resume Tips & Ideas 💡**")
                resume_score, suggestions = analyzer.calculate_resume_score(resume_text)
                
                for suggestion in suggestions:
                    st.markdown(f"⚠️ {suggestion}")
                
                st.subheader("**Resume Score 📝**")
                st.markdown(
                    """
                    <style>
                        .stProgress > div > div > div > div {
                            background-color: #d73b5c;
                        }
                    </style>""",
                    unsafe_allow_html=True,
                )
                
                my_bar = st.progress(0)
                for percent_complete in range(resume_score):
                    time.sleep(0.05)
                    my_bar.progress(percent_complete + 1)
                
                st.success(f'**Your Resume Writing Score: {resume_score}**')
                st.warning("**Note: This score is calculated based on the content you have in your resume.**")
                
                # Bonus videos
                st.header("**Bonus Video for Resume Writing Tips 💡**")
                resume_vid = random.choice(resume_videos)
                st.video(resume_vid)
                
                st.header("**Bonus Video for Interview Tips 💡**")
                interview_vid = random.choice(interview_videos)
                st.video(interview_vid)
                
                st.balloons()
            else:
                st.error('Something went wrong while parsing the resume.')
    
    else:
        # Admin section
        st.success('Welcome to Admin Side')
        ad_user = st.text_input("Username")
        ad_password = st.text_input("Password", type='password')
        
        if st.button('Login'):
            if ad_user == 'admin' and ad_password == 'admin@123':
                st.success("Welcome Admin!")
                st.header("**User's Data**")
                # Display analytics here
                st.info("Connect to database to display user analytics")
            else:
                st.error("Wrong ID & Password")

if __name__ == '__main__':
    main()