# 1. DEFINIMOS LAS KEYWORDS
# Estas son las listas que el sistema usará para
# clasificar la urgencia de forma instantánea, las definimos nosotros.
KEYWORDS_URGENCIA_ALTA = [
    "roto", "no funciona", "desastre", "caído", "error fatal",
    "urgente", "inmediato", "no puedo trabajar", "estafa",
    "fraude", "no acceso", "crítico", "emergencia", "bloqueado",
    "perdí", "robaron", "hackear", "urgent", "critical",
    "emergency", "broken", "crashed", "down", "failed",
    "disaster", "help", "asap", "immediately"
]

KEYWORDS_URGENCIA_MEDIA = [
    "lento", "tarda mucho", "problema", "ayuda", "duda",
    "consulta", "pregunta", "mejorar", "sugerencia", "demora",
    "retraso", "confuso", "difícil", "complicado", "issue",
    "slow", "delay", "question", "support", "confused",
    "problem", "bug", "error"
]


# 2. LA FUNCIÓN CLASIFICADORA (entregable)
def classify_urgency(text: str) -> dict:
    """
    Clasifica la urgencia de un texto basado en keywords predefinidas.

    Args:
        text (str): El feedback del cliente.

    Returns:
        dict: Un diccionario con 'label' y 'score'.
    """
    if not text or not isinstance(text, str):
        return {"label": "BAJA", "score": 0.0}

    text_lower = text.lower()

    alta_matches = sum(1 for keyword in KEYWORDS_URGENCIA_ALTA if keyword in text_lower)
    media_matches = sum(1 for keyword in KEYWORDS_URGENCIA_MEDIA if keyword in text_lower)

    if alta_matches >= 2:
        return {"label": "ALTA", "score": 0.95}
    elif alta_matches >= 1:
        return {"label": "ALTA", "score": 0.8}
    elif media_matches >= 2:
        return {"label": "MEDIA", "score": 0.65}
    elif media_matches >= 1:
        return {"label": "MEDIA", "score": 0.5}
    else:
        return {"label": "BAJA", "score": 0.3}

# 3. PRUEBA RÁPIDA (Para probar el archivo)
if __name__ == "__main__":
    print("\n--- PRUEBA DE URGENCIA (REGLAS) ---")

    test_1 = "¡Es un desastre! ¡¡No funciona!!"
    test_2 = "Hola, tengo una pregunta sobre el envío."
    test_3 = "Todo bien, gracias."

    print(f"Texto: '{test_1}'")
    print(f"Resultado: {classify_urgency(test_1)}")

    print(f"\nTexto: '{test_2}'")
    print(f"Resultado: {classify_urgency(test_2)}")

    print(f"\nTexto: '{test_3}'")
    print(f"Resultado: {classify_urgency(test_3)}")