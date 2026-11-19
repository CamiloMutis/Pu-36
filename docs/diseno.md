# Diseño de Pu-36

## Principio

Es una antena Yagi-Uda de discos. Su tamaño depende de la longitud de onda de la señal:

λ = c / f = (3 × 10⁸ m/s) / (2,4 × 10⁹ Hz) = **12,5 cm**

Solo el **parche** (elemento activo) va conectado al cable. El reflector y los directores son elementos parásitos: la señal induce en ellos corrientes que vuelven a irradiar. Hacia el frente esas ondas se suman y hacia atrás se cancelan en parte. Así la antena concentra la energía en una dirección y gana en dBi.

## Medidas

Todas salen del plano del video de KREOSAN (minuto 1:08). La distancia es de cara a cara entre discos.

| Disco | Diámetro | Radio para el compás | Separación del anterior | Posición desde el reflector |
|---|---|---|---|---|
| Reflector (plano) | 9 cm | **4,5 cm** | — | 0 cm |
| Parche (elemento activo) | 6,8 cm | **3,4 cm** | 1,1 cm | 1,1 cm |
| 2.º disco | 5,4 cm | **2,7 cm** | 1,2 cm | 2,3 cm |
| Director 1 | 3,8 cm | **1,9 cm** | 3,2 cm | 5,5 cm |
| Director 2 | 3,7 cm | **1,85 cm** | 2,8 cm | 8,3 cm |
| Director 3 | 3,7 cm | **1,85 cm** | 2,8 cm | 11,1 cm |
| Director 4 | 3,7 cm | **1,85 cm** | 2,8 cm | 13,9 cm |

- **Alimentación:** a **1 cm del centro**. El cable entra por un agujero de 0,3 cm en el reflector y su vivo se suelda al parche.
- **Separación entre directores:** el plano permite de 2,8 a 3,2 cm. Se usó 2,8 cm; lo importante es que los tres espacios sean iguales.

### Diferencias con el plano original

| Plano del video | Pu-36 | Por qué |
|---|---|---|
| Reflector en caja, con borde de 1,5 cm | Disco plano | En el video el reflector se armó plano; doblar el borde parejo es difícil y la diferencia es pequeña |
| Varilla de 4 mm | Varilla de 1/4" (6,35 mm) | Es la que se consigue en ferretería; casi no afecta la señal |
| Directores de 1 mm | Lámina de 0,25 mm | A 2,4 GHz la corriente circula solo por la superficie; el grosor no cambia el funcionamiento |
| Conector SMA en el reflector | Base de la antena original del adaptador, con conector RP-SMA | Se reutilizó el cable de una antena desarmada |

## Materiales

| Material | Detalle |
|---|---|
| Lámina de cobre para repujado | Calibre 30 (≈0,25 mm), se corta con tijera. Con 20 × 30 cm alcanza para todo, con repuesto del parche |
| Varilla roscada 1/4" | Se usan unos 15 cm |
| Tuercas 1/4" | 2 por disco (14) y 2 de reserva |
| Cable de una antena RP-SMA | La base blanca de la antena original del TL-WN722N, con unos 1,5 cm de coaxial |
| Alambre de cobre sólido | Unos 2 cm, para alargar el vivo hasta el parche (comprobado con imán: no se pega, es cobre) |
| Soldadura 60/40 y pasta | — |
| Extensión RP-SMA macho–hembra | Opcional, de 1 m como máximo, en cable flexible (RG58, RG174 o RG316) |
| Trípode flexible | Para apuntar y girar la antena |

## Conexión

```
vivo  ──► parche, a 1 cm del centro
malla ──► reflector, por detrás
```

### Versión 1: adaptador USB (pruebas en casa)

```
Pu-36 ── base blanca (RP-SMA macho) ── TL-WN722N ── extensión USB ── portátil
```

Sirve para probar la antena en casa con el script `herramientas/medir.py`.

### Versión 2: router (ensayo con el docente)

```
Pu-36 ── base blanca ── [extensión RP-SMA ≤ 1 m] ── router
```

- Se quita una antena del router y en ese conector va Pu-36. Las demás antenas se dejan puestas, igual en todas las pruebas.
- El router debe tener **antenas desenroscables RP-SMA**. Si son fijas, hay que abrirlo y soldar el coaxial adentro: vivo con vivo, malla con malla.

Ninguna de las dos versiones necesita conectores F ni adaptadores de cable de TV.
