
CLUSTERS = {
    "C1": {
        "name": "Life Sciences",
        "subjects": ["biology", "anatomy", "physiology", "biochemistry", "microbiology", "genetics", "pathology"],
        "degrees": ["MPH", "MSHI"]
    },
    "C2": {
        "name": "Physical Sciences",
        "subjects": ["physics", "chemistry", "environmental chemistry", "earth science"],
        "degrees": ["MPH"]
    },
    "C3": {
        "name": "Quant & Analytical",
        "subjects": ["statistics", "biostatistics", "calculus", "data science", "econometrics", "machine learning", "algorithms", "data structures"],
        "degrees": ["MPH", "MSHI", "MBA-HC"]
    },
    "C4": {
        "name": "Social & Behavioral",
        "subjects": ["psychology", "sociology", "social work", "community studies", "anthropology", "cultural anthropology", "gender studies", "social research methods"],
        "degrees": ["MPH", "MHA"]
    },
    "C5": {
        "name": "Business & Management",
        "subjects": ["accounting", "finance", "economics", "marketing", "management", "hr", "entrepreneurship", "corporate finance", "financial accounting", "cost accounting", "taxation", "auditing", "business law"],
        "degrees": ["MBA-HC", "MHA"]
    },
    "C6": {
        "name": "Health & Clinical",
        "subjects": ["public health", "epidemiology", "clinical medicine", "health policy", "pharmacology", "global health", "community medicine", "oral medicine", "dental surgery", "community health nursing", "mental health nursing", "nursing administration", "geriatric nursing", "health & society"],
        "degrees": ["MHA", "MPH", "MSHI"]
    },
    "C7": {
        "name": "Information Technology",
        "subjects": ["computer science", "python", "sql", "database management", "database systems", "cybersecurity", "cloud computing", "software engineering", "java", "ehr integration"],
        "degrees": ["MSHI", "MBA-HC"]
    },
    "C8": {
        "name": "Policy, Law & Ethics",
        "subjects": ["political science", "healthcare law", "public policy", "regulatory affairs", "bioethics", "constitutional law", "public administration", "political philosophy", "international relations"],
        "degrees": ["MPH", "MHA"]
    },
    "C9": {
        "name": "Comm & Humanities",
        "subjects": ["english", "writing", "journalism", "public speaking", "philosophy", "history", "indian politics"],
        "degrees": ["MHA", "MPH"]
    },
    "C10": {
        "name": "Engineering & Systems",
        "subjects": ["industrial engineering", "biomedical engineering", "quality management", "lean", "six sigma"],
        "degrees": ["MSHI", "MHA"]
    }
}

DEGREES = {
    "MHA": "Master of Health Administration — Provider operations, hospital leadership",
    "MPH": "Master of Public Health — Population health, epidemiology, policy",
    "MSHI": "Master of Science in Health Informatics — Health IT, data systems, EHR",
    "MBA-HC": "MBA with Healthcare Concentration — Finance, strategy, entrepreneurship"
}

TRACKS = {
    "T01": {
        "name": "Healthcare Administration, Operations, Quality & Risk",
        "primary_degree": "MHA",
        "alt_degrees": ["MPH", "MBA-HC"],
        "sop_keywords": ["leadership", "operations", "quality improvement", "organizational", "hospital", "administrative", "management", "health system", "risk", "administrator", "director", "executive", "ceo", "coo"],
        "experience_keywords": ["hospital", "operations", "administrator", "clinical coordinator", "ward manager", "quality", "accreditation", "nursing administration"]
    },
    "T02": {
        "name": "Healthcare Consulting & Advisory",
        "primary_degree": "MBA-HC",
        "alt_degrees": ["MHA", "MPH"],
        "sop_keywords": ["consulting", "advisory", "strategy", "client", "transformation", "implementation", "project", "problem solving", "mckinsey", "deloitte", "bcg", "consulting firm"],
        "experience_keywords": ["consultant", "advisory", "associate", "deloitte", "kpmg", "mckinsey", "pwc", "project manager", "strategy"]
    },
    "T03": {
        "name": "Healthcare Finance, Payer Strategy & Value-Based Care",
        "primary_degree": "MBA-HC",
        "alt_degrees": ["MHA", "MSHI"],
        "sop_keywords": ["finance", "cfo", "revenue cycle", "payer", "value-based care", "vbc", "aco", "capital", "reimbursement", "contracting", "financial", "cost", "budget", "billing"],
        "experience_keywords": ["finance", "audit", "accounting", "revenue", "billing", "cpa", "payer", "insurance", "actuarial", "financial analyst"]
    },
    "T04": {
        "name": "Behavioral Health & Human Services Management",
        "primary_degree": "MPH",
        "alt_degrees": ["MHA"],
        "sop_keywords": ["mental health", "behavioral health", "substance use", "sud", "community behavioral", "psychology", "social work", "counseling", "addiction", "wellbeing", "psychiatric"],
        "experience_keywords": ["mental health", "behavioral", "counselor", "social worker", "psychiatric", "therapy", "rehabilitation"]
    },
    "T05": {
        "name": "Public, Community & Global Health Programs",
        "primary_degree": "MPH",
        "alt_degrees": ["MHA", "MBA-HC"],
        "sop_keywords": ["community health", "health equity", "social determinants", "disease prevention", "outreach", "education", "global health", "underserved", "vulnerable population", "sdoh", "health promotion", "public health"],
        "experience_keywords": ["community", "outreach", "ngo", "health educator", "community health worker", "program coordinator", "health promotion"]
    },
    "T06": {
        "name": "Population Health Analytics, Epidemiology & Outcomes Research",
        "primary_degree": "MPH",
        "alt_degrees": ["MSHI", "MBA-HC"],
        "sop_keywords": ["epidemiology", "biostatistics", "data analysis", "outcomes", "research", "surveillance", "population health", "evaluation", "methodology", "cohort", "clinical research", "analytics"],
        "experience_keywords": ["analyst", "epidemiologist", "researcher", "biostatistician", "data scientist", "outcomes", "research assistant"]
    },
    "T07": {
        "name": "Health Policy, Economics & Advocacy",
        "primary_degree": "MPH",
        "alt_degrees": ["MBA-HC", "MHA"],
        "sop_keywords": ["policy", "legislation", "advocacy", "government", "regulatory", "health economics", "ayushman", "reform", "law", "political", "legislative", "national health", "ministry", "public policy", "think tank"],
        "experience_keywords": ["policy", "government", "ministry", "think tank", "advocacy", "legislative", "regulator", "health economist"]
    },
    "T08": {
        "name": "Environmental, Occupational & Climate Health",
        "primary_degree": "MPH",
        "alt_degrees": ["MHA"],
        "sop_keywords": ["environmental health", "occupational safety", "toxicology", "exposure", "food safety", "climate health", "pollution", "industrial hygiene", "ehs"],
        "experience_keywords": ["environmental", "occupational", "safety", "toxicologist", "ehs", "osha", "industrial hygiene"]
    },
    "T09": {
        "name": "Digital Health, Informatics & Data Governance",
        "primary_degree": "MSHI",
        "alt_degrees": ["MHA", "MBA-HC"],
        "sop_keywords": ["ehr", "health it", "informatics", "fhir", "interoperability", "clinical decision support", "digital health", "data governance", "health data", "electronic health record", "cds", "hl7", "healthcare technology", "health informatics"],
        "experience_keywords": ["ehr", "health it", "software developer", "health tech", "fhir", "interoperability", "informatics", "aws", "cloud", "database", "sql", "python"]
    },
    "T10": {
        "name": "Life Sciences, Clinical Research & Regulatory Management",
        "primary_degree": "MBA-HC",
        "alt_degrees": ["MPH", "MSHI"],
        "sop_keywords": ["pharma", "biotech", "medtech", "clinical trials", "regulatory", "fda", "irb", "life sciences", "drug development", "medical device", "cro", "gcp"],
        "experience_keywords": ["pharma", "biotech", "clinical research", "regulatory affairs", "fda", "clinical trials", "medical device", "cro"]
    },
    "T11": {
        "name": "Healthcare Entrepreneurship, Product & Innovation",
        "primary_degree": "MBA-HC",
        "alt_degrees": ["MSHI", "MHA"],
        "sop_keywords": ["startup", "innovation", "entrepreneurship", "product", "venture", "gtm", "scale", "build", "launch", "disrupt", "digital health startup", "healthtech", "founder", "new model", "care model"],
        "experience_keywords": ["startup", "founder", "product manager", "entrepreneur", "venture", "innovation", "health tech startup"]
    }
}
