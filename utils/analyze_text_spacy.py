import spacy



# Betöltjük az angol modellt
nlp = spacy.load("en_core_web_sm")

# Skill lista (vagy akár később bővíthető/custom entitás)
TECH_SKILLS = [
    # Programozási nyelvek
    "python", "java", "c++", "c#", "r", "scala", "javascript", "typescript", "go", "ruby", "php", "swift", "matlab", "bash", "shell", "sql", "sas",

    # Adatbázisok és adattárolás
    "mysql", "postgresql", "mongodb", "cassandra", "redis", "oracle", "sql server", "hadoop", "hdfs", "spark", "bigquery", "elasticsearch",

    # Data Science / ML Frameworkök és Könyvtárak
    "tensorflow", "keras", "pytorch", "scikit-learn", "xgboost", "lightgbm", "catboost", "pandas", "numpy", "matplotlib", "seaborn", "plotly", "dash",

    # Cloud platformok és szolgáltatások
    "aws", "amazon web services", "azure", "google cloud", "gcp", "heroku", "digitalocean",

    # Konténerizáció és Orkesztráció
    "docker", "kubernetes", "openshift", "helm",

    # DevOps, CI/CD
    "jenkins", "gitlab", "circleci", "travisci", "ansible", "terraform", "puppet", "chef",

    # Verziókezelés és egyéb eszközök
    "git", "github", "bitbucket", "jira", "confluence",

    # Webfejlesztés
    "html", "css", "react", "angular", "vue", "node.js", "express", "django", "flask", "spring", "rest api", "graphql",

    # Egyéb fontos kifejezések
    "api", "microservices", "serverless", "nosql", "etl", "data engineering", "data pipeline", "machine learning", "deep learning", "natural language processing", "nlp", "computer vision", "big data",

    # Operációs rendszerek és infrastruktúra
    "linux", "windows", "unix", "ubuntu", "debian",

    # Biztonság
    "oauth", "jwt", "ssl", "tls", "firewall",

    # Adatfeldolgozás, analitika
    "spark", "hadoop", "flink", "airflow",

    # Mobilfejlesztés
    "android", "ios", "flutter", "react native"
]

HARD_SKILLS = [
    # Programozási nyelvek (ezek akár át is kerülhetnek TECH_KEYWORDS közé, de hard skillként is számítanak)
    "python", "java", "c++", "R programming", "R programming language", "sql", "matlab", "scala", "bash", "shell scripting", "javascript", "typescript", "go", "ruby", "php", "swift", "kotlin", "rust", "perl", "dart", "elixir", "haskell", "lua", "groovy", 

    # Adatbázisok
    "mysql", "postgresql", "mongodb", "oracle", "redis", "cassandra", "elasticsearch", "hadoop", "spark", "bigquery", "data warehouse", "data lake", "nosql", "sql server",

    # Adatfeldolgozás, ETL
    "etl", "data wrangling", "data cleaning", "data mining", "data engineering", "data pipeline", "data transformation", "data integration", "data modeling", "data warehousing", "data governance", "data quality", "data architecture", "data strategy",

    # Gépi tanulás / AI
    "machine learning", "deep learning", "neural networks", "natural language processing", "computer vision", "reinforcement learning", "predictive modeling", "model evaluation", "model deployment", "feature engineering", "hyperparameter tuning",

    # Frameworkök, könyvtárak
    "tensorflow", "keras", "pytorch", "scikit-learn", "xgboost", "lightgbm", "catboost", "pandas", "numpy", "scipy", "statsmodels", "nltk", "spaCy", "gensim", "transformers", "huggingface", "openai", "streamlit",

    # Vizualizáció
    "matplotlib", "seaborn", "plotly", "tableau", "power bi", "dash", "ggplot2", "d3.js",

    # Cloud és infrastruktúra
    "aws", "azure", "google cloud", "docker", "kubernetes", "jenkins", "terraform",

    # Webfejlesztés (ha releváns)
    "html", "css", "javascript", "react", "angular", "django", "flask", "node.js", "express", "Java spring",

    # Verziókezelés, DevOps
    "git", "github", "gitlab", "ci/cd", "jenkins", "ansible", "puppet", "chef", "circleci", "travisci", "bitbucket", "jira", "confluence",

    # Egyéb technikai képességek
    "agile methodologies", "scrum", "kanban", "test automation", "api development", "rest api", "graphql", "SAP", "salesforce", "data governance", "data quality", "data architecture", "data strategy"
]
SOFT_SKILLS = [
    "communication", "teamwork", "problem-solving", "critical thinking",
    "time management", "adaptability", "creativity", "leadership",
    "collaboration", "attention to detail", "work ethic", "empathy",
    "conflict resolution", "decision making", "motivation", "patience",
    "stress management", "active listening", "negotiation", "open-mindedness",
    "organizational skills", "self-motivation", "flexibility", "customer service",
    "persuasion", "public speaking", "interpersonal skills",
]


def extract_skills_spacy(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc]

    found_tech = set()
    found_hard = set()
    found_soft = set()

    # Egyszerű keresés a tokenekben, itt bővíthető advanced logikával
    for skill in TECH_SKILLS:
        if skill in text.lower():
            found_tech.add(skill)

    for skill in HARD_SKILLS:
        if skill in text.lower():
            found_hard.add(skill)

    for skill in SOFT_SKILLS:
        if skill in text.lower():
            found_soft.add(skill)

    return list(found_soft), list(found_hard), list(found_tech)
