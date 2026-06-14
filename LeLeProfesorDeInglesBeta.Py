# LELE v100.9 — Tu Asistente Inteligente + Profe de Inglés Encubierto + Amigo Rioplatense.
# Con Castigo "Looser", Extracción de Contexto + Noticias en Tiempo Real + MINIJUEGO INGLES INFINITO.
# ACT. 100.9: Escucha mejorada, saludo IA dinámico, nombre a "Yo" y Sistema Anti-Repetición de frases.

import asyncio
import sys
import re
import threading
import numpy as np
import sounddevice as sd
import tempfile
import os
import random
import time
import uuid
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from faster_whisper import WhisperModel
import edge_tts
import pygame

# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN GENERAL
# ════════════════════════════════════════════════════════════════════════════

TEMP_DIR = tempfile.gettempdir()
CACHE_DIR = r"C:\Users\lex\Desktop\LELE PROFESOR MiniMax\models"
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)
os.environ["HF_HOME"] = CACHE_DIR

pygame.mixer.init(44100, -16, 2, 512)

# Ajustes de audio
MODEL_SIZE = "base"          
SAMPLE_RATE = 16000
CHUNK_SIZE = 2048
SILENCE_SECONDS = 0.6          
MIN_AUDIO_SECONDS = 0.5      
CHUNKS_SILENCE = int(SILENCE_SECONDS * SAMPLE_RATE / CHUNK_SIZE)
ENERGY_THRESHOLD = 0.0050    

VOICE_ES = "es-UY-ValentinaNeural"  
VOICE_EN = "en-US-GuyNeural"        
TTS_RATE = "+10%"                    

# API Groq
GROQ_API_KEY = "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"
GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_MAX_TOKENS = 150
GROQ_TEMPERATURE = 0.7 

lele_is_talking = False

# ════════════════════════════════════════════════════════════════════════════
# NOTICIAS EN TIEMPO REAL (TENDENCIAS ALEATORIAS)
# ════════════════════════════════════════════════════════════════════════════

def fetch_daily_news() -> str:
    """Busca un titular relevante del día en Google News alternando temas"""
    try:
        topics = ['TECHNOLOGY', 'SCIENCE', 'ENTERTAINMENT', 'WORLD']
        topic = random.choice(topics)
        url = f"https://news.google.com/rss/headlines/section/topic/{topic}?hl=es-419&gl=AR&ceid=AR:es-419"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            items = root.findall('.//item')
            if items:
                item = random.choice(items[:5])
                return item.find('title').text
    except Exception as e:
        print(f"[Error buscando noticias: {e}]")
    return "Descubren una nueva tendencia en redes sociales que está volviendo locos a todos."

# ════════════════════════════════════════════════════════════════════════════
# CLASE DE MEMORIA Y PERFIL
# ════════════════════════════════════════════════════════════════════════════

class LeleMemory:
    def __init__(self):
        self.history = []
        self.turn = 0

    def add(self, role: str, content: str):
        self.history.append({"role": role, "content": content, "turn": self.turn})
        self.turn += 1
        if len(self.history) > 40:
            self.history = self.history[-40:]

    def get_context(self) -> list:
        return self.history

lele = LeleMemory()
PROFILE_FILE = os.path.join(TEMP_DIR, "lele_profile.json")

def load_profile() -> dict:
    try:
        if os.path.exists(PROFILE_FILE):
            with open(PROFILE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except:
        pass
    return {"name": "Yo", "facts": {}, "interests": [], "memories": []}

def save_profile(p: dict):
    try:
        with open(PROFILE_FILE, "w", encoding="utf-8") as f:
            json.dump(p, f, ensure_ascii=False, indent=2)
    except:
        pass

def update_profile(user_says: str, lele_says: str):
    p = load_profile()
    if user_says.strip():
        text = user_says.lower()
        keywords_map = {
            "trading": ["trading", "pine script", "binance", "estrategia", "bot", "quantum"],
            "programacion": ["codigo", "python", "programar", "database", "api", "hermes"],
            "branding": ["baba", "carrera store", "logo", "diseño", "marca"]
        }
        for interest, keywords in keywords_map.items():
            if any(kw in text for kw in keywords):
                if interest not in p.setdefault("interests", []):
                    p["interests"].append(interest)
                    
        memories = p.setdefault("memories", [])
        memories.append({"text": user_says.strip(), "time": datetime.now().isoformat()})
        if len(memories) > 30:
            memories[:] = memories[-30:]
    save_profile(p)

# ════════════════════════════════════════════════════════════════════════════
# CONEXIÓN CON GROQ (CEREBRO DINÁMICO)
# ════════════════════════════════════════════════════════════════════════════

def call_ai(prompt: str, context: list, disable_teaching: bool = False, force_teaching: bool = False, initiate_teaching: bool = False, taught_phrases: list = None) -> str:
    rules = (
        "1. Mantené una charla variada y entretenida. Hablá de curiosidades, historia, ciencia, cine o la vida diaria. NO menciones trading, bots ni programación a menos que yo te pregunte directamente por eso. Usá modismos rioplatenses, llamándome 'bombón' ocasionalmente.\n"
        "2. Respuestas ultra cortas, máximo 3 oraciones.\n"
    )
    
    # BLINDAJE ANTI-INVERSIÓN DE IDIOMA EN LOS PROMPTS
    if disable_teaching:
        rules += "3. REGLA ESTRICTA: NO enseñes inglés en esta respuesta. Solo comunicá lo solicitado de forma natural."
    elif force_teaching:
        rules += (
            "3. REGLA ESTRICTA (MODO JUEGO): OBLIGATORIAMENTE generá UNA NUEVA frase, modismo o palabra.\n"
            "4. EL ORDEN ES VITAL. Primero INGLÉS, luego ESPAÑOL.\n"
            "5. FORMATO EXACTO Y OBLIGATORIO: *EN: [Inglés] | ES: [Español]*\n"
            "PROHIBIDO incluir texto en español dentro de la parte de INGLÉS.\n"
            "EJEMPLO CORRECTO: *EN: The key is the meat | ES: La clave es la carne*\n"
        )
    elif initiate_teaching:
        rules += (
            "3. ENSEÑANZA OBLIGATORIA: Llegó el momento de enseñar. Elegí algo que acabo de decir en español y enseñame cómo se dice en inglés.\n"
            "4. EL ORDEN ES VITAL. Primero INGLÉS, luego ESPAÑOL.\n"
            "5. FORMATO ESTRICTO Y OBLIGATORIO: *EN: [Inglés] | ES: [Español]*\n"
            "PROHIBIDO incluir texto en español dentro de la parte de INGLÉS.\n"
            "EJEMPLO CORRECTO: *EN: The key is the meat | ES: La clave es la carne*\n"
        )
    else:
        rules += "3. NO enseñes inglés en este turno. Mantené la charla 100% natural y terminá con una pregunta."

    # BLOQUEO ANTI-REPETICIÓN
    if (force_teaching or initiate_teaching) and taught_phrases:
        ultimas_frases = ", ".join(taught_phrases[-15:])
        rules += f"\n6. REGLA ESTRICTA DE NO REPETICIÓN: ESTÁ PROHIBIDO repetir o enseñar estas frases/palabras que ya me enseñaste: {ultimas_frases}."

    system_msg = (
        f"Sos LELE, mi mejor asistente de IA, amigo rioplatense y profesor de inglés.\n"
        f"REGLAS:\n{rules}"
    )

    messages = [{"role": "system", "content": system_msg}]
    for entry in context[-6:]:
        if entry.get("role") in ("user", "assistant"):
            messages.append({"role": entry["role"], "content": entry["content"]})
    messages.append({"role": "user", "content": prompt})

    if GROQ_API_KEY:
        try:
            import groq
            client = groq.Groq(api_key=GROQ_API_KEY)
            response = client.chat.completions.create(
                model=GROQ_MODEL,
                messages=messages,
                max_tokens=GROQ_MAX_TOKENS,
                temperature=GROQ_TEMPERATURE,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            print(f"[Error en Groq: {e}]")
    return ""

# ════════════════════════════════════════════════════════════════════════════
# PROCESAMIENTO Y AUDIO
# ════════════════════════════════════════════════════════════════════════════

model = None

def load_model():
    global model
    if model is None:
        print("Cargando modelo Whisper desde disco local...")
        model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8", download_root=CACHE_DIR)

def clean_for_tts(text: str) -> str:
    if not text: return ""
    text = re.sub(r'\*([^*]+)\|([^*]+)\*', '', text)
    text = text.replace('*', '')
    text = re.sub(r'[\U0001F000-\U0010FFFF]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def clean_transcription(text: str) -> str:
    if not text: return ""
    text = text.strip()
    return text[0].upper() + text[1:] if text else ""

_speaking_lock = threading.RLock()

def speak(text: str, voice: str = VOICE_ES, wait: bool = True):
    global lele_is_talking
    def _do():
        global lele_is_talking
        lele_is_talking = True
        try:
            clean_text = clean_for_tts(text)
            if not clean_text.strip(): return
            
            async def gen():
                c = edge_tts.Communicate(clean_text, voice, rate=TTS_RATE)
                audio = b""
                async for chunk in c.stream():
                    if chunk["type"] == "audio": audio += chunk["data"]
                return audio

            audio = asyncio.run(gen())
            if not audio or len(audio) < 500: return

            temp_file = os.path.join(TEMP_DIR, f"lele_{uuid.uuid4().hex[:8]}.mp3")
            with open(temp_file, "wb") as f:
                f.write(audio)
                f.flush()
                os.fsync(f.fileno())

            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.music.unload()
            
            time.sleep(0.2)
            try: os.remove(temp_file)
            except: pass
        except Exception as e:
            print(f"[Error TTS]: {e}")
        finally:
            lele_is_talking = False

    with _speaking_lock:
        if wait: _do()
        else: threading.Thread(target=_do, daemon=True).start()

# ════════════════════════════════════════════════════════════════════════════
# MICRÓFONO Y UTILIDADES
# ════════════════════════════════════════════════════════════════════════════

audio_chunks = []
is_listening = False
silence_chunks = 0

def audio_callback(indata, frames, time, status):
    global audio_chunks, is_listening, silence_chunks, lele_is_talking
    if lele_is_talking: return
    
    chunk = indata[:, 0].astype(np.float32)
    if np.sqrt(np.mean(chunk**2)) > ENERGY_THRESHOLD:
        if not is_listening: is_listening = True
        silence_chunks = 0
        audio_chunks.append(chunk)
    else:
        if is_listening: silence_chunks += 1

def transcribe(audio_np: np.ndarray, lang: str = "es") -> str:
    segments, _ = model.transcribe(audio_np.astype(np.float32), language=lang, beam_size=5, vad_filter=True)
    return " ".join(seg.text for seg in segments)

def ordenar_idiomas(p1: str, p2: str):
    """
    Filtro de Seguridad Avanzado V3: Usa etiquetas obligatorias para asegurar el orden
    y luego elimina palabras basura para que el TTS lea solo la frase pura.
    """
    p1_clean = p1.strip()
    p2_clean = p2.strip()

    is_p1_en = re.search(r'^(EN|ENG|ING|INGL[EÉ]S)\b', p1_clean, re.IGNORECASE)
    is_p1_es = re.search(r'^(ES|ESP|ESPAÑOL)\b', p1_clean, re.IGNORECASE)
    is_p2_en = re.search(r'^(EN|ENG|ING|INGL[EÉ]S)\b', p2_clean, re.IGNORECASE)
    is_p2_es = re.search(r'^(ES|ESP|ESPAÑOL)\b', p2_clean, re.IGNORECASE)

    if is_p1_en or is_p2_es:
        en_phrase, es_phrase = p1_clean, p2_clean
    elif is_p1_es or is_p2_en:
        en_phrase, es_phrase = p2_clean, p1_clean
    else:
        if re.search(r'[áéíóúñ¿¡]', p1_clean, re.IGNORECASE):
            en_phrase, es_phrase = p2_clean, p1_clean
        elif re.search(r'[áéíóúñ¿¡]', p2_clean, re.IGNORECASE):
            en_phrase, es_phrase = p1_clean, p2_clean
        else:
            es_words = r'\b(el|la|los|las|un|una|de|con|en|por|para|que|del|al|es|y|o|yo|tú|él|ella|nosotros|vos|me|te|se|mi|su|puedo|quiero|tengo|soy|estoy|hacer|volar|como|más|pero|este|esta|sí|no|todo|nada|bien|mal|hola|chau|gracias|significa|decir)\b'
            en_words = r'\b(the|a|an|of|with|in|for|by|that|to|is|and|or|i|you|he|she|it|we|they|me|my|his|her|us|them|can|do|have|make|like|more|but|this|yes|no|all|nothing|good|bad|hello|bye|thanks|am|are|was|were|will|fly|what|where|when|who|why|how)\b'

            p1_es = len(re.findall(es_words, p1_clean, re.IGNORECASE))
            p1_en = len(re.findall(en_words, p1_clean, re.IGNORECASE))
            p2_es = len(re.findall(es_words, p2_clean, re.IGNORECASE))
            p2_en = len(re.findall(en_words, p2_clean, re.IGNORECASE))

            if (p1_es - p1_en) > (p2_es - p2_en):
                en_phrase, es_phrase = p2_clean, p1_clean
            elif (p2_es - p2_en) > (p1_es - p1_en):
                en_phrase, es_phrase = p1_clean, p2_clean
            else:
                en_phrase, es_phrase = (p1_clean, p2_clean) if len(p1_clean) < len(p2_clean) else (p2_clean, p1_clean)

    regex_basura = r'^(EN|ENG|ING|INGL[EÉ]S|ES|ESP|ESPAÑOL|SIGNIFICA)[:\s-]*'
    en_phrase = re.sub(regex_basura, '', en_phrase, flags=re.IGNORECASE).strip()
    es_phrase = re.sub(regex_basura, '', es_phrase, flags=re.IGNORECASE).strip()

    return en_phrase, es_phrase

# ════════════════════════════════════════════════════════════════════════════
# BUCLE PRINCIPAL
# ════════════════════════════════════════════════════════════════════════════

def main():
    global audio_chunks, is_listening, silence_chunks
    load_model()
    
    print("\n" + "="*50)
    print(" LELE v100.9 — (Escucha de Alta Precisión & Saludo IA Dinámico)")
    print("="*50)
    
    # === MODIFICACIÓN: PRESENTACIÓN ESTÁTICA Y DIRECTA ===
    saludo_estatico = "Autodidactas que quieran aprender inglés con inteligencia Artificial, Soy LELE, tu profesora de inglés y asistente inteligente. Estoy acá para hablar con vos de lo que se te cante, mantenerte al día con las noticias, y sobre todo, funcionar como tu profesor de inglés, poniéndote a prueba con minijuegos cuando menos te lo esperes. ¡Gratis para todos los Autodidactas que siguen a Regalos Digitales! Esta es la version Beta, Para comprar un profesor de ingles mas avanzado envia un mensaje a @INGLES_iA "
    print(f"\nLELE: {saludo_estatico}")
    speak(saludo_estatico, VOICE_ES)
    
    # --- NUEVO SISTEMA DE SALUDO DINÁMICO CON NOTICIAS REALES ---
    print("\n>>> Pensando de qué hablar hoy...")
    news_title = fetch_daily_news()
    prompt_saludo = f"Generá un saludo corto y amigable para iniciar la charla. Rompé el hielo mencionando casualmente esta noticia: '{news_title}'. Terminá preguntándome de qué quiero charlar. Usá tono rioplatense (me podés decir amigo o bombón). Máximo 2 oraciones."
    
    saludo_inicial = call_ai(prompt_saludo, [], disable_teaching=True)
    if not saludo_inicial or "*|" in saludo_inicial:
        saludo_inicial = f"¡Qué onda! Recién veía una noticia sobre esto: '{news_title}'. ¿Vos en qué andás?"
    
    print(f"\nLELE: {saludo_inicial}")
    speak(saludo_inicial, VOICE_ES)
    # -------------------------------------------------------------
    
    practice_mode = False
    practice_tries = 0
    target_english_phrase = None
    target_spanish_meaning = None
    
    turns_without_practice = 0
    target_practice_turn = random.randint(3, 5)
    
    # ARRAY PARA GUARDAR LAS FRASES YA ENSEÑADAS (MEMORIA A CORTO PLAZO ANTI-REPETICIÓN)
    taught_phrases = []
    
    stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=audio_callback, blocksize=CHUNK_SIZE)
    with stream:
        print("\n>>> Escuchando...")
        while True:
            time.sleep(0.05)
            
            if is_listening and silence_chunks >= CHUNKS_SILENCE:
                is_listening = False
                
                if len(audio_chunks) > 0:
                    audio_np = np.concatenate(audio_chunks)
                    audio_duration = len(audio_np) / SAMPLE_RATE
                    audio_chunks = []; silence_chunks = 0
                    
                    if audio_duration >= MIN_AUDIO_SECONDS:
                        current_lang = "en" if practice_mode else "es"
                        user_text = clean_transcription(transcribe(audio_np, lang=current_lang))
                        
                        if len(user_text.strip()) > 1:
                            print(f"\nYo: {user_text}")
                            
                            if practice_mode and target_english_phrase:
                                clean_user = re.sub(r'[^\w\s]', '', user_text.lower()).strip()
                                clean_target = re.sub(r'[^\w\s]', '', target_english_phrase.lower()).strip()
                                user_words = set(clean_user.split())
                                target_words = set(clean_target.split())
                                
                                # Si acierta la pronunciación
                                if clean_target in clean_user or (len(target_words)>0 and len(user_words.intersection(target_words))/len(target_words) >= 0.5):
                                    msg_exito = "¡Espectacular! Te salió impecable."
                                    print(f"LELE: {msg_exito} (Significaba: {target_spanish_meaning})")
                                    speak(msg_exito, VOICE_ES)
                                    
                                    practice_tries = 0
                                    print(">>> [LELE preparando la próxima ronda...]")
                                    
                                    prompt_next = "Acabo de pronunciar excelente. Dame UNA NUEVA palabra o frase corta en inglés para que siga jugando. FORMATO ESTRICTO: *EN: [Inglés] | ES: [Español]*. EJEMPLO: *EN: The key is the meat | ES: La clave es la carne*. PROHIBIDO usar palabras en español dentro de la parte en inglés."
                                    
                                    # PASAMOS LAS FRASES YA ENSEÑADAS PARA QUE LA IA NO LAS REPITA
                                    ai_next = call_ai(prompt_next, lele.get_context(), force_teaching=True, taught_phrases=taught_phrases)
                                    match_next = re.search(r'\*([^*]+)\|([^*]+)\*', ai_next)
                                    
                                    if match_next:
                                        part1 = match_next.group(1).strip()
                                        part2 = match_next.group(2).strip()
                                        target_english_phrase, target_spanish_meaning = ordenar_idiomas(part1, part2)
                                    else:
                                        salvavidas = [("Piece of cake", "Pan comido"), ("Never give up", "Nunca te rindas"), ("Awesome", "Impresionante"), ("See you later", "Nos vemos luego")]
                                        frase_en, frase_es = random.choice(salvavidas)
                                        target_english_phrase = frase_en
                                        target_spanish_meaning = frase_es
                                        
                                    target_english_phrase = re.sub(r'\(.*?\)', '', target_english_phrase).strip()
                                    
                                    # GUARDAMOS LA NUEVA FRASE EN LA LISTA NEGRA
                                    if target_english_phrase not in taught_phrases:
                                        taught_phrases.append(target_english_phrase)
                                        if len(taught_phrases) > 20: # Mantenemos solo las últimas 20 para no saturar el prompt
                                            taught_phrases.pop(0)
                                    
                                    print(f"--- NUEVO DESAFÍO: {target_english_phrase} | Significa: {target_spanish_meaning} ---")
                                    
                                    speak(f"A ver si te sale esta. Significa: {target_spanish_meaning}. Y en inglés se dice:", VOICE_ES)
                                    speak(target_english_phrase, VOICE_EN)
                                        
                                # Si falla la pronunciación
                                else:
                                    practice_tries += 1
                                    if practice_tries >= 3:
                                        print("LELE: Eres un looser.")
                                        speak("Eres un looser.", VOICE_ES)
                                        news_title = fetch_daily_news()
                                        transition_prompt = f"Ignorá todo lo anterior. Acabo de fallar 3 veces en el inglés y me dijiste 'Eres un looser'. Cambiá de tema bruscamente comentando ESTA noticia de hoy: '{news_title}'. Hacé una pregunta al final."
                                        ai_response = call_ai(transition_prompt, lele.get_context(), disable_teaching=True)
                                        print(f"LELE: {ai_response}")
                                        speak(ai_response, VOICE_ES)
                                        
                                        practice_mode = False; practice_tries = 0; target_english_phrase = None; target_spanish_meaning = None
                                        turns_without_practice = 0 
                                        target_practice_turn = random.randint(3, 5)
                                        lele.add("assistant", ai_response)
                                        continue
                                        
                                    fail_msg = f"Casi. Intento {practice_tries} de 3. Escuchá de nuevo:"
                                    print(f"LELE: {fail_msg}")
                                    speak(fail_msg, VOICE_ES)
                                    speak(target_english_phrase, VOICE_EN)
                                continue
                            
                            # ----------------------------------------------------
                            # FLUJO DE CONVERSACIÓN NORMAL
                            # ----------------------------------------------------
                            update_profile(user_text, "")
                            lele.add("user", user_text)
                            
                            turns_without_practice += 1
                            trigger_teaching = (turns_without_practice >= target_practice_turn)
                            
                            # SE PASA LA LISTA AL LLAMADO NORMAL POR SI TOCA ENSEÑAR
                            ai_response = call_ai(user_text, lele.get_context(), initiate_teaching=trigger_teaching, taught_phrases=taught_phrases)
                            if not ai_response: ai_response = "Me colgué. ¿Qué me decías?"
                            
                            match = re.search(r'\*([^*]+)\|([^*]+)\*', ai_response)
                            if match:
                                part1 = match.group(1).strip()
                                part2 = match.group(2).strip()
                                
                                english_phrase, spanish_phrase = ordenar_idiomas(part1, part2)
                                english_phrase = re.sub(r'\(.*?\)', '', english_phrase).strip()
                                
                                clean_response = ai_response.replace(match.group(0), "").strip()
                                if not clean_response: clean_response = "A ver, te enseño esto:"
                                
                                lele.add("assistant", clean_response)
                                print(f"LELE: {clean_response}")
                                speak(clean_response, VOICE_ES)
                                time.sleep(0.4)
                                
                                print(f"--- NUEVO DESAFÍO: {english_phrase} | Significa: {spanish_phrase} ---")
                                
                                speak(f"Decime vos. Significa {spanish_phrase}, pero en inglés se dice:", VOICE_ES)
                                speak(english_phrase, VOICE_EN)
                                
                                target_english_phrase = english_phrase
                                target_spanish_meaning = spanish_phrase 
                                
                                # GUARDAMOS LA NUEVA FRASE EN LA LISTA NEGRA
                                if target_english_phrase not in taught_phrases:
                                    taught_phrases.append(target_english_phrase)
                                    if len(taught_phrases) > 20: 
                                        taught_phrases.pop(0)

                                practice_mode = True
                                practice_tries = 0
                                
                            else:
                                lele.add("assistant", ai_response)
                                print(f"LELE: {ai_response}")
                                speak(ai_response, VOICE_ES)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt:
        print("\n¡Chau! Nos vemos.")
        pygame.mixer.quit()