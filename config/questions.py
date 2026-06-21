'''
'''

###################################################### APPLICATION INPUTS ######################################################

# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "1"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://zafran-sakowi.my"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/zafran-sakowi/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Other"

## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 4000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes


# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 0            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "RM" in it (Example: What is your current CTC in RM), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 0                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Software Engineer | Full-Stack Developer | Next.js & Spring Boot" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
Bachelor of Computer Science (Software Engineering) student at Universiti Teknologi Malaysia (graduating Aug 2026) with a GPA of 3.79/4.00.
Experience as a Software Developer Intern at Mattel Malaysia and Part-time Full-Stack Developer at Cipta Craft Solutions.
Skilled in Next.js, React, Java/Spring Boot, Python/FastAPI, PostgreSQL, and Docker.
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am writing to express my strong interest in the Software Engineer position. As a Computer Science (Software Engineering) student at Universiti Teknologi Malaysia graduating in August 2026, and with practical experience as a Software Developer Intern at Mattel Malaysia and a Full-Stack Developer at Cipta Craft Solutions, I am excited to contribute my skills to your team.

Throughout my internship and part-time roles, I have developed a solid foundation in building robust web applications, optimizing database performance, and deploying containerized applications. I have worked extensively with Next.js, React, Java (Spring Boot), Python (FastAPI), and PostgreSQL.

I am eager to bring my technical expertise, problem-solving mindset, and passion for software development to your company. Thank you for your time and consideration.

Sincerely,
Zafran Bin Muhamad Sakowi
"""

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all = """
ZAFRAN BIN MUHAMAD SAKOWI
Selangor, MY | +60 165972862 | zafransakowi@gmail.com
zafran-sakowi.my | linkedin.com/in/zafran-sakowi/

EDUCATION
UNIVERSITI TEKNOLOGI MALAYSIA, Johor, MY
Bachelor of Computer Science (Software Engineering) with Honours, Graduate Aug 2026
* Academic Standing: Cumulative GPA: 3.79/4.00
* Honours: Recipient of continuous Dean's List Commendations (2022 - 2026)

SKILLS
* Languages: TypeScript, JavaScript, Java, Python, T-SQL, Classic ASP, VBScript
* Frontend Frameworks: Next.js 14/15, React, React Native, TailwindCSS, shadcn/ui, MVVM architecture
* Backend Architectures: Spring Boot, FastAPI, Node.js, Laravel, RESTful API Design, Inversion of Control (IoC)
* Database Management: PostgreSQL, MySQL, SQL Server, Supabase, Row Level Security (RLS), Hibernate ORM
* DevOps & Infrastructure: Docker, Nginx, Caddy, CI/CD (Gitea), Ubuntu Server, Cloudflare R2, Proxmox VE
* Security & Monitoring: JWT Authentication, RBAC, Automated Audit Logging, Rate Limiting
* Tooling & Methodologies: Postman, VS Code, Git/GitHub, Jira, Agile Sprint Frameworks

WORK EXPERIENCE
Mattel Malaysia Sdn Bhd, Penang, MY
Software Developer Intern, Aug 2025 - Jan 2026
* Eliminated an 8-second query bottleneck on high-traffic manufacturing QC dashboards, reducing data retrieval latency by 94% via T-SQL index restructuring and execution plan optimization; improved real-time monitoring responsiveness for 20+ production floor operators.
* Architected a state-machine-driven audit trail for global manufacturing workflows, enforcing tamper-proof record integrity across multi-region operations; the system passed Mattel's internal compliance audit on first submission with zero remediation requests.

Cipta Craft Solutions, Johor, MY
Part Time Full-Stack Developer, Jun 2025 - Present
* Built XFitness, a full-stack gym management platform (Next.js 15, Supabase, PostgreSQL, Docker) with QR-based access control, automated membership billing, and trainer scheduling; reduced client administrative overhead by 15 hours/week and eliminated manual billing errors.
* Delivered Anjung Meriah CMS, a corporate website with JWT-authenticated content management, append-only audit logging, and <1s page rebuild time, removing 100% developer dependency for routine content operations.
* Coordinated a 4-person engineering team across 3 delivery sprints using Git branching, PR review gates, and automated CI pipelines; all milestones delivered within agreed 10-week sprint timeline.
"""
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Cipta Craft Solutions" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "9"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##

# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False        # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive
