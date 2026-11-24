import time  # MEJORA 3: para medir el tiempo

import gradio as gr
from transformers import pipeline

# Carga el modelo una sola vez, al encender la app
clasificador = pipeline(
    "image-classification",
    model="google/mobilenet_v2_1.0_224",
)


def clasificar(imagen):
    """Recibe una imagen PIL y regresa las 3 etiquetas más probables con su porcentaje."""
    # ===== MEJORA 3: medir cuánto tarda el modelo =====
    inicio = time.perf_counter()
    resultados = clasificador(imagen, top_k=3)
    segundos = time.perf_counter() - inicio
    # ==================================================
    etiquetas = {r["label"]: r["score"] for r in resultados}
    return etiquetas, f"{segundos:.2f} s"  # MEJORA 3: dos salidas


demo = gr.Interface(
    fn=clasificar,                      # tu función
    inputs=gr.Image(type="pil"),        # lo que pide: una foto
    outputs=[
        gr.Label(num_top_classes=3),             # 3 categorías con porcentaje
        gr.Textbox(label="Tiempo en CPU"),       # MEJORA 3: cuadro de texto con el tiempo
    ],
    # ===== MEJORA 1: título y descripción =====
    title="¿Qué hay en la foto?",
    description="Usa el modelo MobileNetV2 (google/mobilenet_v2_1.0_224) para clasificar tu imagen.",
    # ==========================================
    # ===== MEJORA 2: fotos de ejemplo (un clic y responde) =====
    examples=["ejemplos/GTA_6.png", "ejemplos/mi-foto.jpg","ejemplos/Carro.png"],
    # ===========================================================
)

demo.launch()  # enciende la página en http://127.0.0.1:7860