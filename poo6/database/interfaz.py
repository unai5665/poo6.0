from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Button, DataTable, Label
from textual.containers import Vertical
from cosasdefrutas import ColeccionDatos
from screens import BorrarFrutaScreen, BorrarFormaScreen, BorrarColorScreen, AñadirColorScreen, AñadirFormaScreen, AñadirScreen


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("FRUTAS")
        yield Vertical(
            DataTable(classes="table1"),
            Vertical(
                Button("Añadir fruta", id="boton_anadirF"),
                Button("Eliminar fruta", id="boton_eliminarF"),
                Button("Actualizar", id="boton_actualizarF")  
            )
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "boton_anadirF":
            self.app.switch_to_edit("fru")
        elif event.button.id == "boton_eliminarF":
            self.app.switch_to_delete("fru")
        elif event.button.id == "boton_actualizarF": 
            self.actualizar_tabla()

    def on_mount(self) -> None:
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        table = self.query_one(DataTable)
        if table:
            table.cursor_type = "none"
            table.clear()

            if not table.columns:
                table.add_columns("ID", "Nombre de la fruta")

            frutas = self.app.coleccion.leer("fru")
            for fruta in frutas:
                table.add_rows([(str(fruta[0]), fruta[1])])




class FormasScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("FORMAS")
        yield Vertical(
            DataTable(classes="table2"),
            Vertical(
                Button("Añadir forma", id="boton_anadirFo"),
                Button("Eliminar forma", id="boton_eliminarFo"),
                Button("Actualizar", id="boton_actualizarFo")  
            )
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "boton_anadirFo":
            self.app.switch_to_edit("for")
        elif event.button.id == "boton_eliminarFo":
            self.app.switch_to_delete("for")
        elif event.button.id == "boton_actualizarFo":  
            self.actualizar_tabla()

    def on_mount(self) -> None:
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        table = self.query_one(DataTable)
        if table:
            table.cursor_type = "none"
            table.clear()

            if not table.columns:
                table.add_columns("ID", "Nombre de la forma")

            formas = self.app.coleccion.leer("for")
            for forma in formas:
                table.add_rows([(str(forma[0]), forma[1])])




class ColoresScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("COLORES")
        yield Vertical(
            DataTable(classes="table3"),
            Vertical(
                Button("Añadir color", id="boton_anadirC"),
                Button("Eliminar color", id="boton_eliminarC"),
                Button("Actualizar", id="boton_actualizarC")  
            )
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "boton_anadirC":
            self.app.switch_to_edit("col")
        elif event.button.id == "boton_eliminarC":
            self.app.switch_to_delete("col")
        elif event.button.id == "boton_actualizarC":  
            self.actualizar_tabla()

    def on_mount(self) -> None:
        self.actualizar_tabla()

    def actualizar_tabla(self) -> None:
        table = self.query_one(DataTable)
        if table:
            table.cursor_type = "none"
            table.clear()

            if not table.columns:
                table.add_columns("ID", "Nombre del color")

            colores = self.app.coleccion.leer("col")
            for color in colores:
                table.add_rows([(str(color[0]), color[1])])




class FooterApp(App):
    BINDINGS = [
        ("f", "switch_mode('main')", "Frutas"),
        ("m", "switch_mode('formas')", "Formas"),
        ("c", "switch_mode('colores')", "Colores"),
        ("q", "quit", "Cerrar Programa"),
    ]
    MODES = {
        "main": MainScreen,
        "formas": FormasScreen,
        "colores": ColoresScreen,
    }
    
    def compose(self) -> ComposeResult:
        yield Footer()


class Pantallas(FooterApp):
    def __init__(self):
        super().__init__()
        self.coleccion = ColeccionDatos()
    
    def on_mount(self) -> None:
        self.switch_to_main()

    def switch_to_main(self) -> None:
        self.push_screen(MainScreen())

    def switch_to_formas(self) -> None:
        self.push_screen(FormasScreen())

    def switch_to_colores(self) -> None:
        self.push_screen(ColoresScreen())

    def switch_to_edit(self, tipo) -> None:
        if tipo == "for":
            self.push_screen(AñadirFormaScreen())
        elif tipo == "fru":
            self.push_screen(AñadirScreen())
        elif tipo == "col":
            self.push_screen(AñadirColorScreen())

    def switch_to_delete(self, tipo) -> None:
        if tipo == "for":
            self.push_screen(BorrarFormaScreen())
        elif tipo == "fru":
            self.push_screen(BorrarFrutaScreen())
        elif tipo == "col":
            self.push_screen(BorrarColorScreen())
        

if __name__ == "__main__":
    app = Pantallas()
    app.run()