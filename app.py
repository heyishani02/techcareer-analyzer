import streamlit as st
import plotly.express as px
import pandas as pd

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="TechCareer Analyzer", layout="wide")
st.title("TechCareer Analyzer 🎯")
st.write("Analyze your skills and discover your ideal tech career path!")

# -----------------------
# User Input Widgets
# -----------------------
skills_input = st.text_input(
    "Enter your skills (comma separated, e.g., Python, Excel, Communication):",
    key="skills_input_1"
)

experience = st.slider(
    "Years of Experience:",
    min_value=0,
    max_value=20,
    value=1,
    key="experience_slider_1"
)

# -----------------------
# Button to Generate Recommendations
# -----------------------
if st.button("Get Career Recommendations", key="get_recommend_1"):

    if skills_input.strip() == "":
        st.warning("Please enter at least one skill!")
    else:
        # -----------------------
        # Skill Mapping Dictionary (Handles abbreviations and variations)
        # -----------------------
        skill_mapping = {
            # Machine Learning variations
            "ml": "machine learning",
            "machine-learning": "machine learning",
            
            # Deep Learning variations
            "dl": "deep learning",
            "deep-learning": "deep learning",
            
            # Artificial Intelligence variations
            "ai": "artificial intelligence",
            "artificial-intelligence": "artificial intelligence",
            
            # Database variations
            "database": "sql",
            "databases": "sql",
            "rdbms": "sql",
            
            # Programming language variations
            "py": "python",
            "cpp": "c++",
            "c plus plus": "c++",
            
            # Cloud platforms
            "amazon web services": "aws",
            "google cloud": "gcp",
            "google cloud platform": "gcp",
            "microsoft azure": "azure",
            
            # DevOps tools
            "k8s": "kubernetes",
            "kube": "kubernetes",
            
            # Data visualization
            "data viz": "data visualization",
            "dataviz": "data visualization",
            "visualizations": "data visualization",
            
            # ETL variations
            "extract transform load": "etl",
            
            # Statistics variations
            "stats": "statistics",
            "statistical analysis": "statistics",
            
            # Object Oriented Programming
            "object oriented programming": "oop",
            "object-oriented": "oop",
            
            # MLOps variations
            "ml ops": "mlops",
            "ml-ops": "mlops",
            "machine learning operations": "mlops",
            
            # Analytics variations
            "data analytics": "analytics",
            "data analysis": "analytics",
            
            # Communication variations
            "communications": "communication",
            "verbal communication": "communication",
            "written communication": "communication",
            
            # Mathematics variations
            "maths": "math",
            "mathematics": "math",
            
            # Version control
            "github": "git",
            "version control": "git",
            "gitlab": "git",
            
            # Big Data
            "apache spark": "spark",
            "pyspark": "spark",
            "apache hadoop": "hadoop",
            "apache airflow": "airflow"
        }
        
        # Clean and validate skills input with mapping
        raw_skills = [skill.strip().lower() for skill in skills_input.split(",") if skill.strip()]
        
        # Map abbreviations to full forms
        skills_list = []
        for skill in raw_skills:
            # Check if skill has a mapping, otherwise use as-is
            mapped_skill = skill_mapping.get(skill, skill)
            skills_list.append(mapped_skill)
        
        # Remove duplicates while preserving order
        skills_list = list(dict.fromkeys(skills_list))
        
        if not skills_list:
            st.warning("Please enter valid skills!")
        else:
            # Skill mapping applied silently in the background
            # No display to user - keeps UI clean
            
            # -----------------------
            # Expanded Career Database + Skill Weights
            # -----------------------
            career_db = {
                "Data Scientist": {
                    "skills": ["python", "machine learning", "statistics", "sql", "data visualization", "deep learning"],
                    "weight": [0.3, 0.25, 0.15, 0.1, 0.1, 0.1]
                },
                "AI Engineer": {
                    "skills": ["python", "deep learning", "tensorflow", "pytorch", "math", "mlops"],
                    "weight": [0.25, 0.25, 0.15, 0.15, 0.1, 0.1]
                },
                "Business Analyst": {
                    "skills": ["excel", "sql", "communication", "power bi", "tableau", "statistics"],
                    "weight": [0.25, 0.2, 0.15, 0.15, 0.15, 0.1]
                },
                "Product Manager": {
                    "skills": ["communication", "planning", "analytics", "leadership", "roadmap", "stakeholder management"],
                    "weight": [0.2, 0.2, 0.2, 0.15, 0.15, 0.1]
                },
                "Software Developer": {
                    "skills": ["python", "java", "c++", "git", "oop", "algorithms"],
                    "weight": [0.25, 0.2, 0.15, 0.1, 0.15, 0.15]
                },
                "Cloud Engineer": {
                    "skills": ["aws", "azure", "gcp", "python", "docker", "kubernetes"],
                    "weight": [0.2, 0.2, 0.2, 0.15, 0.15, 0.1]
                },
                "Data Engineer": {
                    "skills": ["python", "sql", "spark", "hadoop", "etl", "airflow"],
                    "weight": [0.2, 0.2, 0.2, 0.15, 0.15, 0.1]
                }
            }

            # Learning Resources for Missing Skills
            learning_resources = {
                "python": "https://www.coursera.org/learn/python",
                "sql": "https://www.coursera.org/learn/sql",
                "machine learning": "https://www.coursera.org/learn/machine-learning",
                "deep learning": "https://www.coursera.org/specializations/deep-learning",
                "tensorflow": "https://www.tensorflow.org/tutorials",
                "pytorch": "https://pytorch.org/tutorials/",
                "excel": "https://www.coursera.org/learn/excel",
                "power bi": "https://learn.microsoft.com/en-us/power-bi/",
                "tableau": "https://www.tableau.com/learn/training",
                "communication": "https://www.coursera.org/learn/wharton-communication-skills",
                "planning": "https://www.coursera.org/learn/project-planning",
                "leadership": "https://www.coursera.org/learn/leadership-skills",
                "analytics": "https://www.coursera.org/learn/data-analytics",
                "roadmap": "https://www.coursera.org/learn/product-management",
                "stakeholder management": "https://www.coursera.org/learn/stakeholder-management",
                "aws": "https://aws.amazon.com/training/",
                "azure": "https://learn.microsoft.com/en-us/training/azure/",
                "gcp": "https://cloud.google.com/training",
                "docker": "https://www.docker.com/101-tutorial",
                "kubernetes": "https://kubernetes.io/docs/tutorials/",
                "spark": "https://spark.apache.org/docs/latest/",
                "hadoop": "https://hadoop.apache.org/docs/stable/",
                "etl": "https://www.coursera.org/learn/data-warehousing",
                "airflow": "https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html",
                "algorithms": "https://www.coursera.org/learn/algorithms-part1",
                "oop": "https://www.coursera.org/learn/java-object-oriented",
                "java": "https://www.coursera.org/learn/java-programming",
                "c++": "https://www.coursera.org/learn/c-plus-plus-a",
                "git": "https://www.coursera.org/learn/version-control",
                "statistics": "https://www.coursera.org/learn/statistics",
                "data visualization": "https://www.coursera.org/learn/data-visualization",
                "math": "https://www.coursera.org/learn/mathematics-machine-learning",
                "mlops": "https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops"
            }

            # -----------------------
            # Recommendation Calculation
            # -----------------------
            recommendations = []
            for career, data in career_db.items():
                required_skills = data["skills"]
                weights = data["weight"]
                
                # Calculate weighted score
                matched_skills = []
                score = 0
                for i, skill in enumerate(required_skills):
                    if skill in skills_list:
                        score += weights[i]
                        matched_skills.append(skill)
                
                missing_skills = [skill for skill in required_skills if skill not in matched_skills]
                recommendations.append((career, score, missing_skills, matched_skills))

            recommendations.sort(key=lambda x: x[1], reverse=True)

            # Store recommendations in session state for global section
            st.session_state['recommendations'] = recommendations
            st.session_state['skills_list'] = skills_list
            st.session_state['experience'] = experience

            # -----------------------
            # Display Top 3 Recommendations
            # -----------------------
            st.subheader("🎯 Top Career Opportunities:")
            
            for i, (career, score, missing_skills, matched_skills) in enumerate(recommendations[:3]):
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.markdown(f"### {i+1}. {career}")
                    with col2:
                        st.metric("Match Score", f"{score*100:.0f}%")
                    
                    # Show matched skills
                    if matched_skills:
                        st.success(f"✅ Matched Skills: {', '.join([s.title() for s in matched_skills])}")
                    
                    # Horizontal Bar Chart for Missing Skills
                    if missing_skills:
                        st.warning(f"⚠️ Skills to Develop: {len(missing_skills)} skill(s)")
                        
                        # Create urgency levels based on skill importance
                        df_missing = pd.DataFrame({
                            'Skill': [s.title() for s in missing_skills],
                            'Priority': list(range(len(missing_skills), 0, -1))
                        })
                        
                        fig = px.bar(
                            df_missing, 
                            y='Skill', 
                            x='Priority', 
                            orientation='h',
                            text='Skill',
                            color='Priority',
                            color_continuous_scale='Reds',
                            labels={'Priority': 'Learning Priority'}
                        )
                        fig.update_layout(
                            showlegend=False,
                            height=max(200, len(missing_skills) * 40),
                            margin=dict(l=0, r=0, t=20, b=0)
                        )
                        fig.update_traces(textposition='inside', textfont_size=12)
                        st.plotly_chart(fig, use_container_width=True)

                        # Learning Links
                        st.write("📚 **Upskill Resources:**")
                        for skill in missing_skills:
                            skill_lower = skill.lower()
                            if skill_lower in learning_resources:
                                st.markdown(f"- [{skill.title()}]({learning_resources[skill_lower]})")
                            else:
                                st.write(f"- {skill.title()} (Search for courses online)")
                        
                        # Progress bar based on actual match percentage
                        st.progress(int(score * 100))
                    else:
                        st.success("🎉 Perfect Match! All skills aligned!")
                        st.progress(100)

                    # Predicted Salary (India) - Consistent calculation
                    base_salary = 12  # Base salary in LPA
                    skill_bonus = score * 15  # Up to 15 LPA based on skill match
                    experience_bonus = experience * 1.2  # 1.2 LPA per year of experience
                    predicted_salary = base_salary + skill_bonus + experience_bonus
                    
                    st.markdown(f"💰 **Predicted Salary (India):** ₹{predicted_salary:.1f} LPA")
                    st.write("---")

            # -----------------------
            # Additional Insights
            # -----------------------
            st.subheader("💡 Career Insights")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Your Skill Count", len(skills_list))
            
            with col2:
                best_match = recommendations[0]
                st.metric("Best Match", best_match[0])
            
            with col3:
                avg_match = sum([r[1] for r in recommendations]) / len(recommendations)
                st.metric("Avg Match Score", f"{avg_match*100:.0f}%")
            
            st.info("💡 **Tip:** Focus on developing skills for your top-matched career to maximize your opportunities!")

# -----------------------
# Global Top-Paying Roles (Always Visible)
# -----------------------
st.write("---")
st.subheader("🌎 Global Opportunities & Salary Trends")

# Country selector - OUTSIDE the button, always visible
country = st.selectbox(
    "Select a country to see personalized salary insights:",
    ["USA", "India", "Germany", "UK", "Canada"],
    key="country_select_global"
)

# Currency symbols by country
currency_map = {
    "USA": "$",
    "India": "₹",
    "Germany": "€",
    "UK": "£",
    "Canada": "CAD $"
}

# Salary units by country
salary_unit_map = {
    "USA": "per year",
    "India": "LPA",
    "Germany": "per year",
    "UK": "per year",
    "Canada": "per year"
}

global_salary_db = {
    "USA": {
        "Data Scientist": 120000,
        "AI Engineer": 150000,
        "Business Analyst": 95000,
        "Product Manager": 160000,
        "Software Developer": 130000,
        "Cloud Engineer": 140000,
        "Data Engineer": 135000
    },
    "India": {
        "Data Scientist": 25,
        "AI Engineer": 30,
        "Business Analyst": 20,
        "Product Manager": 35,
        "Software Developer": 28,
        "Cloud Engineer": 32,
        "Data Engineer": 30
    },
    "Germany": {
        "Data Scientist": 75000,
        "AI Engineer": 85000,
        "Business Analyst": 65000,
        "Product Manager": 90000,
        "Software Developer": 70000,
        "Cloud Engineer": 80000,
        "Data Engineer": 78000
    },
    "UK": {
        "Data Scientist": 65000,
        "AI Engineer": 75000,
        "Business Analyst": 55000,
        "Product Manager": 80000,
        "Software Developer": 60000,
        "Cloud Engineer": 70000,
        "Data Engineer": 68000
    },
    "Canada": {
        "Data Scientist": 95000,
        "AI Engineer": 110000,
        "Business Analyst": 75000,
        "Product Manager": 115000,
        "Software Developer": 90000,
        "Cloud Engineer": 105000,
        "Data Engineer": 100000
    }
}

country_salaries = global_salary_db[country]
currency = currency_map[country]
unit = salary_unit_map[country]

# Check if user has generated recommendations
if 'recommendations' in st.session_state:
    # Show personalized top 3 roles based on user's match scores
    st.write(f"**🎯 Your Top 3 Matching Roles in {country} (Based on Your Skills):**")
    
    personalized_roles = []
    for career, score, missing_skills, matched_skills in st.session_state['recommendations'][:3]:
        salary = country_salaries.get(career, 0)
        personalized_roles.append((career, salary, score))
    
    for idx, (role, salary, match_score) in enumerate(personalized_roles, 1):
        if country == "India":
            st.write(f"{idx}. **{role}** - {currency}{salary} {unit} | Match: {match_score*100:.0f}%")
        else:
            st.write(f"{idx}. **{role}** - {currency}{salary:,} {unit} | Match: {match_score*100:.0f}%")
    
    # Interactive Bar Chart for Personalized Roles
    df_personalized = pd.DataFrame({
        'Role': [r[0] for r in personalized_roles],
        'Salary': [r[1] for r in personalized_roles],
        'Match Score': [f"{r[2]*100:.0f}%" for r in personalized_roles]
    })
    
    # Set appropriate label based on country
    if country == "India":
        salary_label = f'Salary (LPA)'
    else:
        salary_label = f'Salary ({currency})'
    
    fig_personalized = px.bar(
        df_personalized,
        x='Role',
        y='Salary',
        color='Salary',
        text='Match Score',
        color_continuous_scale='Blues',
        labels={'Salary': salary_label},
        title=f"Your Best Matches in {country}"
    )
    fig_personalized.update_traces(textposition='outside')
    fig_personalized.update_layout(height=400)
    st.plotly_chart(fig_personalized, use_container_width=True)
    

st.info(f"💡 **Tip:** Salaries shown are based on market data for {country} and represent typical compensation for professionals in these roles. Focus on developing skills for your top-matched careers to maximize opportunities!")
