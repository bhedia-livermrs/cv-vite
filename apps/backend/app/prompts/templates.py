"""Modèles de prompts LLM pour le traitement de CV.

Les instructions sont chargées depuis des fichiers texte éditables
dans le dossier instructions/. Les schémas JSON restent ici car ce
sont des structures de données, pas des instructions éditables.
"""

from app.prompts.loader import load_prompt

# Langue unique : français
LANGUAGE_NAMES = {
    "fr": "Français",
}


def get_language_name(code: str) -> str:
    """Retourne le nom complet de la langue. Toujours Français."""
    return LANGUAGE_NAMES.get(code, "Français")


# Schema with example values - used for prompts to show LLM expected format
RESUME_SCHEMA_EXAMPLE = """{
  "personalInfo": {
    "name": "Jean Dupont",
    "title": "Ingénieur Logiciel",
    "email": "jean@example.com",
    "phone": "+33-1-23-45-67-89",
    "location": "Paris, France",
    "website": "https://jeandupont.dev",
    "linkedin": "linkedin.com/in/jeandupont",
    "github": "github.com/jeandupont"
  },
  "summary": "Ingénieur logiciel expérimenté avec plus de 5 ans...",
  "workExperience": [
    {
      "id": 1,
      "title": "Ingénieur Logiciel Senior",
      "company": "Tech Corp",
      "location": "Paris, France",
      "years": "Jan 2020 - Présent",
      "description": [
        "Dirigé le développement d'une architecture microservices",
        "Amélioré les performances du système de 40%"
      ]
    }
  ],
  "education": [
    {
      "id": 1,
      "institution": "Université de Paris",
      "degree": "M2 Informatique",
      "years": "2014 - 2018",
      "description": "Diplômé avec mention"
    }
  ],
  "personalProjects": [
    {
      "id": 1,
      "name": "Outil Open Source",
      "role": "Créateur & Mainteneur",
      "years": "Mar 2021 - Présent",
      "description": [
        "Développé un outil CLI avec plus de 1000 étoiles GitHub",
        "Utilisé par plus de 50 entreprises dans le monde"
      ]
    }
  ],
  "additional": {
    "technicalSkills": ["Python", "JavaScript", "AWS", "Docker"],
    "languages": ["Français (Natif)", "Anglais (Courant)"],
    "certificationsTraining": ["AWS Solutions Architect"],
    "awards": ["Employé de l'année 2022"]
  },
  "customSections": {
    "publications": {
      "sectionType": "itemList",
      "items": [
        {
          "id": 1,
          "title": "Titre de l'article",
          "subtitle": "Nom de la revue",
          "years": "Juin 2023",
          "description": ["Brève description de la publication"]
        }
      ]
    },
    "travail_benevole": {
      "sectionType": "text",
      "text": "Description des activités bénévoles..."
    }
  }
}"""

# Schema for improve prompts - excludes personalInfo (preserved from original)
IMPROVE_SCHEMA_EXAMPLE = """{
  "summary": "Ingénieur logiciel expérimenté avec plus de 5 ans...",
  "workExperience": [
    {
      "id": 1,
      "title": "Ingénieur Logiciel Senior",
      "company": "Tech Corp",
      "location": "Paris, France",
      "years": "Jan 2020 - Présent",
      "description": [
        "Dirigé le développement d'une architecture microservices",
        "Amélioré les performances du système de 40%"
      ]
    }
  ],
  "education": [
    {
      "id": 1,
      "institution": "Université de Paris",
      "degree": "M2 Informatique",
      "years": "2014 - 2018",
      "description": "Diplômé avec mention"
    }
  ],
  "personalProjects": [
    {
      "id": 1,
      "name": "Outil Open Source",
      "role": "Créateur & Mainteneur",
      "years": "Mar 2021 - Présent",
      "description": [
        "Développé un outil CLI avec plus de 1000 étoiles GitHub",
        "Utilisé par plus de 50 entreprises dans le monde"
      ]
    }
  ],
  "additional": {
    "technicalSkills": ["Python", "JavaScript", "AWS", "Docker"],
    "languages": ["Français (Natif)", "Anglais (Courant)"],
    "certificationsTraining": ["AWS Solutions Architect"],
    "awards": ["Employé de l'année 2022"]
  },
  "customSections": {
    "publications": {
      "sectionType": "itemList",
      "items": [
        {
          "id": 1,
          "title": "Titre de l'article",
          "subtitle": "Nom de la revue",
          "years": "Juin 2023",
          "description": ["Brève description de la publication"]
        }
      ]
    },
    "travail_benevole": {
      "sectionType": "text",
      "text": "Description des activités bénévoles..."
    }
  }
}"""

# --- Prompts chargés depuis fichiers texte éditables ---

PARSE_RESUME_PROMPT = load_prompt("parse_resume")

EXTRACT_KEYWORDS_PROMPT = load_prompt("extract_keywords")

CRITICAL_TRUTHFULNESS_RULES_TEMPLATE = load_prompt("truthfulness_rules")


def _build_truthfulness_rules(rule_7: str) -> str:
    return CRITICAL_TRUTHFULNESS_RULES_TEMPLATE.format(rule_7=rule_7)


CRITICAL_TRUTHFULNESS_RULES = {
    "nudge": _build_truthfulness_rules(
        "NE PAS ajouter de nouveaux points ou contenu - uniquement reformuler le contenu existant"
    ),
    "keywords": _build_truthfulness_rules(
        "Vous pouvez reformuler les points existants pour inclure des mots-clés, mais NE PAS ajouter de nouveaux points"
    ),
    "full": _build_truthfulness_rules(
        "Vous pouvez développer les points existants ou en ajouter de nouveaux qui élaborent sur le travail existant, mais NE PAS inventer de nouvelles responsabilités"
    ),
}

IMPROVE_RESUME_PROMPT_NUDGE = load_prompt("improve_nudge")

IMPROVE_RESUME_PROMPT_KEYWORDS = load_prompt("improve_keywords")

IMPROVE_RESUME_PROMPT_FULL = load_prompt("improve_full")

IMPROVE_PROMPT_OPTIONS = [
    {
        "id": "nudge",
        "label": "Ajustement léger",
        "description": "Modifications minimales pour mieux aligner l'expérience existante.",
    },
    {
        "id": "keywords",
        "label": "Enrichissement mots-clés",
        "description": "Intégration des mots-clés pertinents sans changer le rôle ou le périmètre.",
    },
    {
        "id": "full",
        "label": "Adaptation complète",
        "description": "Adaptation complète en utilisant la description de poste.",
    },
]

IMPROVE_RESUME_PROMPTS = {
    "nudge": IMPROVE_RESUME_PROMPT_NUDGE,
    "keywords": IMPROVE_RESUME_PROMPT_KEYWORDS,
    "full": IMPROVE_RESUME_PROMPT_FULL,
}

DEFAULT_IMPROVE_PROMPT_ID = "keywords"

# Backward-compatible alias
IMPROVE_RESUME_PROMPT = IMPROVE_RESUME_PROMPT_FULL

COVER_LETTER_PROMPT = load_prompt("cover_letter")

OUTREACH_MESSAGE_PROMPT = load_prompt("outreach_message")

GENERATE_TITLE_PROMPT = load_prompt("generate_title")

# Alias for backward compatibility
RESUME_SCHEMA = RESUME_SCHEMA_EXAMPLE

# Instructions de stratégie diff (en français)
DIFF_STRATEGY_INSTRUCTIONS = {
    "nudge": "Effectuer des modifications minimales. Reformuler uniquement là où il y a une correspondance claire. Ne pas ajouter de nouveaux points.",
    "keywords": "Intégrer les mots-clés pertinents là où des preuves existent déjà. Vous pouvez reformuler les points mais ne pas en ajouter de nouveaux.",
    "full": "Effectuer des ajustements ciblés. Vous pouvez reformuler les points, ajouter des compétences vérifiées de la description de poste, et ajouter de nouveaux points qui élaborent sur le travail existant, mais ne pas inventer de nouvelles responsabilités.",
}

SKILL_TARGET_PLAN_PROMPT = load_prompt("skill_target_plan")

DIFF_IMPROVE_PROMPT = load_prompt("diff_improve")
