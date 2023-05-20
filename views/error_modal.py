import dash_bootstrap_components as dbc

modal = dbc.Modal(
                    [
                        dbc.ModalHeader("Error"),
                        dbc.ModalBody("Ocurrió un error"),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Cerrar", id="error-modal-close", className="ml-auto")
                        ),
                    ],
                    id="error-modal",
                    centered=True,
                    is_open=False,
                )