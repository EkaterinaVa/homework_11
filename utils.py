import json


def load_candidates_from_json():
    """
    Возвращает список всех кандидатов
    """
    with open("data/candidates.json", "r") as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id):
    """
    Возвращает одного кандидата по его id
    """
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    """
    candidates = load_candidates_from_json()
    candidates_by_name = []
    for candidate in candidates:
        name_and_surname = candidate["name"].split(" ")
        name = name_and_surname[0]
        if name.lower() == candidate_name.lower():
            candidates_by_name.append(candidate)
    return candidates_by_name


def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    """
    candidates = load_candidates_from_json()
    candidates_by_skill = []
    for candidate in candidates:
        for skill in candidate["skills"].split(", "):
            if skill.lower() == skill_name.lower():
                candidates_by_skill.append(candidate)
    return candidates_by_skill

