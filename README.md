# 📊 TelecomX LATAM - Análisis de Evasión de Clientes (Churn)

Este proyecto forma parte del desafío de análisis de datos en **Telecom X**, donde buscamos comprender los factores que provocan la **evasión de clientes** (churn). Utilizando Python y herramientas de análisis exploratorio, se pretende descubrir patrones relevantes que ayuden a prevenir cancelaciones.

## 🎯 1. Objetivo

Analizar los datos de clientes de Telecom X para identificar variables clave asociadas a la evasión, y generar visualizaciones e insights que sirvan de base para modelos predictivos.

## 🧰 2. Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## 🗂️ 3. Estructura del proyecto


```
TelecomX_LATAM/
├── data/               # Data del proyecto(.json) y diccionario(.md)
│   ├── telecom_data.json
│   └── TelecomX_diccionario.md
├── notebooks/          # Análisis exploratorio
│   └── TelecomX_LATAM.ipynb
├── src/                # Scripts organizados por funcionalidad (ETL, EDA, etc.)
├── outputs/            # Gráficos y archivos generados
└── README.md           # Descripción del proyecto
└── requirements.txt    # Librerías necesarias
```

### 4. Limpieza y Tratamiento de Datos (ETL)
- Se cargó el JSON desde la URL pública (raw GitHub).
- Se normalizó la estructura anidada (`customer`, `phone`, `internet`, `account`) a columnas planas con `pd.json_normalize`.
- Se convirtieron a numéricos: `account.Charges.Monthly`, `account.Charges.Total`. Los nulos en `Total` se imputaron con 0 (clientes nuevos sin acumulado).
- Se filtró `Churn` a valores válidos {Yes, No} y se tiparon columnas categóricas de negocio.

### 5. Análisis Exploratorio (EDA)
- **Churn global:** (ver celda de métricas).
![alt text](/notebooks/outputs/dist_churn.png)

- **Mayor churn** en clientes con contrato **Month-to-month** frente a contratos **One year**/**Two year**.
![alt text](6e45064d-e372-400f-9b77-9e832fe3ac14.png)

- **Servicios de seguridad/soporte** (`OnlineSecurity`, `TechSupport`) se asocian con **menor churn**.

- **Tenure** bajo (clientes recientes) presenta más churn; se estabiliza con mayor antigüedad.
![alt text](outputs/dist_tenure.png)

- **PaperlessBilling** puede mostrar diferencias; revisar junto a método de pago.


### 6. Conclusiones e Insights
- El **tipo de contrato** es un driver clave: contratos mensuales concentran la mayor tasa de churn.
- La **adopción de servicios de valor** (seguridad en línea y soporte técnico) se relaciona con **retención**.
- **Antigüedad (tenure)** es protectora: clientes más antiguos desertan menos.
- **Cargos**: revisar si niveles altos de cargos mensuales impactan en churn en combinación con tipo de servicio.

### 7. Recomendaciones
- **Incentivar upgrades de contrato** (descuentos a 12/24 meses, bundles).
- **Promover paquetes con precio preferente** de `OnlineSecurity` y `TechSupport`.
- **Onboarding reforzado** para clientes nuevos (<6 meses): contacto proactivo y ofertas personalizadas.
- **Revisar fricción de pago**: evaluar impacto por método y paperless, diseñar nudges de recordatorio/pago.
- **Segmentación**: modelos predictivos de churn usando variables comportamentales + servicios contratados.

## 📎 Créditos

Proyecto desarrollado por [NellyCN](https://github.com/NellyCN) como parte del desafío **Churn de Clientes - TelecomX_LATAM**.

---
