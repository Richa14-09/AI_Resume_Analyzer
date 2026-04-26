class ResumeAnalyzer:
    def __init__(self):
        # Skill keywords for different fields
        self.ds_keyword = ['tensorflow', 'keras', 'pytorch', 'machine learning', 'deep learning',
                          'flask', 'streamlit', 'pandas', 'numpy', 'scikit-learn', 'data science',
                          'nlp', 'computer vision', 'opencv']
        
        self.web_keyword = ['react', 'django', 'node js', 'react js', 'php', 'laravel', 'magento',
                           'wordpress', 'javascript', 'angular js', 'c#', 'flask', 'html', 'css',
                           'bootstrap', 'jquery']
        
        self.android_keyword = ['android', 'android development', 'flutter', 'kotlin', 'xml', 'kivy']
        
        self.ios_keyword = ['ios', 'ios development', 'swift', 'cocoa', 'cocoa touch', 'xcode']
        
        self.uiux_keyword = ['ux', 'adobe xd', 'figma', 'zeplin', 'balsamiq', 'ui', 'prototyping',
                            'wireframes', 'storyframes', 'adobe photoshop', 'photoshop', 'editing',
                            'adobe illustrator', 'illustrator']

    def predict_field(self, skills):
        """Predict the candidate's field based on skills"""
        skills_lower = [skill.lower() for skill in skills]
        
        for skill in skills_lower:
            if skill in self.ds_keyword:
                return 'Data Science', self.recommend_ds_skills()
            elif skill in self.web_keyword:
                return 'Web Development', self.recommend_web_skills()
            elif skill in self.android_keyword:
                return 'Android Development', self.recommend_android_skills()
            elif skill in self.ios_keyword:
                return 'IOS Development', self.recommend_ios_skills()
            elif skill in self.uiux_keyword:
                return 'UI-UX Development', self.recommend_uiux_skills()
        
        return 'General', []

    def recommend_ds_skills(self):
        return ['Data Visualization', 'Predictive Analysis', 'Statistical Modeling', 'Data Mining',
                'Clustering & Classification', 'Data Analytics', 'Quantitative Analysis',
                'Web Scraping', 'ML Algorithms', 'Keras', 'Pytorch', 'Probability', 'Scikit-learn',
                'Tensorflow', 'Flask', 'Streamlit']

    def recommend_web_skills(self):
        return ['React', 'Django', 'Node JS', 'React JS', 'php', 'laravel', 'Magento', 'wordpress',
                'Javascript', 'Angular JS', 'c#', 'Flask', 'SDK']

    def recommend_android_skills(self):
        return ['Android', 'Android development', 'Flutter', 'Kotlin', 'XML', 'Java',
                'Kivy', 'GIT', 'SDK', 'SQLite']

    def recommend_ios_skills(self):
        return ['IOS', 'IOS Development', 'Swift', 'Cocoa', 'Cocoa Touch', 'Xcode', 'Objective-C',
                'SQLite', 'Plist', 'StoreKit', 'UI-Kit', 'AV Foundation', 'Auto-Layout']

    def recommend_uiux_skills(self):
        return ['UI', 'User Experience', 'Adobe XD', 'Figma', 'Zeplin', 'Balsamiq', 'Prototyping',
                'Wireframes', 'Storyframes', 'Adobe Photoshop', 'Editing', 'Illustrator',
                'After Effects', 'Premier Pro', 'Indesign', 'Wireframe', 'Solid', 'Grasp',
                'User Research']

    def calculate_resume_score(self, resume_text):
        """Calculate resume score based on sections present"""
        score = 0
        suggestions = []
        
        sections = {
            'Objective': ['Objective', 'Summary'],
            'Education': ['Education', 'School', 'College'],
            'Experience': ['EXPERIENCE', 'Experience'],
            'Internships': ['INTERNSHIPS', 'INTERNSHIP', 'Internships', 'Internship'],
            'Skills': ['SKILLS', 'Skills', 'SKILL'],
            'Hobbies': ['HOBBIES', 'Hobbies'],
            'Interests': ['Interests', 'INTERESTS'],
            'Achievements': ['ACHIEVEMENTS', 'Achievements'],
            'Certifications': ['CERTIFICATIONS', 'Certifications', 'Certification'],
            'Projects': ['PROJECTS', 'PROJECT', 'Projects']
        }
        
        for section, keywords in sections.items():
            found = any(keyword in resume_text for keyword in keywords)
            if found:
                score += 10
            else:
                suggestions.append(f"Add {section} section to improve your resume")
        
        return score, suggestions

    def get_candidate_level(self, no_of_pages):
        """Determine candidate experience level based on resume pages"""
        if no_of_pages == 1:
            return "Fresher"
        elif no_of_pages == 2:
            return "Intermediate"
        else:
            return "Experienced"