from flask import Flask, jsonify

from exceptions import (
    InvalidFieldException,
    InvalidFigureException,
)
from validators import (
    validate_field,
    validate_figure,
)

app = Flask(__name__)


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def list_available_moves(chess_figure: str, current_field: str):
    try:
        current_field_instance = validate_field(current_field)
    except InvalidFieldException as e:
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": str(e),
                    "figure": chess_figure,
                    "currentField": current_field.upper(),
                }
            ),
            409,
        )

    try:
        chess_figure_instance = validate_figure(chess_figure, current_field_instance)
    except InvalidFigureException as e:
        return (
            jsonify(
                {
                    "availableMoves": [],
                    "error": str(e),
                    "figure": chess_figure,
                    "currentField": current_field.upper(),
                }
            ),
            404,
        )

    return (
        jsonify(
            {
                "availableMoves": [
                    str(_field)
                    for _field in chess_figure_instance.list_available_moves()
                ],
                "error": None,
                "figure": chess_figure,
                "currentField": current_field.upper(),
            }
        ),
        200,
    )


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def validate_move(chess_figure: str, current_field: str, dest_field: str):
    try:
        current_field_instance = validate_field(current_field)
        dest_field_instance = validate_field(dest_field)
    except InvalidFieldException as e:
        return (
            jsonify(
                {
                    "move": None,
                    "error": str(e),
                    "figure": chess_figure,
                    "currentField": current_field.upper(),
                    "destField": dest_field.upper(),
                }
            ),
            409,
        )

    try:
        chess_figure_instance = validate_figure(chess_figure, current_field_instance)
    except InvalidFigureException as e:
        return (
            jsonify(
                {
                    "move": None,
                    "error": str(e),
                    "figure": chess_figure,
                    "currentField": current_field.upper(),
                    "destField": dest_field.upper(),
                }
            ),
            404,
        )

    is_valid_move = chess_figure_instance.validate_move(dest_field_instance)

    return (
        jsonify(
            {
                "move": "valid" if is_valid_move else "invalid",
                "error": None if is_valid_move else "Current move is not permitted.",
                "figure": chess_figure,
                "currentField": current_field.upper(),
                "destField": dest_field.upper(),
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
