import gradio as gr
from transformers import pipeline

# Carga el modelo una sola vez, al encender la app
clasificador = pipeline(
    "image-classification",
    model="google/mobilenet_v2_1.0_224",
)


def clasificar(imagen):
    """Recibe una imagen PIL y regresa las 3 etiquetas más probables con su porcentaje."""
    resultados = clasificador(imagen, top_k=3)
    return {r["label"]: r["score"] for r in resultados}


demo = gr.Interface(
    fn=clasificar,                      # tu función
    inputs=gr.Image(type="pil"),        # lo que pide: una foto
    outputs=gr.Label(num_top_classes=3),  # lo que muestra: 3 categorías con porcentaje
    # ===== MEJORA 1: título y descripción =====
    title="¿Qué hay en la foto?",
    description="Usa el modelo MobileNetV2 (google/mobilenet_v2_1.0_224) para clasificar tu imagen.",
    # ==========================================
)

demo.launch()  # enciende la página en http://127.0.0.1:7860
