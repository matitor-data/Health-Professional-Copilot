from __future__ import annotations

import re

from baseline.schemas import BriefItem, PatientIntake
from nutrition_agent.schemas import PatientState, ReferralDecision


def _item(topic: str, question: str, rationale: str, fields: list[str]) -> tuple[BriefItem, BriefItem]:
    return (
        BriefItem(topic=topic, rationale=rationale, source_patient_fields=fields),
        BriefItem(topic=question, rationale=rationale, source_patient_fields=fields),
    )


def build_gap_coverage(
    patient: PatientIntake, state: PatientState, decisions: list[ReferralDecision]
) -> tuple[list[BriefItem], list[BriefItem]]:
    candidates: list[tuple[BriefItem, BriefItem]] = []
    all_symptoms = " ".join(patient.symptoms).lower()
    diet = patient.dietary_pattern.lower()
    diagnoses = " ".join(patient.known_diagnoses).lower()
    goal_context = f"{patient.reason_for_consultation} {patient.primary_goal}".lower()

    if re.search(r"(?:stuck|swallow)", all_symptoms):
        candidates.extend([
            _item("Ability to swallow liquids and current hydration", "Can you swallow liquids safely, and what food and fluid intake are you currently managing?", "Swallowing liquids and current hydration can change both referral and nutrition preparation.", ["symptoms", "dietary_pattern"]),
            _item("Associated pain, vomiting, or bleeding", "Is there pain, vomiting, bleeding, or another symptom associated with swallowing?", "Associated symptoms can change the urgency and scope of the consultation.", ["symptoms"]),
        ])
    if re.search(r"vomit", all_symptoms):
        candidates.extend([
            _item("Ability to retain fluids", "Can you retain any fluids, and approximately how much have you kept down?", "Fluid retention is immediately relevant to hydration and medical escalation.", ["symptoms", "dietary_pattern"]),
            _item("Blood, severe pain, fever, or confusion", "Have you had blood, severe pain, fever, confusion, or worsening dizziness?", "These associated observations can change escalation urgency.", ["symptoms"]),
        ])
    if "iron deficiency" in diagnoses and patient.supplements:
        candidates.extend([
            _item("Iron supplement dose, timing, duration, and adherence", "What dose was prescribed, when was it started, how is it timed, and how consistently is it taken?", "Treatment details must be clarified without assuming adherence or response.", ["supplements", "known_diagnoses"]),
            _item("Recent follow-up laboratory results", "What follow-up laboratory results or physician review have already occurred?", "Existing follow-up context can change nutrition priorities without requesting new tests.", ["known_diagnoses", "additional_notes"]),
            _item("Menstrual or other blood-loss history", "If relevant, is there menstrual or other known blood-loss context already discussed medically?", "Reported blood-loss context could affect preparation for dietary iron discussion.", ["known_diagnoses"]),
        ])
    if "kidney disease" in diagnoses:
        candidates.extend([
            _item("Renal function trend and clinician nutrition instructions", "What renal-function trend and nutrition instructions have already been provided by nephrology?", "Existing nephrology guidance should determine the boundaries of nutrition preparation.", ["known_diagnoses", "additional_notes", "existing_labs"]),
            _item("Usual sodium intake from packaged foods", "How often and in what portions are packaged soups, deli meats, and other salty foods eaten?", "Usual packaged-food intake is needed to assess sodium exposure.", ["dietary_pattern"]),
            _item("Complete medication and supplement list", "Is the reported medication and supplement list complete and current?", "A complete reported list is needed without recommending medication changes.", ["medications", "supplements"]),
        ])
    if re.search(r"marathon|endurance", goal_context):
        candidates.extend([
            _item("Training-day carbohydrate and fluid intake", "What carbohydrate and fluid intake is used before, during, and after training?", "Training-day intake can change endurance fueling preparation.", ["physical_activity", "dietary_pattern"]),
            _item("Sweat rate and race fueling plan", "What is the current sweat, hydration, and race-day fueling strategy?", "Race-specific hydration and fueling details are needed for a useful consultation.", ["physical_activity"]),
        ])
    if "vegetarian" in diet:
        candidates.append(_item(
            "Iron-rich and fortified food intake", "Which iron-rich and fortified foods are eaten, how often, and in what portions?",
            "Case-specific food frequency is needed without assuming a dietary-pattern deficiency.", ["dietary_pattern"],
        ))
    if re.search(r"takeaway|irregular", diet):
        candidates.extend([
            _item("Barriers to regular meals", "What barriers lead to irregular meals or frequent takeaway food?", "Practical barriers determine whether meal-structure changes are sustainable.", ["dietary_pattern"]),
            _item("Readiness and food preferences", "Which realistic food changes feel acceptable and achievable now?", "Readiness and preferences determine the consultation starting point.", ["primary_goal", "dietary_pattern"]),
        ])
    if state.contradictions:
        candidates.extend([
            _item("Resolve conflicting weight history", "Which weight history is accurate, including amount, intention, and timing?", "The conflicting weight history must be resolved before interpreting risk.", ["recent_weight_change", "additional_notes"]),
            _item("Resolve conflicting meal frequency", "Are three meals usually eaten, or is lunch often skipped?", "The conflicting meal-frequency statements could change the nutrition assessment.", ["dietary_pattern", "additional_notes"]),
        ])
    for decision in decisions:
        if decision.eligibility == "clarify_first":
            candidates.append(_item(
                "Clarify before considering medical referral",
                decision.clarification_question or "What facts must be confirmed before referral?",
                "Clarification could change whether medical evaluation is indicated.",
                decision.source_patient_fields,
            ))
    if state.contradictions:
        contradiction = state.contradictions[0]
        candidates.append(_item(
            "Resolve contradictory intake information",
            "Which of the conflicting intake statements is current and accurate?",
            "Resolving the contradiction could materially change consultation priorities.",
            contradiction.fields,
        ))
    if patient.symptoms:
        fields = ["symptoms", "symptom_duration"]
        candidates.append(_item(
            "Symptom course and effect on intake",
            "How have the reported symptoms changed, and how do they affect food or fluid intake?",
            "Symptom course and intake impact could change nutrition preparation and escalation.", fields,
        ))
    if patient.recent_weight_change is None or re.search(r"(?:loss|gain|not known)", patient.recent_weight_change, re.I):
        candidates.append(_item(
            "Weight-change context", "Was the weight change intentional, over what period, and how was it measured?",
            "Intentionality, magnitude, and timing determine the relevance of weight change.",
            ["recent_weight_change"],
        ))
    if patient.known_diagnoses or patient.medications or patient.supplements:
        candidates.append(_item(
            "Established treatment and follow-up context",
            "What clinician guidance, treatment use, response, and follow-up are actually established?",
            "Known treatment context can change nutrition priorities without assuming adherence or response.",
            [field for field in ("known_diagnoses", "medications", "supplements") if getattr(patient, field)],
        ))
    if not patient.dietary_pattern or patient.dietary_pattern.lower() == "not reported":
        candidates.append(_item(
            "Usual food and beverage intake", "What do you usually eat and drink across a typical day?",
            "A usual intake pattern is necessary to prepare relevant nutrition questions.", ["dietary_pattern"],
        ))
    else:
        candidates.append(_item(
            "Portions, timing, and meal composition",
            "What are the usual portions, timing, beverages, and composition of meals and snacks?",
            "The reported dietary pattern does not establish portions or meal distribution.", ["dietary_pattern"],
        ))
    if patient.physical_activity or patient.sleep:
        candidates.append(_item(
            "Activity, recovery, and sleep context",
            "How do activity demands, recovery, and sleep interact with the nutrition goal?",
            "Activity and recovery context can change meal timing and adequacy priorities.",
            [field for field in ("physical_activity", "sleep") if getattr(patient, field)],
        ))
    candidates.append(_item(
        "Consultation priorities and constraints",
        "Which change matters most now, and what preferences or barriers should shape the plan?",
        "Priorities and constraints determine which nutrition changes are practical.",
        ["primary_goal", "reason_for_consultation"],
    ))
    unique: list[tuple[BriefItem, BriefItem]] = []
    seen: set[str] = set()
    for gap, question in candidates:
        key = gap.topic.lower()
        if key not in seen:
            seen.add(key)
            unique.append((gap, question))
    selected = unique[:5]
    return [gap for gap, _ in selected], [question for _, question in selected]
