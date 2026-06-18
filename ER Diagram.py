from graphviz import Digraph

er = Digraph('Zecpath_ER_Diagram', format='png')

er.node('User', '''User
-----------------
id(PK)
username 
email
password
role
created_at''', shape='box')

er.node('Employer', '''Employer
----------------
id(PK)
user_id (FK)
company_name
company_description
company_website
location''', shape='box')

er.node('Candidate', '''Candidate
----------------
id (PK)
user_id (PK)
full_name
phone
resume
skills
experience''', shape='box')

er.node('Job', '''Job
---------------
id (PK)
employer_id (FK)
title
description
location
salary
created_at''', shape='box')

er.node('Application', '''Application
----------------
id (PK)
job_id (FK)
candidate_id (FK)
status
applied_at''',shape='box')

#Relationships
er.edge('User', 'Employer', label='1:1')
er.edge('User', 'Candidate', label='1:1')
er.edge('Employer', 'Job', label='1:M')
er.edge('Job', 'Application', label='1:M')
er.edge('Candidate', 'Application', label='1:M')

#save diagram
er.render('Zecpath_er_diagram', view=True)

print("ER Diagram generated successfully")