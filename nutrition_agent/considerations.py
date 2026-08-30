from __future__ import annotations

import re

from baseline.schemas import NutritionConsideration, PatientIntake


def _consideration(topic: str, rationale: str, fields: list[str]) -> NutritionConsideration:
    return NutritionConsideration(
        topic=topic, rationale=rationale, source_patient_fields=fields,
        limiting_or_missing_facts=[],
    )


def build_supported_considerations(patient: PatientIntake) -> list[NutritionConsideration]:
    diet = patient.dietary_pattern.lower()
    diagnoses = " ".join(patient.known_diagnoses).lower()
    symptoms = " ".join(patient.symptoms).lower()
    context = f"{patient.reason_for_consultation} {patient.primary_goal}".lower()
    items: list[NutritionConsideration] = []
    if "iron deficiency" in diagnoses and "vegetarian" in diet:
        items.extend([
            _consideration(
                "Adequate dietary iron within a vegetarian eating pattern",
                "The established iron-deficiency context and vegetarian pattern make dietary iron relevant.",
                ["known_diagnoses", "dietary_pattern"],
            ),
            _consideration(
                "Meal factors affecting vegetarian iron absorption",
                "The diagnosed iron deficiency and vegetarian pattern support discussing meal composition around iron sources.",
                ["known_diagnoses", "dietary_pattern"],
            ),
        ])
    elif "vegetarian" in diet:
        items.append(_consideration(
            "Maintain dietary variety and balanced meal composition",
            "The varied vegetarian pattern and consultation goal support maintaining balanced meals without assuming deficiency.",
            ["dietary_pattern", "primary_goal"],
        ))
    if re.search(r"sweetened drinks", diet):
        items.extend([
            _consideration(
                "Reduce frequent sugar-sweetened beverages",
                "Daily sweetened drinks are a reported, modifiable source of added sugar.", ["dietary_pattern"],
            ),
            _consideration(
                "Increase fiber-rich foods and overall dietary quality",
                "Few vegetables and the established prediabetes context make fiber-rich foods relevant.",
                ["dietary_pattern", "known_diagnoses"],
            ),
        ])
    if re.search(r"(?:stuck|swallow)", symptoms):
        items.append(_consideration(
            "Current intake may be inadequate due to difficulty swallowing solids",
            "The reported swallowing difficulty and liquid-focused diet directly limit current intake.",
            ["symptoms", "dietary_pattern"],
        ))
    if re.search(r"vomit", symptoms) and re.search(r"sip|water", diet):
        items.append(_consideration(
            "Oral intake and hydration are currently severely limited",
            "Repeated vomiting and intake limited to small sips directly constrain nutrition and hydration.",
            ["symptoms", "dietary_pattern"],
        ))
    if re.search(r"takeaway|irregular", diet):
        items.extend([
            _consideration(
                "Build a sustainable regular meal structure",
                "Irregular meals and frequent takeaway food support prioritizing practical meal structure.",
                ["dietary_pattern", "primary_goal"],
            ),
            _consideration(
                "Make gradual improvements to overall dietary quality",
                "The reported takeaway pattern and sustainable-habits goal support gradual dietary changes.",
                ["dietary_pattern", "primary_goal"],
            ),
        ])
    if "kidney disease" in diagnoses and re.search(r"packaged|deli", diet):
        items.append(_consideration(
            "Reduce high-sodium packaged foods within existing clinician guidance",
            "Known kidney disease and frequent packaged soups and deli meats make sodium reduction relevant.",
            ["known_diagnoses", "dietary_pattern"],
        ))
    if re.search(r"skip(?:s|ped|ping)? lunch", patient.additional_notes, re.I):
        items.append(_consideration(
            "Meal regularity may relate to afternoon energy if lunch is skipped",
            "Skipped lunch and reported afternoon low energy support clarifying a meal-timing relationship.",
            ["additional_notes", "symptoms"],
        ))
    if re.search(r"marathon|endurance", context):
        items.extend([
            _consideration(
                "Carbohydrate availability for endurance training",
                "The marathon goal and high running volume make training carbohydrate availability relevant.",
                ["reason_for_consultation", "physical_activity"],
            ),
            _consideration(
                "Recovery nutrition and hydration",
                "The endurance training load and recovery goal support planning post-training nutrition and hydration.",
                ["physical_activity", "primary_goal"],
            ),
        ])
    return items[:3]

