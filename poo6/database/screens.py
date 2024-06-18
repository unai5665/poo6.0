from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Button, Input
from textual.containers import Horizontal, Vertical

class AñadirScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre de la fruta", id="fruta")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        fruta = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and fruta:
            self.app.coleccion.insertar(fruta, "fru")
            self.app.switch_to_main()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_main()

class AñadirFormaScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre de la forma", id="forma")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        forma = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and forma:
            self.app.coleccion.insertar(forma, "for")
            self.app.switch_to_formas()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_formas()

class AñadirColorScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del color", id="color")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        color = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and color:
            self.app.coleccion.insertar(color, "col")
            self.app.switch_to_colores()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_colores()

class BorrarFrutaScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre de la fruta", id="fruta")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        fruta = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and fruta:
            self.app.coleccion.borrar(fruta, "fru")
            self.app.switch_to_main()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_main()

class BorrarFormaScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre de la forma", id="forma")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        forma = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and forma:
            self.app.coleccion.borrar(forma, "for")
            self.app.switch_to_formas()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_formas()

class BorrarColorScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nombre del color", id="color")
        yield Horizontal(
            Button("Aceptar", id="boton_aceptar"),
            Button("Cancelar", id="boton_cancelar")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        color = self.query_one(Input).value
        if event.button.id == "boton_aceptar" and color:
            self.app.coleccion.borrar(color, "col")
            self.app.switch_to_colores()
        elif event.button.id == "boton_cancelar":
            self.app.switch_to_colores()
