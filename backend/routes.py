#endpoints

from flask import Blueprint, request, jsonify
from lenguajes import (
    generar_cadenas,
    pertenece,
    union,
    concatenacion,
    kleene_star,
    kleene_plus,
    analizar_crecimiento,
)

api = Blueprint("api", __name__)



def _parse_lista(texto: str) -> list[str]:
    """Convierte una cadena separada por comas en una lista limpia."""
    return [s.strip() for s in texto.split(",")]


OPERACIONES = {
    "generar",
    "pertenece",
    "union",
    "concatenacion",
    "kleene_star",
    "kleene_plus",
    "crecimiento",
}


#principal
@api.route("/api/ejecutar", methods=["POST"])
def ejecutar():
    """
    Recibe un JSON con la clave 'operacion' y los parámetros necesarios,
    ejecuta la operación correspondiente y devuelve el resultado.
    """
    data      = request.get_json(force=True)
    operacion = data.get("operacion")

    if operacion not in OPERACIONES:
        return jsonify({"error": f"Operación desconocida: '{operacion}'"}), 400

    try:
        resultado = _despachar(operacion, data)
        return jsonify({"resultado": resultado})

    except (KeyError, ValueError) as e:
        return jsonify({"error": f"Parámetro inválido: {e}"}), 400
    except Exception as e:                          # noqa: BLE001
        return jsonify({"error": str(e)}), 500


#despachador
def _despachar(operacion: str, data: dict):
    """Selecciona y ejecuta la función correspondiente a la operación."""

    if operacion == "generar":
        alfabeto = _parse_lista(data["alfabeto"])
        max_len  = int(data["max_len"])
        return generar_cadenas(alfabeto, max_len)

    if operacion == "pertenece":
        cadena   = data["cadena"]
        lenguaje = _parse_lista(data["lenguaje"])
        res      = pertenece(cadena, lenguaje)
        return f"¿Pertenece?: {'Sí' if res else 'No'}"

    if operacion == "union":
        return union(_parse_lista(data["l1"]), _parse_lista(data["l2"]))

    if operacion == "concatenacion":
        return concatenacion(_parse_lista(data["l1"]), _parse_lista(data["l2"]))

    if operacion == "kleene_star":
        lenguaje = _parse_lista(data["lenguaje"])
        max_iter = int(data["max_iter"])
        res      = kleene_star(lenguaje, max_iter)
        return ["ε" if x == "" else x for x in res]  # visualizar épsilon

    if operacion == "kleene_plus":
        lenguaje = _parse_lista(data["lenguaje"])
        max_iter = int(data["max_iter"])
        return kleene_plus(lenguaje, max_iter)

    if operacion == "crecimiento":
        lenguaje = _parse_lista(data["lenguaje"])
        datos    = analizar_crecimiento(lenguaje)
        return [f"Iteración {r['iteracion']}: {r['cantidad']} cadenas" for r in datos]
