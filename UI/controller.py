import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo creato con successo!"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} edges"))
        self._view.update_page()
        pass

    def handleCompConnessa(self,e):
        idAdded=self._view._txtIdOggetto.value
        try:
            intId=int(idAdded)
            self._view._txt_result.controls.clear()


            if intId not in self._model.idMap:
                self._view._txt_result.controls.append(ft.Text("Inserire un id valido!"))
            else:

                self._view._txt_result.controls.append(ft.Text(f"L'oggetto {intId} è presente nel grafo"))
                n=self._model.getCompConn(intId)
                self._view._txt_result.controls.append(ft.Text(f"Tale oggetto è in una componente connessa di {n} nodi"))








        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un valore intero!"))

        self._view.update_page()

