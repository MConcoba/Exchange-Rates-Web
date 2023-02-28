import dash_bootstrap_components as dbc

def get_error_modal(message):
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Error")),
            dbc.ModalBody(message),
            dbc.ModalFooter(
                dbc.Button("Cerrar", id="error-modal-close", className="ml-auto")
            ),
        ],
        id="error-modal",
        centered=True,
        is_open=True,
    )


