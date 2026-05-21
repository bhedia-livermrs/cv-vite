"""Modèles de prompts LLM pour l'enrichissement de CV par IA.

Les instructions sont chargées depuis des fichiers texte éditables
dans le dossier instructions/.
"""

from app.prompts.loader import load_prompt

ANALYZE_RESUME_PROMPT = load_prompt("analyze_resume")

ENHANCE_DESCRIPTION_PROMPT = load_prompt("enhance_description")


# ============================================
# Fonctionnalité de régénération IA
# ============================================


REGENERATE_ITEM_PROMPT = load_prompt("regenerate_item")


REGENERATE_SKILLS_PROMPT = load_prompt("regenerate_skills")
