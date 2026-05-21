"""Chargeur de fichiers d'instructions pour les prompts IA.

Ce module charge les fichiers .txt depuis le dossier instructions/ et les met
en cache en mémoire. Les fichiers peuvent être édités sans toucher au code Python.
"""

import logging
from pathlib import Path

logger = logging.getLogger(__name__)

_INSTRUCTIONS_DIR = Path(__file__).parent / "instructions"
_cache: dict[str, str] = {}


def load_prompt(name: str) -> str:
    """Charge un prompt depuis un fichier texte dans instructions/.

    Args:
        name: Nom du fichier sans l'extension .txt (ex: "analyze_resume").

    Returns:
        Le contenu du fichier texte.

    Raises:
        FileNotFoundError: Si le fichier n'existe pas.
    """
    if name in _cache:
        return _cache[name]

    path = _INSTRUCTIONS_DIR / f"{name}.txt"
    if not path.exists():
        raise FileNotFoundError(
            f"Fichier d'instructions introuvable : {path}"
        )

    content = path.read_text(encoding="utf-8")
    _cache[name] = content
    logger.debug("Prompt chargé depuis %s", path)
    return content


def reload_prompt(name: str) -> str:
    """Force le rechargement d'un prompt depuis le disque (ignore le cache).

    Utile après modification d'un fichier d'instructions en cours d'exécution.
    """
    _cache.pop(name, None)
    return load_prompt(name)


def clear_cache() -> None:
    """Vide le cache de tous les prompts chargés."""
    _cache.clear()
