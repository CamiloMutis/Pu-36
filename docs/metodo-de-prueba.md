# Método de prueba

## Qué se compara

| Configuración | Para qué |
|---|---|
| **Cable pelado** (sin antena) | Punto de partida: muestra lo poco que capta el vivo solo |
| **Antena original** (del adaptador o del router) | Referencia comercial |
| **Pu-36** | La antena del proyecto |

Las tres se miden con el **mismo equipo, en el mismo conector y en el mismo lugar**, para que la única diferencia sea la antena.

## Variables

- **RSSI** en dBm, con WiFi Analyzer, NetSpot o `herramientas/medir.py`.
- **Velocidad de descarga y de subida** y **latencia**, con Speedtest.
- **Distancia** al router: 5, 10, 15 y 20 m.
- **Ángulo** de Pu-36 respecto al router: 0°, 45°, 90°, 135° y 180°, donde 0° es apuntando al router.

## Procedimiento

1. Dejar fijo el router y el equipo que mide. Anotar la posición.
2. En cada distancia, medir primero con la antena original y después con Pu-36 en el mismo conector.
3. Con Pu-36, repetir girándola de a 45° sin mover el equipo que mide.
4. Hacer cada medición **3 veces** y sacar el promedio.
5. Registrar todo en un CSV con la [plantilla](../pruebas/plantilla_mediciones.csv), una carpeta por sesión dentro de `pruebas/`.

## Cuidados

- **No medir demasiado cerca del router.** El adaptador marca 100 % para cualquier señal de −40 dBm o más fuerte, así que las antenas se ven iguales. Buscar un punto donde la antena original dé entre 50 y 70 %.
- **Conteo de redes:** al repetir escaneos seguidos el sistema acumula redes vistas antes. Para comparar, usar el número del primer escaneo.
- **Conversión aproximada** de porcentaje a dBm (fórmula de NetworkManager): dBm ≈ % × 0,6 − 100.
- **Soldadura de la malla:** si queda floja, el forro del cable empieza a captar señal por sí mismo y se mezcla con la antena.

## Criterio de éxito

Pu-36 es funcional si:

1. Apuntando al router (0°) da un **RSSI más cercano a cero** que la antena original, sobre todo a 15 y 20 m.
2. Al girarla, la señal **baja claramente** a 90° y 180°. Eso demuestra que la ganancia viene de la antena y no del cable.
3. La velocidad es igual o mayor que con la antena original a mayores distancias.

Valores esperados: la antena original del TL-WN722N es de unos 4 dBi omnidireccional. Una Yagi de discos de este tamaño suele dar unos 10 dBi al frente, pero en una antena casera cualquier error de medida o de soldadura puede bajar ese valor.
