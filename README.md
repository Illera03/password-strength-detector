# 🔐 Password Strength Detector (ML-powered)

Este proyecto utiliza técnicas de Machine Learning para clasificar contraseñas como **débiles** o **fuertes**, y detectar patrones peligrosos aunque cumplan las reglas típicas de complejidad.

---

## 🧠 ¿Por qué no basta con reglas básicas?

Muchas contraseñas comunes cumplen requisitos mínimos (números, símbolos, mayúsculas...), pero siguen siendo predecibles. Este clasificador aprende de contraseñas reales filtradas para identificar patrones débiles más complejos.

---

## ⚙️ Tecnologías usadas

- Python 3
- scikit-learn
- pandas
- Streamlit (para la interfaz)
- TfidfVectorizer (NLP para texto corto)
- Dataset: [RockYou](https://github.com/danielmiessler/SecLists) filtrado

---

## 🚀 Cómo usar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/password-strength-detector.git
   cd password-strength-detector
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Lanza la aplicación:
   ```bash
   streamlit run app/streamlit_app.py
   ```

### 🧪 Ejemplo

- Contraseña supuestamente segura (contiene mayúsculas, caracteres especiales, números y 8 caracteres o mas): 

      H0l@123:)
   → Resultado: Débil (Muy común, patrón predecible)


- Contraseña segura: 

      W!qRz9@v$M2e
   → Resultado: Fuerte

### 📁 Estructura del proyecto
```bash
  password-strength-detector/
  ├── app/
  │   └── streamlit_app.py              # Interfaz de usuario
  ├── data/
  │   ├── rockyou.txt                   # Dataset de contraseñas reales
  │   ├── rock_you_filtered.txt         # Dataset de contraseñas reales (limpiado)
  │   └── strong_passwords.txt          # Contraseñas generadas seguras
  ├── models/
  │   ├── password_model.pkl            # Modelo entrenado
  │   ├──scaler.pkl                     # Escalador para normalizar datos
  │   └── vectorizer.pkl                # Vectorizador para transformar texto
  ├── notebooks/
  │   └── exploratory_analysis.ipynb    # Análisis inicial y pruebas
  ├── src/
  │   ├── __init__.py                   # Inicialización del paquete
  │   ├── model_training.py             # Entrena y guarda el modelo
  │   ├── prepare_week_passwords.py     # Crea el dataset filtrado
  │   ├── strong_password_generator.py  # Crea el dataset de contraseñas seguras
  │   └── utils.py                      # Funciones auxiliares (cálculo entropía, etc.)
  ├── requirements.txt                  # Librerías necesarias
  └── README.md                         # Descripción del proyecto
  ```
### 📌 Posibles mejoras
Explicabilidad: usar SHAP o LIME para mostrar qué hace que una contraseña sea débil

Detección de similitudes con otras contraseñas

Validación de listas masivas de contraseñas (auditoría)

### 🧑‍💻 Autor
Hecho por Jorge Illera Rivera – jillera10@gmail.com.

🔒 Este proyecto es educativo y no almacena ni transmite contraseñas reales.
