def resolve_canonical_to_target_note(canonical_key, target_profile, master_config):
    # Pass 1: Standard Direct Validation Match
    target_note = target_profile.canonical_to_note.get(canonical_key)
    if target_note is not None:
        return int(target_note)
        
    # Pass 2: Evaluate Schema Specific Global Fallback Chains
    fallbacks = master_config.get("global_fallbacks", {}).get(canonical_key, [])
    for fallback_key in fallbacks:
        target_note = target_profile.canonical_to_note.get(fallback_key)
        if target_note is not None:
            return int(target_note)
            
    # Pass 3: Evaluate Relative Structural Tom Stepping
    if "TOM" in canonical_key:
        tom_sequence = ["TOM_2_HIT", "TOM_3_HIT", "TOM_4_HIT", "TOM_1_HIT"]
        for tom_fallback in tom_sequence:
            target_note = target_profile.canonical_to_note.get(tom_fallback)
            if target_note is not None:
                return int(target_note)

    return None